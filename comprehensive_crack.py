#!/usr/bin/env python3
import re
import string

ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gH8|CR-^S(Cb^}R.RX|8^]|CbR]|C(g|8^HmRX|C(H#}*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^(#(#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p}^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^Sb(gb^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

cipher_clean = ciphertext.replace('\n', ' ')

def score_english(text):
    """Score text based on how English-like it is"""
    # Printable characters
    printable = sum(1 for c in text if 32 <= ord(c) < 127)
    score = printable * 1.0
    
    # Common English words (case insensitive)
    text_lower = text.lower()
    common_words = ['the', 'and', 'is', 'are', 'for', 'with', 'that', 'this', 'from', 'have', 'been', 'can', 'not']
    for word in common_words:
        score += text_lower.count(' ' + word + ' ') * 10
        score += text_lower.count('^' + word + ' ') * 10  # In case ^ is still there
    
    # Letter frequency
    letters = sum(1 for c in text if c.isalpha())
    score += letters * 0.5
    
    # Spaces
    spaces = text.count(' ')
    score += spaces * 2
    
    return score

print("Brute forcing LCG parameters with comprehensive search...")
print("="*60)

best_score = 0
best_result = None

# Try with more a values and all c, seed combinations
# Common 'a' values for LCG that are coprime to 256
good_a_values = [1, 5, 7, 9, 11, 13, 17, 19, 21, 23, 25, 29, 31, 33, 37, 39, 41, 43, 45, 47, 49, 51, 53, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 79, 81, 83, 85, 87, 89, 93, 95, 97, 99, 101, 103, 105, 107, 109, 113, 115, 117, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 145, 147, 149, 151, 153, 155, 157, 159, 163, 165, 167, 169, 171, 173, 177, 179, 181, 183, 185, 187, 189, 191, 193, 197, 199, 201, 205, 207, 209, 211, 213, 215, 217, 219, 221, 223, 225, 227, 229, 231, 233, 235, 237, 239, 241, 243, 245, 247, 249, 251, 253, 255]

counter = 0
total = len(good_a_values) * 256 * 256

for a in good_a_values:
    for c in range(256):
        for seed in range(256):
            counter += 1
            if counter % 10000 == 0:
                print(f"Progress: {counter}/{total} ({100*counter/total:.1f}%) - Best score so far: {best_score:.0f}")
            
            # Generate keystream with LCG
            x = seed
            keystream = []
            for _ in range(len(cipher_clean)):
                keystream.append(x)
                x = (a * x + c) % 256
            
            # Decrypt
            decrypted = ''.join([chr(ord(cipher_clean[i]) ^ keystream[i]) for i in range(len(cipher_clean))])
            
            # Score
            score = score_english(decrypted)
            
            if score > best_score:
                best_score = score
                best_result = (a, c, seed, decrypted)
                
                # If score is very high, we probably found it
                if score > len(cipher_clean) * 2:
                    print(f"\n*** VERY HIGH SCORE FOUND ***")
                    print(f"a = {a}, c = {c}, seed = {seed}")
                    print(f"Score: {score:.0f}")
                    print("\nDecrypted message:")
                    print("="*60)
                    print(decrypted)
                    
                    # Look for flag
                    flags = re.findall(r'USCC\{[^}]+\}', decrypted)
                    if flags:
                        print("\n" + "="*60)
                        print("FLAG FOUND:")
                        print("="*60)
                        for flag in flags:
                            print(flag)
                        exit(0)

print(f"\nSearch complete. Best result:")
if best_result:
    a, c, seed, decrypted = best_result
    print(f"a = {a}, c = {c}, seed = {seed}")
    print(f"Score: {best_score:.0f}")
    print("\nDecrypted message:")
    print("="*60)
    print(decrypted)
    
    # Look for flag
    flags = re.findall(r'USCC\{[^}]+\}', decrypted)
    if flags:
        print("\n" + "="*60)
        print("POSSIBLE FLAG:")
        print("="*60)
        for flag in flags:
            print(flag)
