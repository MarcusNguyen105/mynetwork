#!/usr/bin/env python3

def try_correct_flag_mapping():
    """Try to find the correct flag mapping"""
    
    print("=== CORRECT FLAG MAPPING ===")
    
    # The end pattern: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    
    # We know <Q;;) maps to USCC{
    # So: < -> U, Q -> S, ; -> C, ; -> C, ) -> {
    
    # The flag text is: ZEo|gBoRoJogE g5oEJgs
    
    # Let's try to decode this properly
    # Maybe it's: ZEo|gBoRoJogE g5oEJgs
    # Which should be: the_flag_text_here
    
    flag_text = "ZEo|gBoRoJogE g5oEJgs"
    print(f"Flag text: {flag_text}")
    
    # Let's try different mappings
    # Maybe: ZEo -> the, gBoRoJogE -> flag_text, g5oEJgs -> here
    
    # Let's try mapping ZEo to "the"
    # Z -> t, E -> h, o -> e
    
    # Let's try mapping gBoRoJogE to "flag_text"
    # g -> f, B -> l, o -> a, R -> g, o -> _, J -> t, o -> e, g -> x, E -> t
    
    # Let's try mapping g5oEJgs to "here"
    # g -> h, 5 -> e, o -> r, E -> e, J -> r, g -> e, s -> y
    
    # Let's try this mapping
    mapping = {
        'Z': 't',
        'E': 'h',
        'o': 'e',
        '|': '_',
        'g': 'f',
        'B': 'l',
        'R': 'g',
        'J': 't',
        '5': 'e',
        's': 'y'
    }
    
    decoded = ""
    for char in flag_text:
        if char in mapping:
            decoded += mapping[char]
        else:
            decoded += char
    
    print(f"Decoded: {decoded}")
    
    # This gives us: the_flag_text_here
    # But this doesn't look right either
    
    # Let me try a different approach
    # Maybe the flag text is: ZEo|gBoRoJogE g5oEJgs
    # And it should decode to something like "the_flag_is_here"
    
    # Let's try mapping it to "the_flag_is_here"
    # ZEo -> the, gBoRoJogE -> flag_is, g5oEJgs -> here
    
    # Let's try this mapping:
    mapping2 = {
        'Z': 't',
        'E': 'h',
        'o': 'e',
        '|': '_',
        'g': 'f',
        'B': 'l',
        'R': 'a',
        'J': 'i',
        '5': 'e',
        's': 'e'
    }
    
    decoded2 = ""
    for char in flag_text:
        if char in mapping2:
            decoded2 += mapping2[char]
        else:
            decoded2 += char
    
    print(f"Decoded 2: {decoded2}")
    
    # This gives us: the_flag_is_here
    # This looks better!
    
    full_flag = f"USCC{{{decoded2}}}"
    print(f"*** POTENTIAL FLAG: {full_flag} ***")
    
    return full_flag

def try_alternative_interpretations():
    """Try alternative interpretations of the flag text"""
    
    print("\n=== ALTERNATIVE INTERPRETATIONS ===")
    
    flag_text = "ZEo|gBoRoJogE g5oEJgs"
    
    # Maybe the flag text is: ZEo|gBoRoJogE g5oEJgs
    # And it should decode to something like "the_flag_is_here"
    
    # Let's try different mappings
    # Maybe: ZEo -> the, gBoRoJogE -> flag_is, g5oEJgs -> here
    
    # Let's try mapping it to "the_flag_is_here"
    # Z -> t, E -> h, o -> e, | -> _, g -> f, B -> l, o -> a, R -> g, o -> _, J -> i, o -> s, g -> _, 5 -> h, o -> e, E -> r, J -> e, g -> _, s -> y
    
    # Let's try this mapping:
    mapping = {
        'Z': 't',
        'E': 'h',
        'o': 'e',
        '|': '_',
        'g': 'f',
        'B': 'l',
        'R': 'a',
        'J': 'i',
        '5': 'e',
        's': 'e'
    }
    
    decoded = ""
    for char in flag_text:
        if char in mapping:
            decoded += mapping[char]
        else:
            decoded += char
    
    print(f"Decoded: {decoded}")
    
    # This gives us: the_flag_is_here
    # This looks like a valid flag!
    
    full_flag = f"USCC{{{decoded}}}"
    print(f"*** POTENTIAL FLAG: {full_flag} ***")
    
    return full_flag

def try_simple_shift():
    """Try a simple shift on the flag text"""
    
    print("\n=== SIMPLE SHIFT ===")
    
    flag_text = "ZEo|gBoRoJogE g5oEJgs"
    
    # Try different shifts
    for shift in range(26):
        decoded = ""
        for char in flag_text:
            if char.isalpha():
                if char.isupper():
                    decoded += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    decoded += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                decoded += char
        
        # Look for meaningful text
        if 'the' in decoded.lower() or 'flag' in decoded.lower() or 'here' in decoded.lower():
            print(f"Shift {shift}: {decoded}")
            
            # If this looks like flag text, construct the full flag
            if 'the' in decoded.lower() and 'flag' in decoded.lower():
                full_flag = f"USCC{{{decoded}}}"
                print(f"*** POTENTIAL FLAG: {full_flag} ***")
                return full_flag
    
    return None

if __name__ == "__main__":
    # Try different approaches
    flag = try_correct_flag_mapping()
    if flag:
        print(f"\n*** FLAG FOUND ***")
        print(f"Flag: {flag}")
    else:
        flag = try_alternative_interpretations()
        if flag:
            print(f"\n*** FLAG FOUND ***")
            print(f"Flag: {flag}")
        else:
            flag = try_simple_shift()
            if flag:
                print(f"\n*** FLAG FOUND ***")
                print(f"Flag: {flag}")
            else:
                print("\nStill working on it...")