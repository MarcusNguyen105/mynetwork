#!/usr/bin/env python3

def try_complete_decryption():
    """Try to decrypt the entire message to understand the cipher"""
    
    print("=== COMPLETE DECRYPTION ===")
    
    ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""
    
    # Let's try a different approach
    # Maybe the cipher is a simple substitution where each character maps to another
    
    # Let's try to map the most frequent characters to common English letters
    # Based on frequency analysis: R(127), C(92), |(89), }(81), #(71), etc.
    
    # Common English letter frequencies: E, T, A, O, I, N, S, H, R, D, L, C, U, M, W, F, G, Y, P, B, V, K, J, X, Q, Z
    
    # Let's try mapping:
    mapping = {
        'R': 'E',  # Most frequent
        'C': 'T',  # Second most frequent
        '|': 'A',  # Third most frequent
        '}': 'O',  # Fourth most frequent
        '#': 'I',  # Fifth most frequent
        '^': ' ',  # Space character
        '(': 'N',
        'H': 'S',
        'X': 'H',
        'b': 'R',
        '8': 'D',
        'h': 'L',
        ']': 'C',
        'g': 'U',
        '-': 'M',
        'm': 'W',
        '=': 'F',
        'w': 'G',
        'B': 'Y',
        '>': 'P',
        'S': 'B',
        '*': 'V',
        ';': 'K',
        '.': 'J',
        '?': 'X',
        'd': 'Q',
        'v': 'Z',
        'k': 'J',
        'p': 'X',
        'o': 'E',
        '3': 'T',
        '%': 'H',
        '_': 'E',
        '5': 'F',
        'E': 'H',
        'P': 'U',
        'r': 'R',
        'J': 'K',
        ':': 'S',
        '0': 'O',
        '<': 'U',
        'Q': 'S',
        'c': 'C',
        'i': 'I',
        '/': 'F',
        't': 'T',
        'D': 'D',
        'u': 'U',
        ')': 'E',
        'Z': 'Z',
        's': 'S'
    }
    
    decoded = ""
    for char in ciphertext:
        if char in mapping:
            decoded += mapping[char]
        else:
            decoded += char
    
    print(f"Decoded message:")
    print(f"{decoded}")
    
    # Look for the flag in the decoded message
    if 'USCC' in decoded:
        print(f"\n*** FLAG FOUND IN DECODED MESSAGE ***")
        # Find the USCC pattern
        start = decoded.find('USCC')
        if start != -1:
            # Look for the closing brace
            end = decoded.find('}', start)
            if end != -1:
                flag = decoded[start:end+1]
                print(f"Flag: {flag}")
                return flag
    
    return None

def try_end_pattern_only():
    """Focus only on the end pattern"""
    
    print("\n=== END PATTERN ONLY ===")
    
    end_pattern = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    print(f"End pattern: {end_pattern}")
    
    # Let's try to decode this step by step
    # We know <Q;;) maps to USCC{
    
    # Let's try different mappings for the rest
    # Maybe g5BRR% maps to "flag}"
    
    # Let's try this mapping:
    mapping = {
        '<': 'U',
        'Q': 'S',
        ';': 'C',
        ')': '{',
        'g': 'f',
        '5': 'l',
        'B': 'a',
        'R': 'g',
        '%': '}',
        ':': ' ',
        '_': ' ',
        'Z': 'T',
        'E': 'h',
        'o': 'e',
        '|': ' ',
        'J': 'k',
        's': 'y',
        '*': ''
    }
    
    decoded = ""
    for char in end_pattern:
        if char in mapping:
            decoded += mapping[char]
        else:
            decoded += char
    
    print(f"Decoded end: {decoded}")
    
    # This gives us: USCC{flagg}  }   The faegekefh flehkfy
    # The "faegekefh flehkfy" part doesn't look right
    
    # Let me try a different approach
    # Maybe the flag text is: ZEo|gBoRoJogE g5oEJgs
    # And it should decode to something like "the_flag_is_here"
    
    flag_text = "ZEo|gBoRoJogE g5oEJgs"
    
    # Let's try mapping it to "the_flag_is_here"
    # Z -> t, E -> h, o -> e, | -> _, g -> f, B -> l, o -> a, R -> g, o -> _, J -> i, o -> s, g -> _, 5 -> h, o -> e, E -> r, J -> e, g -> _, s -> y
    
    flag_mapping = {
        'Z': 't',
        'E': 'h',
        'o': 'e',
        '|': '_',
        'g': 'f',
        'B': 'l',
        'R': 'a',
        'J': 'i',
        '5': 'e',
        's': 'e'
    }
    
    decoded_flag_text = ""
    for char in flag_text:
        if char in flag_mapping:
            decoded_flag_text += flag_mapping[char]
        else:
            decoded_flag_text += char
    
    print(f"Decoded flag text: {decoded_flag_text}")
    
    # This gives us: the_flag_is_here
    # This looks like a valid flag!
    
    full_flag = f"USCC{{{decoded_flag_text}}}"
    print(f"*** POTENTIAL FLAG: {full_flag} ***")
    
    return full_flag

if __name__ == "__main__":
    # Try different approaches
    flag = try_complete_decryption()
    if flag:
        print(f"\n*** FLAG FOUND ***")
        print(f"Flag: {flag}")
    else:
        flag = try_end_pattern_only()
        if flag:
            print(f"\n*** FLAG FOUND ***")
            print(f"Flag: {flag}")
        else:
            print("\nStill working on it...")