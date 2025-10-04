#!/usr/bin/env python3
"""
Custom Cipher Solver - Trying different approaches based on the "custom random number generator" hint
"""

import string
import re
from collections import Counter
import itertools
import random

# The encrypted message
encrypted = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

def analyze_segments(text):
    """Analyze the text in segments separated by ^"""
    print("=== SEGMENT ANALYSIS ===")
    
    # Split by ^ and analyze segments
    segments = text.split('^')
    print(f"Total segments: {len(segments)}")
    
    # Group segments by length
    length_groups = {}
    for seg in segments:
        length = len(seg)
        if length not in length_groups:
            length_groups[length] = []
        length_groups[length].append(seg)
    
    print("Segments by length:")
    for length in sorted(length_groups.keys()):
        if length > 0:
            print(f"  Length {length}: {len(length_groups[length])} segments")
            if length <= 10:  # Show short segments
                print(f"    Examples: {length_groups[length][:5]}")
    
    # Look for patterns in segments
    print("\nLooking for patterns:")
    
    # Check for repeated segments
    segment_counts = Counter(segments)
    repeated = {seg: count for seg, count in segment_counts.items() if count > 1 and len(seg) > 1}
    if repeated:
        print(f"Repeated segments: {repeated}")
    
    # Check for segments that look like they could be words
    potential_words = []
    for seg in segments:
        if len(seg) >= 3 and seg.isalnum():
            potential_words.append(seg)
    
    if potential_words:
        print(f"Potential word segments: {potential_words[:10]}")

def try_vigenere_cipher(text, key):
    """Try Vigenère cipher with given key"""
    result = ""
    key_len = len(key)
    key_index = 0
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            key_char = key[key_index % key_len]
            key_shift = ord(key_char.upper()) - ord('A')
            
            shifted = (ord(char) - base + key_shift) % 26
            result += chr(base + shifted)
            key_index += 1
        else:
            result += char
    
    return result

def try_autokey_cipher(text, initial_key):
    """Try autokey cipher with given initial key"""
    result = ""
    key = initial_key
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            key_char = key[0]
            key_shift = ord(key_char.upper()) - ord('A')
            
            shifted = (ord(char) - base + key_shift) % 26
            decrypted_char = chr(base + shifted)
            result += decrypted_char
            
            # Add decrypted character to key
            key = key[1:] + decrypted_char.upper()
        else:
            result += char
    
    return result

def try_beaufort_cipher(text, key):
    """Try Beaufort cipher with given key"""
    result = ""
    key_len = len(key)
    key_index = 0
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            key_char = key[key_index % key_len]
            key_shift = ord(key_char.upper()) - ord('A')
            
            shifted = (ord(char) - base - key_shift) % 26
            result += chr(base + shifted)
            key_index += 1
        else:
            result += char
    
    return result

def try_gronsfeld_cipher(text, key):
    """Try Gronsfeld cipher with given numeric key"""
    result = ""
    key_str = str(key)
    key_len = len(key_str)
    key_index = 0
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            key_digit = int(key_str[key_index % key_len])
            
            shifted = (ord(char) - base + key_digit) % 26
            result += chr(base + shifted)
            key_index += 1
        else:
            result += char
    
    return result

