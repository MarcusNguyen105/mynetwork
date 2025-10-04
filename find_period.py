#!/usr/bin/env python3
from collections import defaultdict

ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gH8|CR-^S(Cb^}R.RX|8^]|CbR]|C(g|8^HmRX|C(H#}*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^m RHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^Sb(gb^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

cipher_clean = ciphertext.replace('\n', ' ')

# Known plaintext mappings from analysis
patterns = {
    'vbR^': 'The ',
    '^|#-^': ' and ',
    '^(}^': ' is ',
    '^|XR^': ' are ',
    '^wHX^': ' for ',
    '^Cb|C^': ' that ',
}

def find_all(pattern, text):
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            positions.append(i)
    return positions

# Extract key bytes
key_map = {}
for cipher_pat, plain in patterns.items():
    positions = find_all(cipher_pat, cipher_clean)
    for pos in positions:
        for i in range(len(plain)):
            key_map[pos + i] = ord(cipher_clean[pos + i]) ^ ord(plain[i])

print(f"Extracted {len(key_map)} key bytes from known patterns")
print("="*60)

# Try to find the period
for period in range(2, 33):
    # Build the repeating key
    period_key = {}
    conflicts = 0
    
    for pos, kb in key_map.items():
        key_idx = pos % period
        if key_idx in period_key:
            if period_key[key_idx] != kb:
                conflicts += 1
        else:
            period_key[key_idx] = kb
    
    coverage = len(period_key) / period
    
    if conflicts == 0 and coverage > 0.5:
        print(f"Period {period}: {len(period_key)}/{period} positions ({100*coverage:.0f}% coverage), 0 conflicts")
        
        if coverage >= 0.9:  # If we have most of the key
            print(f"\n*** Likely key period: {period} ***")
            
            # Fill in missing positions by trying all ASCII printable characters
            if len(period_key) < period:
                print(f"Filling {period - len(period_key)} missing positions...")
                
            # Convert to list
            key_list = []
            for i in range(period):
                if i in period_key:
                    key_list.append(period_key[i])
                else:
                    key_list.append(None)
            
            print(f"Key pattern: {key_list}")
            
            # If we have most of the key, try to complete it
            if key_list.count(None) <= 2:
                # Try to decrypt with what we have
                result = []
                for i, c in enumerate(cipher_clean):
                    kb = key_list[i % period]
                    if kb is not None:
                        result.append(chr(ord(c) ^ kb))
                    else:
                        result.append('?')
                
                partial = ''.join(result)
                print("\nPartial decryption:")
                print("="*60)
                print(partial[:400])
                
                # Try to guess missing bytes
                for missing_idx in [i for i, k in enumerate(key_list) if k is None]:
                    print(f"\nTrying to find key byte at position {missing_idx}...")
                    # Look at characters at this position
                    test_chars = []
                    for i in range(missing_idx, len(cipher_clean), period):
                        test_chars.append(cipher_clean[i])
                    
                    # Try common key bytes
                    for test_kb in [34, 10, 55, 126, 48, 39, 73, 29, 77, 42, 17, 65, 14, 90, 84, 4]:
                        test_result = ''.join([chr(ord(c) ^ test_kb) for c in test_chars])
                        if all(32 <= ord(ch) < 127 for ch in test_result):
                            print(f"  Candidate {test_kb}: '{test_result[:20]}...'")
            
            print(f"\nFull key bytes: {[k for k in key_list if k is not None]}")
            
            break

print("\n" + "="*60)
print("Analyzing key bytes we found:")
print("="*60)
unique_keys = sorted(set(key_map.values()))
print(f"Unique key bytes: {unique_keys}")
