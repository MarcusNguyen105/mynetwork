#!/usr/bin/env python3
import re
from collections import defaultdict

ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gH8|CR-^S(Cb^}R.RX|8^]|CbR]|C(g|8^HmRX|C(H#}*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^(#(#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p}^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^Sb(gb^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

cipher_clean = ciphertext.replace('\n', ' ')

# Known patterns
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

patterns_known = {
    'vbR^': 'The ',
    '^|#-^': ' and ',
    '^(}^': ' is ',
    '^|XR^': ' are ',
    '^wHX^': ' for ',
    '^Cb|C^': ' that ',
}

# Extract key bytes
key_map = {}
for cipher_pat, plain in patterns_known.items():
    positions = find_all_occurrences(cipher_pat, cipher_clean)
    for pos in positions:
        for i in range(len(plain)):
            key_map[pos + i] = ord(cipher_clean[pos + i]) ^ ord(plain[i])

print(f"Extracted {len(key_map)} key bytes from known patterns")
print("="*60)

# Try various key lengths
test_key_lengths = list(range(2, 150)) + [256]

best_results = []

for key_len in test_key_lengths:
    # Reconstruct key
    reconstructed_key = {}
    conflicts = 0
    
    for pos, kb in key_map.items():
        key_idx = pos % key_len
        if key_idx in reconstructed_key:
            if reconstructed_key[key_idx] != kb:
                conflicts += 1
        else:
            reconstructed_key[key_idx] = kb
    
    filled = len(reconstructed_key)
    coverage = filled / key_len
    
    # Only consider keys with good coverage and no conflicts
    if conflicts == 0 and coverage >= 0.7:
        best_results.append((key_len, coverage, reconstructed_key))
        print(f"Key length {key_len}: {filled}/{key_len} = {100*coverage:.1f}% coverage, 0 conflicts")

if not best_results:
    print("No perfect key lengths found. Showing top candidates with some conflicts:")
    
    # Show top candidates even with conflicts
    candidates = []
    for key_len in test_key_lengths:
        reconstructed_key = {}
        conflicts = 0
        
        for pos, kb in key_map.items():
            key_idx = pos % key_len
            if key_idx in reconstructed_key:
                if reconstructed_key[key_idx] != kb:
                    conflicts += 1
            else:
                reconstructed_key[key_idx] = kb
        
        filled = len(reconstructed_key)
        coverage = filled / key_len
        
        if coverage >= 0.5:
            candidates.append((key_len, coverage, conflicts, reconstructed_key))
    
    # Sort by fewest conflicts, then best coverage
    candidates.sort(key=lambda x: (x[2], -x[1]))
    
    for key_len, coverage, conflicts, reconstructed_key in candidates[:10]:
        print(f"Key length {key_len}: {len(reconstructed_key)}/{key_len} = {100*coverage:.1f}% coverage, {conflicts} conflicts")

# Try the best candidate(s)
print("\n" + "="*60)
print("Testing best candidates:")
print("="*60)

for key_len, coverage, data in best_results[:5] if best_results else [(candidates[0][0], candidates[0][1], candidates[0][3]) for candidates in [candidates] if candidates][:5]:
    reconstructed_key = data if isinstance(data, dict) else {}
    
    # Convert to list
    key_list = []
    for i in range(key_len):
        if i in reconstructed_key:
            key_list.append(reconstructed_key[i])
        else:
            # Try to guess missing bytes (most common: 126 for space)
            key_list.append(126)  # Default guess
    
    # Decrypt
    result = []
    for i, c in enumerate(cipher_clean):
        result.append(chr(ord(c) ^ key_list[i % key_len]))
    
    decrypted = ''.join(result)
    
    print(f"\nKey length {key_len}:")
    print(f"First 200 chars: {decrypted[:200]}")
    
    # Count printable characters
    printable = sum(1 for ch in decrypted if 32 <= ord(ch) < 127)
    print(f"Printable: {printable}/{len(decrypted)} = {100*printable/len(decrypted):.1f}%")
    
    if printable / len(decrypted) > 0.95:
        print("\n*** HIGH QUALITY DECRYPTION ***")
        print("Full text:")
        print(decrypted)
        
        # Look for flag
        flags = re.findall(r'USCC\{[^}]+\}', decrypted)
        if flags:
            print("\n" + "="*60)
            print("FLAG FOUND:")
            print("="*60)
            for flag in flags:
                print(flag)
            break
