#!/usr/bin/env python3

def try_substitution_with_hints():
    """Try substitution cipher using the hints from the end pattern"""
    
    print("=== SUBSTITUTION WITH HINTS ===")
    
    # The end pattern: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    
    # If this contains the flag USCC{...}, let's try to map it
    # Looking at the pattern, it seems like:
    # <Q;;) might be USCC{
    
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
    
    end_pattern = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    
    decoded = ""
    for char in end_pattern:
        if char in mapping:
            decoded += mapping[char]
        else:
            decoded += char
    
    print(f"Decoded end: {decoded}")
    
    # This gives us: USCC{flagg}  }   The faegekefh flehkfy
    # The "flagg" part doesn't look right, let me try a different approach
    
    # Maybe the flag is: USCC{the_flag_text_here}
    # And the flag text is: ZEo|gBoRoJogE g5oEJgs
    
    flag_text = "ZEo|gBoRoJogE g5oEJgs"
    
    # Let's try different mappings for this part
    print(f"\nTrying different mappings for flag text: {flag_text}")
    
    # Maybe it's a simple substitution where each character maps to another
    # Let's try to decode this as if it's English text
    
    # Looking at the pattern: ZEo|gBoRoJogE g5oEJgs
    # Maybe the | and 5 are separators or special characters
    
    # Let's try: ZEo gBoRoJogE g oEJgs
    # This could be: THE FLAG TEXT HERE
    
    # Let's try a different approach - maybe it's a simple shift
    print("\nTrying different shifts on the flag text:")
    
    for shift in range(26):
        decoded_flag = ""
        for char in flag_text:
            if char.isalpha():
                if char.isupper():
                    decoded_flag += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    decoded_flag += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                decoded_flag += char
        
        # Look for meaningful words
        if 'the' in decoded_flag.lower() or 'flag' in decoded_flag.lower() or 'text' in decoded_flag.lower():
            print(f"Shift {shift}: {decoded_flag}")
            
            # If this looks like flag text, construct the full flag
            if 'the' in decoded_flag.lower() or 'flag' in decoded_flag.lower():
                # Clean up the flag text
                clean_flag = decoded_flag.replace('|', ' ').replace('5', ' ')
                clean_flag = ' '.join(clean_flag.split())  # Remove extra spaces
                full_flag = f"USCC{{{clean_flag}}}"
                print(f"*** POTENTIAL FLAG: {full_flag} ***")
                return full_flag
    
    return None

def try_different_cipher_types():
    """Try different types of ciphers"""
    
    print("\n=== TRYING DIFFERENT CIPHER TYPES ===")
    
    # Maybe it's not a Vigenère cipher at all
    # Let's try other cipher types
    
    ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""
    
    # Try Atbash cipher
    print("Trying Atbash cipher...")
    atbash_result = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                atbash_result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                atbash_result += chr(ord('z') - (ord(char) - ord('a')))
        else:
            atbash_result += char
    
    if 'USCC' in atbash_result or 'flag' in atbash_result.lower():
        print(f"*** ATBASH SUCCESS ***")
        print(f"Atbash result: {atbash_result}")
        return atbash_result
    
    # Try ROT13
    print("Trying ROT13...")
    rot13_result = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                rot13_result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                rot13_result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            rot13_result += char
    
    if 'USCC' in rot13_result or 'flag' in rot13_result.lower():
        print(f"*** ROT13 SUCCESS ***")
        print(f"ROT13 result: {rot13_result}")
        return rot13_result
    
    return None

def try_simple_substitution():
    """Try simple substitution cipher"""
    
    print("\n=== SIMPLE SUBSTITUTION ===")
    
    # Maybe it's a simple substitution cipher
    # Let's try to map the most frequent characters to common English letters
    
    ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""
    
    # Character frequency analysis
    freq = {}
    for char in ciphertext:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    
    # Sort by frequency
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    print("Character frequencies:")
    for char, count in sorted_freq[:10]:
        print(f"'{char}': {count}")
    
    # Common English letter frequencies: E, T, A, O, I, N, S, H, R, D, L, C, U, M, W, F, G, Y, P, B, V, K, J, X, Q, Z
    
    # Try mapping the most frequent characters
    # R (127) -> E, C (92) -> T, | (89) -> A, } (81) -> O, # (71) -> I
    
    mapping = {
        'R': 'E',
        'C': 'T', 
        '|': 'A',
        '}': 'O',
        '#': 'I',
        '^': ' ',
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
        'v': 'Z'
    }
    
    decoded = ""
    for char in ciphertext:
        if char in mapping:
            decoded += mapping[char]
        else:
            decoded += char
    
    print(f"\nDecoded with frequency mapping:")
    print(f"{decoded[:500]}...")
    
    if 'USCC' in decoded or 'flag' in decoded.lower():
        print(f"*** SUBSTITUTION SUCCESS ***")
        return decoded
    
    return None

if __name__ == "__main__":
    # Try different approaches
    flag = try_substitution_with_hints()
    if flag:
        print(f"\n*** FLAG FOUND ***")
        print(f"Flag: {flag}")
    else:
        result = try_different_cipher_types()
        if result:
            print(f"\n*** CIPHER SUCCESS ***")
            print(f"Result: {result}")
        else:
            result = try_simple_substitution()
            if result:
                print(f"\n*** SUBSTITUTION SUCCESS ***")
                print(f"Result: {result}")
            else:
                print("\nStill working on it...")