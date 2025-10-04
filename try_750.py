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

print("Trying seed = 750 with various RNG algorithms...")
print("="*60)

# Try different LCG parameters with seed=750
lcg_params = [
    (1103515245, 12345, 2**31, "glibc"),
    (214013, 2531011, 2**32, "MSVC"),
    (134775813, 1, 2**32, "Borland"),
    (1664525, 1013904223, 2**32, "Numerical Recipes"),
    (69069, 0, 2**32, "VAX"),
    (65539, 0, 2**31, "RANDU"),
    # 8-bit LCGs
    (5, 1, 256, "Simple 5,1"),
    (7, 1, 256, "Simple 7,1"),
    (13, 7, 256, "Simple 13,7"),
    (21, 5, 256, "Simple 21,5"),
    (17, 3, 256, "Simple 17,3"),
    (25, 7, 256, "Simple 25,7"),
    (69, 71, 256, "Simple 69,71"),
    (181, 97, 256, "Combo 181,97"),
]

for a, c, m, name in lcg_params:
    print(f"\nTesting {name} with seed=750:")
    print(f"  a={a}, c={c}, m={m}")
    
    # Generate keystream
    x = 750
    keystream = []
    for _ in range(len(cipher_clean)):
        keystream.append(x & 0xFF)
        x = (a * x + c) % m
    
    # Decrypt
    decrypted = ''.join([chr(ord(cipher_clean[i]) ^ keystream[i]) for i in range(len(cipher_clean))])
    
    # Check quality
    printable = sum(1 for ch in decrypted if 32 <= ord(ch) < 127)
    print(f"  Printable: {printable}/{len(cipher_clean)} = {100*printable/len(cipher_clean):.1f}%")
    print(f"  First 150 chars: {decrypted[:150]}")
    
    if printable / len(cipher_clean) > 0.95:
        print("\n" + "="*60)
        print("*** LIKELY SOLUTION FOUND ***")
        print("="*60)
        print(f"{name}: seed=750, a={a}, c={c}, m={m}")
        print("\nFull decrypted message:")
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
