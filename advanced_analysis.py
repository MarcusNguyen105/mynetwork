#!/usr/bin/env python3

encrypted_message = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

def analyze_word_patterns():
    """Analyze word patterns to identify common words"""
    print("=== Word Pattern Analysis ===")
    
    # Split by ^ and analyze segments
    segments = [s for s in encrypted_message.split('^') if s and len(s) > 1]
    
    # Look for common English word patterns
    common_patterns = {
        1: ['a', 'I'],
        2: ['of', 'to', 'in', 'it', 'is', 'be', 'as', 'at', 'so', 'we', 'he', 'by', 'or', 'on', 'do', 'if', 'me', 'my', 'up', 'an', 'go', 'no', 'us', 'am'],
        3: ['the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'man', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'its', 'let', 'put', 'say', 'she', 'too', 'use']
    }
    
    # Count segment lengths
    length_counts = {}
    for segment in segments:
        length = len(segment)
        if length not in length_counts:
            length_counts[length] = []
        length_counts[length].append(segment)
    
    print("Segments by length:")
    for length in sorted(length_counts.keys()):
        if length <= 5:  # Focus on short segments
            unique_segments = list(set(length_counts[length]))
            print(f"Length {length}: {unique_segments[:10]}")  # Show first 10
    
    # Look for the most common 3-letter segment (likely "the")
    if 3 in length_counts:
        three_letter_freq = {}
        for segment in length_counts[3]:
            three_letter_freq[segment] = three_letter_freq.get(segment, 0) + 1
        
        most_common_3 = max(three_letter_freq.items(), key=lambda x: x[1])
        print(f"\nMost common 3-letter segment: '{most_common_3[0]}' (appears {most_common_3[1]} times)")
        
        # If this is "the", we can start building a substitution table
        if most_common_3[0]:
            return most_common_3[0]
    
    return None

def build_substitution_from_the(cipher_the):
    """Build substitution cipher mapping assuming cipher_the = 'the'"""
    print(f"\n=== Building substitution assuming '{cipher_the}' = 'the' ===")
    
    mapping = {}
    if len(cipher_the) == 3:
        mapping[cipher_the[0]] = 't'
        mapping[cipher_the[1]] = 'h' 
        mapping[cipher_the[2]] = 'e'
    
    print(f"Initial mapping: {mapping}")
    
    # Apply this mapping to see if it makes sense
    test_text = encrypted_message[:200]  # First 200 characters
    result = ""
    
    for char in test_text:
        if char.lower() in mapping:
            if char.isupper():
                result += mapping[char.lower()].upper()
            else:
                result += mapping[char.lower()]
        else:
            result += char
    
    print(f"Partial decryption: {result}")
    
    return mapping

def try_frequency_substitution():
    """Try frequency-based substitution"""
    print("\n=== Frequency-based Substitution ===")
    
    # English letter frequencies (approximate)
    english_freq = "etaoinshrdlcumwfgypbvkjxqz"
    
    # Get cipher letter frequencies (excluding non-letters)
    cipher_letters = ""
    for char in encrypted_message:
        if char.isalpha():
            cipher_letters += char.lower()
    
    # Count frequencies
    freq_count = {}
    for char in cipher_letters:
        freq_count[char] = freq_count.get(char, 0) + 1
    
    # Sort by frequency
    cipher_freq_order = ''.join([char for char, _ in sorted(freq_count.items(), key=lambda x: x[1], reverse=True)])
    
    print(f"Cipher frequency order: {cipher_freq_order}")
    print(f"English frequency order: {english_freq}")
    
    # Create mapping
    mapping = {}
    for i, cipher_char in enumerate(cipher_freq_order):
        if i < len(english_freq):
            mapping[cipher_char] = english_freq[i]
    
    print(f"Frequency mapping: {mapping}")
    
    # Test the mapping
    test_segment = "vbR w8|="  # Should contain "the flag" if this works
    result = ""
    for char in test_segment:
        if char.lower() in mapping:
            if char.isupper():
                result += mapping[char.lower()].upper()
            else:
                result += mapping[char.lower()]
        else:
            result += char
    
    print(f"Test decryption of 'vbR w8|=': '{result}'")
    
    # If this looks promising, decrypt more
    if 'the' in result.lower() or 'flag' in result.lower():
        print("Frequency mapping looks promising! Decrypting full message...")
        full_result = ""
        for char in encrypted_message:
            if char.lower() in mapping:
                if char.isupper():
                    full_result += mapping[char.lower()].upper()
                else:
                    full_result += mapping[char.lower()]
            else:
                full_result += char
        
        print("Full decryption:")
        print(full_result)
        
        # Look for flag
        if "USCC{" in full_result:
            flag_start = full_result.find("USCC{")
            flag_end = full_result.find("}", flag_start)
            if flag_end != -1:
                flag = full_result[flag_start:flag_end+1]
                print(f"\n🎉 FOUND FLAG: {flag}")
                return flag
    
    return None

if __name__ == "__main__":
    # First, try to identify "the"
    possible_the = analyze_word_patterns()
    
    if possible_the:
        build_substitution_from_the(possible_the)
    
    # Try frequency analysis
    flag = try_frequency_substitution()
    
    if not flag:
        print("\nFrequency analysis didn't yield clear results. This might be a more complex cipher.")