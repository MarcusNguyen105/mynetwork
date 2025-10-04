#!/usr/bin/env python3

ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gH8|CR-^S(Cb^}R.RX|8^]|CbR]|C(g|8^HmRX|C(H#}*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

# Let's try known plaintext attack
# Assuming "vbR" -> "The" (very likely since "vbR" appears frequently like "the" in English)

def xor_bytes(b1, b2):
    """XOR two byte strings"""
    return bytes([a ^ b for a, b in zip(b1, b2)])

# Known plaintext: "The" -> "vbR"
known_plain = "The"
known_cipher = "vbR"

# Extract key bytes
key_bytes = xor_bytes(known_plain.encode(), known_cipher.encode())
print(f"Key bytes from 'The' -> 'vbR': {key_bytes.hex()}")
print(f"Key bytes as integers: {list(key_bytes)}")

# Let's try more known plaintext
# "is" is common, and "(}" appears to be 2 chars which matches
# Let's assume the pattern and try to find the key stream

# First, let's see if the key repeats
def try_key_length(ciphertext, key):
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

# Try the key we found
print("\n" + "="*50)
print("Attempting decryption with extracted key bytes:")
print("="*50)

partial_decrypt = try_key_length(ciphertext, key_bytes)
print(partial_decrypt[:200])

# Let's also try to find more of the key by assuming more common words
# "and" is very common
print("\n" + "="*50)
print("Looking for more patterns...")
print("="*50)

# Let's try a different approach - brute force the key if it's short
# Or test if it's a simple LCG

# Common LCG parameters
def lcg(seed, a, c, m):
    """Linear Congruential Generator"""
    while True:
        seed = (a * seed + c) % m
        yield seed

# Let's try to find the key by assuming the first word is "A"
first_char_cipher = ord('P')
# Common starting words: "A", "I", "The", etc.
possible_first_chars = ['A', 'I', 'T', 'W', 'Y', 'S']

for first_char in possible_first_chars:
    key_byte = ord('P') ^ ord(first_char)
    print(f"\nIf first char is '{first_char}', key byte = {key_byte} ({chr(key_byte) if 32 <= key_byte < 127 else '?'})")

# Let's also try to extend our key by looking at more patterns
# If "vbR^" -> "The ", we can get 4 key bytes
known_plain_ext = "The "
known_cipher_ext = "vbR^"
key_bytes_ext = xor_bytes(known_plain_ext.encode(), known_cipher_ext.encode())
print(f"\nExtended key bytes from 'The ' -> 'vbR^': {list(key_bytes_ext)}")

# Try decryption with extended key
partial_decrypt = try_key_length(ciphertext, key_bytes_ext)
print("\n" + "="*50)
print("Decryption attempt with 4-byte key:")
print("="*50)
print(partial_decrypt[:400])
