#!/usr/bin/env python3

encrypted_message = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

def decode_full_message():
    """Decode the full message with ROT13 to understand context"""
    
    print("=== Full Message ROT13 Decode ===")
    
    decoded = ""
    for char in encrypted_message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decoded += chr((ord(char) - base + 13) % 26 + base)
        else:
            decoded += char
    
    print("Decoded message:")
    print(decoded)
    print("\n" + "="*50)
    
    # Look for any mentions of flags, keys, or important information
    lines = decoded.split('\n')
    for i, line in enumerate(lines):
        if any(word in line.lower() for word in ['flag', 'key', 'uscc', 'answer', 'solution']):
            print(f"Important line {i+1}: {line}")
    
    return decoded

def look_for_patterns(decoded_text):
    """Look for patterns in the decoded text that might help"""
    
    print("\n=== Pattern Analysis ===")
    
    # Look for numbers that might be RNG parameters
    import re
    
    # Find all numbers
    numbers = re.findall(r'\d+', decoded_text)
    print(f"Numbers found: {numbers}")
    
    # Look for specific patterns
    if '32' in decoded_text or '64' in decoded_text:
        print("Found bit-size references (32 or 64)")
    
    if 'seed' in decoded_text.lower():
        print("Found 'seed' reference")
    
    if 'key' in decoded_text.lower():
        print("Found 'key' reference")

def try_different_approach():
    """Try a completely different decoding approach"""
    
    print("\n=== Different Approach ===")
    
    # Maybe the flag is encoded with a simple pattern
    # Let's look at the flag line again: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    
    flag_line = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    
    # What if we need to extract specific characters?
    # Or what if the numbers are important?
    
    # Extract just the alphanumeric parts
    import re
    alphanum_parts = re.findall(r'[a-zA-Z0-9]+', flag_line)
    print(f"Alphanumeric parts: {alphanum_parts}")
    
    # Maybe we need to concatenate them in a specific way
    concatenated = ''.join(alphanum_parts)
    print(f"Concatenated: {concatenated}")
    
    # Try ROT13 on this
    rot13_concat = ""
    for char in concatenated:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rot13_concat += chr((ord(char) - base + 13) % 26 + base)
        else:
            rot13_concat += char
    
    print(f"ROT13 of concatenated: {rot13_concat}")
    
    # Maybe we need to apply the same substitution as before
    # < = U, Q = S, ; = C, ) = {, * = }
    
    substitution = {'<': 'U', 'Q': 'S', ';': 'C', ')': '{', '*': '}'}
    
    # Apply substitution first
    substituted = ""
    for char in flag_line:
        if char in substitution:
            substituted += substitution[char]
        else:
            substituted += char
    
    print(f"After substitution: {substituted}")
    
    # Now extract the content between { and }
    if '{' in substituted and '}' in substituted:
        start = substituted.find('{')
        end = substituted.find('}')
        flag_content = substituted[start+1:end]
        print(f"Flag content: {flag_content}")
        
        # Clean it up - remove special characters and spaces
        clean_content = re.sub(r'[^a-zA-Z0-9]', '', flag_content)
        print(f"Clean content: {clean_content}")
        
        # Try different decoding methods
        print(f"Potential flag 1: USCC{{{clean_content}}}")
        
        # ROT13 version
        rot13_clean = ""
        for char in clean_content:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                rot13_clean += chr((ord(char) - base + 13) % 26 + base)
            else:
                rot13_clean += char
        
        print(f"Potential flag 2: USCC{{{rot13_clean}}}")

if __name__ == "__main__":
    decoded_message = decode_full_message()
    look_for_patterns(decoded_message)
    try_different_approach()