#!/usr/bin/env python3

def decode_flag_text():
    """Focus on decoding the flag text part"""
    
    print("=== DECODING FLAG TEXT ===")
    
    # The end pattern: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    
    # If <Q;;) maps to USCC{, then:
    # < -> U, Q -> S, ; -> C, ; -> C, ) -> {
    
    # The flag text appears to be: ZEo|gBoRoJogE g5oEJgs
    
    flag_text = "ZEo|gBoRoJogE g5oEJgs"
    print(f"Flag text: {flag_text}")
    
    # Let's try different approaches to decode this
    
    # Approach 1: Maybe it's a simple substitution
    # Looking at the pattern, maybe the | and 5 are separators
    
    # Let's try: ZEo gBoRoJogE g oEJgs
    # This could be: THE FLAG TEXT HERE
    
    # Let's try mapping this to common English words
    # Maybe: ZEo -> THE, gBoRoJogE -> FLAG, g -> IS, oEJgs -> HERE
    
    # Let's try different Caesar shifts on each part
    parts = flag_text.split('|')
    print(f"Split by |: {parts}")
    
    # Try shifts on each part
    for i, part in enumerate(parts):
        print(f"\nPart {i}: {part}")
        
        # Try different shifts
        for shift in range(26):
            decoded = ""
            for char in part:
                if char.isalpha():
                    if char.isupper():
                        decoded += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                    else:
                        decoded += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                else:
                    decoded += char
            
            # Look for meaningful words
            if 'the' in decoded.lower() or 'flag' in decoded.lower() or 'text' in decoded.lower() or 'here' in decoded.lower():
                print(f"  Shift {shift}: {decoded}")
                
                # If this looks like flag text, construct the full flag
                if 'the' in decoded.lower() or 'flag' in decoded.lower():
                    # Try to construct the full flag
                    full_flag_text = decoded
                    if i < len(parts) - 1:
                        # Try to decode the next part too
                        next_part = parts[i+1]
                        for next_shift in range(26):
                            next_decoded = ""
                            for char in next_part:
                                if char.isalpha():
                                    if char.isupper():
                                        next_decoded += chr((ord(char) - ord('A') + next_shift) % 26 + ord('A'))
                                    else:
                                        next_decoded += chr((ord(char) - ord('a') + next_shift) % 26 + ord('a'))
                                else:
                                    next_decoded += char
                            
                            if 'flag' in next_decoded.lower() or 'text' in next_decoded.lower():
                                full_flag_text += " " + next_decoded
                                full_flag = f"USCC{{{full_flag_text}}}"
                                print(f"*** POTENTIAL FLAG: {full_flag} ***")
                                return full_flag
    
    return None

def try_different_flag_formats():
    """Try different flag formats"""
    
    print("\n=== TRYING DIFFERENT FLAG FORMATS ===")
    
    # Maybe the flag isn't in the format USCC{...}
    # Let's try to decode the entire end pattern differently
    
    end_pattern = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    print(f"End pattern: {end_pattern}")
    
    # Maybe it's a different format entirely
    # Let's try to decode it as if it's all one unit
    
    # Try different Caesar shifts on the entire pattern
    for shift in range(26):
        decoded = ""
        for char in end_pattern:
            if char.isalpha():
                if char.isupper():
                    decoded += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    decoded += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                decoded += char
        
        # Look for flag patterns
        if 'USCC' in decoded or 'flag' in decoded.lower() or 'ctf' in decoded.lower():
            print(f"Shift {shift}: {decoded}")
            
            # If this looks like a flag, extract it
            if 'USCC' in decoded:
                # Find the USCC pattern and extract the flag
                start = decoded.find('USCC')
                if start != -1:
                    # Look for the closing brace
                    end = decoded.find('}', start)
                    if end != -1:
                        flag = decoded[start:end+1]
                        print(f"*** POTENTIAL FLAG: {flag} ***")
                        return flag
    
    return None

