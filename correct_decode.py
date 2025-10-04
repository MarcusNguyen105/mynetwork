#!/usr/bin/env python3

def test_the_hypothesis():
    """Test if 'ioE' could be 'The' with some transformation"""
    
    print("=== Testing 'ioE' = 'The' ===")
    
    # Maybe it's not ROT13 but a different shift
    # Let's see what shift would make 'ioE' become 'The'
    
    cipher_word = "ioE"
    target_word = "The"
    
    print(f"Cipher: {cipher_word}")
    print(f"Target: {target_word}")
    
    # Check each character
    for i in range(len(cipher_word)):
        cipher_char = cipher_word[i]
        target_char = target_word[i]
        
        # Calculate the shift needed
        if cipher_char.isalpha() and target_char.isalpha():
            # Convert to same case for calculation
            c_upper = cipher_char.upper()
            t_upper = target_char.upper()
            
            shift = (ord(t_upper) - ord(c_upper)) % 26
            print(f"  {cipher_char} -> {target_char}: shift = {shift}")
    
    # The shifts are: i->T (11), o->h (25), E->e (0)
    # This is not consistent, so it's not a simple Caesar cipher
    
    # But wait - what if it's case-sensitive in a different way?
    # Let me try a different approach
    
    print("\nTrying different case handling...")
    
    # What if lowercase letters shift differently than uppercase?
    # Or what if we need to consider the ASCII values differently?
    
    # Let me try: what if 'i' maps to 'T', 'o' maps to 'h', 'E' maps to 'e'?
    # This could be a substitution cipher
    
    substitution_map = {'i': 'T', 'o': 'h', 'E': 'e'}
    
    # Test this on "ioE j8|="
    test_text = "ioE j8|="
    result = ""
    
    for char in test_text:
        if char in substitution_map:
            result += substitution_map[char]
        else:
            result += char
    
    print(f"With substitution map {substitution_map}: '{test_text}' -> '{result}'")
    
    # That gives "The j8|=" - close but not quite "The flag"
    
    return substitution_map

def try_keyboard_shift():
    """Maybe it's a keyboard shift cipher"""
    
    print("\n=== Keyboard Shift Test ===")
    
    # QWERTY keyboard layout
    qwerty_rows = [
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"
    ]
    
    # Maybe each letter is shifted by one position on the keyboard?
    # This is less likely but worth checking
    
    pass

def examine_rot13_result_more():
    """Look more carefully at the ROT13 result"""
    
    print("\n=== Examining ROT13 Result ===")
    
    # The ROT13 result was: "ioE j8|= (} <D;;)t5OEE% :%:_ MRb|tObEbWbtR t5bRWtf*"
    # Let's focus on this and see if we can make sense of it
    
    rot13_flag_line = "ioE^j8|=^(}^<D;;)t5OEE% :%:_ MRb|tObEbWbtR t5bRWtf*"
    
    print(f"ROT13 flag line: {rot13_flag_line}")
    
    # Split by ^
    parts = rot13_flag_line.split('^')
    print(f"Parts: {parts}")
    
    # We have: ["ioE", "j8|=", "(}", "<D;;)t5OEE% :%:_ MRb|tObEbWbtR t5bRWtf*"]
    
    # What if "ioE" and "j8|=" need a different transformation?
    # And what if the flag part uses the substitution we found earlier?
    
    # From earlier: < = U, Q = S, ; = C, ) = {, * = }
    # But after ROT13, Q becomes D
    # So maybe: < = U, D = S, ; = C, ) = {, * = }
    
    flag_part = "<D;;)t5OEE% :%:_ MRb|tObEbWbtR t5bRWtf*"
    
    substitution = {'<': 'U', 'D': 'S', ';': 'C', ')': '{', '*': '}'}
    
    result = ""
    for char in flag_part:
        if char in substitution:
            result += substitution[char]
        else:
            result += char
    
    print(f"After substitution: {result}")
    
    # That gives: "USCC{t5OEE% :%:_ MRb|tObEbWbtR t5bRWtf}"
    # This is what we had before!
    
    # But maybe we need to clean it up differently
    # Let's remove the special characters and see what we get
    
    import re
    flag_content = "t5OEE% :%:_ MRb|tObEbWbtR t5bRWtf"
    clean_content = re.sub(r'[^a-zA-Z0-9]', '', flag_content)
    
    print(f"Clean flag content: {clean_content}")
    print(f"Potential flag: USCC{{{clean_content}}}")
    
    return f"USCC{{{clean_content}}}"

