#!/usr/bin/env python3

import re

def analyze_more_patterns():
    # The full cipher text
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

    print("Looking for more substitution patterns...")

    # I already know g5 -> US, oEJ -> CC, gs -> {}
    # Let me see what other patterns I can find

    # Look for other repeated patterns that might correspond to common words
    print("Common 3-letter combinations that appear multiple times:")

    # Find all 3-letter combinations and their frequencies
    patterns_3 = {}
    for i in range(len(cipher_text) - 2):
        pattern = cipher_text[i:i+3]
        patterns_3[pattern] = patterns_3.get(pattern, 0) + 1

    # Sort by frequency
    sorted_3 = sorted(patterns_3.items(), key=lambda x: x[1], reverse=True)

    print("Top 3-letter patterns:")
    for pattern, count in sorted_3[:20]:
        print(f"  '{pattern}': {count}")

    # Look for patterns that might be related to the flag
    print("\nLooking for patterns that could be related to USCC{}")

    # Check if any of these patterns, when substituted, give flag-like results
    test_patterns = ['^Cb', 'CbR', 'bR^', 'R^w', 'w8|', '8|=', '|=^', '=^(', '^(}', '^}<', '}<Q', '<Q;', 'Q;;', ';;)', ';)g', ')g5', 'g5B', '5BR', 'BRR', 'RR%', 'R% ', '% :', ' :%', ':%:', '%:_', ':_ ', '_ Z', ' ZE', 'ZEo', 'Eo|', 'o|g', '|gB', 'gBo', 'BoR', 'oRo', 'RoJ', 'oJo', 'Jog', 'ogE', 'gE ', 'E g', ' g5', 'g5o', '5oE', 'oEJ', 'EJg', 'Jgs']

    print("\nTesting individual patterns for substitution...")

    # I need to think of what other common patterns might exist
    # Maybe the cipher is using a key of 750, and each character is shifted by some amount

    # Let's try to understand if this is a Caesar cipher or similar
    print("\nTrying to understand if this is a shift cipher...")

    # Let's take a sample and try different shifts
    sample = "g5oEJgs"
    print(f"Sample: '{sample}'")

    for shift in range(1, 26):
        result = ''
        for char in sample:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                shifted = chr((ord(char) - base - shift) % 26 + base)
                result += shifted
            else:
                result += char

        print(f"Shift {shift}: '{result}'")

    # Let's also check the final section
    final_sample = "vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs"
    print(f"\nFinal section: '{final_sample}'")

    # Try to see if this could be base64 or other encoding
    import base64
    try:
        # Remove non-base64 chars
        cleaned = re.sub(r'[^A-Za-z0-9+/=]', '', final_sample)
        print(f"Cleaned for base64: '{cleaned}'")
        decoded = base64.b64decode(cleaned)
        print(f"Base64 decode: '{decoded.decode('utf-8', errors='ignore')}'")
    except Exception as e:
        print(f"Base64 failed: {e}")

if __name__ == "__main__":
    analyze_more_patterns()