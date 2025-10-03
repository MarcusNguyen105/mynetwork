#!/usr/bin/env python3

def systematic_decrypt():
    """Try systematic decryption approaches"""
    
    ciphertext = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"
    
    print("Systematic decryption attempts...")
    print(f"Ciphertext length: {len(ciphertext)}")
    
    # Try all possible Caesar shifts
    print(f"\n{'='*50}")
    print("Testing all Caesar shifts:")
    
    for shift in range(26):
        result = ""
        for char in ciphertext:
            if char.isalpha():
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result += shifted
            else:
                result += char
        
        print(f"Shift {shift:2d}: {result[:30]}...")
        
        # Check for flag patterns
        if 'USCC' in result:
            print(f"*** USCC FOUND with shift {shift}! ***")
            print(f"Full result: {result}")
            
            # Look for complete flag
            if '{' in result and '}' in result:
                start = result.find('USCC')
                end = result.find('}', start) + 1
                flag = result[start:end]
                print(f"*** COMPLETE FLAG: {flag} ***")
                return flag
        
        # Check for other promising patterns
        if any(word in result for word in ['FLAG', 'CIPHER', 'SECRET', 'ENIGMA', 'BLETCHLEY']):
            print(f"  -> Contains promising word!")
    
    # Try Vigenère with more keys
    print(f"\n{'='*50}")
    print("Testing Vigenère with various keys:")
    
    keys_to_try = [
        'ENIGMA', 'BLETCHLEY', 'PARK', 'SECRET', 'CIPHER', 'FLAG',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ',
        'GZV', 'DBR', 'GZVDBR', 'SJT', 'SJ2', '1209', 'SEPTEMBER',
        'GEHEIM', 'WALZE', 'RING', 'STECKER'
    ]
    
    for key in keys_to_try:
        result = vigenere_decrypt(ciphertext, key)
        
        if 'USCC' in result:
            print(f"*** USCC FOUND with key '{key}'! ***")
            print(f"Full result: {result}")
            
            # Look for complete flag
            if '{' in result and '}' in result:
                start = result.find('USCC')
                end = result.find('}', start) + 1
                flag = result[start:end]
                print(f"*** COMPLETE FLAG: {flag} ***")
                return flag
        
        # Check for other promising patterns
        if any(word in result for word in ['FLAG', 'CIPHER', 'SECRET', 'ENIGMA', 'BLETCHLEY']):
            print(f"Key '{key}': Contains promising word - {result[:40]}...")
    
    # Try reverse cipher
    print(f"\n{'='*50}")
    print("Testing reverse cipher:")
    
    reversed_cipher = ciphertext[::-1]
    print(f"Reversed: {reversed_cipher[:50]}...")
    
    if 'USCC' in reversed_cipher:
        print(f"*** USCC FOUND in reversed text! ***")
        print(f"Full result: {reversed_cipher}")
    
    # Try Caesar on reversed text
    for shift in range(26):
        result = ""
        for char in reversed_cipher:
            if char.isalpha():
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result += shifted
            else:
                result += char
        
        if 'USCC' in result:
            print(f"*** USCC FOUND in reversed text with shift {shift}! ***")
            print(f"Full result: {result}")
            
            if '{' in result and '}' in result:
                start = result.find('USCC')
                end = result.find('}', start) + 1
                flag = result[start:end]
                print(f"*** COMPLETE FLAG: {flag} ***")
                return flag
    
    # Try Playfair cipher with various keys
    print(f"\n{'='*50}")
    print("Testing other approaches...")
    
    # Try interpreting numbers in header as shifts
    shifts_from_header = [5, 2, 12, 9, 1, 1, 1, 6, 25, 21, 3, 1, 17]  # From 5JT, SJ2, 1209, 111, GZV, DBR
    
    for i, shift in enumerate(shifts_from_header):
        result = ""
        for char in ciphertext:
            if char.isalpha():
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result += shifted
            else:
                result += char
        
        if 'USCC' in result:
            print(f"*** USCC FOUND with header-based shift {shift} (index {i})! ***")
            print(f"Full result: {result}")
            return result
    
    print("No clear flag found with systematic approaches.")
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
    result = systematic_decrypt()
    if result:
        print(f"\n{'='*60}")
        print("SUCCESS! Flag found:")
        print(result)