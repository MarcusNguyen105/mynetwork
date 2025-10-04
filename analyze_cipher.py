#!/usr/bin/env python3

import collections
import re
from typing import Dict, List, Tuple

def analyze_cipher_text():
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

    print(f"Total characters: {len(cipher_text)}")
    print(f"Unique characters: {len(set(cipher_text))}")

    # Character frequency analysis
    char_freq = collections.Counter(cipher_text)
    print("\nCharacter frequency (most common first):")
    for char, count in char_freq.most_common():
        print(f"'{char}': {count}")

    # Look for common patterns
    print("\nCommon patterns:")
    # Find repeated sequences
    patterns = {}
    for i in range(len(cipher_text) - 1):
        pair = cipher_text[i:i+2]
        if pair in patterns:
            patterns[pair] += 1
        else:
            patterns[pair] = 1

    # Sort by frequency
    sorted_patterns = sorted(patterns.items(), key=lambda x: x[1], reverse=True)
    print("Most common 2-character patterns:")
    for pattern, count in sorted_patterns[:20]:
        print(f"'{pattern}': {count}")

    # Look for longer patterns
    print("\nLonger patterns:")
    for length in range(3, 8):
        patterns = {}
        for i in range(len(cipher_text) - length + 1):
            pattern = cipher_text[i:i+length]
            if pattern in patterns:
                patterns[pattern] += 1
            else:
                patterns[pattern] = 1

        # Find patterns that appear more than once
        repeated_patterns = {k: v for k, v in patterns.items() if v > 1}
        if repeated_patterns:
            sorted_patterns = sorted(repeated_patterns.items(), key=lambda x: x[1], reverse=True)
            print(f"Most common {length}-character patterns:")
            for pattern, count in sorted_patterns[:10]:
                print(f"'{pattern}': {count}")

    # Look for the word boundaries or structure
    print("\nPotential word boundaries:")
    print("Looking for patterns that might indicate word boundaries...")

    # Check if there are any obvious separators
    separators = ['*', '^', '|', '#']
    for sep in separators:
        parts = cipher_text.split(sep)
        if len(parts) > 1:
            print(f"Split by '{sep}': {len(parts)} parts")
            # Show some part lengths
            part_lengths = [len(part) for part in parts if part]
            if part_lengths:
                print(f"Part lengths: {sorted(set(part_lengths))}")

    # Look at the final part that looks different
    final_part = cipher_text.split('*')[-1] if '*' in cipher_text else ""
    if final_part:
        print(f"\nFinal part after last *: '{final_part}'")
        print(f"Final part length: {len(final_part)}")

        # Analyze the final part separately
        final_freq = collections.Counter(final_part)
        print("Final part character frequency:")
        for char, count in final_freq.most_common():
            print(f"'{char}': {count}")

if __name__ == "__main__":
    analyze_cipher_text()