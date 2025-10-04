#!/usr/bin/env python3

import string

encrypted_message = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H]^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

def frequency_analysis():
    """Analyze character frequencies to help identify cipher type"""
    # Remove the delimiter '^' for cleaner analysis
    clean_text = encrypted_message.replace('^', ' ')
    
    # Count letter frequencies
    letter_freq = {}
    for char in clean_text:
        if char.isalpha():
            char = char.upper()
            letter_freq[char] = letter_freq.get(char, 0) + 1
    
    # Sort by frequency
    sorted_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)
    
    print("Letter frequency analysis:")
    for letter, count in sorted_freq:
        print(f"{letter}: {count}")
    
    return sorted_freq

def test_substitution_cipher():
    """Test if this is a simple substitution cipher"""
    # Most common letters in English: E, T, A, O, I, N, S, H, R
    # Most common in our cipher: R, C, H, X, B, etc.
    
    # Let's try mapping the most frequent cipher letters to most frequent English letters
    cipher_freq = frequency_analysis()
    english_freq = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'U']
    
    # Create a mapping
    mapping = {}
    for i, (cipher_char, _) in enumerate(cipher_freq[:12]):
        if i < len(english_freq):
            mapping[cipher_char] = english_freq[i]
    
    print(f"\nTesting substitution mapping: {mapping}")
    
    # Apply the mapping to a small portion
    test_text = "vbR^w8|="  # Should be "The flag" if this works
    result = ""
    for char in test_text:
        if char.upper() in mapping:
            if char.isupper():
                result += mapping[char.upper()]
            else:
                result += mapping[char.upper()].lower()
        else:
            result += char
    
    print(f"Test decryption of 'vbR^w8|=': {result}")
    
    return mapping

def analyze_rng_patterns():
    """Look for patterns that might indicate RNG-based encryption"""
    print("\n=== RNG Pattern Analysis ===")
    
    # If it's an RNG-based stream cipher, we might see:
    # 1. Consistent character mappings throughout
    # 2. No obvious patterns in the keystream
    
    # Let's check if the same plaintext always maps to the same ciphertext
    segments = encrypted_message.split('^')
    
    # Look for repeated segments and see if they're consistently encrypted
    segment_mappings = {}
    for segment in segments:
        if len(segment) > 2:  # Only consider meaningful segments
            if segment in segment_mappings:
                print(f"Repeated segment: '{segment}'")
            else:
                segment_mappings[segment] = True
    
    # The fact that we have repeated segments suggests it might be a substitution cipher
    # rather than a stream cipher (which would have different outputs for same input)
    
def try_rot_cipher():
    """Try ROT13 and other rotation ciphers"""
    print("\n=== Testing ROT Ciphers ===")
    
    test_segment = "vbR"  # Might be "the"
    
    for rot in range(1, 26):
        result = ""
        for char in test_segment:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base - rot) % 26 + base)
            else:
                result += char
        
        if result.lower() == "the":
            print(f"ROT{rot} works! 'vbR' -> '{result}'")
            return rot
    
    return None

def decrypt_with_rot(text, rot):
    """Decrypt text using ROT cipher"""
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - rot) % 26 + base)
        else:
            result += char
    return result

if __name__ == "__main__":
    # Try ROT cipher first since it's simple
    rot_key = try_rot_cipher()
    
    if rot_key:
        print(f"\nFound ROT{rot_key}! Decrypting full message...")
        decrypted = decrypt_with_rot(encrypted_message, rot_key)
        print("\nDecrypted message:")
        print(decrypted)
        
        # Look for the flag
        if "USCC{" in decrypted:
            flag_start = decrypted.find("USCC{")
            flag_end = decrypted.find("}", flag_start)
            if flag_end != -1:
                flag = decrypted[flag_start:flag_end+1]
                print(f"\n🎉 FOUND FLAG: {flag}")
    else:
        print("ROT cipher didn't work, trying other approaches...")
        test_substitution_cipher()
        analyze_rng_patterns()