#!/usr/bin/env python3

def reexamine_cipher():
    """Re-examine the cipher with fresh eyes"""
    
    ciphertext = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"
    
    print("Re-examining the cipher...")
    print(f"Ciphertext: {ciphertext}")
    print(f"Length: {len(ciphertext)}")
    
    # Let me try more Vigenère keys systematically
    keys_to_try = [
        # From the header
        '5JT', 'SJ2', '1209', '111', 'GZV', 'DBR',
        # Combinations
        '5JTSJ2', 'SJ21209', '1209111', '111GZV', 'GZVDBR',
        # Numbers as letters
        'EAJT', 'SJB', 'ABAI', 'AAA', 
        # Other possibilities
        'ENIGMA', 'BLETCHLEY', 'PARK', 'GEHEIM',
        # Single letters
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    
    print(f"\nTesting {len(keys_to_try)} different Vigenère keys...")
    
    for key in keys_to_try:
        result = vigenere_decrypt(ciphertext, key)
        
        # Check for flag patterns more thoroughly
        if 'USCC{' in result and '}' in result:
            print(f"*** COMPLETE FLAG FOUND with key '{key}'! ***")
            start = result.find('USCC{')
            end = result.find('}', start) + 1
            flag = result[start:end]
            print(f"Flag: {flag}")
            print(f"Full text: {result}")
            return flag
        elif 'USCC' in result:
            print(f"Key '{key}' contains USCC:")
            print(f"  {result}")
            uscc_pos = result.find('USCC')
            context = result[max(0, uscc_pos-10):uscc_pos+30]
            print(f"  Context: ...{context}...")
        elif any(word in result for word in ['FLAG', 'CIPHER', 'SECRET', 'BLETCHLEY', 'ENIGMA']):
            print(f"Key '{key}' contains promising words:")
            print(f"  {result[:60]}...")
    
    # Try Caesar cipher more systematically
    print(f"\n{'='*50}")
    print("Testing Caesar cipher systematically...")
    
    for shift in range(26):
        result = ""
        for char in ciphertext:
            if char.isalpha():
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result += shifted
        
        if 'USCC{' in result and '}' in result:
            print(f"*** COMPLETE FLAG FOUND with Caesar shift {shift}! ***")
            start = result.find('USCC{')
            end = result.find('}', start) + 1
            flag = result[start:end]
            print(f"Flag: {flag}")
            return flag
        elif 'USCC' in result:
            print(f"Caesar shift {shift} contains USCC:")
            print(f"  {result}")
    
    # Try Atbash cipher
    print(f"\n{'='*50}")
    print("Testing Atbash cipher...")
    
    atbash_result = ""
    for char in ciphertext:
        if char.isalpha():
            atbash_char = chr(ord('Z') - (ord(char) - ord('A')))
            atbash_result += atbash_char
    
    print(f"Atbash result: {atbash_result}")
    if 'USCC' in atbash_result:
        print("*** USCC found in Atbash! ***")
        return atbash_result
    
    # Try reverse + Caesar
    print(f"\n{'='*50}")
    print("Testing reverse + Caesar...")
    
    reversed_cipher = ciphertext[::-1]
    
    for shift in range(26):
        result = ""
        for char in reversed_cipher:
            if char.isalpha():
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result += shifted
        
        if 'USCC{' in result and '}' in result:
            print(f"*** COMPLETE FLAG FOUND with reverse + Caesar shift {shift}! ***")
            start = result.find('USCC{')
            end = result.find('}', start) + 1
            flag = result[start:end]
            print(f"Flag: {flag}")
            return flag
        elif 'USCC' in result:
            print(f"Reverse + Caesar shift {shift} contains USCC:")
            print(f"  {result[:60]}...")
    
    print("No clear flag found. Let me try some other approaches...")
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

if __name__ == "__main__":
    flag = reexamine_cipher()
    if flag:
        print(f"\n{'='*60}")
        print(f"FINAL FLAG: {flag}")
    else:
        print("\nNeed to try more approaches...")