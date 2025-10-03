#!/usr/bin/env python3
"""
Cipher solver for the given secret text
"""

def vigenere_decrypt(ciphertext, key):
    """Decrypt Vigenère cipher"""
    result = ""
    key = key.upper()
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Get the shift amount from the key
            shift = ord(key[key_index % len(key)]) - ord('A')
            
            # Decrypt the character
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            result += decrypted_char
            key_index += 1
        else:
            result += char
    
    return result

def caesar_decrypt(ciphertext, shift):
    """Decrypt Caesar cipher"""
    result = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char
    return result

def analyze_frequency(text):
    """Analyze character frequency"""
    freq = {}
    for char in text:
        if char.isalpha():
            char = char.upper()
            freq[char] = freq.get(char, 0) + 1
    
    # Sort by frequency
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq

def try_common_keys(ciphertext):
    """Try common keys for Vigenère cipher"""
    common_keys = [
        "CIPHER", "SECRET", "KEY", "PASSWORD", "CRYPTO", "CODE", 
        "MYSTERY", "PUZZLE", "HIDDEN", "FLAG", "USCC", "NAME",
        "VIGENERE", "ENCRYPT", "DECODE", "SOLVE"
    ]
    
    results = []
    for key in common_keys:
        decrypted = vigenere_decrypt(ciphertext, key)
        results.append((key, decrypted))
    
    return results

def atbash_decrypt(ciphertext):
    """Decrypt Atbash cipher (A=Z, B=Y, etc.)"""
    result = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                result += chr(ord('z') - (ord(char) - ord('a')))
        else:
            result += char
    return result

def rot13_decrypt(ciphertext):
    """Decrypt ROT13"""
    return caesar_decrypt(ciphertext, 13)

def main():
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    print("Cipher Analysis")
    print("=" * 50)
    print(f"Ciphertext: {ciphertext}")
    print(f"Length: {len(ciphertext)}")
    print()
    
    # Try Atbash
    print("Atbash Cipher:")
    atbash_result = atbash_decrypt(ciphertext)
    print(f"Atbash: {atbash_result}")
    print()
    
    # Try ROT13
    print("ROT13 Cipher:")
    rot13_result = rot13_decrypt(ciphertext)
    print(f"ROT13: {rot13_result}")
    print()
    
    # Try all Caesar shifts and look for readable text
    print("Caesar Cipher - All Shifts:")
    for shift in range(1, 26):
        decrypted = caesar_decrypt(ciphertext, shift)
        # Look for common English patterns
        if any(pattern in decrypted.upper() for pattern in ["THE", "AND", "FLAG", "USCC", "SECRET", "CIPHER"]):
            print(f"Shift {shift}: {decrypted}")
    print()
    
    # Extended key attempts
    extended_keys = [
        "NAME", "MYNAME", "SECRETS", "KNOWMYNAME", "JUSTTBECAUSE", 
        "VIGENERE", "CIPHER", "CRYPTO", "DECODE", "MYSTERY",
        "ALICE", "BOB", "CHARLIE", "DAVID", "EVE", "FRANK",
        "JOHN", "JANE", "SMITH", "JONES", "BROWN", "WILSON"
    ]
    
    print("Extended Vigenère Key Attempts:")
    for key in extended_keys:
        decrypted = vigenere_decrypt(ciphertext, key)
        # Check for readable patterns
        if any(pattern in decrypted.upper() for pattern in ["THE", "AND", "FLAG", "USCC", "SECRET", "CIPHER", "YOU", "ARE"]):
            print(f"Key '{key}': {decrypted}")
    
    # Try reverse of the ciphertext
    print("\nReverse cipher:")
    reversed_cipher = ciphertext[::-1]
    print(f"Reversed: {reversed_cipher}")
    
    # Try simple substitution - maybe it's a monoalphabetic cipher
    print("\nLooking for patterns in the original text...")
    # Look for repeated sequences
    for length in [2, 3, 4]:
        sequences = {}
        for i in range(len(ciphertext) - length + 1):
            seq = ciphertext[i:i+length]
            if seq in sequences:
                sequences[seq] += 1
            else:
                sequences[seq] = 1
        
        repeated = {k: v for k, v in sequences.items() if v > 1}
        if repeated:
            print(f"Repeated {length}-grams: {repeated}")
    
    # Try the hint as a key
    hint_keys = ["JUSTBECAUSEYOUKNOWMYNAMENOESNTMEANYOUKNOWMYSECRETS", "JUSTBECAUSE", "YOUKNOWMYNAME", "MYSECRETS"]
    print("\nHint-based keys:")
    for key in hint_keys:
        decrypted = vigenere_decrypt(ciphertext, key)
        print(f"Key '{key}': {decrypted[:100]}...")  # Show first 100 chars

if __name__ == "__main__":
    main()