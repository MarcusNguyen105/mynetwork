#!/usr/bin/env python3
"""
Lost Cipher Guesser - Solver for the encrypted message
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

def analyze_cipher(text):
    """Analyze the cipher text for patterns and characteristics"""
    print("=== CIPHER ANALYSIS ===")
    print(f"Total length: {len(text)}")
    print(f"Unique characters: {len(set(text))}")
    print(f"Character frequency (top 10):")
    
    # Count character frequencies
    freq = Counter(text)
    for char, count in freq.most_common(10):
        print(f"  '{char}': {count}")
    
    print(f"\nAll unique characters: {sorted(set(text))}")
    
    # Look for patterns
    print(f"\nLines: {text.count('*')}")
    print(f"Words (separated by spaces): {len(text.split())}")
    
    # Check for common English patterns
    print(f"\nPotential word separators: {[c for c in text if c in '^#*-']}")
    
    return freq

def try_caesar_cipher(text, shift):
    """Try Caesar cipher with given shift"""
    result = ""
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Apply shift
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char
    return result

def try_substitution_cipher(text, key_map):
    """Try substitution cipher with given key mapping"""
    result = ""
    for char in text:
        result += key_map.get(char, char)
    return result

def try_xor_cipher(text, key):
    """Try XOR cipher with given key"""
    result = ""
    key_len = len(key)
    for i, char in enumerate(text):
        result += chr(ord(char) ^ ord(key[i % key_len]))
    return result

def try_rail_fence_cipher(text, rails):
    """Try rail fence cipher with given number of rails"""
    if rails <= 1:
        return text
    
    # Create the rail pattern
    pattern = []
    for i in range(rails):
        pattern.append([])
    
    # Fill the pattern
    rail = 0
    direction = 1
    for char in text:
        pattern[rail].append(char)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    # Read the pattern
    result = ""
    for rail in pattern:
        result += "".join(rail)
    
    return result

def try_columnar_transposition(text, key_length):
    """Try columnar transposition cipher"""
    # Remove spaces and special characters for analysis
    clean_text = re.sub(r'[^a-zA-Z]', '', text)
    
    if len(clean_text) % key_length != 0:
        # Pad if necessary
        clean_text += 'X' * (key_length - len(clean_text) % key_length)
    
    # Create columns
    columns = []
    for i in range(key_length):
        columns.append(clean_text[i::key_length])
    
    # Try different column orders
    for perm in itertools.permutations(range(key_length)):
        result = ""
        for i in perm:
            result += columns[i]
        yield result

def look_for_english_patterns(text):
    """Look for patterns that might indicate English text"""
    # Common English words
    common_words = ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'CAN', 'HER', 'WAS', 'ONE', 'OUR', 'HAD', 'BY', 'WORD', 'WHAT', 'SOME', 'WE', 'IT', 'IS', 'OR', 'AN', 'AS', 'AT', 'BE', 'HE', 'IN', 'ON', 'TO', 'OF', 'A', 'I']
    
    # Check for common letter patterns
    text_upper = text.upper()
    found_words = []
    
    for word in common_words:
        if word in text_upper:
            found_words.append(word)
    
    return found_words

def main():
    print("Lost Cipher Guesser - Solver")
    print("=" * 50)
    
    # Analyze the cipher
    freq = analyze_cipher(encrypted)
    
    print("\n=== TRYING DIFFERENT CIPHER TYPES ===")
    
    # Try Caesar cipher with different shifts
    print("\n1. Trying Caesar Cipher:")
    for shift in range(1, 26):
        decrypted = try_caesar_cipher(encrypted, shift)
        english_words = look_for_english_patterns(decrypted)
        if english_words:
            print(f"  Shift {shift}: Found English words: {english_words[:5]}")
            print(f"    Sample: {decrypted[:100]}...")
    
    # Try XOR with common keys
    print("\n2. Trying XOR Cipher:")
    common_keys = ['A', 'B', 'C', 'KEY', 'FLAG', 'SECRET', 'PASSWORD']
    for key in common_keys:
        decrypted = try_xor_cipher(encrypted, key)
        english_words = look_for_english_patterns(decrypted)
        if english_words:
            print(f"  Key '{key}': Found English words: {english_words[:5]}")
            print(f"    Sample: {decrypted[:100]}...")
    
    # Try rail fence cipher
    print("\n3. Trying Rail Fence Cipher:")
    for rails in range(2, 8):
        decrypted = try_rail_fence_cipher(encrypted, rails)
        english_words = look_for_english_patterns(decrypted)
        if english_words:
            print(f"  Rails {rails}: Found English words: {english_words[:5]}")
            print(f"    Sample: {decrypted[:100]}...")
    
    # Try columnar transposition
    print("\n4. Trying Columnar Transposition:")
    for key_len in range(2, 8):
        print(f"  Key length {key_len}:")
        for i, decrypted in enumerate(try_columnar_transposition(encrypted, key_len)):
            if i >= 3:  # Limit to first 3 permutations
                break
            english_words = look_for_english_patterns(decrypted)
            if english_words:
                print(f"    Permutation {i}: Found English words: {english_words[:5]}")
                print(f"      Sample: {decrypted[:100]}...")
    
    # Look for flag pattern
    print("\n=== LOOKING FOR FLAG PATTERN ===")
    flag_pattern = r'USCC\{[^}]+\}'
    for shift in range(26):
        decrypted = try_caesar_cipher(encrypted, shift)
        if re.search(flag_pattern, decrypted, re.IGNORECASE):
            print(f"Found flag with Caesar shift {shift}:")
            print(decrypted)
            break

if __name__ == "__main__":
    main()