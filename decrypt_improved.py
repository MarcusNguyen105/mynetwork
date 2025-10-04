#!/usr/bin/env python3

ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gH8|CR-^S(Cb^}R.RX|8^]|CbR]|C(g|8^HmRX|C(H#}*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^Sb(gb^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

def xor_bytes(b1, b2):
    """XOR two byte strings"""
    return bytes([a ^ b for a, b in zip(b1, b2)])

def try_decrypt(ciphertext, key):
    """Try to decrypt with a repeating key"""
    result = []
    key_len = len(key)
    key_idx = 0
    
    for char in ciphertext:
        if char == '\n':
            result.append('\n')
            continue
        result.append(chr(ord(char) ^ key[key_idx % key_len]))
        key_idx += 1
    
    return ''.join(result)

# We know "vbR^" -> "The "
# Let's try to find more mappings by guessing common phrases

# Looking at the ciphertext structure, let me try to identify more patterns
# "vbR^]RCbH-^XRmXR}R#C}" likely starts with "The method represent"

# Let's try different key lengths and see which makes sense
# First, let's see what we get with different assumptions

print("Testing different known plaintexts...")
print("="*60)

# Try: "vbR^]RCbH-" -> "The method"
known_pairs = [
    ("The ", "vbR^"),
    ("The method", "vbR^]RCbH-"),
    (" and ", "^|#-^"),
    (" is ", "^(}^"),
    (" are ", "^|XR^"),
    (" for ", "^wHX^"),
]

for plain, cipher in known_pairs:
    if len(plain) == len(cipher):
        key_bytes = xor_bytes(plain.encode(), cipher.encode())
        print(f"'{plain}' -> '{cipher}': key = {list(key_bytes)}")

# Let's extract key using "vbR^]RCbH-" -> "The method"
test_plain = "The method"
test_cipher = "vbR^]RCbH-"
key = list(xor_bytes(test_plain.encode(), test_cipher.encode()))
print(f"\nExtracted key from 'The method': {key}")
print(f"Key length: {len(key)}")

# Try decryption
result = try_decrypt(ciphertext, key)
print("\n" + "="*60)
print("Decryption with 10-byte key:")
print("="*60)
print(result[:500])

# If that doesn't work perfectly, let's try to find the correct key length
# by testing common key lengths

print("\n" + "="*60)
print("Testing different key lengths...")
print("="*60)

for key_len in [4, 8, 10, 16, 32]:
    # Use only the first key_len bytes
    test_key = key[:key_len]
    result = try_decrypt(ciphertext, test_key)
    print(f"\nKey length {key_len}:")
    print(result[:200])
    print("...")
