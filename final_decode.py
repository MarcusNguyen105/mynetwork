#!/usr/bin/env python3

def clean_and_decode():
    """Try to clean up and decode the flag properly"""
    
    # We established: < = U, Q = S, ; = C, ) = {, * = }
    # Original: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    # Becomes: USCC{g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs}
    
    flag_content = "g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs"
    
    print("=== Cleaning and Decoding Flag ===")
    print(f"Original content: {flag_content}")
    
    # Maybe the special characters are just noise or separators
    # Let's try removing them and see what we get
    
    import re
    
    # Extract only alphanumeric characters
    clean_content = re.sub(r'[^a-zA-Z0-9]', '', flag_content)
    print(f"Alphanumeric only: {clean_content}")
    
    # Try ROT13 on the clean content
    rot13_clean = ""
    for char in clean_content:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rot13_clean += chr((ord(char) - base + 13) % 26 + base)
        else:
            rot13_clean += char
    
    print(f"ROT13 of clean content: {rot13_clean}")
    print(f"Potential flag: USCC{{{rot13_clean}}}")
    
    # Let's also try keeping the structure but only decoding letters
    structured_decode = ""
    for char in flag_content:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            structured_decode += chr((ord(char) - base + 13) % 26 + base)
        else:
            structured_decode += char
    
    print(f"Structured ROT13: {structured_decode}")
    print(f"Structured flag: USCC{{{structured_decode}}}")
    
    # Let's try other common transformations
    # Maybe it's not ROT13 but a different shift
    
    print("\n=== Trying Different Shifts on Clean Content ===")
    for shift in range(1, 26):
        shifted = ""
        for char in clean_content:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted += chr((ord(char) - base + shift) % 26 + base)
            else:
                shifted += char
        
        # Check if this looks like a reasonable flag content
        if any(word in shifted.lower() for word in ['random', 'number', 'generator', 'key', 'cipher', 'rng', 'prng', 'seed']):
            print(f"Shift {shift}: {shifted} (contains crypto-related word!)")
        elif shift in [1, 13, 25]:
            print(f"Shift {shift}: {shifted}")

def try_reverse_engineering():
    """Try to reverse engineer based on expected content"""
    
    print("\n=== Reverse Engineering ===")
    
    # The challenge is about RNGs, so the flag might contain words like:
    # RANDOM, NUMBER, GENERATOR, SEED, KEY, etc.
    
    clean_content = "g5BRRZEogBoRoJogEg5oEJgs"
    
    # Let's see if we can find patterns that match these words
    # For example, if "gBoRoJogE" decodes to "generator" or similar
    
    target_words = ['RANDOM', 'NUMBER', 'GENERATOR', 'SEED', 'KEY', 'RNG', 'PRNG']
    
    for word in target_words:
        print(f"\nTrying to match '{word}':")
        
        # Find substrings of the right length
        word_len = len(word)
        for i in range(len(clean_content) - word_len + 1):
            substr = clean_content[i:i+word_len]
            
            # Try different shifts to see if substr becomes word
            for shift in range(26):
                decoded = ""
                for char in substr:
                    if char.isalpha():
                        base = ord('A') if char.isupper() else ord('a')
                        decoded += chr((ord(char) - base + shift) % 26 + base)
                    else:
                        decoded += char
                
                if decoded.upper() == word:
                    print(f"  Found '{word}' at position {i} with shift {shift}: '{substr}' -> '{decoded}'")
                    
                    # Apply this shift to the entire content
                    full_decoded = ""
                    for char in clean_content:
                        if char.isalpha():
                            base = ord('A') if char.isupper() else ord('a')
                            full_decoded += chr((ord(char) - base + shift) % 26 + base)
                        else:
                            full_decoded += char
                    
                    print(f"    Full content with shift {shift}: {full_decoded}")
                    print(f"    Potential flag: USCC{{{full_decoded}}}")

def manual_inspection():
    """Manual inspection of the patterns"""
    
    print("\n=== Manual Inspection ===")
    
    # Let's look at the parts again:
    # g5BRR, ZEo, gBoRoJogE, g5oEJgs
    
    parts = ['g5BRR', 'ZEo', 'gBoRoJogE', 'g5oEJgs']
    
    print("Analyzing each part:")
    
    for part in parts:
        print(f"\nPart: '{part}'")
        
        # Try ROT13
        rot13_part = ""
        for char in part:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                rot13_part += chr((ord(char) - base + 13) % 26 + base)
            else:
                rot13_part += char
        print(f"  ROT13: {rot13_part}")
        
        # Try shift by 1
        shift1_part = ""
        for char in part:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shift1_part += chr((ord(char) - base + 1) % 26 + base)
            else:
                shift1_part += char
        print(f"  Shift+1: {shift1_part}")
        
        # Try shift by -1 (25)
        shift25_part = ""
        for char in part:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shift25_part += chr((ord(char) - base + 25) % 26 + base)
            else:
                shift25_part += char
        print(f"  Shift-1: {shift25_part}")

if __name__ == "__main__":
    clean_and_decode()
    try_reverse_engineering()
    manual_inspection()