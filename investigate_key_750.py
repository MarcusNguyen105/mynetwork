#!/usr/bin/env python3

import re

def investigate_key_750():
    # The cipher text
    cipher_text = """
P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
"""

    # Clean up
    cipher_text = re.sub(r'\s+', '', cipher_text.strip())

    print("Investigating connection to key 750...")

    # Maybe the cipher uses 750 as a seed or key for encryption
    # Let's see if there are numerical patterns related to 750

    # Count occurrences of digits
    digits = re.findall(r'\d', cipher_text)
    print(f"Found digits: {digits}")
    print(f"Digit frequency: {len(digits)} total")

    from collections import Counter
    digit_count = Counter(digits)
    print(f"Digit counts: {dict(digit_count)}")

    # Maybe 750 is related to ASCII values or character codes
    print("\nChecking if 750 relates to character codes...")

    # 750 % 256 = 750 - 2*256 = 750 - 512 = 238
    # 750 % 128 = 750 - 5*128 = 750 - 640 = 110
    # 750 % 64 = 750 - 11*64 = 750 - 704 = 46

    print("750 mod 256 =", 750 % 256)
    print("750 mod 128 =", 750 % 128)
    print("750 mod 64 =", 750 % 64)

    # Maybe the cipher is a Vigenère cipher with key 750
    # Or maybe it's using 750 as a seed for a pseudorandom number generator

    # Let's try to see if there's a pattern where each character is shifted by an amount derived from 750

    # Maybe the "750" is not literal, but represents something else

    # Let's look at the final section again and see if I can find more patterns

    final_section = cipher_text.split('*')[-2]  # The second to last section
    print(f"\nFinal section: '{final_section}'")

    # Let's see if I can find more substitution patterns
    # I already know g5 -> US, but maybe there are others

    # Let's try to find what "ZEo|gBoRoJogE" could map to
    # If g5 -> US, maybe other patterns follow similar logic

    # Notice that "g5BRR" becomes "USBRR" with the substitution
    # And "g5oEJgs" becomes "USCC{}" with g5->US, oEJ->CC, gs->{}

    # Maybe I can find what "ZEo|gBoRoJogE" maps to
    # Let's see if there's a pattern like "Z" = ?, "E" = ?, etc.

    # Maybe this is a cipher where certain character combinations represent letters
    # Let's try to see if I can find more such patterns

    print("\nLooking for patterns that might represent common letters or words...")

    # Let's look at the structure of the final section
    parts = final_section.split()
    print(f"Parts: {parts}")

    # The parts are: ['vbR^w8|=^(}^<Q;;)g5BRR%', ':%:_', 'ZEo|gBoRoJogE', 'g5oEJgs']

    # I already know the last part 'g5oEJgs' -> 'USCC{}'
    # Now let's see if I can find patterns in the other parts

    # Let's try applying the same substitution to the entire final section
    result = final_section
    result = result.replace('g5', 'US')
    result = result.replace('oEJ', 'CC')
    result = result.replace('gs', '{}')

    print(f"After substitution: '{result}'")

    # Now I have: 'vbR^w8|=^(}^<Q;;)USBRR% :%:_ ZEo|gBoRoJogE USCC{}'

    # This looks like it might be "USB RR" or something
    # Maybe "USBRR" is "USBRR" and "USCC{}" is the flag

    # Wait, but the flag format is USCC{}, and I have "USCC{}" at the end

    # But let me check if this is indeed the flag by looking at the context

    # Maybe the flag is USCC{750} or something like that

    # Let's see if 750 appears in the decoded text
    if '750' in result:
        print("Found '750' in decoded text!")
        # Find where
        pos = result.find('750')
        context = result[max(0, pos-10):pos+10]
        print(f"Context: '{context}'")

if __name__ == "__main__":
    investigate_key_750()