#!/usr/bin/env python3

import re

def analyze_cipher_structure():
    # The cipher text from the user's message
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

    # Clean up the text - remove extra whitespace and newlines
    cipher_text = re.sub(r'\s+', '', cipher_text.strip())

    # Split into sections by *
    sections = cipher_text.split('*')
    print(f"Number of sections: {len(sections)}")

    for i, section in enumerate(sections):
        print(f"\nSection {i}: (length {len(section)})")
        print(f"'{section}'")

        # Analyze each section
        if section:
            # Character frequency for this section
            char_freq = {}
            for char in section:
                char_freq[char] = char_freq.get(char, 0) + 1

            print("Character frequency:")
            for char in sorted(char_freq.keys()):
                print(f"  '{char}': {char_freq[char]}")

    # Look for the pattern "750" or related numbers
    print("\nSearching for '750' pattern:")
    if '750' in cipher_text:
        print("Found '750' in cipher text")
        # Find position
        pos = cipher_text.find('750')
        print(f"Position: {pos}")
        print(f"Context: '{cipher_text[max(0, pos-10):pos+10]}'")
    else:
        print("'750' not found literally")

    # Look for other number patterns
    print("\nNumber-like patterns in text:")
    number_pattern = re.findall(r'\d+', cipher_text)
    for num in number_pattern:
        print(f"Found number: {num}")

    # Check for patterns that might represent numbers
    print("\nPotential number encodings:")
    # Look for patterns like digit-like sequences
    for i in range(len(cipher_text) - 2):
        triplet = cipher_text[i:i+3]
        if all(c in '0123456789' for c in triplet):
            print(f"Found digit triplet '{triplet}' at position {i}")

    # Look at the last section more carefully
    last_section = sections[-1]
    print(f"\nLast section: '{last_section}'")
    print(f"Last section length: {len(last_section)}")

    # Try to decode the last section as base64-like
    import base64
    try:
        # Clean it up - remove non-base64 chars
        cleaned = re.sub(r'[^A-Za-z0-9+/=]', '', last_section)
        print(f"Cleaned for base64: '{cleaned}'")
        decoded = base64.b64decode(cleaned + '==')  # padding
        print(f"Base64 decode attempt: {decoded}")
    except Exception as e:
        print(f"Base64 decode failed: {e}")

    # Try other common encodings
    try:
        import codecs
        # Try rot13
        rot13 = codecs.decode(last_section, 'rot13')
        print(f"ROT13 decode attempt: {rot13}")
    except Exception as e:
        print(f"ROT13 decode failed: {e}")

if __name__ == "__main__":
    analyze_cipher_structure()