def try_different_substitution():
    """Try a different substitution approach"""
    
    import re
    
    print("\n=== Different Substitution Approach ===")
    
    # What if the message uses ROT13, but the flag uses a different cipher?
    # Let's go back to the original flag part and try different approaches
    
    original_flag = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    
    # What if it's not < = U, but something else?
    # Let's try all possible mappings for the first 4 characters
    
    # We want <Q;; to become USCC
    # So: < = U, Q = S, first ; = C, second ; = C
    
    # But what if ) is not { but part of the flag content?
    # Let's try: <Q;;) = USCC{ where ) = {
    
    # Actually, let me try a completely different approach
    # What if the numbers and special characters are important?
    
    # Looking at: g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs
    # What if the numbers indicate something?
    
    # 5 appears twice: g5BRR and g5oEJgs
    # Maybe 5 is a separator or indicator?
    
    parts_by_5 = original_flag.split('5')
    print(f"Split by '5': {parts_by_5}")
    
    # That gives: ['<Q;;)g', 'BRR% :%:_ ZEo|gBoRoJogE g', 'oEJgs*']
    
    # What if we only decode the alphabetic parts?
    alpha_only = re.sub(r'[^a-zA-Z]', '', original_flag)
    print(f"Alpha only: {alpha_only}")
    
    # Try ROT13 on just the letters
    rot13_alpha = ""
    for char in alpha_only:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rot13_alpha += chr((ord(char) - base + 13) % 26 + base)
    
    print(f"ROT13 of alpha only: {rot13_alpha}")
    
    # Now apply our substitution to the beginning
    if rot13_alpha.startswith('DQ'):
        # D = S (from Q+13), Q = D (from D+13)... wait, that's not right
        pass
    
    # Let me recalculate what <Q;; becomes with ROT13
    test_chars = "<Q;;"
    rot13_test = ""
    for char in test_chars:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rot13_test += chr((ord(char) - base + 13) % 26 + base)
        else:
            rot13_test += char
    
    print(f"<Q;; with ROT13: {rot13_test}")
    
    # < is not alphabetic, so it stays <
    # Q becomes D
    # ; is not alphabetic, so it stays ;
    # So <Q;; becomes <D;;
    
    # If we want USCC, then < = U, D = S, ; = C, ; = C
    
    return None

if __name__ == "__main__":
    substitution_map = test_the_hypothesis()
    
    flag_candidate = examine_rot13_result_more()
    print(f"\nFlag candidate from ROT13 approach: {flag_candidate}")
    
    try_different_substitution()
    
    # Let me try one more approach - what if it's simpler than I think?
    print("\n=== Simple Approach ===")
    
    # What if I just need to:
    # 1. Apply ROT13 to get the readable text
    # 2. Apply the substitution < = U, D = S, ; = C, ) = {, * = } to the flag part
    # 3. Clean up the result
    
    # From the ROT13 result: <D;;)t5OEE% :%:_ MRb|tObEbWbtR t5bRWtf*
    
    rot13_flag_part = "<D;;)t5OEE% :%:_ MRb|tObEbWbtR t5bRWtf*"
    
    # Apply substitution
    substitution = {'<': 'U', 'D': 'S', ';': 'C', ')': '{', '*': '}'}
    
    substituted = ""
    for char in rot13_flag_part:
        if char in substitution:
            substituted += substitution[char]
        else:
            substituted += char
    
    print(f"Substituted: {substituted}")
    
    # Extract content between { and }
    if '{' in substituted and '}' in substituted:
        start = substituted.find('{')
        end = substituted.find('}')
        content = substituted[start+1:end]
        
        print(f"Flag content: {content}")
        
        # Maybe the special characters and numbers are part of the flag?
        print(f"Final flag attempt: USCC{{{content}}}")
        
        # Or maybe we need to clean it differently
        # Keep only alphanumeric
        import re
        clean = re.sub(r'[^a-zA-Z0-9]', '', content)
        print(f"Clean version: USCC{{{clean}}}")
        
        # Or maybe keep some structure
        semi_clean = re.sub(r'[%:\s]', '', content)
        print(f"Semi-clean version: USCC{{{semi_clean}}}")