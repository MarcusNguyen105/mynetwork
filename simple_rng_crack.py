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

# Try the simplest possible RNG: just incrementing counter or simple operations
# Try: key[i] = (seed + i * multiplier) % 256

print("Trying simple RNG formulas...")
print("="*60)

# We know first 4 bytes should give us "The " from "P^8("
known_plain = "A linear "
known_cipher = cipher_clean[:len(known_plain)]

# Extract expected keystream
expected_keystream = [ord(c) ^ ord(p) for c, p in zip(known_cipher, known_plain)]
print(f"Expected keystream for '{known_plain}': {expected_keystream}")

# Try to find pattern
# Test formula: key[i] = (seed + i * mult) % mod
for mod in [256, 255, 128]:
    for mult in range(1, 256):
        for seed in range(256):
            # Generate keystream
            generated = [(seed + i * mult) % mod for i in range(len(expected_keystream))]
            
            if generated == expected_keystream:
                print(f"\n*** FOUND MATCH ***")
                print(f"Formula: key[i] = (seed + i * mult) % mod")
                print(f"seed = {seed}, mult = {mult}, mod = {mod}")
                
                # Decrypt full message
                full_key = [(seed + i * mult) % mod for i in range(len(cipher_clean))]
                decrypted = ''.join([chr(ord(cipher_clean[i]) ^ full_key[i]) for i in range(len(cipher_clean))])
                
                print("\nDecrypted:")
                print(decrypted[:300])
                
                # Check if it looks good
                printable = sum(1 for ch in decrypted if 32 <= ord(ch) < 127)
                print(f"\nPrintable: {printable}/{len(decrypted)}")
                
                if printable / len(decrypted) > 0.95:
                    print("\nFull message:")
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
        else:
            continue
        break
    else:
        continue
    break
else:
    print("\nNo match found with simple additive formula.")
    print("Let me try simple LCG with small parameters...")
    
    # Try simple LCG: X_{n+1} = (a * X_n + c) % m
    for m in [256]:
        for a in [1, 5, 7, 13, 17, 21, 25, 29, 33, 37, 41, 45, 69, 85, 101, 117, 133, 149, 165, 181, 197, 213, 229, 245]:
            for c in range(256):
                for seed in range(256):
                    # Generate keystream
                    x = seed
                    generated = []
                    for _ in range(len(expected_keystream)):
                        generated.append(x % 256)
                        x = (a * x + c) % m
                    
                    if generated == expected_keystream:
                        print(f"\n*** FOUND LCG MATCH ***")
                        print(f"a = {a}, c = {c}, m = {m}, seed = {seed}")
                        
                        # Decrypt full message
                        x = seed
                        full_key = []
                        for _ in range(len(cipher_clean)):
                            full_key.append(x % 256)
                            x = (a * x + c) % m
                        
                        decrypted = ''.join([chr(ord(cipher_clean[i]) ^ full_key[i]) for i in range(len(cipher_clean))])
                        
                        print("\nFull message:")
                        print(decrypted)
                        
                        # Look for flag
                        flags = re.findall(r'USCC\{[^}]+\}', decrypted)
                        if flags:
                            print("\n" + "="*60)
                            print("FLAG FOUND:")
                            print("="*60)
                            for flag in flags:
                                print(flag)
                        exit(0)
