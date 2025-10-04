#!/usr/bin/env python3

flag_line = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"

def try_all_caesar_shifts():
    """Try all Caesar cipher shifts on the flag line"""
    
    print("=== All Caesar Shifts ===")
    
    for shift in range(26):
        result = ""
        for char in flag_line:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        
        print(f"Shift +{shift:2d}: {result}")
        
        # Check for USCC pattern
        if result.startswith('USCC') or 'USCC{' in result:
            print(f"  *** FOUND USCC PATTERN! ***")
            return shift, result
    
    return None, None

def try_reverse_caesar():
    """Try Caesar shifts in reverse direction"""
    
    print("\n=== Reverse Caesar Shifts ===")
    
    for shift in range(26):
        result = ""
        for char in flag_line:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base - shift) % 26 + base)
            else:
                result += char
        
        if shift <= 5 or shift == 13 or shift >= 20:  # Show some key ones
            print(f"Shift -{shift:2d}: {result}")
        
        # Check for USCC pattern
        if result.startswith('USCC') or 'USCC{' in result:
            print(f"  *** FOUND USCC PATTERN! ***")
            return shift, result
    
    return None, None

def try_letter_number_substitution():
    """Try A=1, B=2, etc. substitutions"""
    
    print("\n=== Letter-Number Substitution ===")
    
    # Maybe some characters represent numbers?
    # Or maybe numbers represent letters?
    
    # A=1, B=2, ..., Z=26
    # or 1=A, 2=B, etc.
    
    # Look for patterns with the number 5 in the flag
    print(f"Original: {flag_line}")
    print("The number 5 appears twice - maybe it's significant")
    
    # What if 5 = E (5th letter)?
    result_5_to_E = flag_line.replace('5', 'E')
    print(f"Replace 5 with E: {result_5_to_E}")
    
    # What if other numbers have similar meanings?
    # We also see 8 in "w8|="
    result_8_to_H = result_5_to_E.replace('8', 'H')
    print(f"Replace 8 with H: {result_8_to_H}")

def try_keyboard_substitution():
    """Try keyboard-based substitutions"""
    
    print("\n=== Keyboard Substitution ===")
    
    # QWERTY keyboard layout
    qwerty = "qwertyuiopasdfghjklzxcvbnm"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Try QWERTY -> alphabet mapping
    qwerty_map = {}
    for i, char in enumerate(qwerty):
        if i < len(alphabet):
            qwerty_map[char] = alphabet[i]
            qwerty_map[char.upper()] = alphabet[i].upper()
    
    result = ""
    for char in flag_line:
        if char in qwerty_map:
            result += qwerty_map[char]
        else:
            result += char
    
    print(f"QWERTY mapping: {result}")

def try_simple_patterns():
    """Look for simple patterns in the flag"""
    
    print("\n=== Simple Pattern Analysis ===")
    
    print(f"Original flag line: {flag_line}")
    
    # What if we just need to rearrange or extract certain parts?
    
    # Extract all uppercase letters
    uppercase = ''.join([c for c in flag_line if c.isupper()])
    print(f"Uppercase letters: {uppercase}")
    
    # Extract all lowercase letters  
    lowercase = ''.join([c for c in flag_line if c.islower()])
    print(f"Lowercase letters: {lowercase}")
    
    # Extract all numbers
    numbers = ''.join([c for c in flag_line if c.isdigit()])
    print(f"Numbers: {numbers}")
    
    # What if the flag is just the alphabetic characters in order?
    alpha_only = ''.join([c for c in flag_line if c.isalpha()])
    print(f"All alphabetic: {alpha_only}")
    
    # Try ROT13 on just the alphabetic part
    rot13_alpha = ""
    for char in alpha_only:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rot13_alpha += chr((ord(char) - base + 13) % 26 + base)
    
    print(f"ROT13 of alphabetic: {rot13_alpha}")
    
    # What if we need to apply the substitution we found?
    # < = U, Q = S, ; = C, ) = {, * = }
    # But first extract the relevant part
    
    # The flag structure might be: <Q;;)....*
    # Which becomes: USCC{....}
    
    if flag_line.startswith('<Q;;)') and flag_line.endswith('*'):
        content = flag_line[5:-1]  # Remove <Q;;) and *
        print(f"Flag content (between markers): {content}")
        
        # Clean this content
        clean_content = ''.join([c for c in content if c.isalnum()])
        print(f"Clean content: {clean_content}")
        
        # Try ROT13 on clean content
        rot13_clean = ""
        for char in clean_content:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                rot13_clean += chr((ord(char) - base + 13) % 26 + base)
            else:
                rot13_clean += char
        
        print(f"ROT13 of clean content: {rot13_clean}")
        print(f"Potential flag: USCC{{{rot13_clean}}}")
        
        return f"USCC{{{rot13_clean}}}"
    
    return None

def manual_decode_attempt():
    """Manual decoding based on what we know"""
    
    print("\n=== Manual Decode ===")
    
    # We know from the context that this should be about RNGs
    # And the flag format is USCC{...}
    
    # Let's assume < = U, Q = S, ; = C, ) = {, * = }
    # And the middle part needs some transformation
    
    # Original: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    
    # Step 1: Apply known substitutions
    step1 = flag_line.replace('<', 'U').replace('Q', 'S').replace(';', 'C').replace(')', '{').replace('*', '}')
    print(f"Step 1 - substitution: {step1}")
    
    # Step 2: Extract flag content
    if '{' in step1 and '}' in step1:
        start = step1.find('{')
        end = step1.find('}')
        content = step1[start+1:end]
        print(f"Step 2 - flag content: {content}")
        
        # Step 3: Try different transformations on the content
        
        # Option A: Just clean it up
        clean_a = ''.join([c for c in content if c.isalnum()])
        print(f"Option A - alphanumeric only: USCC{{{clean_a}}}")
        
        # Option B: ROT13 on letters only
        rot13_b = ""
        for char in content:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                rot13_b += chr((ord(char) - base + 13) % 26 + base)
            elif char.isalnum():
                rot13_b += char
        print(f"Option B - ROT13 letters: USCC{{{rot13_b}}}")
        
        # Option C: Different Caesar shift
        for shift in [1, 3, 7, 11, 17, 19, 23, 25]:
            shifted = ""
            for char in content:
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
                    shifted += chr((ord(char) - base + shift) % 26 + base)
                elif char.isalnum():
                    shifted += char
            
            if shift in [1, 25]:  # Show a couple
                print(f"Option C - shift {shift}: USCC{{{shifted}}}")

if __name__ == "__main__":
    shift, result = try_all_caesar_shifts()
    
    if not result:
        shift, result = try_reverse_caesar()
    
    try_letter_number_substitution()
    try_keyboard_substitution()
    
    flag_candidate = try_simple_patterns()
    if flag_candidate:
        print(f"\nFlag candidate: {flag_candidate}")
    
    manual_decode_attempt()