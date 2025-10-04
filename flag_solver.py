#!/usr/bin/env python3
"""
Flag Solver - Focus on the last line which contains the flag pattern
"""

import string
import re
from collections import Counter

# The last line containing the flag
last_line = "vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs"

def try_caesar_on_flag_part(text):
    """Try Caesar cipher on the flag part"""
    print("=== CAESAR CIPHER ON FLAG PART ===")
    
    # Extract the flag part
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    print(f"Flag part: '{flag_part}'")
    
    for shift in range(26):
        result = ""
        for char in flag_part:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + shift) % 26
                result += chr(base + shifted)
            else:
                result += char
        
        print(f"Shift {shift:2d}: {result}")
        
        # Check if it looks like a flag
        if 'USCC' in result or 'FLAG' in result or 'CTF' in result:
            print(f"  *** POTENTIAL FLAG: {result} ***")

def try_vigenere_on_flag_part(text):
    """Try Vigenère cipher on the flag part"""
    print("\n=== VIGENÈRE CIPHER ON FLAG PART ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    
    # Try common keys
    keys = ['USCC', 'FLAG', 'KEY', 'SECRET', 'CIPHER', 'RANDOM', 'CUSTOM', '750']
    
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
        
        print(f"Key '{key}': {result}")
        
        if 'USCC' in result or 'FLAG' in result or 'CTF' in result:
            print(f"  *** POTENTIAL FLAG: {result} ***")

def try_substitution_on_flag_part(text):
    """Try substitution cipher on the flag part"""
    print("\n=== SUBSTITUTION CIPHER ON FLAG PART ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    
    # Try different character mappings
    mappings = [
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}'},
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}'},
    ]
    
    for i, mapping in enumerate(mappings):
        result = ""
        for char in flag_part:
            result += mapping.get(char, char)
        print(f"Mapping {i+1}: {result}")

def try_numeric_key_cipher(text):
    """Try cipher with numeric keys"""
    print("\n=== NUMERIC KEY CIPHER ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    
    # Try different numeric keys
    keys = ['750', '88', '5', '8', '3', '0']
    
    for key in keys:
        result = ""
        key_index = 0
        for char in flag_part:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key[key_index % len(key)]
                key_shift = int(key_char)
                
                shifted = (ord(char) - base + key_shift) % 26
                result += chr(base + shifted)
                key_index += 1
            else:
                result += char
        
        print(f"Key '{key}': {result}")
        
        if 'USCC' in result or 'FLAG' in result or 'CTF' in result:
            print(f"  *** POTENTIAL FLAG: {result} ***")

def try_reverse_cipher(text):
    """Try reverse cipher"""
    print("\n=== REVERSE CIPHER ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    
    # Try reversing the text
    reversed_text = flag_part[::-1]
    print(f"Reversed: {reversed_text}")
    
    # Try Caesar on reversed text
    for shift in range(26):
        result = ""
        for char in reversed_text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + shift) % 26
                result += chr(base + shifted)
            else:
                result += char
        
        print(f"Reversed + Shift {shift:2d}: {result}")
        
        if 'USCC' in result or 'FLAG' in result or 'CTF' in result:
            print(f"  *** POTENTIAL FLAG: {result} ***")

def try_atbash_cipher(text):
    """Try Atbash cipher"""
    print("\n=== ATBASH CIPHER ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    
    result = ""
    for char in flag_part:
        if char.isalpha():
            if char.isupper():
                result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                result += chr(ord('z') - (ord(char) - ord('a')))
        else:
            result += char
    
    print(f"Atbash: {result}")
    
    if 'USCC' in result or 'FLAG' in result or 'CTF' in result:
        print(f"  *** POTENTIAL FLAG: {result} ***")

def try_rot13_cipher(text):
    """Try ROT13 cipher"""
    print("\n=== ROT13 CIPHER ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    
    result = ""
    for char in flag_part:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + 13) % 26
            result += chr(base + shifted)
        else:
            result += char
    
    print(f"ROT13: {result}")
    
    if 'USCC' in result or 'FLAG' in result or 'CTF' in result:
        print(f"  *** POTENTIAL FLAG: {result} ***")

def try_all_combinations(text):
    """Try all combinations of different ciphers"""
    print("\n=== TRYING ALL COMBINATIONS ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    
    # Try different approaches
    approaches = [
        ("Caesar", lambda t, s: ''.join(chr((ord(c) - ord('A') + s) % 26 + ord('A')) if c.isupper() else chr((ord(c) - ord('a') + s) % 26 + ord('a')) if c.islower() else c for c in t)),
        ("Vigenère", lambda t, k: ''.join(chr((ord(c) - ord('A') + ord(k[i % len(k)]) - ord('A')) % 26 + ord('A')) if c.isupper() else chr((ord(c) - ord('a') + ord(k[i % len(k)]) - ord('A')) % 26 + ord('a')) if c.islower() else c for i, c in enumerate(t))),
    ]
    
    # Try Caesar with different shifts
    for shift in range(26):
        result = ""
        for char in flag_part:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + shift) % 26
                result += chr(base + shifted)
            else:
                result += char
        
        if 'USCC' in result:
            print(f"*** FOUND FLAG: {result} ***")
            return result
    
    return None

def main():
    print("Flag Solver")
    print("=" * 50)
    
    print(f"Last line: '{last_line}'")
    
    # Try different approaches
    try_caesar_on_flag_part(last_line)
    try_vigenere_on_flag_part(last_line)
    try_substitution_on_flag_part(last_line)
    try_numeric_key_cipher(last_line)
    try_reverse_cipher(last_line)
    try_atbash_cipher(last_line)
    try_rot13_cipher(last_line)
    
    # Try all combinations
    result = try_all_combinations(last_line)
    
    if result:
        print(f"\n*** FINAL FLAG: {result} ***")
    else:
        print("\nNo flag found with these approaches.")

if __name__ == "__main__":
    main()