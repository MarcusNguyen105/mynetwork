#!/usr/bin/env python3

# Let me try a completely different approach
# Maybe the flag is hidden in a different way

encrypted_message = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

def look_for_hidden_patterns():
    """Look for hidden patterns in the message"""
    
    print("=== Looking for Hidden Patterns ===")
    
    # Maybe the flag is encoded in the first letters of words?
    # Or in specific positions?
    
    # Let's look at the ROT13 decoded message again and see if there are clues
    rot13_message = ""
    for char in encrypted_message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rot13_message += chr((ord(char) - base + 13) % 26 + base)
        else:
            rot13_message += char
    
    # Clean it up
    clean_message = rot13_message.replace('^', ' ')
    print("ROT13 decoded message:")
    print(clean_message)
    
    # Look for any mentions of specific numbers or patterns
    lines = clean_message.split('\n')
    for line in lines:
        if 'flag' in line.lower():
            print(f"\nFlag line: {line}")
            
            # Maybe the flag format is different?
            # Look for any {...} patterns
            import re
            
            # Look for patterns that might be flags
            patterns = re.findall(r'[A-Z]{3,4}\{[^}]+\}', line)
            if patterns:
                print(f"Found potential flags: {patterns}")
            
            # Look for the specific part after "flag is"
            if 'flag' in line and 'is' in line:
                parts = line.split()
                flag_index = -1
                for i, part in enumerate(parts):
                    if 'flag' in part.lower():
                        flag_index = i
                        break
                
                if flag_index != -1 and flag_index + 2 < len(parts):
                    # The flag might be a few words after "flag is"
                    potential_flag_part = ' '.join(parts[flag_index+2:])
                    print(f"Potential flag part: {potential_flag_part}")

def try_base64_or_hex():
    """Maybe some parts are base64 or hex encoded"""
    
    print("\n=== Base64/Hex Check ===")
    
    flag_line = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    
    # Extract parts that might be encoded
    import re
    
    # Look for base64-like strings (alphanumeric)
    alphanum_parts = re.findall(r'[A-Za-z0-9]{4,}', flag_line)
    print(f"Alphanumeric parts: {alphanum_parts}")
    
    for part in alphanum_parts:
        if len(part) >= 4:
            try:
                import base64
                # Try base64 decode
                decoded = base64.b64decode(part + '==')  # Add padding
                print(f"Base64 decode of '{part}': {decoded}")
            except:
                pass
            
            # Try hex decode
            try:
                if len(part) % 2 == 0:
                    decoded = bytes.fromhex(part)
                    print(f"Hex decode of '{part}': {decoded}")
            except:
                pass

def check_specific_transformations():
    """Check specific transformations that might work"""
    
    print("\n=== Specific Transformations ===")
    
    # What if the flag uses a specific pattern from the message?
    # The message talks about RNGs, maybe the flag contains RNG-related terms?
    
    # Let's try some RNG-related substitutions
    flag_content = "g5BRRZEogBoRoJogEg5oEJgs"
    
    # What if this spells out something RNG-related when decoded properly?
    
    # Try Atbash cipher
    atbash_result = ""
    for char in flag_content:
        if char.isalpha():
            if char.isupper():
                atbash_result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                atbash_result += chr(ord('z') - (ord(char) - ord('a')))
        else:
            atbash_result += char
    
    print(f"Atbash of flag content: {atbash_result}")
    print(f"Atbash flag: USCC{{{atbash_result}}}")
    
    # What if we need to reverse the string?
    reversed_content = flag_content[::-1]
    print(f"Reversed flag content: {reversed_content}")
    print(f"Reversed flag: USCC{{{reversed_content}}}")
    
    # What if we split it differently?
    # Maybe g5 and 5 are separators?
    parts = flag_content.split('5')
    print(f"Split by '5': {parts}")
    
    if len(parts) >= 3:
        middle_part = parts[1]  # The part between the two 5s
        print(f"Middle part: {middle_part}")
        
        # Try different transformations on the middle part
        rot13_middle = ""
        for char in middle_part:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                rot13_middle += chr((ord(char) - base + 13) % 26 + base)
            else:
                rot13_middle += char
        
        print(f"ROT13 of middle part: {rot13_middle}")
        print(f"Middle part flag: USCC{{{rot13_middle}}}")

def try_vigenere_with_rng_keys():
    """Try Vigenère cipher with RNG-related keys"""
    
    print("\n=== Vigenère with RNG Keys ===")
    
    flag_content = "g5BRRZEogBoRoJogEg5oEJgs"
    
    # Remove numbers for Vigenère
    letters_only = ''.join([c for c in flag_content if c.isalpha()])
    print(f"Letters only: {letters_only}")
    
    # Try RNG-related keys
    rng_keys = ['RNG', 'PRNG', 'SEED', 'LINEAR', 'RANDOM', 'GENERATOR', 'LCG']
    
    def vigenere_decrypt(text, key):
        result = ""
        key_index = 0
        
        for char in text:
            if char.isalpha():
                key_char = key[key_index % len(key)]
                shift = ord(key_char.upper()) - ord('A')
                
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base - shift) % 26 + base)
                
                key_index += 1
            else:
                result += char
        
        return result
    
    for key in rng_keys:
        decrypted = vigenere_decrypt(letters_only, key)
        print(f"Key '{key}': {decrypted}")
        print(f"  Flag: USCC{{{decrypted}}}")
        
        # Check if this looks like a reasonable flag
        if any(word in decrypted.lower() for word in ['random', 'linear', 'generator', 'seed', 'key']):
            print(f"  *** This looks promising! ***")

if __name__ == "__main__":
    look_for_hidden_patterns()
    try_base64_or_hex()
    check_specific_transformations()
    try_vigenere_with_rng_keys()