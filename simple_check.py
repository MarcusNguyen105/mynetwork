#!/usr/bin/env python3

def simple_check():
    """Try the simplest possible approaches first"""
    
    ciphertext = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"
    
    print("Trying the simplest approaches...")
    
    # Maybe it's just a simple Caesar cipher and I missed it
    print("Testing all Caesar shifts for complete flags:")
    
    for shift in range(26):
        result = ""
        for char in ciphertext:
            if char.isalpha():
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result += shifted
        
        # Look for complete flag format
        if 'USCC{' in result and '}' in result:
            start = result.find('USCC{')
            end = result.find('}', start) + 1
            flag = result[start:end]
            print(f"*** COMPLETE FLAG found with Caesar shift {shift}! ***")
            print(f"FLAG: {flag}")
            return flag
        
        # Also check for USCC followed by reasonable content
        if 'USCC' in result:
            uscc_pos = result.find('USCC')
            after_uscc = result[uscc_pos+4:uscc_pos+30]
            
            # Check if the content after USCC looks like it could be a flag
            # Look for patterns like all caps, reasonable length, etc.
            if len(after_uscc) >= 10:
                # Try to find a natural break point
                for i in range(10, min(30, len(after_uscc))):
                    potential_content = after_uscc[:i]
                    
                    # Check if this looks like a reasonable flag
                    if potential_content.isalnum():
                        potential_flag = f"USCC{{{potential_content}}}"
                        print(f"Shift {shift:2d}: Potential flag - {potential_flag}")
    
    # Try Atbash cipher
    print(f"\nTrying Atbash cipher:")
    atbash_result = ""
    for char in ciphertext:
        if char.isalpha():
            atbash_char = chr(ord('Z') - (ord(char) - ord('A')))
            atbash_result += atbash_char
    
    print(f"Atbash: {atbash_result[:50]}...")
    if 'USCC{' in atbash_result and '}' in atbash_result:
        start = atbash_result.find('USCC{')
        end = atbash_result.find('}', start) + 1
        flag = atbash_result[start:end]
        print(f"*** FLAG found with Atbash: {flag} ***")
        return flag
    elif 'USCC' in atbash_result:
        uscc_pos = atbash_result.find('USCC')
        context = atbash_result[uscc_pos:uscc_pos+30]
        print(f"Atbash contains USCC: {context}")
    
    # Try ROT13
    print(f"\nTrying ROT13:")
    rot13_result = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            rot13_result += shifted
    
    print(f"ROT13: {rot13_result[:50]}...")
    if 'USCC{' in rot13_result and '}' in rot13_result:
        start = rot13_result.find('USCC{')
        end = rot13_result.find('}', start) + 1
        flag = rot13_result[start:end]
        print(f"*** FLAG found with ROT13: {flag} ***")
        return flag
    elif 'USCC' in rot13_result:
        uscc_pos = rot13_result.find('USCC')
        context = rot13_result[uscc_pos:uscc_pos+30]
        print(f"ROT13 contains USCC: {context}")
    
    # Maybe the flag is hidden in the original text somehow
    print(f"\nChecking if flag is hidden in original text:")
    
    # Check every position for USCC
    for i in range(len(ciphertext) - 3):
        if ciphertext[i:i+4] == 'USCC':
            print(f"Found USCC at position {i} in original text!")
            context = ciphertext[i:i+30]
            print(f"Context: {context}")
    
    # Try reading backwards
    print(f"\nTrying backwards:")
    backwards = ciphertext[::-1]
    print(f"Backwards: {backwards[:50]}...")
    
    if 'USCC' in backwards:
        print("USCC found in backwards text!")
        uscc_pos = backwards.find('USCC')
        context = backwards[uscc_pos:uscc_pos+30]
        print(f"Context: {context}")
    
    # Try simple Vigenère with very short keys
    print(f"\nTrying simple Vigenère with short keys:")
    
    for key in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        result = vigenere_decrypt(ciphertext, key)
        
        if 'USCC{' in result and '}' in result:
            start = result.find('USCC{')
            end = result.find('}', start) + 1
            flag = result[start:end]
            print(f"*** FLAG found with Vigenère key '{key}': {flag} ***")
            return flag
        elif 'USCC' in result:
            uscc_pos = result.find('USCC')
            context = result[uscc_pos:uscc_pos+20]
            print(f"Key '{key}': USCC found - {context}")
    
    return None

def vigenere_decrypt(ciphertext, key):
    """Decrypt using Vigenère cipher"""
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

if __name__ == "__main__":
    flag = simple_check()
    if flag:
        print(f"\n{'='*60}")
        print(f"FINAL FLAG: {flag}")
    else:
        print("\nNo simple solution found. The cipher may be more complex.")