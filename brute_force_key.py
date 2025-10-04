#!/usr/bin/env python3
import string
import re

ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gH8|CR-^S(Cb^}R.RX|8^]|CbR]|C(g|8^HmRX|C(H#}*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^(#(#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^Sb(gb^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

cipher_clean = ciphertext.replace('\n', ' ')

def score_english(text):
    """Score text based on English character frequency"""
    # Common English letters
    common = set(string.ascii_letters + string.digits + ' .,;:!?\'-')
    score = sum(1 for c in text if c in common)
    # Bonus for common words
    text_lower = text.lower()
    for word in ['the', 'and', 'is', 'are', 'for', 'with', 'that', 'this']:
        score += text_lower.count(' ' + word + ' ') * 5
    return score

def decrypt_with_seed(cipher, seed):
    """Try decrypting assuming seed is the initial state"""
    # Simple LCG with common parameters
    params_list = [
        (1103515245, 12345, 2**31),  # glibc
        (134775813, 1, 2**32),  # Borland C/C++
        (214013, 2531011, 2**32),  # MS Visual C++
        (1664525, 1013904223, 2**32),  # Numerical Recipes
        (69069, 0, 2**32),  # VAX
        (65539, 0, 2**31),  # RANDU (IBM)
    ]
    
    results = []
    for a, c, m in params_list:
        state = seed
        decrypted = []
        for ch in cipher:
            key_byte = state & 0xFF  # Use lowest 8 bits
            decrypted.append(chr(ord(ch) ^ key_byte))
            state = (a * state + c) % m
        
        text = ''.join(decrypted)
        score = score_english(text)
        results.append((score, text, a, c, m, seed))
    
    return max(results, key=lambda x: x[0])

print("Brute forcing seed values...")
print("="*60)

best_score = 0
best_result = None

# Try seeds from 0 to 10000
for seed in range(10001):
    if seed % 1000 == 0:
        print(f"Testing seed {seed}...")
    
    score, text, a, c, m, s = decrypt_with_seed(cipher_clean, seed)
    
    if score > best_score:
        best_score = score
        best_result = (score, text, a, c, m, s)
        
        # If score is high enough, we probably found it
        if score > len(cipher_clean) * 0.9:
            print(f"\n*** HIGH SCORE FOUND ***")
            print(f"Seed: {s}")
            print(f"LCG params: a={a}, c={c}, m={m}")
            print(f"Score: {score}/{len(cipher_clean)}")
            print("\nDecrypted text:")
            print("="*60)
            print(text)
            
            # Look for flag
            flags = re.findall(r'USCC\{[^}]+\}', text)
            if flags:
                print("\n" + "="*60)
                print("FLAG FOUND:")
                print("="*60)
                for flag in flags:
                    print(flag)
                break

if best_result and best_score < len(cipher_clean) * 0.9:
    print(f"\nBest result found:")
    score, text, a, c, m, s = best_result
    print(f"Seed: {s}")
    print(f"LCG params: a={a}, c={c}, m={m}")
    print(f"Score: {score}/{len(cipher_clean)}")
    print("\nFirst 300 characters:")
    print(text[:300])
