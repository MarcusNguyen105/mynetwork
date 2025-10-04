#!/usr/bin/env python3
"""
Final Attempt - Try a different approach to solve the cipher
"""

# The encrypted message
encrypted = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

def try_different_cipher_approaches():
    """Try different cipher approaches"""
    print("=== TRYING DIFFERENT CIPHER APPROACHES ===")
    
    # Extract the last line
    lines = encrypted.split('*')
    last_line = lines[-1].strip()
    print(f"Last line: '{last_line}'")
    
    # Try different approaches on the entire text
    print("\n1. Trying Caesar cipher on entire text:")
    for shift in range(26):
        result = ""
        for char in encrypted:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + shift) % 26
                result += chr(base + shifted)
            else:
                result += char
        
        # Check for flag pattern
        if 'USCC{' in result:
            print(f"  *** FOUND FLAG with shift {shift} ***")
            print(f"  {result}")
            return result
    
    # Try Vigenère cipher
    print("\n2. Trying Vigenère cipher:")
    keys = ['USCC', 'FLAG', 'KEY', 'SECRET', 'CIPHER', 'RANDOM', 'CUSTOM', '750']
    
    for key in keys:
        result = ""
        key_index = 0
        for char in encrypted:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key[key_index % len(key)]
                key_shift = ord(key_char.upper()) - ord('A')
                
                shifted = (ord(char) - base + key_shift) % 26
                result += chr(base + shifted)
                key_index += 1
            else:
                result += char
        
        # Check for flag pattern
        if 'USCC{' in result:
            print(f"  *** FOUND FLAG with key '{key}' ***")
            print(f"  {result}")
            return result
    
    return None

def try_substitution_cipher():
    """Try substitution cipher"""
    print("\n=== TRYING SUBSTITUTION CIPHER ===")
    
    # Try mapping the most frequent character to space
    from collections import Counter
    freq = Counter(encrypted)
    most_frequent = freq.most_common(1)[0][0]
    print(f"Most frequent character: '{most_frequent}' ({freq[most_frequent]} times)")
    
    # Try mapping it to space
    text_with_spaces = encrypted.replace(most_frequent, ' ')
    print(f"With '{most_frequent}' as space: {text_with_spaces[:100]}...")
    
    # Check for flag pattern
    if 'USCC{' in text_with_spaces:
        print(f"  *** FOUND FLAG ***")
        print(f"  {text_with_spaces}")
        return text_with_spaces
    
    # Try mapping it to 'E'
    text_with_e = encrypted.replace(most_frequent, 'E')
    print(f"With '{most_frequent}' as 'E': {text_with_e[:100]}...")
    
    # Check for flag pattern
    if 'USCC{' in text_with_e:
        print(f"  *** FOUND FLAG ***")
        print(f"  {text_with_e}")
        return text_with_e
    
    return None

def try_numeric_key_cipher():
    """Try cipher with numeric keys"""
    print("\n=== TRYING NUMERIC KEY CIPHER ===")
    
    # Try different numeric keys
    keys = ['750', '88', '5', '8', '3', '0']
    
    for key in keys:
        result = ""
        key_index = 0
        for char in encrypted:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key[key_index % len(key)]
                key_shift = int(key_char)
                
                shifted = (ord(char) - base + key_shift) % 26
                result += chr(base + shifted)
                key_index += 1
            else:
                result += char
        
        # Check for flag pattern
        if 'USCC{' in result:
            print(f"  *** FOUND FLAG with key '{key}' ***")
            print(f"  {result}")
            return result
    
    return None

def try_character_frequency_mapping():
    """Try character frequency mapping"""
    print("\n=== TRYING CHARACTER FREQUENCY MAPPING ===")
    
    from collections import Counter
    
    # Get character frequencies
    freq = Counter(encrypted)
    
    # English letter frequencies (approximate)
    english_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    
    # Map most frequent characters to most frequent English letters
    most_frequent = [char for char, count in freq.most_common(26)]
    
    print("Character frequency mapping:")
    for i, char in enumerate(most_frequent):
        if i < len(english_freq):
            print(f"  '{char}' -> '{english_freq[i]}' ({freq[char]} times)")
    
    # Try the mapping
    char_map = {}
    for i, char in enumerate(most_frequent):
        if i < len(english_freq):
            char_map[char] = english_freq[i]
    
    # Apply mapping
    mapped_text = ""
    for char in encrypted:
        mapped_text += char_map.get(char, char)
    
    print(f"\nMapped text sample: {mapped_text[:200]}...")
    
    # Check for flag pattern
    if 'USCC{' in mapped_text:
        print(f"  *** FOUND FLAG ***")
        print(f"  {mapped_text}")
        return mapped_text
    
    return None

def main():
    print("Final Attempt - Cipher Solver")
    print("=" * 50)
    
    # Try different cipher approaches
    result = try_different_cipher_approaches()
    if result:
        print(f"\n*** FINAL FLAG: {result} ***")
        return
    
    # Try substitution cipher
    result = try_substitution_cipher()
    if result:
        print(f"\n*** FINAL FLAG: {result} ***")
        return
    
    # Try numeric key cipher
    result = try_numeric_key_cipher()
    if result:
        print(f"\n*** FINAL FLAG: {result} ***")
        return
    
    # Try character frequency mapping
    result = try_character_frequency_mapping()
    if result:
        print(f"\n*** FINAL FLAG: {result} ***")
        return
    
    print("\nNo flag found with these approaches.")
    print("Let me try one more approach...")
    
    # Try a different approach - maybe the flag is in a different part
    print("\n=== TRYING DIFFERENT APPROACH ===")
    
    # Try the entire text with different ciphers
    print("Trying entire text with different ciphers...")
    
    # Try Caesar on entire text
    for shift in range(26):
        result = ""
        for char in encrypted:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + shift) % 26
                result += chr(base + shifted)
            else:
                result += char
        
        if 'USCC{' in result:
            print(f"*** FOUND FLAG: {result} ***")
            break

if __name__ == "__main__":
    main()