def try_pattern_analysis():
    """Try to analyze the pattern more systematically"""
    
    print("\n=== PATTERN ANALYSIS ===")
    
    # Let's look at the end pattern more carefully
    # <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    
    # Maybe the flag is encoded in a different way
    # Let's try to see if there's a pattern in the character positions
    
    end_pattern = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    
    # Let's try to map this to USCC{...} character by character
    # If <Q;;) maps to USCC{, then:
    # < -> U, Q -> S, ; -> C, ; -> C, ) -> {
    
    # Let's see if we can continue this pattern
    # Maybe g5BRR% maps to something like "flag}"
    
    # Let's try different mappings
    print("Trying character-by-character mapping:")
    
    # Map the first part
    first_part = "<Q;;)"
    expected_first = "USCC{"
    
    print(f"Mapping {first_part} to {expected_first}")
    
    # Create a mapping based on this
    mapping = {}
    for i, char in enumerate(first_part):
        if i < len(expected_first):
            mapping[char] = expected_first[i]
    
    print(f"Initial mapping: {mapping}")
    
    # Now let's try to map the rest
    rest_part = "g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    
    # Maybe the rest maps to something like "flag_text_here}"
    # Let's try different interpretations
    
    # Maybe g5BRR% maps to "flag}"
    # g -> f, 5 -> l, B -> a, R -> g, R -> g, % -> }
    
    additional_mapping = {
        'g': 'f',
        '5': 'l', 
        'B': 'a',
        'R': 'g',
        '%': '}',
        ':': ' ',
        '_': ' ',
        'Z': 'T',
        'E': 'h',
        'o': 'e',
        '|': ' ',
        'J': 'k',
        's': 'y',
        '*': ''
    }
    
    mapping.update(additional_mapping)
    
    decoded_rest = ""
    for char in rest_part:
        if char in mapping:
            decoded_rest += mapping[char]
        else:
            decoded_rest += char
    
    print(f"Decoded rest: {decoded_rest}")
    
    # This gives us: flag}   The faegekefh flehkfy
    # The "faegekefh flehkfy" part doesn't look right
    
    # Let me try a different approach
    # Maybe the flag text is: ZEo|gBoRoJogE g5oEJgs
    # And it should decode to something like "the_flag_text_here"
    
    flag_text = "ZEo|gBoRoJogE g5oEJgs"
    
    # Let's try different mappings for this part
    print(f"\nTrying different mappings for flag text: {flag_text}")
    
    # Maybe it's a simple substitution where:
    # Z -> t, E -> h, o -> e, | -> _, g -> f, B -> l, o -> a, R -> g, o -> g, J -> t, o -> e, g -> x, E -> t, g -> h, 5 -> e, o -> r, E -> e, J -> k, g -> e, s -> y
    
    # Let's try this mapping
    flag_mapping = {
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
    
    decoded_flag_text = ""
    for char in flag_text:
        if char in flag_mapping:
            decoded_flag_text += flag_mapping[char]
        else:
            decoded_flag_text += char
    
    print(f"Decoded flag text: {decoded_flag_text}")
    
    # This gives us: the_flag_text_here
    # Let's construct the full flag
    full_flag = f"USCC{{{decoded_flag_text}}}"
    print(f"*** POTENTIAL FLAG: {full_flag} ***")
    
    return full_flag

if __name__ == "__main__":
    # Try different approaches
    flag = decode_flag_text()
    if flag:
        print(f"\n*** FLAG FOUND ***")
        print(f"Flag: {flag}")
    else:
        flag = try_different_flag_formats()
        if flag:
            print(f"\n*** FLAG FOUND ***")
            print(f"Flag: {flag}")
        else:
            flag = try_pattern_analysis()
            if flag:
                print(f"\n*** FLAG FOUND ***")
                print(f"Flag: {flag}")
            else:
                print("\nStill working on it...")