#!/usr/bin/env python3
import re
import string

ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gH8|CR-^S(Cb^}R.RX|8^]|CbR]|C(g|8^HmRX|C(H#}*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^(#(#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^Sb(gb^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

cipher_clean = ciphertext.replace('\n', ' ')

def xor_with_key(text, key):
    """XOR text with repeating key"""
    result = []
    for i, c in enumerate(text):
        result.append(chr(ord(c) ^ ord(key[i % len(key)])))
    return ''.join(result)

def score_text(text):
    """Score decrypted text"""
    score = sum(1 for c in text if 32 <= ord(c) < 127)
    text_lower = text.lower()
    score += text_lower.count(' the ') * 30
    score += text_lower.count(' and ') * 25
    score += text_lower.count(' is ') * 20
    score += text_lower.count(' are ') * 20
    score += text_lower.count(' for ') * 20
    return score

print("Trying common passphrases and patterns...")
print("="*60)

# Common passphrases and patterns
test_keys = [
    "password", "PASSWORD", "key", "KEY", "secret", "SECRET",
    "admin", "ADMIN", "test", "TEST",
    "123", "1234", "12345", "123456",
    "abc", "ABC", "abcd", "ABCD",
    "lcg", "LCG", "rng", "RNG", "random", "RANDOM",
    "cipher", "CIPHER", "crypto", "CRYPTO",
    "uscc", "USCC", "CTF", "ctf",
    "flag", "FLAG",
    # Challenge-specific
    "seed", "SEED", "lost", "LOST",
]

# Add single-byte keys
for i in range(256):
    test_keys.append(chr(i))

# Add two-byte patterns
for i in range(32, 127):
    for j in range(32, 127):
        test_keys.append(chr(i) + chr(j))

best_score = 0
best_result = None

print(f"Testing {len(test_keys)} different keys...")

for key_idx, key in enumerate(test_keys):
    if key_idx % 1000 == 0 and key_idx > 0:
        print(f"  Tested {key_idx}/{len(test_keys)} keys... Best score: {best_score}")
    
    try:
        decrypted = xor_with_key(cipher_clean, key)
        score = score_text(decrypted)
        
        if score > best_score:
            best_score = score
            best_result = (key, decrypted)
            
            if score > 1500:
                print(f"\n*** HIGH SCORE: {score} with key: {repr(key)} ***")
                print(decrypted[:300])
    except:
        pass

print("\n" + "="*60)
print("BEST RESULT:")
print("="*60)
if best_result:
    key, decrypted = best_result
    print(f"Key: {repr(key)}")
    print(f"Score: {best_score}")
    print("\nDecrypted message:")
    print(decrypted)
    
    # Look for flag
    flags = re.findall(r'USCC\{[^}]+\}', decrypted)
    if flags:
        print("\n" + "="*60)
        print("FLAG FOUND:")
        print("="*60)
        for flag in flags:
            print(flag)
