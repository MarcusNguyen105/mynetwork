#!/usr/bin/env python3
"""
Try variations of FLAG-based keys
"""

def vigenere_decrypt(ciphertext, key):
    """Decrypt Vigenère cipher"""
    result = ""
    key = key.upper()
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            result += decrypted_char
            key_index += 1
        else:
            result += char
    return result

def main():
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    # Try various FLAG-related keys
    flag_keys = [
        "FLAG", "FLAGS", "FLAGG", "FLAGA", "FLAGB", "FLAGC", "FLAGD", "FLAGE", "FLAGF",
        "FLAGFL", "FLAGFLA", "FLAGFLAG",
        "USCC", "USCCF", "USCCFL", "USCCFLA", "USCCFLAG",
        "CTFFLAG", "CTFFLAGS",
        "SECRETFLAG", "HIDDENFLAG", "MYSTERFLAG",
        "CIPHER", "CIPHERFLAG", "DECODE", "DECODEFLAG"
    ]
    
    print("Trying FLAG-related keys:")
    print("=" * 50)
    
    for key in flag_keys:
        decrypted = vigenere_decrypt(ciphertext, key)
        print(f"Key '{key}' (len {len(key)}): {decrypted[:100]}...")
        
        # Check if this looks like readable English
        words = decrypted.upper().split()
        english_words = ["THE", "AND", "FLAG", "USCC", "SECRET", "YOU", "ARE", "THIS", "THAT", "WITH", "HAVE", "WILL", "FROM", "THEY", "BEEN", "SAID", "EACH", "WHICH", "THEIR", "CONGRATULATIONS", "WELL", "DONE", "GOOD", "JOB", "FOUND", "SOLVED", "CORRECT"]
        
        if any(word in english_words for word in words[:10]):  # Check first 10 words
            print(f"  *** LOOKS LIKE ENGLISH: {decrypted}")
            print()
        
        # Also check for common letter patterns
        if "TH" in decrypted.upper() or "ER" in decrypted.upper() or "ING" in decrypted.upper():
            print(f"  *** HAS COMMON PATTERNS: {decrypted}")
            print()
        
        print()

if __name__ == "__main__":
    main()