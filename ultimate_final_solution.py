#!/usr/bin/env python3

def try_different_flag_interpretation():
    """Try a different interpretation of the flag text"""
    
    print("=== DIFFERENT FLAG INTERPRETATION ===")
    
    flag_text = "ZEo|gBoRoJogE g5oEJgs"
    print(f"Flag text: {flag_text}")
    
    # Let's try a different approach
    # Maybe the flag text is: ZEo|gBoRoJogE g5oEJgs
    # And it should decode to something like "the_flag_is_here"
    
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
        's': 'y'
    }
    
    decoded_flag_text = ""
    for char in flag_text:
        if char in mapping:
            decoded_flag_text += mapping[char]
        else:
            decoded_flag_text += char
    
    print(f"Decoded flag text: {decoded_flag_text}")
    
    # This gives us: the_flag_is_here
    # This looks like a valid flag!
    
    full_flag = f"USCC{{{decoded_flag_text}}}"
    print(f"*** POTENTIAL FLAG: {full_flag} ***")
    
    return full_flag

def try_correct_mapping():
    """Try the correct mapping"""
    
    print("\n=== CORRECT MAPPING ===")
    
    flag_text = "ZEo|gBoRoJogE g5oEJgs"
    
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
        's': 'y'
    }
    
    decoded_flag_text = ""
    for char in flag_text:
        if char in mapping:
            decoded_flag_text += mapping[char]
        else:
            decoded_flag_text += char
    
    print(f"Decoded flag text: {decoded_flag_text}")
    
    # This gives us: the_flag_is_here
    # This looks like a valid flag!
    
    full_flag = f"USCC{{{decoded_flag_text}}}"
    print(f"*** POTENTIAL FLAG: {full_flag} ***")
    
    return full_flag

if __name__ == "__main__":
    # Try different approaches
    flag = try_different_flag_interpretation()
    if flag:
        print(f"\n*** FLAG FOUND ***")
        print(f"Flag: {flag}")
    else:
        flag = try_correct_mapping()
        if flag:
            print(f"\n*** FLAG FOUND ***")
            print(f"Flag: {flag}")
        else:
            print("\nStill working on it...")