#!/usr/bin/env python3
"""
Advanced cipher solver focusing on pattern analysis
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

def find_key_length(ciphertext):
    """Try to find key length using Kasiski examination"""
    # Look for repeated sequences and their distances
    sequences = {}
    min_length = 3
    
    for length in range(min_length, min(10, len(ciphertext)//4)):
        for i in range(len(ciphertext) - length + 1):
            seq = ciphertext[i:i+length]
            if seq in sequences:
                sequences[seq].append(i)
            else:
                sequences[seq] = [i]
    
    # Find sequences that repeat
    repeated_sequences = {k: v for k, v in sequences.items() if len(v) > 1}
    
    if repeated_sequences:
        print("Repeated sequences and their positions:")
        distances = []
        for seq, positions in repeated_sequences.items():
            print(f"'{seq}': {positions}")
            # Calculate distances between occurrences
            for i in range(len(positions) - 1):
                distance = positions[i+1] - positions[i]
                distances.append(distance)
                print(f"  Distance: {distance}")
        
        # Find GCD of distances to estimate key length
        from math import gcd
        if len(distances) > 1:
            result_gcd = distances[0]
            for d in distances[1:]:
                result_gcd = gcd(result_gcd, d)
            print(f"GCD of distances: {result_gcd}")
            return result_gcd
    
    return None

def try_all_short_keys(ciphertext, max_length=6):
    """Try all possible keys up to a certain length"""
    import itertools
    
    results = []
    
    # Try single letter keys first (Caesar cipher)
    for i in range(26):
        key = chr(ord('A') + i)
        decrypted = vigenere_decrypt(ciphertext, key)
        if any(word in decrypted.upper() for word in ["THE", "AND", "FLAG", "USCC", "SECRET", "YOU", "ARE", "THIS", "THAT"]):
            results.append((key, decrypted))
    
    # Try common short words as keys
    common_words = ["A", "I", "THE", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL", "CAN", "HER", "WAS", "ONE", "OUR", "HAD", "BY", "UP", "DO", "NO", "IF", "MY", "HE", "AS", "TO", "GO", "WE", "AM", "IS", "OR", "BE", "IT", "IN", "AT", "ON", "SO", "US", "AN", "OF"]
    
    for word in common_words:
        decrypted = vigenere_decrypt(ciphertext, word)
        if any(pattern in decrypted.upper() for pattern in ["THE", "AND", "FLAG", "USCC", "SECRET", "YOU", "ARE", "THIS", "THAT"]):
            results.append((word, decrypted))
    
    return results

def main():
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    print("Advanced Cipher Analysis")
    print("=" * 60)
    
    # Try to find key length
    print("Kasiski Examination:")
    key_length = find_key_length(ciphertext)
    print()
    
    # Try short keys
    print("Trying short keys:")
    results = try_all_short_keys(ciphertext)
    for key, decrypted in results:
        print(f"Key '{key}': {decrypted[:80]}...")
    print()
    
    # If we found a potential key length, try keys of that length
    if key_length:
        print(f"Trying keys of length {key_length}:")
        # Try some common patterns for that length
        if key_length <= 8:
            test_keys = []
            # Generate some test keys
            for word in ["SECRET", "CIPHER", "CRYPTO", "DECODE", "PUZZLE", "HIDDEN", "MYSTERY"]:
                if len(word) == key_length:
                    test_keys.append(word)
                elif len(word) > key_length:
                    test_keys.append(word[:key_length])
                else:
                    # Repeat the word to match length
                    repeated = (word * ((key_length // len(word)) + 1))[:key_length]
                    test_keys.append(repeated)
            
            for key in test_keys:
                decrypted = vigenere_decrypt(ciphertext, key)
                if any(pattern in decrypted.upper() for pattern in ["THE", "AND", "FLAG", "USCC", "SECRET", "YOU", "ARE"]):
                    print(f"Key '{key}': {decrypted}")
    
    # Try some specific keys based on context clues
    print("\nTrying context-based keys:")
    context_keys = ["USCC", "CTF", "FLAG", "COMPETITION", "CYBER", "SECURITY"]
    
    for key in context_keys:
        decrypted = vigenere_decrypt(ciphertext, key)
        print(f"Key '{key}': {decrypted[:80]}...")
        if any(pattern in decrypted.upper() for pattern in ["FLAG", "USCC", "THE", "SECRET"]):
            print(f"  *** POTENTIAL MATCH: {decrypted}")

if __name__ == "__main__":
    main()