#!/usr/bin/env python3
"""
Final comprehensive attempt at solving the cipher
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

def autokey_decrypt(ciphertext, key):
    """Decrypt autokey cipher"""
    result = ""
    key = key.upper()
    extended_key = key
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            if i < len(extended_key):
                shift = ord(extended_key[i]) - ord('A')
            else:
                # Use previous decrypted character as key
                shift = ord(result[i - len(key)].upper()) - ord('A')
            
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            result += decrypted_char
            if len(extended_key) <= i:
                extended_key += decrypted_char.upper()
        else:
            result += char
    
    return result

def beaufort_decrypt(ciphertext, key):
    """Decrypt Beaufort cipher"""
    result = ""
    key = key.upper()
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.isupper():
                decrypted_char = chr((shift - (ord(char) - ord('A'))) % 26 + ord('A'))
            else:
                decrypted_char = chr((shift - (ord(char) - ord('a'))) % 26 + ord('a'))
            result += decrypted_char
            key_index += 1
        else:
            result += char
    return result

def gronsfeld_decrypt(ciphertext, key):
    """Decrypt Gronsfeld cipher (Vigenère with numeric key)"""
    result = ""
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            shift = int(key[key_index % len(key)])
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            result += decrypted_char
            key_index += 1
        else:
            result += char
    return result

def is_good_english(text):
    """Enhanced English detection"""
    text = text.upper()
    
    # Common English words
    common_words = [
        "THE", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL", "CAN", "HER", 
        "WAS", "ONE", "OUR", "HAD", "BY", "UP", "DO", "NO", "IF", "MY", "HE", 
        "AS", "TO", "GO", "WE", "AM", "IS", "OR", "BE", "IT", "IN", "AT", "ON", 
        "SO", "US", "AN", "OF", "CONGRATULATIONS", "WELL", "DONE", "GOOD", "JOB", 
        "FOUND", "SOLVED", "CORRECT", "FLAG", "USCC", "SECRET", "CIPHER", "DECODE", 
        "HIDDEN", "MYSTERY", "CHALLENGE", "COMPETITION", "CYBER", "SECURITY", "CTF",
        "GREAT", "EXCELLENT", "SUCCESS", "WINNER", "VICTORY"
    ]
    
    # Common patterns
    common_bigrams = ["TH", "HE", "IN", "ER", "AN", "RE", "ED", "ND", "ON", "EN", "AT", "OU", "IT", "IS", "OR", "TI", "HI", "AS", "TO", "LL"]
    
    words = text.split()
    if len(words) < 3:
        return False, 0
    
    # Score based on common words
    word_score = sum(3 for word in words[:15] if word in common_words)
    
    # Score based on common patterns
    pattern_score = sum(1 for pattern in common_bigrams if pattern in text)
    
    # Score based on reasonable word lengths
    length_score = sum(1 for word in words[:10] if 2 <= len(word) <= 12)
    
    total_score = word_score + pattern_score + length_score
    
    return total_score > 10, total_score

def main():
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    print("Final Comprehensive Cipher Analysis")
    print("=" * 60)
    
    # Try different cipher types with various keys
    cipher_methods = [
        ("Vigenère", vigenere_decrypt),
        ("Autokey", autokey_decrypt),
        ("Beaufort", beaufort_decrypt)
    ]
    
    # Extended key list
    keys_to_try = [
        # Based on repeated distance of 72
        "A" * 72, "B" * 72, "C" * 72,  # Single letter repeated
        
        # Factors of 72: [1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72]
        "AB", "ABC", "ABCD", "ABCDEF", "ABCDEFGH", "ABCDEFGHI",
        "ABCDEFGHIJKL", "ABCDEFGHIJKLMNOPQR", "ABCDEFGHIJKLMNOPQRSTUVWX",
        
        # Competition related
        "USCC", "CTF", "FLAG", "CYBER", "SECURITY", "COMPETITION",
        
        # From hint analysis
        "JUSTBECAUSE", "YOUKNOW", "MYNAME", "SECRETS", "KNOWMYNAME",
        
        # Try the hint itself as key
        "JUSTBECAUSEYOUKNOWMYNAMENOESNTMEANYOUKNOWMYSECRETS",
        
        # Common cipher keys
        "SECRET", "CIPHER", "DECODE", "HIDDEN", "MYSTERY", "PUZZLE",
        "KEY", "CODE", "PASS", "WORD", "CRYPTO", "ENCRYPT",
        
        # Names that might be referenced
        "ALICE", "BOB", "CHARLIE", "DAVID", "EVE", "FRANK",
        
        # Try some patterns based on the 72-character repeat
        "SECRETSECRETSECRETSECRETSECRETSECRETSECRETSECRETSECRETSECRETSECRETSECRET",
        "FLAGFLAGFLAGFLAGFLAGFLAGFLAGFLAGFLAGFLAGFLAGFLAGFLAGFLAGFLAGFLAGFLAGFLAG",
        "USCCUSCCUSCCUSCCUSCCUSCCUSCCUSCCUSCCUSCCUSCCUSCCUSCCUSCCUSCCUSCCUSCCUSCC",
        
        # Try some specific patterns
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 3,  # Alphabet repeated
    ]
    
    # Also try numeric keys for Gronsfeld
    numeric_keys = [
        "123", "1234", "12345", "123456", "1234567890",
        "072", "72", "164",  # Based on cipher length and repeat distance
        "111", "222", "333", "123123123"
    ]
    
    best_results = []
    
    # Try alphabetic keys
    for method_name, method_func in cipher_methods:
        print(f"\nTrying {method_name} cipher:")
        
        for key in keys_to_try:
            try:
                decrypted = method_func(ciphertext, key)
                is_good, score = is_good_english(decrypted)
                
                if score > 5:  # Only show promising results
                    print(f"  Key '{key[:20]}{'...' if len(key) > 20 else ''}' (Score: {score}): {decrypted[:80]}...")
                    
                    if is_good:
                        print(f"    *** EXCELLENT MATCH! ***")
                        best_results.append((method_name, key, decrypted, score))
                        print(f"    Full text: {decrypted}")
                        
                        # Check for flag format
                        if "USCC{" in decrypted or "FLAG{" in decrypted:
                            print(f"    *** FOUND FLAG! ***")
                            return decrypted
                
            except Exception as e:
                pass  # Skip errors
    
    # Try Gronsfeld with numeric keys
    print(f"\nTrying Gronsfeld cipher:")
    for key in numeric_keys:
        try:
            decrypted = gronsfeld_decrypt(ciphertext, key)
            is_good, score = is_good_english(decrypted)
            
            if score > 5:
                print(f"  Key '{key}' (Score: {score}): {decrypted[:80]}...")
                
                if is_good:
                    print(f"    *** EXCELLENT MATCH! ***")
                    best_results.append(("Gronsfeld", key, decrypted, score))
                    print(f"    Full text: {decrypted}")
                    
                    if "USCC{" in decrypted or "FLAG{" in decrypted:
                        print(f"    *** FOUND FLAG! ***")
                        return decrypted
        except:
            pass
    
    # Show best results
    if best_results:
        print("\n" + "="*60)
        print("BEST RESULTS:")
        best_results.sort(key=lambda x: x[3], reverse=True)
        
        for method, key, text, score in best_results[:3]:
            print(f"\n{method} with key '{key[:30]}{'...' if len(key) > 30 else ''}' (Score: {score}):")
            print(f"  {text}")
            
            if "USCC{" in text or "FLAG{" in text:
                return text
    
    return None

if __name__ == "__main__":
    result = main()
    if result:
        print(f"\n{'='*60}")
        print(f"FINAL ANSWER: {result}")
    else:
        print(f"\n{'='*60}")
        print("No clear solution found. The cipher may require a different approach.")
        print("Consider: book cipher, custom cipher, or steganography.")