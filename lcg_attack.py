#!/usr/bin/env python3
"""
Attack on LCG-based stream cipher.
LCG formula: X_{n+1} = (a * X_n + c) mod m

Common parameters:
- Java: a=25214903917, c=11, m=2^48
- glibc: a=1103515245, c=12345, m=2^31
- MINSTD: a=48271, c=0, m=2^31-1
- Simple: often m=256 for byte-oriented ciphers
"""

ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gH8|CR-^S(Cb^}R.RX|8^]|CbR]|C(g|8^HmRX|C(H#}*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^(#(#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^Sb(gb^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

cipher_clean = ciphertext.replace('\n', ' ')

# Let's assume the plaintext starts with a common phrase about RNGs/LCGs
# Try different starting phrases
guesses = [
    "A linear congruential",
    "The linear congruential",
    "A pseudorandom number",
    "The pseudorandom number",
]

def try_lcg_params(keystream, m_values=[256, 255, 128, 512]):
    """Try to find LCG parameters from keystream"""
    if len(keystream) < 3:
        return None
    
    for m in m_values:
        # Assume keystream values are from LCG mod m
        # X_1, X_2, X_3 are consecutive outputs
        # X_2 = a*X_1 + c (mod m)
        # X_3 = a*X_2 + c (mod m)
        # Solving: X_3 - X_2 = a*(X_2 - X_1) (mod m)
        
        x0, x1, x2 = keystream[0] % m, keystream[1] % m, keystream[2] % m
        
        # Try to find 'a'
        diff1 = (x1 - x0) % m
        diff2 = (x2 - x1) % m
        
        if diff1 == 0:
            continue
        
        # a = diff2 / diff1 (mod m)
        # Need modular inverse
        try:
            # Extended Euclidean algorithm for modular inverse
            def modinv(a, m):
                if a < 0:
                    a = (a % m + m) % m
                g, x, _ = extended_gcd(a, m)
                if g != 1:
                    return None
                return x % m
            
            def extended_gcd(a, b):
                if a == 0:
                    return b, 0, 1
                gcd, x1, y1 = extended_gcd(b % a, a)
                x = y1 - (b // a) * x1
                y = x1
                return gcd, x, y
            
            inv_diff1 = modinv(diff1, m)
            if inv_diff1 is not None:
                a = (diff2 * inv_diff1) % m
                c = (x1 - a * x0) % m
                
                # Verify
                valid = True
                for i in range(len(keystream) - 1):
                    expected = (a * keystream[i] + c) % m
                    actual = keystream[i + 1] % m
                    if expected != actual:
                        valid = False
                        break
                
                if valid:
                    return (a, c, m, keystream[0])
        except:
            continue
    
    return None

print("Trying to extract keystream and find LCG parameters...")
print("="*60)

for guess in guesses:
    print(f"\nTrying plaintext: '{guess}'...")
    
    if len(guess) > len(cipher_clean):
        continue
    
    # Extract keystream
    keystream = [ord(cipher_clean[i]) ^ ord(guess[i]) for i in range(len(guess))]
    print(f"First 20 keystream bytes: {keystream[:20]}")
    
    # Try to find LCG parameters
    params = try_lcg_params(keystream)
    
    if params:
        a, c, m, seed = params
        print(f"\n*** FOUND LCG PARAMETERS ***")
        print(f"a = {a}")
        print(f"c = {c}")
        print(f"m = {m}")
        print(f"seed = {seed}")
        
        # Generate full keystream and decrypt
        def lcg_stream(seed, a, c, m, length):
            result = []
            x = seed
            for _ in range(length):
                result.append(x % 256)  # Use mod 256 for XOR cipher
                x = (a * x + c) % m
            return result
        
        full_keystream = lcg_stream(seed, a, c, m, len(cipher_clean))
        decrypted = ''.join([chr(ord(cipher_clean[i]) ^ full_keystream[i]) for i in range(len(cipher_clean))])
        
        print("\n" + "="*60)
        print("DECRYPTED MESSAGE:")
        print("="*60)
        print(decrypted)
        
        # Look for the flag
        import re
        flags = re.findall(r'USCC\{[^}]+\}', decrypted)
        if flags:
            print("\n" + "="*60)
            print("FLAG FOUND:")
            print("="*60)
            for flag in flags:
                print(flag)
        
        break
else:
    print("\nNo valid LCG parameters found with these guesses.")
    print("Let me try a brute force approach with different starting bytes...")