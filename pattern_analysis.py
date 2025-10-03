#!/usr/bin/env python3
"""
Deep pattern analysis of the cipher
"""

def analyze_j_pattern(ciphertext):
    """Analyze patterns around the letter J"""
    print("Analyzing J patterns:")
    j_positions = [i for i, char in enumerate(ciphertext) if char == 'J']
    print(f"J appears at positions: {j_positions}")
    
    # Split by J and analyze
    parts = ciphertext.split('J')
    print(f"Split by J gives {len(parts)} parts:")
    for i, part in enumerate(parts):
        if part:
            print(f"  Part {i}: {part}")
    
    # Get first letter of each non-empty part
    first_letters = ''.join(part[0] if part else '' for part in parts if part)
    print(f"First letters: {first_letters}")
    
    return first_letters

def try_book_cipher(ciphertext):
    """Try to see if this could be a book cipher"""
    print("\nBook cipher analysis:")
    
    # Look for number patterns that might indicate page/line/word references
    # Convert letters to numbers (A=1, B=2, etc.)
    numbers = []
    for char in ciphertext:
        if char.isalpha():
            numbers.append(ord(char.upper()) - ord('A') + 1)
    
    print(f"First 20 letter-to-number conversions: {numbers[:20]}")
    
    # Look for patterns in these numbers
    # Check if they could be coordinates
    pairs = [(numbers[i], numbers[i+1]) for i in range(0, len(numbers)-1, 2)]
    print(f"First 10 number pairs: {pairs[:10]}")

def try_morse_like_patterns(ciphertext):
    """See if there are morse-like patterns"""
    print("\nMorse-like pattern analysis:")
    
    # Try treating certain letters as dots/dashes
    # Common approach: vowels as dots, consonants as dashes
    vowels = "AEIOU"
    morse_like = ""
    for char in ciphertext:
        if char in vowels:
            morse_like += "."
        else:
            morse_like += "-"
    
    print(f"Vowel=dot, consonant=dash: {morse_like[:100]}...")

def try_keyboard_shift(ciphertext):
    """Try keyboard shift cipher"""
    print("\nKeyboard shift analysis:")
    
    # QWERTY keyboard layout
    qwerty = "QWERTYUIOPASDFGHJKLZXCVBNM"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Try shifting by different amounts
    for shift in [1, -1, 2, -2]:
        result = ""
        for char in ciphertext:
            if char in qwerty:
                old_pos = qwerty.index(char)
                new_pos = (old_pos + shift) % len(qwerty)
                result += qwerty[new_pos]
            else:
                result += char
        
        print(f"QWERTY shift {shift}: {result[:80]}...")
        
        if any(word in result.upper() for word in ["THE", "AND", "FLAG", "USCC"]):
            print(f"  *** POTENTIAL MATCH: {result}")

def try_reverse_patterns(ciphertext):
    """Try various reverse patterns"""
    print("\nReverse pattern analysis:")
    
    # Try reversing the entire string
    reversed_full = ciphertext[::-1]
    print(f"Full reverse: {reversed_full[:80]}...")
    
    # Try reversing in chunks
    for chunk_size in [2, 3, 4, 5, 6, 8]:
        chunks = [ciphertext[i:i+chunk_size] for i in range(0, len(ciphertext), chunk_size)]
        reversed_chunks = [chunk[::-1] for chunk in chunks]
        result = ''.join(reversed_chunks)
        print(f"Reverse {chunk_size}-char chunks: {result[:80]}...")
        
        if any(word in result.upper() for word in ["THE", "AND", "FLAG", "USCC"]):
            print(f"  *** POTENTIAL MATCH: {result}")

def try_simple_substitution_patterns(ciphertext):
    """Try some simple substitution patterns"""
    print("\nSimple substitution patterns:")
    
    # Try ROT variations
    for rot in range(1, 26):
        result = ""
        for char in ciphertext:
            if char.isalpha():
                shifted = chr((ord(char) - ord('A') + rot) % 26 + ord('A'))
                result += shifted
            else:
                result += char
        
        if any(word in result.upper() for word in ["THE", "AND", "FLAG", "USCC", "SECRET", "CONGRATULATIONS"]):
            print(f"ROT{rot}: {result[:80]}...")
            print(f"  *** POTENTIAL MATCH: {result}")

def main():
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    print("Deep Pattern Analysis")
    print("=" * 60)
    
    # Analyze J patterns
    first_letters = analyze_j_pattern(ciphertext)
    
    # Try book cipher
    try_book_cipher(ciphertext)
    
    # Try morse-like patterns
    try_morse_like_patterns(ciphertext)
    
    # Try keyboard shift
    try_keyboard_shift(ciphertext)
    
    # Try reverse patterns
    try_reverse_patterns(ciphertext)
    
    # Try simple substitution
    try_simple_substitution_patterns(ciphertext)
    
    # Special analysis based on the hint
    print("\nHint-based analysis:")
    print("Hint: 'Just because you know my name doesn't mean you know my secrets'")
    
    # Maybe the "name" is hidden in the cipher somehow
    # Try extracting letters at specific intervals related to the word "NAME"
    name_positions = [13, 0, 12, 4]  # N=14th letter (13), A=1st (0), M=13th (12), E=5th (4)
    
    extracted = ""
    for i in range(len(ciphertext)):
        if i % 4 in name_positions:
            extracted += ciphertext[i]
    
    print(f"Letters at NAME positions: {extracted[:50]}...")
    
    # Try using "NAME" as a pattern
    name_pattern = "NAME" * (len(ciphertext) // 4 + 1)
    name_pattern = name_pattern[:len(ciphertext)]
    
    result = ""
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(name_pattern[i]) - ord('A')
            decrypted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result += decrypted
        else:
            result += char
    
    print(f"Using 'NAME' as Vigenère key: {result[:80]}...")
    
    if any(word in result.upper() for word in ["THE", "AND", "FLAG", "USCC", "SECRET", "CONGRATULATIONS"]):
        print(f"  *** POTENTIAL MATCH: {result}")

if __name__ == "__main__":
    main()