#!/usr/bin/env python3
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

def score_text(text):
    """Quick scoring function"""
    score = sum(1 for c in text if 32 <= ord(c) < 127)
    text_lower = text.lower()
    score += text_lower.count(' the ') * 20
    score += text_lower.count(' and ') * 20
    score += text_lower.count(' is ') * 15
    score += text_lower.count(' are ') * 15
    return score

print("Testing focused set of LCG parameters...")
print("="*60)

# Test specific well-known LCG parameters, plus simple variations
lcg_params = [
    # (a, c, m, name)
    (1103515245, 12345, 2**31, "glibc"),
    (214013, 2531011, 2**32, "MSVC"),
    (134775813, 1, 2**32, "Borland"),
    (1664525, 1013904223, 2**32, "Numerical Recipes"),
    (69069, 0, 2**32, "VAX"),
    (65539, 0, 2**31, "RANDU"),
    # Simple 8-bit LCGs
    (5, 1, 256, "Simple 5,1"),
    (7, 1, 256, "Simple 7,1"),
    (13, 7, 256, "Simple 13,7"),
    (21, 5, 256, "Simple 21,5"),
    (17, 3, 256, "Simple 17,3"),
    (25, 7, 256, "Simple 25,7"),
    (69, 71, 256, "Simple 69,71"),
    (181, 97, 256, "Combo 181,97"),
]

best_overall = (0, None, None)

for a, c, m, name in lcg_params:
    print(f"\nTesting {name}: a={a}, c={c}, m={m}")
    best_for_param = (0, None, None)
    
    # Try seeds from 0 to 10000
    for seed in range(min(10001, m)):
        if seed % 1000 == 0 and seed > 0:
            print(f"  Testing seed {seed}...")
        
        # Generate keystream
        x = seed
        keystream = []
        for _ in range(len(cipher_clean)):
            keystream.append(x & 0xFF)  # Use lowest 8 bits for XOR
            x = (a * x + c) % m
        
        # Decrypt
        decrypted = ''.join([chr(ord(cipher_clean[i]) ^ keystream[i]) for i in range(len(cipher_clean))])
        
        # Score
        score = score_text(decrypted)
        
        if score > best_for_param[0]:
            best_for_param = (score, seed, decrypted)
        
        if score > best_overall[0]:
            best_overall = (score, (a, c, m, name, seed), decrypted)
            
        # If very high score, we found it
        if score > 1500:
            print(f"\n*** HIGH SCORE: {score} ***")
            print(f"{name}: seed = {seed}")
            print("\nDecrypted:")
            print(decrypted)
            
            flags = re.findall(r'USCC\{[^}]+\}', decrypted)
            if flags:
                print("\n" + "="*60)
                print("FLAG FOUND:")
                print("="*60)
                for flag in flags:
                    print(flag)
                exit(0)
    
    score, seed, decrypted = best_for_param
    print(f"  Best score for {name}: {score} (seed={seed})")
    if score > 100:
        print(f"  Preview: {decrypted[:100]}")

print("\n" + "="*60)
print("BEST OVERALL RESULT:")
print("="*60)
if best_overall[1]:
    score, (a, c, m, name, seed), decrypted = best_overall
    print(f"{name}: a={a}, c={c}, m={m}, seed={seed}")
    print(f"Score: {score}")
    print("\nDecrypted:")
    print(decrypted)
    
    flags = re.findall(r'USCC\{[^}]+\}', decrypted)
    if flags:
        print("\n" + "="*60)
        print("POSSIBLE FLAG:")
        print("="*60)
        for flag in flags:
            print(flag)
