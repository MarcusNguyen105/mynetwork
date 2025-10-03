#!/usr/bin/env python3

def analyze_decrypted():
    """Analyze the decrypted text more carefully"""
    
    ciphertext = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"
    key = "SJ2"
    
    # Decrypt using Vigenère with key SJ2
    result = vigenere_decrypt(ciphertext, key)
    
    print(f"Full decrypted text:")
    print(result)
    print(f"Length: {len(result)}")
    print()
    
    # Break it into chunks for easier reading
    chunk_size = 10
    chunks = [result[i:i+chunk_size] for i in range(0, len(result), chunk_size)]
    
    print("Text in 10-character chunks:")
    for i, chunk in enumerate(chunks):
        print(f"{i*chunk_size:3d}: {chunk}")
    
    print()
    
    # Look for patterns around USCC
    uscc_pos = result.find('USCC')
    if uscc_pos != -1:
        print(f"Context around USCC (position {uscc_pos}):")
        start = max(0, uscc_pos - 20)
        end = min(len(result), uscc_pos + 30)
        context = result[start:end]
        print(f"  ...{context}...")
        
        # Highlight the USCC part
        before = result[start:uscc_pos]
        uscc_part = result[uscc_pos:uscc_pos+4]
        after = result[uscc_pos+4:end]
        print(f"  ...{before}[{uscc_part}]{after}...")
    
    # Try to find readable words or patterns
    print(f"\nLooking for readable patterns...")
    
    # Check if any part looks like English words
    possible_words = []
    for i in range(len(result) - 2):
        for length in range(3, 8):
            if i + length <= len(result):
                word = result[i:i+length]
                if is_english_like(word):
                    possible_words.append((i, word))
    
    if possible_words:
        print("Possible English-like words found:")
        for pos, word in possible_words[:10]:  # Show first 10
            print(f"  Position {pos}: '{word}'")
    
    # Try different interpretations of the flag
    print(f"\nTrying different flag interpretations...")
    
    # Maybe the flag is encoded differently
    # Try reading every nth character
    for n in [2, 3, 4, 5]:
        nth_chars = ""
        for i in range(0, len(result), n):
            nth_chars += result[i]
        print(f"Every {n}th character: {nth_chars[:50]}...")
        if 'USCC' in nth_chars:
            print(f"  -> Contains USCC!")
    
    # Try reading backwards from USCC
    if uscc_pos != -1:
        backwards = result[uscc_pos::-1]
        print(f"Backwards from USCC: {backwards[:50]}...")
    
    # Try Caesar shifts on just the part after USCC
    if uscc_pos != -1:
        after_uscc = result[uscc_pos+4:uscc_pos+30]
        print(f"\nTrying Caesar shifts on text after USCC:")
        print(f"Original: {after_uscc}")
        
        for shift in range(1, 26):
            shifted = ""
            for char in after_uscc:
                if char.isalpha():
                    shifted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    shifted += char
            
            if any(word in shifted for word in ['FLAG', 'CIPHER', 'SECRET', 'ENIGMA']) or is_more_readable(shifted):
                print(f"Shift {shift:2d}: {shifted}")
    
    # Maybe the flag is the entire decrypted text with USCC prefix
    print(f"\nPossible complete flags:")
    print(f"1. USCC{{{result}}}")
    
    # Maybe just the part after USCC
    if uscc_pos != -1:
        after_uscc = result[uscc_pos+4:]
        print(f"2. USCC{{{after_uscc}}}")
        
        # Try cleaning up the after_uscc part
        clean_after = ''.join(c for c in after_uscc if c.isalnum())
        print(f"3. USCC{{{clean_after}}}")

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

def is_english_like(word):
    """Check if a word looks English-like"""
    english_words = ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'CAN', 'HER', 'WAS', 'ONE', 'OUR', 'HAD', 'USE', 'FLAG', 'CIPHER', 'SECRET', 'ENIGMA', 'CODE', 'MESSAGE']
    return word.upper() in english_words

def is_more_readable(text):
    """Check if text has more readable characteristics"""
    # Simple heuristic: check for common letter patterns
    common_patterns = ['TH', 'HE', 'IN', 'ER', 'AN', 'RE', 'ED', 'ND', 'ON', 'EN', 'AT', 'OU', 'IT', 'IS', 'OR', 'TI', 'AS', 'TO']
    count = sum(1 for pattern in common_patterns if pattern in text)
    return count >= 2

if __name__ == "__main__":
    analyze_decrypted()