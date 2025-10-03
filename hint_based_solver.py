#!/usr/bin/env python3
"""
Try keys based on the hint message
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

def is_likely_english(text):
    """Check if text looks like English"""
    text = text.upper()
    common_words = ["THE", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL", "CAN", "HER", "WAS", "ONE", "OUR", "HAD", "BY", "UP", "DO", "NO", "IF", "MY", "HE", "AS", "TO", "GO", "WE", "AM", "IS", "OR", "BE", "IT", "IN", "AT", "ON", "SO", "US", "AN", "OF", "FLAG", "USCC", "CONGRATULATIONS", "WELL", "DONE", "GOOD", "JOB", "FOUND", "SOLVED", "CORRECT", "SECRET", "CIPHER", "DECODE", "HIDDEN", "MYSTERY"]
    
    words = text.split()
    if len(words) < 3:
        return False
    
    # Check if at least 30% of words are common English words
    common_count = sum(1 for word in words[:20] if word in common_words)  # Check first 20 words
    return common_count >= len(words[:20]) * 0.3

def main():
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    # Keys based on the hint
    hint_keys = [
        # Direct from hint
        "JUSTBECAUSEYOUKNOWMYNAMENOESNTMEANYOUKNOWMYSECRETS",
        "JUSTBECAUSE", "YOUKNOW", "MYNAME", "DOESNTMEAN", "MYSECRETS",
        "KNOW", "NAME", "SECRETS", "MEAN", "JUST", "BECAUSE",
        
        # Common names that might be referenced
        "ALICE", "BOB", "CHARLIE", "DAVID", "EVE", "FRANK", "GRACE", "HENRY",
        "JOHN", "JANE", "SMITH", "JONES", "BROWN", "WILSON", "TAYLOR", "DAVIS",
        
        # Cipher-related names
        "VIGENERE", "CAESAR", "PLAYFAIR", "ENIGMA", "TURING", "SHANNON",
        
        # Try the word "SECRET" and variations
        "SECRET", "SECRETS", "SECRETKEY", "TOPSECRET", "CLASSIFIED",
        
        # Try combinations
        "NAMEKEY", "SECRETNAME", "KNOWSECRET", "MYNAMESECRET"
    ]
    
    print("Trying hint-based keys:")
    print("=" * 60)
    
    for key in hint_keys:
        decrypted = vigenere_decrypt(ciphertext, key)
        
        print(f"Key '{key}' (len {len(key)}):")
        print(f"  {decrypted[:120]}...")
        
        if is_likely_english(decrypted):
            print(f"  *** LOOKS LIKE ENGLISH! ***")
            print(f"  Full text: {decrypted}")
            print()
            return decrypted
        
        # Also check for specific patterns that might indicate success
        if "USCC{" in decrypted or "FLAG{" in decrypted or "CONGRATULATIONS" in decrypted.upper():
            print(f"  *** FOUND FLAG PATTERN! ***")
            print(f"  Full text: {decrypted}")
            print()
            return decrypted
        
        print()
    
    print("No clear English text found with hint-based keys.")
    return None

if __name__ == "__main__":
    result = main()
    if result:
        print(f"\nFINAL RESULT: {result}")