#!/usr/bin/env python3

encrypted_message = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

def test_rot13_properly():
    """Test ROT13 but look more carefully at the result"""
    
    print("=== Proper ROT13 Test ===")
    
    # Apply ROT13 to the entire message
    rot13_message = ""
    for char in encrypted_message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rot13_message += chr((ord(char) - base + 13) % 26 + base)
        else:
            rot13_message += char
    
    print("ROT13 decoded message (cleaned up):")
    clean_message = rot13_message.replace('^', ' ')
    print(clean_message)
    
    # Look specifically at the flag line
    lines = rot13_message.split('\n')
    flag_line = lines[-1] if lines else ""
    print(f"\nFlag line after ROT13: {flag_line}")
    
    # Now apply the substitution we found
    substitution = {'<': 'U', 'Q': 'S', ';': 'C', ')': '{', '*': '}'}
    
    # But wait - after ROT13, the characters would have changed
    # Let's see what < Q ; ) * become after ROT13
    
    original_chars = "<Q;)*"
    rot13_chars = ""
    for char in original_chars:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rot13_chars += chr((ord(char) - base + 13) % 26 + base)
        else:
            rot13_chars += char
    
    print(f"After ROT13: '{original_chars}' becomes '{rot13_chars}'")
    
    return rot13_message

def look_for_uscc_pattern():
    """Look for USCC pattern in different ways"""
    
    print("\n=== Looking for USCC Pattern ===")
    
    # Maybe USCC is encoded differently
    # Let's see what USCC would look like in different ciphers
    
    uscc = "USCC"
    
    print("USCC in different ciphers:")
    
    # ROT13
    rot13_uscc = ""
    for char in uscc:
        rot13_uscc += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
    print(f"ROT13: {rot13_uscc}")
    
    # ROT-1 through ROT-25
    for shift in [1, 2, 3, 5, 7, 11, 17, 19, 23, 25]:
        shifted = ""
        for char in uscc:
            shifted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        print(f"ROT{shift}: {shifted}")
    
    # Atbash
    atbash_uscc = ""
    for char in uscc:
        atbash_uscc += chr(ord('Z') - (ord(char) - ord('A')))
    print(f"Atbash: {atbash_uscc}")
    
    # Now search for these patterns in the original message
    print(f"\nSearching for these patterns in the message...")
    
    patterns_to_find = [rot13_uscc, "HFPP", "VTDD", "XGEE"]  # Some common shifts
    
    for pattern in patterns_to_find:
        if pattern in encrypted_message:
            print(f"Found pattern '{pattern}' in message!")
            # Find its position and context
            pos = encrypted_message.find(pattern)
            context = encrypted_message[max(0, pos-10):pos+20]
            print(f"  Context: {context}")

def examine_flag_line_structure():
    """Examine the flag line structure more carefully"""
    
    print("\n=== Flag Line Structure Analysis ===")
    
    flag_line = "vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    
    print(f"Full flag line: {flag_line}")
    
    # Split by ^
    parts = flag_line.split('^')
    print(f"Parts: {parts}")
    
    # The structure seems to be: "vbR" "w8|=" "(}" "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    # This could be: "The" "flag" "is" "<actual flag>"
    
    # Let's test if "vbR" = "The", "w8|=" = "flag", "(}" = "is"
    
    # If vbR = The, then we need: v->T, b->h, R->e
    # Let's see what shift this would be
    
    v_to_t = (ord('T') - ord('v')) % 26  # Should be 24 (or -2)
    b_to_h = (ord('h') - ord('b')) % 26  # Should be 6
    R_to_e = (ord('e') - ord('R')) % 26  # Should be 13
    
    print(f"Shifts needed: v->T ({v_to_t}), b->h ({b_to_h}), R->e ({R_to_e})")
    
    # These are different shifts, so it's not a simple Caesar cipher
    # But maybe it's ROT13 with case considerations?
    
    # Let's try ROT13 on "vbR"
    rot13_vbr = ""
    for char in "vbR":
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rot13_vbr += chr((ord(char) - base + 13) % 26 + base)
    
    print(f"ROT13 of 'vbR': {rot13_vbr}")
    
    # That gives "ioE" - not "The"
    
    # What about the reverse direction?
    reverse_rot13_vbr = ""
    for char in "vbR":
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            reverse_rot13_vbr += chr((ord(char) - base - 13) % 26 + base)
    
    print(f"Reverse ROT13 of 'vbR': {reverse_rot13_vbr}")

def try_mixed_case_rot13():
    """Try ROT13 but handle mixed case differently"""
    
    print("\n=== Mixed Case ROT13 ===")
    
    # Maybe the cipher preserves case but shifts all letters by 13
    test_text = "vbR w8|="
    
    result = ""
    for char in test_text:
        if char.isalpha():
            # Always use uppercase base for the shift calculation
            shifted_ord = (ord(char.upper()) - ord('A') + 13) % 26 + ord('A')
            shifted_char = chr(shifted_ord)
            
            # Preserve original case
            if char.islower():
                result += shifted_char.lower()
            else:
                result += shifted_char
        else:
            result += char
    
    print(f"Mixed case ROT13 of '{test_text}': {result}")
    
    # Try the reverse
    result_reverse = ""
    for char in test_text:
        if char.isalpha():
            shifted_ord = (ord(char.upper()) - ord('A') - 13) % 26 + ord('A')
            shifted_char = chr(shifted_ord)
            
            if char.islower():
                result_reverse += shifted_char.lower()
            else:
                result_reverse += shifted_char
        else:
            result_reverse += char
    
    print(f"Reverse mixed case ROT13 of '{test_text}': {result_reverse}")

if __name__ == "__main__":
    rot13_result = test_rot13_properly()
    look_for_uscc_pattern()
    examine_flag_line_structure()
    try_mixed_case_rot13()