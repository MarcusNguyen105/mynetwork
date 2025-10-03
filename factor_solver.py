#!/usr/bin/env python3
"""
Try keys that are factors of 72
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

def get_factors(n):
    """Get all factors of n"""
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

def main():
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    factors = get_factors(72)
    print(f"Factors of 72: {factors}")
    print()
    
    # Try keys of each factor length
    for factor in factors:
        if factor <= 12:  # Don't try extremely long keys
            print(f"Trying keys of length {factor}:")
            
            # Generate some test keys of this length
            test_keys = []
            
            # Try repeating single letters
            for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                test_keys.append(letter * factor)
            
            # Try common words repeated/truncated to this length
            words = ["SECRET", "CIPHER", "CRYPTO", "DECODE", "PUZZLE", "HIDDEN", "MYSTERY", "USCC", "FLAG", "CTF", "KEY", "CODE", "PASS", "WORD"]
            for word in words:
                if len(word) == factor:
                    test_keys.append(word)
                elif len(word) < factor:
                    # Repeat the word
                    repeated = (word * ((factor // len(word)) + 1))[:factor]
                    test_keys.append(repeated)
                else:
                    # Truncate the word
                    test_keys.append(word[:factor])
            
            # Test each key
            for key in test_keys:
                decrypted = vigenere_decrypt(ciphertext, key)
                # Look for English-like patterns
                if any(pattern in decrypted.upper() for pattern in ["THE", "AND", "FLAG", "USCC", "SECRET", "YOU", "ARE", "THIS", "THAT", "WITH", "HAVE", "WILL", "FROM", "THEY", "BEEN", "SAID", "EACH", "WHICH", "THEIR"]):
                    print(f"  Key '{key}': {decrypted}")
                    print("  *** POTENTIAL MATCH ***")
                    print()
            
            print()

if __name__ == "__main__":
    main()