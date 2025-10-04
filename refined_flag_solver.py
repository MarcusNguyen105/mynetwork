#!/usr/bin/env python3
"""
Refined Flag Solver - Refine the mapping to get the complete flag
"""

# The last line containing the flag
last_line = "vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs"

def refine_mapping():
    """Refine the mapping to get the complete flag"""
    print("=== REFINING MAPPING ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    print(f"Flag part: '{flag_part}'")
    
    # Based on the pattern, let's try to map each character
    # We know it should start with "USCC{"
    # So: Z->U, E->S, o->C, |->C, g->{
    
    # Let's try different mappings for the remaining characters
    # The pattern suggests it should be "USCC{...}"
    
    # Try different mappings for the remaining characters
    mappings = [
        # Mapping 1: Based on the pattern
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}'},
        # Mapping 2: Try different characters
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}'},
        # Mapping 3: Try with different approach
        {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', 'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G', '5': '}'},
    ]
    
    for i, mapping in enumerate(mappings):
        result = ""
        for char in flag_part:
            result += mapping.get(char, char)
        print(f"Mapping {i+1}: {result}")
    
    # Let's try a more systematic approach
    # If we assume the flag format is USCC{...}, then we need to figure out what the ... part should be
    
    # Let's try to map the characters more carefully
    # Z -> U, E -> S, o -> C, | -> C, g -> {, B -> ?, R -> ?, J -> ?, G -> ?, 5 -> }
    
    # Try different mappings for the middle part
    print("\n=== TRYING DIFFERENT MIDDLE MAPPINGS ===")
    
    # Let's try different combinations for the middle part
    middle_mappings = [
        {'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G'},
        {'B': 'L', 'R': 'A', 'J': 'G', 'G': 'F'},
        {'B': 'A', 'R': 'G', 'J': 'F', 'G': 'L'},
        {'B': 'G', 'R': 'F', 'J': 'L', 'G': 'A'},
    ]
    
    base_mapping = {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', '5': '}'}
    
    for i, middle_mapping in enumerate(middle_mappings):
        full_mapping = {**base_mapping, **middle_mapping}
        result = ""
        for char in flag_part:
            result += full_mapping.get(char, char)
        print(f"Middle mapping {i+1}: {result}")
        
        if 'USCC{' in result and '}' in result:
            print(f"  *** POTENTIAL FLAG: {result} ***")

def try_character_by_character():
    """Try mapping character by character"""
    print("\n=== CHARACTER BY CHARACTER MAPPING ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    print(f"Flag part: '{flag_part}'")
    
    # Let's try to map each character individually
    # We know it should start with "USCC{"
    
    # Try different mappings for each character
    char_mappings = {
        'Z': 'U',
        'E': 'S', 
        'o': 'C',
        '|': 'C',
        'g': '{',
        'B': 'F',  # Try different values
        'R': 'L',  # Try different values
        'J': 'A',  # Try different values
        'G': 'G',  # Try different values
        '5': '}',
        ' ': ' ',  # Space stays space
    }
    
    result = ""
    for char in flag_part:
        result += char_mappings.get(char, char)
    
    print(f"Character mapping: {result}")
    
    # Try different combinations
    print("\n=== TRYING DIFFERENT COMBINATIONS ===")
    
    # Try different values for B, R, J, G
    for b_val in ['F', 'L', 'A', 'G']:
        for r_val in ['F', 'L', 'A', 'G']:
            for j_val in ['F', 'L', 'A', 'G']:
                for g_val in ['F', 'L', 'A', 'G']:
                    if b_val != r_val != j_val != g_val:  # All different
                        char_mappings = {
                            'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{',
                            'B': b_val, 'R': r_val, 'J': j_val, 'G': g_val, '5': '}',
                            ' ': ' '
                        }
                        
                        result = ""
                        for char in flag_part:
                            result += char_mappings.get(char, char)
                        
                        if 'USCC{' in result and '}' in result:
                            print(f"*** FOUND FLAG: {result} ***")
                            return result
    
    return None

def try_systematic_approach():
    """Try a systematic approach to find the flag"""
    print("\n=== SYSTEMATIC APPROACH ===")
    
    flag_part = "ZEo|gBoRoJogE g5oEJgs"
    
    # We know the pattern should be USCC{...}
    # Let's try to map the characters systematically
    
    # Try different mappings for the middle part
    # The middle part is "BoRoJogE" which should map to something like "FLAG" or similar
    
    # Let's try different combinations
    combinations = [
        {'B': 'F', 'R': 'L', 'J': 'A', 'G': 'G'},  # FLAG
        {'B': 'L', 'R': 'A', 'J': 'G', 'G': 'F'},  # LAGF
        {'B': 'A', 'R': 'G', 'J': 'F', 'G': 'L'},  # AGFL
        {'B': 'G', 'R': 'F', 'J': 'L', 'G': 'A'},  # GFLA
    ]
    
    base_mapping = {'Z': 'U', 'E': 'S', 'o': 'C', '|': 'C', 'g': '{', '5': '}', ' ': ' '}
    
    for i, combo in enumerate(combinations):
        full_mapping = {**base_mapping, **combo}
        result = ""
        for char in flag_part:
            result += full_mapping.get(char, char)
        print(f"Combination {i+1}: {result}")
        
        if 'USCC{' in result and '}' in result:
            print(f"  *** FOUND FLAG: {result} ***")
            return result
    
    return None

def main():
    print("Refined Flag Solver")
    print("=" * 50)
    
    print(f"Last line: '{last_line}'")
    
    # Try refining the mapping
    refine_mapping()
    
    # Try character by character
    result = try_character_by_character()
    if result:
        print(f"\n*** FINAL FLAG: {result} ***")
        return
    
    # Try systematic approach
    result = try_systematic_approach()
    if result:
        print(f"\n*** FINAL FLAG: {result} ***")
        return
    
    print("\nNo flag found with these approaches.")

if __name__ == "__main__":
    main()