#!/usr/bin/env python3

# We found that < = U, Q = S, ; = C, ) = {
# So the flag starts with USCC{
# Now we need to decode: g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*

flag_content = "g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"

def find_closing_brace():
    """Find where the flag should end (looking for })"""
    print("=== Finding Flag Boundaries ===")
    
    # The flag should end with }
    # Let's see what character might represent }
    # We know ) = {, so maybe * = } or some other character
    
    # Let's try different characters as }
    candidates = ['*', '%', '_', '|']
    
    for char in candidates:
        print(f"If '{char}' = '}}', flag content would be everything before it")
        
        if char in flag_content:
            pos = flag_content.find(char)
            content_before = flag_content[:pos]
            print(f"  Content: '{content_before}'")

def try_rot13_on_content():
    """Try ROT13 on the flag content"""
    print("\n=== ROT13 on Flag Content ===")
    
    # Remove the * at the end and try ROT13
    content = flag_content.rstrip('*')
    print(f"Content without *: '{content}'")
    
    rot13_result = ""
    for char in content:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rot13_result += chr((ord(char) - base + 13) % 26 + base)
        else:
            rot13_result += char
    
    print(f"ROT13 result: '{rot13_result}'")
    
    # Try other rotations too
    for shift in [1, 2, 3, 5, 7, 11, 17, 19, 23, 25]:
        shifted = ""
        for char in content:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted += chr((ord(char) - base + shift) % 26 + base)
            else:
                shifted += char
        
        if shift in [1, 13, 25]:  # Show some key ones
            print(f"Shift {shift}: '{shifted}'")

def analyze_structure():
    """Analyze the structure of the flag content"""
    print("\n=== Structure Analysis ===")
    
    content = "g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs"
    print(f"Content: '{content}'")
    
    # This might be multiple words or parts
    # Let's see if we can identify word boundaries
    
    # Split by spaces and special characters
    import re
    parts = re.split(r'[^a-zA-Z0-9]', content)
    parts = [p for p in parts if p]  # Remove empty strings
    
    print(f"Parts: {parts}")
    
    # Try ROT13 on each part
    print("\nROT13 on each part:")
    for part in parts:
        rot13_part = ""
        for char in part:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                rot13_part += chr((ord(char) - base + 13) % 26 + base)
            else:
                rot13_part += char
        print(f"'{part}' -> '{rot13_part}'")

def try_complete_flag():
    """Try to construct the complete flag"""
    print("\n=== Complete Flag Construction ===")
    
    # We know the start: USCC{
    # We need to decode the middle and find the end
    
    # Let's assume * = } (common in substitution ciphers)
    # So the flag would be: USCC{g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs}
    
    # But we need to decode the middle part
    # Let's try ROT13 on the entire middle section
    
    middle = "g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs"
    
    # Try ROT13
    rot13_middle = ""
    for char in middle:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rot13_middle += chr((ord(char) - base + 13) % 26 + base)
        else:
            rot13_middle += char
    
    flag_rot13 = f"USCC{{{rot13_middle}}}"
    print(f"Flag with ROT13 middle: {flag_rot13}")
    
    # Try other common shifts
    for shift in [1, 25]:  # +1 and -1
        shifted_middle = ""
        for char in middle:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted_middle += chr((ord(char) - base + shift) % 26 + base)
            else:
                shifted_middle += char
        
        flag_shifted = f"USCC{{{shifted_middle}}}"
        print(f"Flag with shift {shift}: {flag_shifted}")

def test_mixed_cipher():
    """Test if it's a mixed cipher (different parts use different methods)"""
    print("\n=== Mixed Cipher Test ===")
    
    # Maybe the structure is different
    # Let's look at the original again: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    
    # What if the entire thing uses the same substitution as the beginning?
    # We found < = U, Q = S, ; = C, ) = {
    
    # Let's build a more complete mapping
    # Looking at common patterns, maybe we can deduce more mappings
    
    # If this is about RNGs and cryptography, common words might be:
    # "random", "number", "generator", "key", "cipher", etc.
    
    # Let's try to extend our mapping
    mapping = {'<': 'U', 'Q': 'S', ';': 'C', ')': '{', '*': '}'}
    
    # Apply this mapping to see what we get
    original = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    result = ""
    
    for char in original:
        if char in mapping:
            result += mapping[char]
        else:
            result += char
    
    print(f"With extended mapping: {result}")
    
    # Now try ROT13 on the remaining letters
    final_result = ""
    for char in result:
        if char.isalpha() and char not in "USCC{}":
            base = ord('A') if char.isupper() else ord('a')
            final_result += chr((ord(char) - base + 13) % 26 + base)
        else:
            final_result += char
    
    print(f"After ROT13 on remaining letters: {final_result}")

if __name__ == "__main__":
    find_closing_brace()
    try_rot13_on_content()
    analyze_structure()
    try_complete_flag()
    test_mixed_cipher()