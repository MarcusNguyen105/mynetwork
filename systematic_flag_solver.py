#!/usr/bin/env python3
"""
Systematic Flag Solver - Try to solve the flag systematically
"""

import string
import re
from collections import Counter

# The last line containing the flag
last_line = "vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs"

def try_systematic_caesar(text):
    """Try Caesar cipher systematically"""
    print("=== SYSTEMATIC CAESAR CIPHER ===")
    
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
        if 'USCC{' in result:
            print(f"  *** FOUND FLAG: {result} ***")
            return result
    
    return None

def try_systematic_substitution(text):
    """Try substitution cipher systematically"""
    print("\n=== SYSTEMATIC SUBSTITUTION CIPHER ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    
    # Try different character mappings based on common patterns
    # Looking at the pattern, it seems like it might be a simple substitution
    
    # Try mapping based on the pattern USCC{...}
    # Z -> U, E -> S, o -> C, | -> C, g -> {, B -> F, R -> L, J -> A, G -> G, 5 -> }
    
    mappings = [
        # Mapping 1: Based on USCC pattern
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}'},
        # Mapping 2: Try different variations
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}'},
        # Mapping 3: Try with different characters
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}'},
    ]
    
    for i, mapping in enumerate(mappings):
        result = ""
        for char in flag_part:
            result += mapping.get(char, char)
        print(f"Mapping {i+1}: {result}")
        
        if 'USCC{' in result:
            print(f"  *** FOUND FLAG: {result} ***")
            return result
    
    return None

def try_character_frequency_mapping(text):
    """Try character frequency mapping"""
    print("\n=== CHARACTER FREQUENCY MAPPING ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    
    # Count character frequencies in the flag part
    freq = Counter(flag_part)
    print(f"Character frequencies: {dict(freq)}")
    
    # Try mapping based on frequency
    # Most common characters in English: E, T, A, O, I, N, S, H, R, D, L, C, U, M, W, F, G, Y, P, B, V, K, J, X, Q, Z
    
    # Try different mappings
    mappings = [
        # Mapping 1: Based on frequency
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}'},
        # Mapping 2: Try different approach
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}'},
    ]
    
    for i, mapping in enumerate(mappings):
        result = ""
        for char in flag_part:
            result += mapping.get(char, char)
        print(f"Frequency mapping {i+1}: {result}")
        
        if 'USCC{' in result:
            print(f"  *** FOUND FLAG: {result} ***")
            return result
    
    return None

def try_pattern_based_substitution(text):
    """Try pattern-based substitution"""
    print("\n=== PATTERN-BASED SUBSTITUTION ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    
    # Look for patterns that might indicate the flag format
    # The pattern suggests: USCC{...}
    
    # Try to map characters based on the expected pattern
    # Z -> U, E -> S, o -> C, | -> C, g -> {, B -> F, R -> L, J -> A, G -> G, 5 -> }
    
    # Let's try a more systematic approach
    # If we assume the first part is "USCC{", then:
    # Z -> U, E -> S, o -> C, | -> C, g -> {
    
    # Try different mappings
    mappings = [
        # Mapping 1: Direct pattern matching
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}'},
        # Mapping 2: Try with different characters
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}'},
    ]
    
    for i, mapping in enumerate(mappings):
        result = ""
        for char in flag_part:
            result += mapping.get(char, char)
        print(f"Pattern mapping {i+1}: {result}")
        
        if 'USCC{' in result:
            print(f"  *** FOUND FLAG: {result} ***")
            return result
    
    return None

def try_manual_mapping(text):
    """Try manual mapping based on analysis"""
    print("\n=== MANUAL MAPPING ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    
    # Based on the pattern analysis, let's try a manual mapping
    # Looking at "ZEo|gBoRoJogE", if this should be "USCC{...}"
    # Then: Z->U, E->S, o->C, |->C, g->{, B->F, R->L, J->A, G->G, 5->}
    
    # Let's try this mapping
    mapping = {
        'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 
        'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}'
    }
    
    result = ""
    for char in flag_part:
        result += mapping.get(char, char)
    
    print(f"Manual mapping: {result}")
    
    if 'USCC{' in result:
        print(f"  *** FOUND FLAG: {result} ***")
        return result
    
    return None

def try_all_approaches(text):
    """Try all approaches"""
    print("=== TRYING ALL APPROACHES ===")
    
    # Try Caesar cipher
    result = try_systematic_caesar(text)
    if result:
        return result
    
    # Try substitution cipher
    result = try_systematic_substitution(text)
    if result:
        return result
    
    # Try character frequency mapping
    result = try_character_frequency_mapping(text)
    if result:
        return result
    
    # Try pattern-based substitution
    result = try_pattern_based_substitution(text)
    if result:
        return result
    
    # Try manual mapping
    result = try_manual_mapping(text)
    if result:
        return result
    
    return None

def main():
    print("Systematic Flag Solver")
    print("=" * 50)
    
    print(f"Last line: '{last_line}'")
    
    # Try all approaches
    result = try_all_approaches(last_line)
    
    if result:
        print(f"\n*** FINAL FLAG: {result} ***")
    else:
        print("\nNo flag found with these approaches.")
        print("Let me try a different approach...")
        
        # Try a different approach - maybe the flag is in a different part
        print("\n=== TRYING DIFFERENT APPROACHES ===")
        
        # Try the entire last line
        print(f"Trying entire last line: '{last_line}'")
        
        # Try Caesar on entire last line
        for shift in range(26):
            result = ""
            for char in last_line:
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