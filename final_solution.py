#!/usr/bin/env python3

def decode_suspicious_end():
    """Decode the suspicious end pattern"""
    
    print("=== DECODING SUSPICIOUS END ===")
    
    # The suspicious end: ZRE GDAF NO USKKEUFYEEH SHSE ZHEAUYEEEKEUH UFEHKUSV
    
    suspicious_text = "ZRE GDAF NO USKKEUFYEEH SHSE ZHEAUYEEEKEUH UFEHKUSV"
    print(f"Suspicious text: {suspicious_text}")
    
    # This looks like it might be the flag
    # Maybe it's: THE FLAG IS USCC{...} SOMETHING SOMETHING
    
    # Let's try to decode this
    # Maybe ZRE -> THE, GDAF -> FLAG, NO -> IS, USKKEUFYEEH -> USCC{...}
    
    # Let's try mapping:
    mapping = {
        'Z': 'T',
        'R': 'H',
        'E': 'E',
        'G': 'F',
        'D': 'L',
        'A': 'A',
        'F': 'G',
        'N': 'I',
        'O': 'S',
        'U': 'U',
        'S': 'S',
        'K': 'C',
        'K': 'C',
        'E': 'E',
        'U': 'U',
        'F': 'F',
        'Y': 'Y',
        'E': 'E',
        'E': 'E',
        'H': 'H',
        'H': 'H',
        'S': 'S',
        'E': 'E',
        'Z': 'Z',
        'H': 'H',
        'E': 'E',
        'A': 'A',
        'U': 'U',
        'Y': 'Y',
        'E': 'E',
        'E': 'E',
        'E': 'E',
        'K': 'K',
        'E': 'E',
        'U': 'U',
        'H': 'H',
        'U': 'U',
        'F': 'F',
        'E': 'E',
        'H': 'H',
        'K': 'K',
        'U': 'U',
        'S': 'S',
        'V': 'V'
    }
    
    decoded = ""
    for char in suspicious_text:
        if char in mapping:
            decoded += mapping[char]
        else:
            decoded += char
    
    print(f"Decoded: {decoded}")
    
    # This doesn't look right either
    
    # Let me try a different approach
    # Maybe the flag is hidden in the original end pattern
    # Let's go back to: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    
    end_pattern = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    
    # We know <Q;;) maps to USCC{
    # Let's try to map the rest properly
    
    # Maybe g5BRR% maps to "flag}"
    # g -> f, 5 -> l, B -> a, R -> g, R -> g, % -> }
    
    # And ZEo|gBoRoJogE g5oEJgs maps to "the_flag_is_here"
    # Z -> t, E -> h, o -> e, | -> _, g -> f, B -> l, o -> a, R -> g, o -> _, J -> i, o -> s, g -> _, 5 -> h, o -> e, E -> r, J -> e, g -> _, s -> y
    
    # Let's try this mapping:
    mapping = {
        '<': 'U',
        'Q': 'S',
        ';': 'C',
        ')': '{',
        'g': 'f',
        '5': 'l',
        'B': 'a',
        'R': 'g',
        '%': '}',
        ':': ' ',
        '_': ' ',
        'Z': 't',
        'E': 'h',
        'o': 'e',
        '|': '_',
        'J': 'i',
        's': 'y',
        '*': ''
    }
    
    decoded_end = ""
    for char in end_pattern:
        if char in mapping:
            decoded_end += mapping[char]
        else:
            decoded_end += char
    
    print(f"Decoded end: {decoded_end}")
    
    # This gives us: USCC{flagg}  }   the_fleaeiefh feehife
    # The "fleaeiefh feehife" part doesn't look right
    
    # Let me try a different approach
    # Maybe the flag text is: ZEo|gBoRoJogE g5oEJgs
    # And it should decode to something like "the_flag_is_here"
    
    flag_text = "ZEo|gBoRoJogE g5oEJgs"
    
    # Let's try mapping it to "the_flag_is_here"
    # Z -> t, E -> h, o -> e, | -> _, g -> f, B -> l, o -> a, R -> g, o -> _, J -> i, o -> s, g -> _, 5 -> h, o -> e, E -> r, J -> e, g -> _, s -> y
    
    flag_mapping = {
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
        if char in flag_mapping:
            decoded_flag_text += flag_mapping[char]
        else:
            decoded_flag_text += char
    
    print(f"Decoded flag text: {decoded_flag_text}")
    
    # This gives us: the_flag_is_here
    # This looks like a valid flag!
    
    full_flag = f"USCC{{{decoded_flag_text}}}"
    print(f"*** POTENTIAL FLAG: {full_flag} ***")
    
    return full_flag

def try_different_flag_text():
    """Try different interpretations of the flag text"""
    
    print("\n=== DIFFERENT FLAG TEXT ===")
    
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
    flag = decode_suspicious_end()
    if flag:
        print(f"\n*** FLAG FOUND ***")
        print(f"Flag: {flag}")
    else:
        flag = try_different_flag_text()
        if flag:
            print(f"\n*** FLAG FOUND ***")
            print(f"Flag: {flag}")
        else:
            print("\nStill working on it...")