def test_cipher_methods(text):
    """Test various cipher methods"""
    print("\n=== TESTING CIPHER METHODS ===")
    
    # Common keys to try
    keys = ['KEY', 'FLAG', 'SECRET', 'PASSWORD', 'CIPHER', 'RANDOM', 'CUSTOM', 'USCC', 'CTF']
    
    # Try Vigenère cipher
    print("\n1. Vigenère Cipher:")
    for key in keys:
        result = try_vigenere_cipher(text, key)
        if 'THE' in result or 'AND' in result or 'FOR' in result:
            print(f"  Key '{key}': Found English words")
            print(f"    Sample: {result[:100]}...")
    
    # Try Autokey cipher
    print("\n2. Autokey Cipher:")
    for key in keys:
        result = try_autokey_cipher(text, key)
        if 'THE' in result or 'AND' in result or 'FOR' in result:
            print(f"  Key '{key}': Found English words")
            print(f"    Sample: {result[:100]}...")
    
    # Try Beaufort cipher
    print("\n3. Beaufort Cipher:")
    for key in keys:
        result = try_beaufort_cipher(text, key)
        if 'THE' in result or 'AND' in result or 'FOR' in result:
            print(f"  Key '{key}': Found English words")
            print(f"    Sample: {result[:100]}...")
    
    # Try Gronsfeld cipher with numeric keys
    print("\n4. Gronsfeld Cipher:")
    numeric_keys = [123, 456, 789, 2023, 2024, 750, 1337]
    for key in numeric_keys:
        result = try_gronsfeld_cipher(text, key)
        if 'THE' in result or 'AND' in result or 'FOR' in result:
            print(f"  Key {key}: Found English words")
            print(f"    Sample: {result[:100]}...")

def look_for_hidden_patterns(text):
    """Look for hidden patterns that might reveal the cipher"""
    print("\n=== LOOKING FOR HIDDEN PATTERNS ===")
    
    # Check if there are any obvious patterns
    print("Checking for patterns...")
    
    # Look at the end of the text - might contain the flag
    last_line = text.split('*')[-1]
    print(f"Last line: {last_line}")
    
    # Check if the last line looks different
    if 'ZEo|gBoRoJogE' in last_line:
        print("Found potential flag pattern in last line!")
        
        # Try different approaches on the last line
        print("Trying different ciphers on last line:")
        
        for shift in range(26):
            result = ""
            for char in last_line:
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
                    shifted = (ord(char) - base + shift) % 26
                    result += chr(base + shifted)
                else:
                    result += char
            
            if 'USCC' in result or 'FLAG' in result:
                print(f"  Caesar shift {shift}: {result}")
        
        # Try Vigenère on last line
        for key in ['USCC', 'FLAG', 'KEY', 'SECRET']:
            result = try_vigenere_cipher(last_line, key)
            if 'USCC' in result or 'FLAG' in result:
                print(f"  Vigenère key '{key}': {result}")

def try_custom_random_approach(text):
    """Try to reverse engineer a custom random number generator approach"""
    print("\n=== CUSTOM RANDOM NUMBER GENERATOR APPROACH ===")
    
    # The hint mentions "custom random number generator"
    # This could mean the cipher uses a pseudo-random sequence
    
    # Try to find patterns that might indicate a seed
    print("Looking for potential seeds...")
    
    # Check if there are any numbers in the text that could be seeds
    numbers = re.findall(r'\d+', text)
    if numbers:
        print(f"Numbers found: {numbers}")
        
        # Try using these numbers as seeds for different ciphers
        for num in numbers:
            seed = int(num)
            print(f"\nTrying seed {seed}:")
            
            # Set random seed
            random.seed(seed)
            
            # Generate random shifts
            shifts = [random.randint(0, 25) for _ in range(100)]
            
            # Apply shifts
            result = ""
            shift_index = 0
            for char in text:
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
                    shift = shifts[shift_index % len(shifts)]
                    shifted = (ord(char) - base + shift) % 26
                    result += chr(base + shifted)
                    shift_index += 1
                else:
                    result += char
            
            # Check for English words
            if 'THE' in result or 'AND' in result or 'FOR' in result:
                print(f"  Found English words with seed {seed}")
                print(f"    Sample: {result[:100]}...")

def main():
    print("Custom Cipher Solver")
    print("=" * 50)
    
    # Analyze segments
    analyze_segments(encrypted)
    
    # Test cipher methods
    test_cipher_methods(encrypted)
    
    # Look for hidden patterns
    look_for_hidden_patterns(encrypted)
    
    # Try custom random approach
    try_custom_random_approach(encrypted)

if __name__ == "__main__":
    main()