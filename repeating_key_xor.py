#!/usr/bin/env python3
import re
from collections import Counter, defaultdict

ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gH8|CR-^S(Cb^}R.RX|8^]|CbR]|C(g|8^HmRX|C(H#}*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^(#(#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p}^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^Sb(gb^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

cipher_clean = ciphertext.replace('\n', ' ')

# Find repeating patterns to determine key length
def find_repeats(text, min_len=3):
    """Find repeating substrings"""
    repeats = defaultdict(list)
    for length in range(min_len, min(20, len(text)//2)):
        for i in range(len(text) - length):
            substring = text[i:i+length]
            repeats[substring].append(i)
    
    # Filter to patterns that repeat
    return {k: v for k, v in repeats.items() if len(v) > 1}

repeats = find_repeats(cipher_clean, min_len=4)

# Sort by number of occurrences
sorted_repeats = sorted(repeats.items(), key=lambda x: len(x[1]), reverse=True)

print("Top repeating patterns:")
print("="*60)
for pattern, positions in sorted_repeats[:15]:
    if len(positions) >= 2:
        # Calculate distances between occurrences
        distances = [positions[i+1] - positions[i] for i in range(len(positions)-1)]
        print(f"'{pattern}' ({len(pattern)} chars): {len(positions)} times at {positions[:5]}")
        print(f"  Distances: {distances[:5]}")

# Calculate GCD of distances to find likely key length
from math import gcd
from functools import reduce

all_distances = []
for pattern, positions in repeats.items():
    if len(positions) >= 2:
        distances = [positions[i+1] - positions[i] for i in range(len(positions)-1)]
        all_distances.extend(distances)

if all_distances:
    overall_gcd = reduce(gcd, all_distances)
    print(f"\n GCD of all distances: {overall_gcd}")
    print(f"Likely key lengths: factors of {overall_gcd}")
    
    # Find factors
    factors = []
    for i in range(2, min(overall_gcd + 1, 100)):
        if overall_gcd % i == 0:
            factors.append(i)
    print(f"Factors: {factors[:20]}")

# Use "vbR^" -> "The " to extract key bytes
def find_all_occurrences(pattern, text):
    positions = []
    start = 0
    while True:
        pos = text.find(pattern, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions

vbr_positions = find_all_occurrences("vbR^", cipher_clean)
print(f"\n'vbR^' found at positions: {vbr_positions}")

# Extract key bytes from known plaintext
key_map = {}
for pos in vbr_positions:
    for i, (c, p) in enumerate(zip("vbR^", "The ")):
        key_map[pos + i] = ord(c) ^ ord(p)

# Try to determine key length from positions
if len(vbr_positions) >= 2:
    vbr_distances = [vbr_positions[i+1] - vbr_positions[i] for i in range(len(vbr_positions)-1)]
    print(f"Distances between 'vbR^': {vbr_distances}")
    
    if len(vbr_distances) >= 2:
        vbr_gcd = reduce(gcd, vbr_distances)
        print(f"GCD of 'vbR^' distances: {vbr_gcd}")

# Try key lengths based on patterns
print("\n" + "="*60)
print("Trying to reconstruct key...")
print("="*60)

# Add more known patterns
patterns_known = {
    'vbR^': 'The ',
    '^|#-^': ' and ',
    '^(}^': ' is ',
    '^|XR^': ' are ',
    '^wHX^': ' for ',
    'k;p}': 'LCGs',
    '^Cb|C^': ' that ',
}

for cipher_pat, plain in patterns_known.items():
    positions = find_all_occurrences(cipher_pat, cipher_clean)
    for pos in positions:
        for i in range(len(plain)):
            key_map[pos + i] = ord(cipher_clean[pos + i]) ^ ord(plain[i])

print(f"Extracted {len(key_map)} key bytes from known patterns")

# Determine key length
possible_key_lengths = [4, 8, 16, 32, 64, 97, 141]  # Including some from GCD analysis

for key_len in possible_key_lengths:
    # Try to reconstruct key
    reconstructed_key = [None] * key_len
    conflicts = 0
    
    for pos, kb in key_map.items():
        key_idx = pos % key_len
        if reconstructed_key[key_idx] is None:
            reconstructed_key[key_idx] = kb
        elif reconstructed_key[key_idx] != kb:
            conflicts += 1
    
    filled = sum(1 for x in reconstructed_key if x is not None)
    
    if conflicts == 0 and filled > key_len * 0.5:
        print(f"\nKey length {key_len}: {filled}/{key_len} filled, 0 conflicts")
        print(f"Key (partially): {reconstructed_key}")
        
        # Try to decrypt
        result = []
        for i, c in enumerate(cipher_clean):
            kb = reconstructed_key[i % key_len]
            if kb is not None:
                result.append(chr(ord(c) ^ kb))
            else:
                result.append('?')
        
        decrypted = ''.join(result)
        print(f"Partial decryption (first 300 chars):")
        print(decrypted[:300])
        
        # Count question marks
        unknown = decrypted.count('?')
        print(f"Unknown characters: {unknown}/{len(decrypted)}")
        
        if unknown < len(decrypted) * 0.1:  # Less than 10% unknown
            print("\n*** This looks promising! ***")
            print("Full decryption:")
            print(decrypted)
            
            # Look for flag
            flags = re.findall(r'USCC\{[^}]+\}', decrypted)
            if flags:
                print("\n" + "="*60)
                print("FLAG FOUND:")
                print("="*60)
                for flag in flags:
                    print(flag)
