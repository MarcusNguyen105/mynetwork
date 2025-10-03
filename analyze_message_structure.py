#!/usr/bin/env python3

def analyze_message_structure():
    """Analyze the message structure for clues"""
    
    # Original message
    header = "5JT DE SJ2 1209 = 111 = GZV DBR ="
    
    ciphertext_lines = [
        "XLWHF DJKUC ZONWZ UFDGB SIILK",
        "GSOBR NPPMF BWFTU CHPCO UUBMB", 
        "NUUMW HMPJG JGJPM AXKPY FENEP",
        "LKHGM LUPUJ WWCZO YATTS CBSKI",
        "QFKSG ADRPZ J"
    ]
    
    print("Analyzing message structure...")
    print(f"Header: {header}")
    print()
    
    # Analyze header components
    print("Header analysis:")
    parts = header.split()
    for i, part in enumerate(parts):
        print(f"  Part {i+1}: '{part}'")
    
    print()
    
    # Analyze ciphertext
    print("Ciphertext analysis:")
    full_cipher = ''.join(''.join(line.split()) for line in ciphertext_lines)
    print(f"Full ciphertext: {full_cipher}")
    print(f"Length: {len(full_cipher)}")
    
    # Check if length matches header claim of 111
    print(f"Header claims 111 characters, actual: {len(full_cipher)}")
    
    # Analyze character frequency
    from collections import Counter
    freq = Counter(full_cipher)
    print(f"\nCharacter frequency (top 10):")
    for char, count in freq.most_common(10):
        print(f"  {char}: {count}")
    
    # Look for patterns
    print(f"\nLooking for repeated patterns...")
    
    # Check for repeated 2-grams
    bigrams = [full_cipher[i:i+2] for i in range(len(full_cipher)-1)]
    bigram_freq = Counter(bigrams)
    print("Most common bigrams:")
    for bigram, count in bigram_freq.most_common(5):
        if count > 1:
            print(f"  {bigram}: {count}")
    
    # Check for repeated 3-grams
    trigrams = [full_cipher[i:i+3] for i in range(len(full_cipher)-2)]
    trigram_freq = Counter(trigrams)
    print("Repeated trigrams:")
    for trigram, count in trigram_freq.most_common(10):
        if count > 1:
            print(f"  {trigram}: {count}")
    
    # Try different interpretations of the header
    print(f"\n{'='*50}")
    print("Alternative interpretations:")
    
    # Maybe 1209 is a key or offset
    print(f"1209 as numeric key: {1209}")
    print(f"1209 as date: December 9th")
    print(f"1209 as time: 12:09")
    
    # Maybe GZV DBR are not rotor positions but something else
    print(f"GZV = {ord('G')-ord('A')}, {ord('Z')-ord('A')}, {ord('V')-ord('A')}")
    print(f"DBR = {ord('D')-ord('A')}, {ord('B')-ord('A')}, {ord('R')-ord('A')}")
    
    # Try simple substitution based on the header info
    print(f"\n{'='*50}")
    print("Trying simple substitution approaches...")
    
    # Try ROT cipher with different shifts
    for shift in [12, 9, 3, 4, 18]:  # Based on numbers in header
        print(f"\nROT{shift}:")
        result = ""
        for char in full_cipher:
            if char.isalpha():
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result += shifted
            else:
                result += char
        print(f"  {result[:50]}...")
        
        # Check for flag pattern
        if 'USCC' in result:
            print(f"  *** USCC FOUND! ***")
            print(f"  Full result: {result}")
    
    # Try Atbash cipher (A=Z, B=Y, etc.)
    print(f"\nAtbash cipher:")
    atbash_result = ""
    for char in full_cipher:
        if char.isalpha():
            atbash_char = chr(ord('Z') - (ord(char) - ord('A')))
            atbash_result += atbash_char
        else:
            atbash_result += char
    print(f"  {atbash_result[:50]}...")
    if 'USCC' in atbash_result:
        print(f"  *** USCC FOUND! ***")
        print(f"  Full result: {atbash_result}")
    
    # Try Vigenère with keys from header
    print(f"\nTrying Vigenère with keys from header...")
    keys_to_try = ['GZV', 'DBR', 'GZVDBR', 'SJT', 'SJ']
    
    for key in keys_to_try:
        print(f"  Key '{key}':")
        result = vigenere_decrypt(full_cipher, key)
        print(f"    {result[:50]}...")
        if 'USCC' in result:
            print(f"    *** USCC FOUND! ***")
            print(f"    Full result: {result}")

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
    analyze_message_structure()