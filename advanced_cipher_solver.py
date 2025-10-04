#!/usr/bin/env python3
"""
Advanced Cipher Solver - Looking for patterns and trying different approaches
"""

import string
import re
from collections import Counter
import itertools

# The encrypted message
encrypted = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

def analyze_structure(text):
    """Analyze the structure of the cipher text"""
    print("=== STRUCTURE ANALYSIS ===")
    
    # Split by lines
    lines = text.split('*')
    print(f"Number of lines: {len(lines)}")
    
    # Analyze each line
    for i, line in enumerate(lines):
        if line.strip():
            print(f"Line {i+1}: {len(line)} chars")
            # Count different separators
            separators = {'^': line.count('^'), '#': line.count('#'), '|': line.count('|')}
            print(f"  Separators: {separators}")
            
            # Look for patterns in segments
            segments = line.split('^')
            print(f"  Segments: {len(segments)}")
            
            # Check if segments look like words
            word_like_segments = []
            for seg in segments:
                if len(seg) > 2 and seg.isalnum():
                    word_like_segments.append(seg)
            
            if word_like_segments:
                print(f"  Word-like segments: {word_like_segments[:5]}")

def try_character_mapping(text):
    """Try to map characters to letters based on frequency and patterns"""
    print("\n=== CHARACTER MAPPING ANALYSIS ===")
    
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
    
    # Look for English words
    words = mapped_text.split()
    english_words = []
    for word in words:
        if len(word) > 2 and word.isalpha():
            # Check if it looks like English
            if any(common in word.upper() for common in ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL']):
                english_words.append(word)
    
    if english_words:
        print(f"Potential English words found: {english_words[:10]}")
    
    return mapped_text

def try_positional_cipher(text):
    """Try positional cipher where position determines the shift"""
    print("\n=== TRYING POSITIONAL CIPHER ===")
    
    # Try different positional patterns
    for pattern_len in [1, 2, 3, 4, 5]:
        print(f"\nTrying pattern length {pattern_len}:")
        
        # Create a pattern
        pattern = [i % 26 for i in range(pattern_len)]
        
        result = ""
        for i, char in enumerate(text):
            if char.isalpha():
                shift = pattern[i % pattern_len]
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + shift) % 26
                result += chr(base + shifted)
            else:
                result += char
        
        # Check for English words
        english_words = []
        words = result.split()
        for word in words:
            if len(word) > 2 and word.isalpha():
                if any(common in word.upper() for common in ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL']):
                    english_words.append(word)
        
        if english_words:
            print(f"  Found English words: {english_words[:5]}")
            print(f"  Sample: {result[:150]}...")

def try_keyword_cipher(text, keyword):
    """Try keyword-based cipher"""
    print(f"\n=== TRYING KEYWORD CIPHER: {keyword} ===")
    
    # Create alphabet with keyword first
    keyword_chars = []
    for char in keyword.upper():
        if char not in keyword_chars:
            keyword_chars.append(char)
    
    # Add remaining letters
    remaining = [char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if char not in keyword_chars]
    cipher_alphabet = keyword_chars + remaining
    
    # Create mapping
    char_map = {}
    for i, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        char_map[cipher_alphabet[i]] = char
    
    # Apply mapping
    result = ""
    for char in text:
        if char.isalpha():
            result += char_map.get(char.upper(), char)
        else:
            result += char
    
    # Check for English words
    english_words = []
    words = result.split()
    for word in words:
        if len(word) > 2 and word.isalpha():
            if any(common in word.upper() for common in ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL']):
                english_words.append(word)
    
    if english_words:
        print(f"Found English words: {english_words[:5]}")
        print(f"Sample: {result[:150]}...")

def look_for_flag_pattern(text):
    """Look for flag pattern in various cipher attempts"""
    print("\n=== LOOKING FOR FLAG PATTERN ===")
    
    flag_pattern = r'USCC\{[^}]+\}'
    
    # Try different Caesar shifts
    for shift in range(26):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + shift) % 26
                result += chr(base + shifted)
            else:
                result += char
        
        if re.search(flag_pattern, result, re.IGNORECASE):
            print(f"Found flag with Caesar shift {shift}:")
            print(result)
            return result
    
    # Try character frequency mapping
    freq = Counter(text)
    most_frequent = [char for char, count in freq.most_common(26)]
    english_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    
    char_map = {}
    for i, char in enumerate(most_frequent):
        if i < len(english_freq):
            char_map[char] = english_freq[i]
    
    mapped_text = ""
    for char in text:
        mapped_text += char_map.get(char, char)
    
    if re.search(flag_pattern, mapped_text, re.IGNORECASE):
        print("Found flag with frequency mapping:")
        print(mapped_text)
        return mapped_text
    
    return None

def main():
    print("Advanced Cipher Solver")
    print("=" * 50)
    
    # Analyze structure
    analyze_structure(encrypted)
    
    # Try character mapping
    mapped_text = try_character_mapping(encrypted)
    
    # Try positional cipher
    try_positional_cipher(encrypted)
    
    # Try keyword ciphers with common keywords
    keywords = ['KEY', 'FLAG', 'SECRET', 'PASSWORD', 'CIPHER', 'RANDOM', 'CUSTOM']
    for keyword in keywords:
        try_keyword_cipher(encrypted, keyword)
    
    # Look for flag pattern
    flag_result = look_for_flag_pattern(encrypted)
    
    if flag_result:
        print("\n=== FLAG FOUND ===")
        print(flag_result)
    else:
        print("\n=== NO FLAG PATTERN FOUND ===")
        print("Need to try more advanced techniques...")

if __name__ == "__main__":
    main()