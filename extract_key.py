#!/usr/bin/env python3
import re
from collections import defaultdict

ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gH8|CR-^S(Cb^}R.RX|8^]|CbR]|C(g|8^HmRX|C(H#}*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^Sb(gb^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

# Remove newlines
cipher_clean = ciphertext.replace('\n', ' ')

# Find all positions of patterns
def find_all(pattern, text):
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            positions.append(i)
    return positions

# Common patterns in ciphertext
patterns = {
    'vbR^': ['The ', 'the '],  # Could be either
    '^|#-^': [' and '],
    '^(}^': [' is '],
    '^|XR^': [' are '],
    '^wHX^': [' for '],
    '^Cb|C^': [' that '],
    '^H#R^': [' one '],
}

print("Finding pattern positions...")
print("="*60)

key_candidates = defaultdict(set)

for cipher_pat, plain_options in patterns.items():
    positions = find_all(cipher_pat, cipher_clean)
    print(f"Pattern '{cipher_pat}' found at {len(positions)} positions: {positions[:5]}")
    
    for pos in positions:
        for plain in plain_options:
            if len(plain) == len(cipher_pat):
                for i in range(len(plain)):
                    kb = ord(cipher_clean[pos + i]) ^ ord(plain[i])
                    key_candidates[pos + i].add(kb)

print("\n" + "="*60)
print("Key candidates per position (first 50):")
print("="*60)

for i in range(min(50, len(cipher_clean))):
    if i in key_candidates:
        if len(key_candidates[i]) == 1:
            kb = list(key_candidates[i])[0]
            print(f"Position {i}: {kb} (confident)")
        else:
            print(f"Position {i}: {key_candidates[i]} (ambiguous)")

# Try to find the key period by looking at confident positions
confident_keys = {}
for pos, candidates in key_candidates.items():
    if len(candidates) == 1:
        confident_keys[pos] = list(candidates)[0]

print("\n" + "="*60)
print(f"Found {len(confident_keys)} confident key positions")
print("="*60)

# Try different periods
for period in range(2, 32):
    # Check if confident keys are consistent with this period
    period_key = [None] * period
    consistent = True
    
    for pos, kb in confident_keys.items():
        key_pos = pos % period
        if period_key[key_pos] is None:
            period_key[key_pos] = kb
        elif period_key[key_pos] != kb:
            consistent = False
            break
    
    if consistent and None not in period_key:
        print(f"\n*** Found consistent key with period {period} ***")
        print(f"Key: {period_key}")
        
        # Decrypt
        result = []
        for i, c in enumerate(cipher_clean):
            result.append(chr(ord(c) ^ period_key[i % period]))
        
        decrypted = ''.join(result)
        print("\n" + "="*60)
        print("DECRYPTED MESSAGE:")
        print("="*60)
        print(decrypted)
        break
