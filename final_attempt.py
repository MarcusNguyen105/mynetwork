#!/usr/bin/env python3

encrypted_message = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

def rot13_decode(text):
    """Decode using ROT13"""
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + 13) % 26 + base)
        else:
            result += char
    return result

def test_all_rotations():
    """Test all possible rotations"""
    print("Testing all rotations on the flag line...")
    
    flag_line = "vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    
    for rot in range(26):
        result = ""
        for char in flag_line:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + rot) % 26 + base)
            else:
                result += char
        
        print(f"ROT{rot}: {result}")
        
        # Check if this contains USCC
        if "USCC" in result:
            print(f"*** FOUND USCC in ROT{rot}! ***")
            return rot
    
    return None

def decode_with_rotation(rot):
    """Decode the entire message with the given rotation"""
    print(f"\nDecoding entire message with ROT{rot}...")
    
    result = ""
    for char in encrypted_message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + rot) % 26 + base)
        else:
            result += char
    
    print("Decoded message:")
    print(result)
    
    # Extract flag
    if "USCC{" in result:
        flag_start = result.find("USCC{")
        flag_end = result.find("}", flag_start)
        if flag_end != -1:
            flag = result[flag_start:flag_end+1]
            print(f"\n🎉 FOUND FLAG: {flag}")
            return flag
    
    return None

def manual_inspection():
    """Manually inspect the flag line for patterns"""
    print("\nManual inspection of flag line:")
    flag_line = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    
    print(f"Flag line: {flag_line}")
    print("Looking for USCC pattern...")
    
    # The format should be USCC{...}
    # Let's see if we can spot it
    
    # Try ROT13 on just this part
    rot13_result = rot13_decode(flag_line)
    print(f"ROT13 of flag line: {rot13_result}")
    
    # Maybe the numbers and symbols are not encoded?
    # Let's try different approaches
    
if __name__ == "__main__":
    # First try ROT13 on the whole thing
    print("=== Trying ROT13 ===")
    rot13_full = rot13_decode(encrypted_message)
    print("ROT13 result (first 200 chars):")
    print(rot13_full[:200])
    
    if "USCC{" in rot13_full:
        flag_start = rot13_full.find("USCC{")
        flag_end = rot13_full.find("}", flag_start)
        if flag_end != -1:
            flag = rot13_full[flag_start:flag_end+1]
            print(f"\n🎉 FOUND FLAG with ROT13: {flag}")
    else:
        print("ROT13 didn't work, trying all rotations...")
        rot = test_all_rotations()
        
        if rot is not None:
            decode_with_rotation(rot)
        else:
            manual_inspection()