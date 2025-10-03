#!/usr/bin/env python3
"""
Detailed frequency analysis and simple substitution attempt
"""

def frequency_analysis(text):
    """Analyze character frequencies"""
    freq = {}
    for char in text:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)

def try_frequency_substitution(ciphertext):
    """Try substitution based on frequency analysis"""
    print("Frequency Analysis:")
    print("=" * 30)
    
    cipher_freq = frequency_analysis(ciphertext)
    print("Cipher character frequencies:")
    for char, count in cipher_freq:
        print(f"  {char}: {count}")
    
    # Most common English letters
    english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    
    # Create mapping
    mapping = {}
    for i, (char, _) in enumerate(cipher_freq):
        if i < len(english_freq):
            mapping[char] = english_freq[i]
    
    print(f"\nMapping based on frequency:")
    for cipher_char, english_char in mapping.items():
        print(f"  {cipher_char} -> {english_char}")
    
    # Apply mapping
    result = ""
    for char in ciphertext:
        if char in mapping:
            result += mapping[char]
        else:
            result += char
    
    print(f"\nDecrypted text: {result}")
    
    # Check if it looks like English
    words = result.split()
    if len(words) > 5:
        print(f"First few words: {' '.join(words[:10])}")
    
    return result

def try_simple_caesar_with_output(ciphertext):
    """Try Caesar cipher and show all results"""
    print("\nCaesar Cipher - All Results:")
    print("=" * 40)
    
    for shift in range(26):
        result = ""
        for char in ciphertext:
            if char.isalpha():
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result += shifted
            else:
                result += char
        
        print(f"ROT{shift:2d}: {result[:60]}...")
        
        # Look for any English-like patterns
        if shift == 13:  # ROT13 is common
            print(f"       (ROT13 - common cipher)")

def check_for_hidden_messages(ciphertext):
    """Look for hidden messages in various ways"""
    print("\nLooking for Hidden Messages:")
    print("=" * 35)
    
    # Check if first letters of words spell something
    # Assume words are separated by certain patterns
    
    # Try different word separators
    separators = ['X', 'Z', 'Q', 'J']  # Less common letters
    
    for sep in separators:
        if sep in ciphertext:
            parts = ciphertext.split(sep)
            if len(parts) > 3:
                first_letters = ''.join(part[0] if part else '' for part in parts if part)
                print(f"First letters when split by '{sep}': {first_letters}")
                
                # Try ROT13 on first letters
                rot13 = ""
                for char in first_letters:
                    if char.isalpha():
                        rot13 += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
                    else:
                        rot13 += char
                print(f"  ROT13: {rot13}")

def try_atbash_cipher(ciphertext):
    """Try Atbash cipher (A=Z, B=Y, etc.)"""
    print("\nAtbash Cipher:")
    print("=" * 20)
    
    result = ""
    for char in ciphertext:
        if char.isalpha():
            # A=Z, B=Y, C=X, etc.
            result += chr(ord('Z') - (ord(char) - ord('A')))
        else:
            result += char
    
    print(f"Atbash result: {result}")
    
    # Check for English patterns
    if any(word in result.upper() for word in ["THE", "AND", "FLAG", "USCC", "SECRET"]):
        print("*** POTENTIAL MATCH FOUND! ***")
        return result
    
    return None

def main():
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    print("DETAILED FREQUENCY ANALYSIS")
    print("=" * 60)
    
    # Frequency analysis
    freq_result = try_frequency_substitution(ciphertext)
    
    # Caesar cipher with all outputs
    try_simple_caesar_with_output(ciphertext)
    
    # Hidden messages
    check_for_hidden_messages(ciphertext)
    
    # Atbash
    atbash_result = try_atbash_cipher(ciphertext)
    
    if atbash_result:
        print(f"\nPOSSIBLE SOLUTION: {atbash_result}")
        return atbash_result
    
    print("\nNo clear solution found with frequency analysis methods.")
    return None

if __name__ == "__main__":
    result = main()
    if result:
        print(f"\nFINAL RESULT: {result}")
        # Check if we need to wrap in flag format
        if "USCC{" not in result and "FLAG{" not in result:
            print(f"Wrapped in flag format: USCC{{{result}}}")