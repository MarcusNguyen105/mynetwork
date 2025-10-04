#!/usr/bin/env python3
from collections import defaultdict

ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gH8|CR-^S(Cb^}R.RX|8^]|CbR]|C(g|8^HmRX|C(H#}*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^(#(#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^Sb(gb^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

cipher_clean = ciphertext.replace('\n', ' ')

# We know "The " -> "vbR^"
known_plain = "The "
known_cipher = "vbR^"

# Extract key from this
base_key = [ord(c) ^ ord(p) for c, p in zip(known_cipher, known_plain)]
print(f"Base key from 'The ': {base_key}")
print("="*60)

# Try each period from 4 to 32
for period in [4, 8, 16, 32, 10, 12, 20, 24]:
    print(f"\nTrying period {period}...")
    
    # Extend the base key to this period
    test_key = base_key[:period] if len(base_key) >= period else base_key + [0] * (period - len(base_key))
    
    # Decrypt
    result = []
    for i, c in enumerate(cipher_clean):
        result.append(chr(ord(c) ^ test_key[i % len(base_key)]))
    
    decrypted = ''.join(result)
    print(f"First 200 chars: {decrypted[:200]}")
    
    # Check if it looks like English
    printable_count = sum(1 for ch in decrypted[:200] if 32 <= ord(ch) < 127)
    print(f"Printable ratio: {printable_count}/200 = {100*printable_count/200:.1f}%")

# Now let's try a smarter approach - use frequency analysis
# Space is the most common character, and we see ^ is very common
print("\n" + "="*60)
print("Character frequency analysis:")
print("="*60)

from collections import Counter
char_freq = Counter(cipher_clean)
most_common = char_freq.most_common(10)
print("Most common characters:")
for ch, count in most_common:
    print(f"  '{ch}': {count} times")

# ^ is likely space (already confirmed)
# Let's use this to find more of the key

# Try period 4 with refinement
print("\n" + "="*60)
print("Refined approach with period 4:")
print("="*60)

key = base_key  # [34, 10, 55, 126]
result = []
for i, c in enumerate(cipher_clean):
    result.append(chr(ord(c) ^ key[i % len(key)]))

decrypted = ''.join(result)
print("Full decryption with period 4:")
print("="*60)
print(decrypted)

# Check if there are any non-ASCII characters
non_ascii = [(i, ch) for i, ch in enumerate(decrypted) if ord(ch) < 32 or ord(ch) >= 127]
if non_ascii:
    print(f"\n{len(non_ascii)} non-ASCII characters found at positions: {[i for i, _ in non_ascii[:10]]}")
