#!/usr/bin/env python3

# Focus on the flag line specifically
flag_line = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"

def analyze_flag_structure():
    """Analyze the structure of the potential flag"""
    print("=== Flag Structure Analysis ===")
    print(f"Flag line: {flag_line}")
    print(f"Length: {len(flag_line)}")
    
    # Look for patterns that might indicate USCC{...}
    # USCC is 4 characters, { is 1, } is 1
    # So we need at least 6 characters for minimal flag
    
    # Maybe the format is different - let's look for any {...} pattern first
    if '{' in flag_line and '}' in flag_line:
        start = flag_line.find('{')
        end = flag_line.find('}')
        print(f"Found braces at positions {start} and {end}")
    
    # Let's try to see if there's a substitution pattern
    # USCC might be encoded as something else
    
    # Look at the structure: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    # This could be: USCC{something}
    
    print("\nLooking for 4-character patterns that could be USCC:")
    for i in range(len(flag_line) - 3):
        substr = flag_line[i:i+4]
        print(f"Position {i}: '{substr}'")

def test_substitution_on_flag():
    """Test various substitution patterns on the flag"""
    print("\n=== Testing Substitution Patterns ===")
    
    # Maybe it's a simple substitution where:
    # < = U, Q = S, ; = C, ) = C, { = {
    
    # Let's try some mappings based on the structure
    # The pattern <Q;;)...* might be USCC{...}
    
    potential_mappings = [
        {'<': 'U', 'Q': 'S', ';': 'C', ')': 'C'},  # Direct mapping
        {'<': 'U', 'Q': 'S', ';': 'C', ')': '{'},  # ) might be {
    ]
    
    for i, mapping in enumerate(potential_mappings):
        print(f"\nTrying mapping {i+1}: {mapping}")
        result = ""
        for char in flag_line:
            if char in mapping:
                result += mapping[char]
            else:
                result += char
        print(f"Result: {result}")

def try_caesar_on_letters_only():
    """Try Caesar cipher on letters only, preserving other characters"""
    print("\n=== Caesar on Letters Only ===")
    
    for shift in range(26):
        result = ""
        for char in flag_line:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        
        if shift in [13, 1, 25]:  # Common shifts
            print(f"Shift {shift}: {result}")
        
        # Check for USCC pattern
        if result.startswith('USCC') or 'USCC{' in result:
            print(f"*** FOUND USCC with shift {shift}: {result} ***")
            return shift, result
    
    return None, None

def manual_decode_attempt():
    """Manual attempt to decode based on patterns"""
    print("\n=== Manual Decode Attempt ===")
    
    # Looking at: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    # This might be: USCC{...}
    
    # Let's assume < = U, Q = S, ; = C, ) = C or {
    # Then we have: USCC...
    
    # Let's try to decode the middle part
    # g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs
    
    # Maybe it's ROT13 but with some characters preserved
    test_part = "ZEo|gBoRoJogE g5oEJgs"
    
    # Try ROT13 on this part
    rot13_result = ""
    for char in test_part:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rot13_result += chr((ord(char) - base + 13) % 26 + base)
        else:
            rot13_result += char
    
    print(f"ROT13 on '{test_part}': {rot13_result}")
    
    # Try other shifts
    for shift in [1, 2, 3, 5, 7, 11, 17, 19, 23, 25]:
        shifted = ""
        for char in test_part:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted += chr((ord(char) - base + shift) % 26 + base)
            else:
                shifted += char
        print(f"Shift {shift}: {shifted}")

def check_atbash():
    """Try Atbash cipher (A=Z, B=Y, etc.)"""
    print("\n=== Atbash Cipher ===")
    
    result = ""
    for char in flag_line:
        if char.isalpha():
            if char.isupper():
                result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                result += chr(ord('z') - (ord(char) - ord('a')))
        else:
            result += char
    
    print(f"Atbash result: {result}")
    
    if 'USCC' in result:
        print("*** FOUND USCC with Atbash! ***")
        return result
    
    return None

if __name__ == "__main__":
    analyze_flag_structure()
    test_substitution_on_flag()
    
    shift, result = try_caesar_on_letters_only()
    if result:
        print(f"\nFound potential flag with Caesar shift {shift}: {result}")
    
    manual_decode_attempt()
    
    atbash_result = check_atbash()
    if atbash_result:
        print(f"Atbash gave us: {atbash_result}")
    
    # Let's also try the reverse - maybe the flag is at the beginning
    print(f"\n=== Checking if flag might be elsewhere ===")
    full_message = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""
    
    # Try ROT13 on the whole message and look for USCC
    rot13_full = ""
    for char in full_message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rot13_full += chr((ord(char) - base + 13) % 26 + base)
        else:
            rot13_full += char
    
    if "USCC{" in rot13_full:
        flag_start = rot13_full.find("USCC{")
        flag_end = rot13_full.find("}", flag_start)
        if flag_end != -1:
            flag = rot13_full[flag_start:flag_end+1]
            print(f"\n🎉 FOUND FLAG in full ROT13: {flag}")
    else:
        print("No USCC{ found in full ROT13 either")