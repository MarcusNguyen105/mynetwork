#!/usr/bin/env python3
"""
Final investigation of promising patterns
"""

def analyze_werziane():
    """Analyze the WERZIANE result"""
    text = "WERZIANE"
    print(f"Analyzing '{text}':")
    
    # Try anagrams
    from itertools import permutations
    
    # Check if it could be rearranged into meaningful words
    # This is computationally expensive, so let's try some manual rearrangements
    manual_arrangements = [
        "WERZIANE",
        "WERIANZE", 
        "WEARIZEN",
        "WEARINZE",
        "WIZARENE",
        "WIZARDEN",
        "NEWZAIRE",
        "NEWZAIRE",
        "AIRWEZEN",
        "AIRWEZNE"
    ]
    
    print("Manual rearrangements:")
    for arr in manual_arrangements:
        print(f"  {arr}")
    
    # Try splitting it
    print("\nTrying to split WERZIANE:")
    splits = [
        ("WER", "ZIANE"),
        ("WERZ", "IANE"),
        ("WERZI", "ANE"),
        ("WE", "RZIANE"),
        ("W", "ERZIANE")
    ]
    
    for part1, part2 in splits:
        print(f"  {part1} + {part2}")
    
    # Try ROT on it again
    print("\nApplying more ROT to WERZIANE:")
    for rot in range(1, 26):
        result = ""
        for char in text:
            if char.isalpha():
                result += chr((ord(char) - ord('A') + rot) % 26 + ord('A'))
            else:
                result += char
        print(f"  ROT{rot}: {result}")
        
        # Check if any of these look meaningful
        if result in ["CONGRATULATIONS", "WELLDONE", "GOODJOB", "SUCCESS", "WINNER", "SOLVED", "CORRECT", "DECODED", "EXCELLENT", "FANTASTIC"]:
            print(f"    *** MEANINGFUL WORD FOUND: {result} ***")
            return result

def check_other_promising_results():
    """Check other promising results from the split analysis"""
    promising = [
        ("J split", "ITLGASTE"),
        ("X split", "JREMVNAR"),
        ("S split", "JOINERJ"),
        ("N split", "JFXEISFWLK")
    ]
    
    print("Checking other promising results:")
    print("=" * 40)
    
    for desc, text in promising:
        print(f"\n{desc}: {text}")
        
        # Try various transformations
        # ROT13
        rot13 = ""
        for char in text:
            if char.isalpha():
                rot13 += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                rot13 += char
        print(f"  ROT13: {rot13}")
        
        # Reverse
        print(f"  Reverse: {text[::-1]}")
        
        # Atbash
        atbash = ""
        for char in text:
            if char.isalpha():
                atbash += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                atbash += char
        print(f"  Atbash: {atbash}")
        
        # Check if any look like words
        words_to_check = [text, rot13, text[::-1], atbash]
        for word in words_to_check:
            if word.lower() in ["congratulations", "welldone", "goodjob", "success", "winner", "solved", "correct", "decoded", "excellent", "fantastic", "flag", "uscc", "secret", "cipher", "decode", "hidden", "mystery"]:
                print(f"    *** FOUND MEANINGFUL WORD: {word} ***")
                return word

def try_simple_word_search():
    """Try searching for simple words hidden in the cipher"""
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    print("Searching for hidden words in the cipher:")
    print("=" * 45)
    
    # Common flag words
    flag_words = ["FLAG", "USCC", "CONGRATULATIONS", "WELLDONE", "GOODJOB", "SUCCESS", "WINNER", "SOLVED", "CORRECT", "DECODED", "EXCELLENT", "FANTASTIC", "SECRET", "CIPHER", "DECODE", "HIDDEN", "MYSTERY"]
    
    # Try to find these words directly
    for word in flag_words:
        if word in ciphertext:
            print(f"Found '{word}' directly in cipher at position {ciphertext.index(word)}")
    
    # Try to find them with simple ROT
    for rot in [1, 13, 25]:
        rotted_cipher = ""
        for char in ciphertext:
            if char.isalpha():
                rotted_cipher += chr((ord(char) - ord('A') + rot) % 26 + ord('A'))
            else:
                rotted_cipher += char
        
        for word in flag_words:
            if word in rotted_cipher:
                print(f"Found '{word}' in ROT{rot} cipher at position {rotted_cipher.index(word)}")
                # Extract surrounding context
                pos = rotted_cipher.index(word)
                start = max(0, pos - 10)
                end = min(len(rotted_cipher), pos + len(word) + 10)
                context = rotted_cipher[start:end]
                print(f"  Context: ...{context}...")
                return f"USCC{{{word}}}"

def main():
    print("FINAL INVESTIGATION OF PROMISING PATTERNS")
    print("=" * 60)
    
    # Analyze WERZIANE
    werziane_result = analyze_werziane()
    if werziane_result:
        return f"USCC{{{werziane_result}}}"
    
    # Check other promising results
    other_result = check_other_promising_results()
    if other_result:
        return f"USCC{{{other_result}}}"
    
    # Try simple word search
    word_result = try_simple_word_search()
    if word_result:
        return word_result
    
    # If nothing found, let's try one more desperate attempt
    print("\nDesperate final attempt - maybe the solution is simpler:")
    
    # What if the flag is just hidden in plain sight with a simple transformation?
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    # Try reading every 13th character (unlucky 13?)
    every_13th = ""
    for i in range(0, len(ciphertext), 13):
        every_13th += ciphertext[i]
    print(f"Every 13th character: {every_13th}")
    
    # Try reading first letter of every 13-character block
    blocks = [ciphertext[i:i+13] for i in range(0, len(ciphertext), 13)]
    first_letters = ''.join(block[0] if block else '' for block in blocks)
    print(f"First letter of each 13-char block: {first_letters}")
    
    # Apply ROT13 to this
    rot13_first = ""
    for char in first_letters:
        if char.isalpha():
            rot13_first += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            rot13_first += char
    print(f"ROT13 of first letters: {rot13_first}")
    
    if any(word in rot13_first for word in ["CONGRATULATIONS", "WELLDONE", "GOODJOB", "SUCCESS", "WINNER", "SOLVED", "CORRECT"]):
        print(f"*** FOUND SOLUTION: {rot13_first} ***")
        return f"USCC{{{rot13_first}}}"
    
    print("\nNo clear solution found. This cipher may require a different approach entirely.")
    return None

if __name__ == "__main__":
    result = main()
    if result:
        print(f"\n{'='*60}")
        print(f"FINAL ANSWER: {result}")
    else:
        print(f"\n{'='*60}")
        print("Unable to solve this cipher with current methods.")
        print("The cipher may be:")
        print("- A custom/proprietary cipher")
        print("- A book cipher requiring a specific text")
        print("- Steganography")
        print("- A multi-stage cipher")
        print("- Require additional context or clues")