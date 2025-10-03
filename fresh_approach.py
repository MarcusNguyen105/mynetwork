#!/usr/bin/env python3

def fresh_approach():
    """Take a completely fresh approach to the cipher"""
    
    # Let me look at the original message again
    header = "5JT DE SJ2 1209 = 111 = GZV DBR ="
    ciphertext_raw = """XLWHF DJKUC ZONWZ UFDGB SIILK
GSOBR NPPMF BWFTU CHPCO UUBMB
NUUMW HMPJG JGJPM AXKPY FENEP
LKHGM LUPUJ WWCZO YATTS CBSKI
QFKSG ADRPZ J"""
    
    ciphertext = ''.join(ciphertext_raw.split())
    
    print("Fresh approach to the cipher...")
    print(f"Header: {header}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Length: {len(ciphertext)}")
    
    # Maybe I need to look at this differently
    # What if the "=" signs are important?
    # What if I need to process the message in sections?
    
    # Let me try splitting by the groups in the original format
    groups = ['XLWHF', 'DJKUC', 'ZONWZ', 'UFDGB', 'SIILK',
              'GSOBR', 'NPPMF', 'BWFTU', 'CHPCO', 'UUBMB',
              'NUUMW', 'HMPJG', 'JGJPM', 'AXKPY', 'FENEP',
              'LKHGM', 'LUPUJ', 'WWCZO', 'YATTS', 'CBSKI',
              'QFKSG', 'ADRPZ', 'J']
    
    print(f"\nMessage in original groups:")
    for i, group in enumerate(groups):
        print(f"  {i+1:2d}: {group}")
    
    # Maybe each group needs different processing?
    # Or maybe I need to read them in a different order?
    
    # Try reading every nth group
    print(f"\nTrying different group reading patterns...")
    
    for n in range(2, 6):
        pattern_text = ""
        for start in range(n):
            for i in range(start, len(groups), n):
                pattern_text += groups[i]
        print(f"Pattern {n}: {pattern_text[:50]}...")
        
        # Try simple Caesar on this pattern
        for shift in range(26):
            result = ""
            for char in pattern_text:
                if char.isalpha():
                    shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                    result += shifted
            
            if 'USCC' in result:
                print(f"  *** USCC found with pattern {n}, shift {shift}! ***")
                print(f"  Result: {result}")
                if '{' in result and '}' in result:
                    start_pos = result.find('USCC')
                    end_pos = result.find('}', start_pos) + 1
                    flag = result[start_pos:end_pos]
                    print(f"  *** FLAG: {flag} ***")
                    return flag
    
    # Maybe the key is in the structure itself
    # What if "111" means to use position 1,1,1 but in a different cipher?
    
    # Try Book cipher approach - use positions from header
    print(f"\nTrying book cipher approach...")
    
    # 1209 could be positions: 1,2,0,9 or 12,09
    positions = [1, 2, 0, 9]  # Convert to 0-based: 0,1,-1,8
    
    book_result = ""
    for pos in positions:
        if 0 <= pos < len(ciphertext):
            book_result += ciphertext[pos]
    
    print(f"Book cipher (1,2,0,9): {book_result}")
    
    # Try with 12, 09
    positions = [12, 9]  # Convert to 0-based: 11, 8
    book_result = ""
    for pos in positions:
        if 0 <= pos < len(ciphertext):
            book_result += ciphertext[pos]
    
    print(f"Book cipher (12,09): {book_result}")
    
    # What if I need to use the Enigma procedure but with a twist?
    # Maybe the date is actually different
    
    # Try interpreting 1209 as September 12th (European date format)
    print(f"\nTrying September 12th interpretation...")
    
    # That would be day 12 in the codebook
    # But maybe I need to use a different procedure
    
    # What if the message is actually multiple layers?
    # First decrypt with one method, then another?
    
    print(f"\nTrying layered decryption...")
    
    # First layer: Simple Caesar
    for shift1 in range(1, 26):
        layer1 = ""
        for char in ciphertext:
            if char.isalpha():
                shifted = chr((ord(char) - ord('A') + shift1) % 26 + ord('A'))
                layer1 += shifted
        
        # Second layer: Vigenère with keys from header
        for key in ['GZV', 'DBR', 'SJ2']:
            layer2 = vigenere_decrypt(layer1, key)
            
            if 'USCC' in layer2:
                print(f"*** USCC found with Caesar {shift1} + Vigenère '{key}'! ***")
                print(f"Result: {layer2}")
                if '{' in layer2 and '}' in layer2:
                    start_pos = layer2.find('USCC')
                    end_pos = layer2.find('}', start_pos) + 1
                    flag = layer2[start_pos:end_pos]
                    print(f"*** FLAG: {flag} ***")
                    return flag
    
    # Maybe it's a Beaufort cipher?
    print(f"\nTrying Beaufort cipher...")
    
    for key in ['GZV', 'DBR', 'SJ2', 'GZVDBR']:
        beaufort_result = beaufort_decrypt(ciphertext, key)
        print(f"Beaufort with '{key}': {beaufort_result[:50]}...")
        
        if 'USCC' in beaufort_result:
            print(f"*** USCC found with Beaufort '{key}'! ***")
            print(f"Result: {beaufort_result}")
            if '{' in beaufort_result and '}' in beaufort_result:
                start_pos = beaufort_result.find('USCC')
                end_pos = beaufort_result.find('}', start_pos) + 1
                flag = beaufort_result[start_pos:end_pos]
                print(f"*** FLAG: {flag} ***")
                return flag
    
    return None

def vigenere_decrypt(ciphertext, key):
    """Decrypt using Vigenère cipher"""
    if not key:
        return ciphertext
        
    result = ""
    key_upper = key.upper()
    key_len = len(key_upper)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = key_upper[i % key_len]
            shift = ord(key_char) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result += decrypted_char
        else:
            result += char
    
    return result

def beaufort_decrypt(ciphertext, key):
    """Decrypt using Beaufort cipher"""
    if not key:
        return ciphertext
        
    result = ""
    key_upper = key.upper()
    key_len = len(key_upper)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = key_upper[i % key_len]
            # Beaufort: plaintext = key - ciphertext (mod 26)
            decrypted_char = chr((ord(key_char) - ord(char)) % 26 + ord('A'))
            result += decrypted_char
        else:
            result += char
    
    return result

if __name__ == "__main__":
    flag = fresh_approach()
    if flag:
        print(f"\n{'='*60}")
        print(f"CORRECT FLAG: {flag}")
    else:
        print("\nStill searching for the correct approach...")