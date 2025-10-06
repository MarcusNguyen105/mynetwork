#!/usr/bin/env python3

def try_substitution_cipher(ciphertext, mapping):
    """Try substitution cipher with given mapping"""
    result = ""
    for char in ciphertext:
        if char in mapping:
            result += mapping[char]
        else:
            result += char
    return result

def analyze_end_systematically():
    """Systematically analyze the end pattern"""
    
    print("=== SYSTEMATIC END ANALYSIS ===")
    
    # The suspicious end pattern: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    
    end_pattern = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    print(f"End pattern: {end_pattern}")
    
    # Let's try to map this to USCC{...}
    # If this is the flag, it should start with USCC{
    
    # Let's try different mappings
    print("\nTrying different mappings:")
    
    # Mapping 1: Direct character substitution
    mapping1 = {
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
    
    decoded1 = try_substitution_cipher(end_pattern, mapping1)
    print(f"Mapping 1: {decoded1}")
    
    # Let's try a different approach - maybe it's a simple shift
    print("\nTrying Caesar cipher shifts:")
    for shift in range(1, 26):
        decoded = ""
        for char in end_pattern:
            if char.isalpha():
                if char.isupper():
                    decoded += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    decoded += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                decoded += char
        
        if 'USCC' in decoded or 'flag' in decoded.lower():
            print(f"Shift {shift}: {decoded}")

def try_atbash_cipher(text):
    """Try Atbash cipher (A=Z, B=Y, etc.)"""
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                result += chr(ord('z') - (ord(char) - ord('a')))
        else:
            result += char
    return result

def try_rot13(text):
    """Try ROT13 cipher"""
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            result += char
    return result

def analyze_full_message():
    """Try to analyze the full message with different cipher types"""
    
    print("\n=== FULL MESSAGE ANALYSIS ===")
    
    ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""
    
    # Try Atbash on the end part
    end_part = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    atbash_end = try_atbash_cipher(end_part)
    print(f"Atbash of end: {atbash_end}")
    
    # Try ROT13 on the end part
    rot13_end = try_rot13(end_part)
    print(f"ROT13 of end: {rot13_end}")
    
    # Let's try a different approach - maybe the flag is embedded differently
    print("\nLooking for flag patterns in the full text...")
    
    # Look for patterns that might be USCC{...}
    # Let's try to find sequences that could be the flag
    
    # Maybe the flag is: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    # Let's try to decode this step by step
    
    # Looking at the pattern, let me try a different mapping
    # Maybe it's not a simple substitution
    
    print("\nTrying custom mapping based on pattern analysis:")
    
    # Let's try to map this to something readable
    # The pattern looks like it might be: USCC{flag_text_here}
    
    custom_mapping = {
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
    
    decoded_custom = try_substitution_cipher(end_part, custom_mapping)
    print(f"Custom mapping: {decoded_custom}")
    
    # Let me try a different approach - maybe the flag is in a different format
    # Let's look for patterns that might be the actual flag
    
    # Maybe the flag is: ZEo|gBoRoJogE g5oEJgs
    # Let's try to decode this part specifically
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    print(f"\nAnalyzing flag part: {flag_part}")
    
    # Try different decodings of this part
    for shift in range(1, 26):
        decoded_flag = ""
        for char in flag_part:
            if char.isalpha():
                if char.isupper():
                    decoded_flag += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    decoded_flag += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                decoded_flag += char
        
        if 'flag' in decoded_flag.lower() or 'key' in decoded_flag.lower():
            print(f"Flag part shift {shift}: {decoded_flag}")

if __name__ == "__main__":
    analyze_end_systematically()
    analyze_full_message()