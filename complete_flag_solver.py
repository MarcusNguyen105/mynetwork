#!/usr/bin/env python3
"""
Complete Flag Solver - Try to get the complete flag
"""

# The last line containing the flag
last_line = "vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs"

def analyze_flag_pattern():
    """Analyze the flag pattern more carefully"""
    print("=== ANALYZING FLAG PATTERN ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    print(f"Flag part: '{flag_part}'")
    print(f"Length: {len(flag_part)}")
    
    # Let's break it down character by character
    print("Character breakdown:")
    for i, char in enumerate(flag_part):
        print(f"  {i:2d}: '{char}'")
    
    # The expected pattern should be USCC{...}
    # So we need to map:
    # Z -> U, E -> S, o -> C, | -> C, g -> {, ... -> ..., 5 -> }
    
    # Let's try to figure out what the middle part should be
    # The middle part is "BoRoJogE" which should map to something meaningful
    
    print("\n=== TRYING DIFFERENT MIDDLE MAPPINGS ===")
    
    # Try different mappings for the middle part
    middle_part = "BoRoJogE"
    print(f"Middle part: '{middle_part}'")
    
    # Try different combinations
    combinations = [
        {'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G'},  # FLAG
        {'B': 'L', 'R': 'A', 'J': 'G', 'G': 'F'},  # LAGF
        {'B': 'A', 'R': 'G', 'J': 'F', 'G': 'L'},  # AGFL
        {'B': 'G', 'R': 'F', 'J': 'L', 'G': 'A'},  # GFLA
        {'B': 'C', 'R': 'T', 'J': 'F', 'G': 'L'},  # CTFL
        {'B': 'T', 'R': 'F', 'J': 'L', 'G': 'C'},  # TFLC
    ]
    
    base_mapping = {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', '5': '}', ' ': ' '}
    
    for i, combo in enumerate(combinations):
        full_mapping = {**base_mapping, **combo}
        result = ""
        for char in flag_part:
            result += full_mapping.get(char, char)
        print(f"Combination {i+1}: {result}")
        
        if 'USCC{' in result and '}' in result:
            print(f"  *** POTENTIAL FLAG: {result} ***")

def try_complete_mapping():
    """Try to get the complete flag"""
    print("\n=== TRYING COMPLETE MAPPING ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    
    # Let's try a different approach
    # Maybe the flag is not exactly what we think
    
    # Try different mappings for all characters
    mappings = [
        # Mapping 1: Based on common flag patterns
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}'},
        # Mapping 2: Try different approach
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'L', 'R': 'A', 'J': 'G', 'G': 'F', '5': '}'},
        # Mapping 3: Try with different characters
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'A', 'R': 'G', 'J': 'F', 'G': 'L', '5': '}'},
        # Mapping 4: Try with different approach
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'G', 'R': 'F', 'J': 'L', 'G': 'A', '5': '}'},
    ]
    
    for i, mapping in enumerate(mappings):
        result = ""
        for char in flag_part:
            result += mapping.get(char, char)
        print(f"Mapping {i+1}: {result}")
        
        if 'USCC{' in result and '}' in result:
            print(f"  *** POTENTIAL FLAG: {result} ***")

def try_different_approach():
    """Try a different approach to solve the flag"""
    print("\n=== TRYING DIFFERENT APPROACH ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    
    # Maybe the flag is not in the format we expect
    # Let's try to map the characters to get something meaningful
    
    # Try different mappings
    mappings = [
        # Mapping 1: Try to get a meaningful flag
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}'},
        # Mapping 2: Try different approach
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'L', 'R': 'A', 'J': 'G', 'G': 'F', '5': '}'},
        # Mapping 3: Try with different characters
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'A', 'R': 'G', 'J': 'F', 'G': 'L', '5': '}'},
        # Mapping 4: Try with different approach
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'G', 'R': 'F', 'J': 'L', 'G': 'A', '5': '}'},
    ]
    
    for i, mapping in enumerate(mappings):
        result = ""
        for char in flag_part:
            result += mapping.get(char, char)
        print(f"Mapping {i+1}: {result}")
        
        # Check if it looks like a valid flag
        if 'USCC{' in result and '}' in result:
            print(f"  *** POTENTIAL FLAG: {result} ***")
            
            # Try to clean it up
            cleaned = result.replace('{', '{').replace('}', '}')
            print(f"  Cleaned: {cleaned}")

def main():
    print("Complete Flag Solver")
    print("=" * 50)
    
    print(f"Last line: '{last_line}'")
    
    # Analyze flag pattern
    analyze_flag_pattern()
    
    # Try complete mapping
    try_complete_mapping()
    
    # Try different approach
    try_different_approach()
    
    print("\n=== FINAL ATTEMPT ===")
    
    # Let's try one more approach
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    
    # Try the most likely mapping
    mapping = {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}', ' ': ' '}
    
    result = ""
    for char in flag_part:
        result += mapping.get(char, char)
    
    print(f"Final result: {result}")
    
    # Try to clean it up
    if 'USCC{' in result:
        # Extract the flag part
        start = result.find('USCC{')
        end = result.find('}', start) + 1
        if end > start:
            flag = result[start:end]
            print(f"*** EXTRACTED FLAG: {flag} ***")
        else:
            print(f"*** POTENTIAL FLAG: {result} ***")

if __name__ == "__main__":
    main()