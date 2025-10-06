#!/usr/bin/env python3

def try_all_shifts(text):
    """Try all possible Caesar cipher shifts"""
    results = []
    for shift in range(26):
        decoded = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    decoded += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    decoded += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                decoded += char
        results.append((shift, decoded))
    return results

def analyze_flag_candidates():
    """Analyze potential flag candidates"""
    
    print("=== FLAG CANDIDATE ANALYSIS ===")
    
    # The end pattern: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    
    # Let's try different interpretations
    # Maybe the flag is: ZEo|gBoRoJogE g5oEJgs (without the special characters)
    
    flag_candidate = "ZEo|gBoRoJogE g5oEJgs"
    print(f"Flag candidate: {flag_candidate}")
    
    # Try all shifts
    shifts = try_all_shifts(flag_candidate)
    print("\nAll Caesar shifts:")
    for shift, decoded in shifts:
        print(f"Shift {shift:2d}: {decoded}")
    
    # Let's also try the part before the spaces
    first_part = "ZEo|gBoRoJogE"
    second_part = "g5oEJgs"
    
    print(f"\nFirst part: {first_part}")
    print(f"Second part: {second_part}")
    
    # Try shifts on each part
    print("\nFirst part shifts:")
    first_shifts = try_all_shifts(first_part)
    for shift, decoded in first_shifts:
        print(f"Shift {shift:2d}: {decoded}")
    
    print("\nSecond part shifts:")
    second_shifts = try_all_shifts(second_part)
    for shift, decoded in second_shifts:
        print(f"Shift {shift:2d}: {decoded}")

def try_different_interpretations():
    """Try different ways to interpret the end pattern"""
    
    print("\n=== DIFFERENT INTERPRETATIONS ===")
    
    end_pattern = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    
    # Maybe the flag is embedded differently
    # Let's try to extract just the alphabetic parts
    
    # Extract all alphabetic characters
    alpha_only = ''.join([c for c in end_pattern if c.isalpha()])
    print(f"Alphabetic only: {alpha_only}")
    
    # Try shifts on alphabetic only
    alpha_shifts = try_all_shifts(alpha_only)
    print("\nAlphabetic shifts:")
    for shift, decoded in alpha_shifts:
        if 'flag' in decoded.lower() or 'key' in decoded.lower() or 'uscc' in decoded.lower():
            print(f"Shift {shift:2d}: {decoded} *** POTENTIAL MATCH ***")
        else:
            print(f"Shift {shift:2d}: {decoded}")
    
    # Maybe the flag is in the middle part
    # Let's try: g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs
    
    middle_part = "g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs"
    print(f"\nMiddle part: {middle_part}")
    
    # Extract alphabetic from middle part
    middle_alpha = ''.join([c for c in middle_part if c.isalpha()])
    print(f"Middle alphabetic: {middle_alpha}")
    
    middle_shifts = try_all_shifts(middle_alpha)
    print("\nMiddle alphabetic shifts:")
    for shift, decoded in middle_shifts:
        if 'flag' in decoded.lower() or 'key' in decoded.lower() or 'uscc' in decoded.lower():
            print(f"Shift {shift:2d}: {decoded} *** POTENTIAL MATCH ***")
        else:
            print(f"Shift {shift:2d}: {decoded}")

def try_reverse_engineering():
    """Try to reverse engineer the flag"""
    
    print("\n=== REVERSE ENGINEERING ===")
    
    # If the flag format is USCC{...}, let's try to work backwards
    
    # Maybe the flag is: USCC{some_text_here}
    # And it's encoded as: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    
    # Let's try to map USCC{ to <Q;;)
    # U -> <, S -> Q, C -> ;, C -> ;, { -> )
    
    # This suggests a mapping where:
    # U = <
    # S = Q  
    # C = ;
    # { = )
    
    # Let's see if this pattern continues
    
    print("Trying to map USCC{ to <Q;;):")
    print("U -> <")
    print("S -> Q")
    print("C -> ;")
    print("{ -> )")
    
    # Let's try to continue this pattern
    # Maybe the flag is: USCC{flag_text_here}
    
    # If we assume the flag text is: ZEo|gBoRoJogE g5oEJgs
    # Let's try to decode this part
    
    flag_text = "ZEo|gBoRoJogE g5oEJgs"
    
    # Try different approaches
    print(f"\nFlag text: {flag_text}")
    
    # Maybe it's a simple substitution where each character is shifted
    # Let's try to find a pattern
    
    # Looking at the characters: Z E o | g B o R o J o g E   g 5 o E J g s
    # Let's try to decode this as if it's a simple substitution
    
    # Maybe the | and 5 are separators or special characters
    # Let's try: ZEo gBoRoJogE g oEJgs
    
    parts = flag_text.split('|')
    print(f"Split by |: {parts}")
    
    # Try shifts on each part
    for i, part in enumerate(parts):
        print(f"\nPart {i}: {part}")
        part_shifts = try_all_shifts(part)
        for shift, decoded in part_shifts:
            if 'flag' in decoded.lower() or 'key' in decoded.lower():
                print(f"  Shift {shift:2d}: {decoded} *** POTENTIAL MATCH ***")
            else:
                print(f"  Shift {shift:2d}: {decoded}")

if __name__ == "__main__":
    analyze_flag_candidates()
    try_different_interpretations()
    try_reverse_engineering()