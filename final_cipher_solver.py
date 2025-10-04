#!/usr/bin/env python3
"""
Final Cipher Solver - Trying different approaches based on the structure
"""

import string
import re
from collections import Counter
import itertools

# The encrypted message - let me extract it properly
encrypted = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

def analyze_last_line(text):
    """Analyze the last line which might contain the flag"""
    print("=== LAST LINE ANALYSIS ===")
    
    lines = text.split('*')
    last_line = lines[-1].strip()
    print(f"Last line: '{last_line}'")
    print(f"Length: {len(last_line)}")
    
    # Check if it looks like it contains a flag
    if 'ZEo|gBoRoJogE' in last_line:
        print("Found potential flag pattern!")
        
        # Try different ciphers on this part
        flag_part = 'ZEo|gBoRoJogE g5oEJgs'
        print(f"Flag part: '{flag_part}'")
        
        # Try Caesar cipher
        for shift in range(26):
            result = ""
            for char in flag_part:
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
                    shifted = (ord(char) - base + shift) % 26
                    result += chr(base + shifted)
                else:
                    result += char
            
            print(f"Caesar shift {shift}: {result}")
            
            # Check if it looks like a flag
            if 'USCC' in result or 'FLAG' in result or 'CTF' in result:
                print(f"  *** POTENTIAL FLAG: {result} ***")
        
        # Try Vigenère with common keys
        keys = ['USCC', 'FLAG', 'KEY', 'SECRET', 'CIPHER']
        for key in keys:
            result = ""
            key_index = 0
            for char in flag_part:
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
                    key_char = key[key_index % len(key)]
                    key_shift = ord(key_char.upper()) - ord('A')
                    
                    shifted = (ord(char) - base + key_shift) % 26
                    result += chr(base + shifted)
                    key_index += 1
                else:
                    result += char
            
            print(f"Vigenère key '{key}': {result}")
            
            if 'USCC' in result or 'FLAG' in result or 'CTF' in result:
                print(f"  *** POTENTIAL FLAG: {result} ***")

def try_substitution_with_patterns(text):
    """Try substitution cipher based on patterns"""
    print("\n=== SUBSTITUTION WITH PATTERNS ===")
    
    # Look for common patterns that might indicate English
    # The character '^' appears very frequently and might be a space or common letter
    
    # Try mapping '^' to space
    text_with_spaces = text.replace('^', ' ')
    print(f"With '^' as space: {text_with_spaces[:100]}...")
    
    # Try mapping '^' to 'E' (most common letter)
    text_with_e = text.replace('^', 'E')
    print(f"With '^' as 'E': {text_with_e[:100]}...")
    
    # Try mapping '^' to 'A'
    text_with_a = text.replace('^', 'A')
    print(f"With '^' as 'A': {text_with_a[:100]}...")

def try_reverse_engineering(text):
    """Try to reverse engineer the cipher"""
    print("\n=== REVERSE ENGINEERING ===")
    
    # Look for the number 750 in the text (from the challenge title)
    if '750' in text:
        print("Found '750' in text - this might be a key!")
        
        # Try using 750 as a key for different ciphers
        key = '750'
        
        # Vigenère with 750
        result = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key[key_index % len(key)]
                key_shift = int(key_char)
                
                shifted = (ord(char) - base + key_shift) % 26
                result += chr(base + shifted)
                key_index += 1
            else:
                result += char
        
        print(f"Vigenère with key '750': {result[:100]}...")
        
        # Check for flag pattern
        if 'USCC{' in result:
            print(f"*** FOUND FLAG: {result} ***")
    
    # Look for other numbers that might be keys
    numbers = re.findall(r'\d+', text)
    unique_numbers = list(set(numbers))
    print(f"Unique numbers found: {unique_numbers}")
    
    # Try each number as a key
    for num in unique_numbers:
        if len(num) >= 2:  # Only try numbers with 2+ digits
            print(f"\nTrying number {num} as key:")
            
            # Vigenère with numeric key
            result = ""
            key_index = 0
            for char in text:
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
                    key_char = num[key_index % len(num)]
                    key_shift = int(key_char)
                    
                    shifted = (ord(char) - base + key_shift) % 26
                    result += chr(base + shifted)
                    key_index += 1
                else:
                    result += char
            
            # Check for English words
            if 'THE' in result or 'AND' in result or 'FOR' in result:
                print(f"  Found English words with key {num}")
                print(f"    Sample: {result[:100]}...")
            
            # Check for flag pattern
            if 'USCC{' in result:
                print(f"  *** FOUND FLAG: {result} ***")

def try_character_frequency_analysis(text):
    """Try character frequency analysis"""
    print("\n=== CHARACTER FREQUENCY ANALYSIS ===")
    
    # Get character frequencies
    freq = Counter(text)
    
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
    for char in text:
        mapped_text += char_map.get(char, char)
    
    print(f"\nMapped text sample: {mapped_text[:200]}...")
    
    # Check for flag pattern
    if 'USCC{' in mapped_text:
        print(f"*** FOUND FLAG: {mapped_text} ***")

def main():
    print("Final Cipher Solver")
    print("=" * 50)
    
    # Analyze last line
    analyze_last_line(encrypted)
    
    # Try substitution with patterns
    try_substitution_with_patterns(encrypted)
    
    # Try reverse engineering
    try_reverse_engineering(encrypted)
    
    # Try character frequency analysis
    try_character_frequency_analysis(encrypted)

if __name__ == "__main__":
    main()