#!/usr/bin/env python3

encrypted_message = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

def test_different_approaches():
    """Test completely different cipher approaches"""
    
    print("=== Testing Different Cipher Methods ===")
    
    # Maybe it's not ROT13 at all - let's test other common ciphers
    
    # 1. Test if it's actually a simple Caesar cipher with different shifts
    test_text = "vbR w8|="  # Should be "The flag" if it's Caesar
    
    print("Testing Caesar shifts on 'vbR w8|=':")
    for shift in range(26):
        result = ""
        for char in test_text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base - shift) % 26 + base)
            else:
                result += char
        
        if "the" in result.lower() and "flag" in result.lower():
            print(f"  Shift -{shift}: {result} *** MATCH! ***")
            return shift
        elif shift in [13, 1, 25]:
            print(f"  Shift -{shift}: {result}")
    
    return None

def test_atbash_cipher():
    """Test Atbash cipher (A=Z, B=Y, etc.)"""
    
    print("\n=== Testing Atbash Cipher ===")
    
    def atbash(text):
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
    
    # Test on the flag line
    flag_line = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    atbash_result = atbash(flag_line)
    print(f"Atbash on flag line: {atbash_result}")
    
    # Test on a small portion
    test_portion = "vbR w8|="
    atbash_test = atbash(test_portion)
    print(f"Atbash on 'vbR w8|=': {atbash_test}")
    
    return atbash_result

def analyze_flag_line_carefully():
    """Analyze the flag line more carefully for patterns"""
    
    print("\n=== Careful Flag Line Analysis ===")
    
    flag_line = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    print(f"Flag line: {flag_line}")
    
    # What if the substitution is different than I thought?
    # Let's consider that USCC might map differently
    
    # If we assume the flag starts with USCC{, then:
    # < should map to U
    # Q should map to S  
    # ; should map to C (first one)
    # ; should map to C (second one)
    # ) should map to {
    
    # But what if it's not ) = { but something else?
    # Let's try different mappings for the opening
    
    possible_mappings = [
        {'<': 'U', 'Q': 'S', ';': 'C', ')': 'C'},  # USCC without {
        {'<': 'U', 'Q': 'S', ';': 'C', ')': '{'},  # USCC{
        {'<': 'U', 'Q': 'S', ';': 'C', ')': 'C', 'g': '{'},  # USCC{ with g as {
    ]
    
    for i, mapping in enumerate(possible_mappings):
        print(f"\nMapping {i+1}: {mapping}")
        result = ""
        for char in flag_line:
            if char in mapping:
                result += mapping[char]
            else:
                result += char
        print(f"Result: {result}")

def try_vigenere_approach():
    """Maybe it's a Vigenère cipher with a key"""
    
    print("\n=== Testing Vigenère Cipher ===")
    
    # Common keys for crypto challenges
    test_keys = ['KEY', 'CIPHER', 'RANDOM', 'RNG', 'PRNG', 'SEED']
    
    def vigenere_decrypt(text, key):
        result = ""
        key_index = 0
        
        for char in text:
            if char.isalpha():
                # Get the shift from the key
                key_char = key[key_index % len(key)]
                shift = ord(key_char.upper()) - ord('A')
                
                # Apply reverse shift
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base - shift) % 26 + base)
                
                key_index += 1
            else:
                result += char
        
        return result
    
    test_text = "vbR w8|="
    
    for key in test_keys:
        decrypted = vigenere_decrypt(test_text, key)
        print(f"Key '{key}': {decrypted}")
        
        if "the" in decrypted.lower() and "flag" in decrypted.lower():
            print(f"  *** POTENTIAL MATCH with key '{key}' ***")
            return key
    
    return None

def check_simple_substitution():
    """Check if it's a simple monoalphabetic substitution"""
    
    print("\n=== Simple Substitution Analysis ===")
    
    # If "vbR" = "the", then v->t, b->h, R->e
    # Let's build a substitution table and see if it's consistent
    
    # Common 3-letter words and their potential cipher equivalents
    common_words = {
        "the": ["vbR", "CbR"],  # We see both vbR and CbR
        "and": ["|#-"],
        "for": ["wHX"],
        "are": ["|XR"],
    }
    
    substitution_table = {}
    
    # If vbR = the
    if True:  # Let's assume this
        substitution_table['v'] = 't'
        substitution_table['b'] = 'h' 
        substitution_table['R'] = 'e'
        
        print("Building substitution table from 'vbR' = 'the':")
        print(f"Current table: {substitution_table}")
        
        # Apply this to see what we get
        test_segments = ["vbR", "w8|=", "CbR", "|#-", "wHX"]
        
        for segment in test_segments:
            result = ""
            for char in segment:
                if char.lower() in substitution_table:
                    if char.isupper():
                        result += substitution_table[char.lower()].upper()
                    else:
                        result += substitution_table[char.lower()]
                else:
                    result += char
            
            print(f"'{segment}' -> '{result}'")

if __name__ == "__main__":
    caesar_shift = test_different_approaches()
    
    if caesar_shift:
        print(f"\nFound Caesar shift: -{caesar_shift}")
        # Apply this to the full message
        full_result = ""
        for char in encrypted_message:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                full_result += chr((ord(char) - base - caesar_shift) % 26 + base)
            else:
                full_result += char
        
        print("Decrypted message (first 200 chars):")
        print(full_result[:200])
        
        # Look for flag
        if "USCC{" in full_result:
            flag_start = full_result.find("USCC{")
            flag_end = full_result.find("}", flag_start)
            if flag_end != -1:
                flag = full_result[flag_start:flag_end+1]
                print(f"\n🎉 FOUND FLAG: {flag}")
    
    atbash_result = test_atbash_cipher()
    analyze_flag_line_carefully()
    vigenere_key = try_vigenere_approach()
    check_simple_substitution()