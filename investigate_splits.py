#!/usr/bin/env python3
"""
Investigate the split patterns more carefully
"""

def analyze_split_pattern(ciphertext, split_char):
    """Analyze splitting by a specific character"""
    print(f"Analyzing split by '{split_char}':")
    
    parts = ciphertext.split(split_char)
    first_letters = ''.join(part[0] if part else '' for part in parts if part)
    
    print(f"  First letters: {first_letters}")
    
    # Try various transformations on the first letters
    transformations = []
    
    # ROT ciphers
    for rot in range(1, 26):
        result = ""
        for char in first_letters:
            if char.isalpha():
                result += chr((ord(char) - ord('A') + rot) % 26 + ord('A'))
            else:
                result += char
        transformations.append((f"ROT{rot}", result))
    
    # Atbash
    atbash = ""
    for char in first_letters:
        if char.isalpha():
            atbash += chr(ord('Z') - (ord(char) - ord('A')))
        else:
            atbash += char
    transformations.append(("Atbash", atbash))
    
    # Reverse
    transformations.append(("Reverse", first_letters[::-1]))
    
    # Show all transformations
    for name, result in transformations:
        print(f"    {name:10}: {result}")
        
        # Check if this looks like a meaningful word or phrase
        if len(result) >= 6:
            # Check for common patterns or words
            if any(word in result.upper() for word in ["FLAG", "USCC", "SECRET", "CIPHER", "DECODE", "SOLVED", "CORRECT", "WELL", "DONE", "GOOD", "JOB", "SUCCESS", "WIN", "CONGRATULATIONS"]):
                print(f"      *** POTENTIAL MATCH: {result} ***")
            
            # Check if it could be a name or meaningful word
            if result.lower() in ["alice", "bob", "charlie", "david", "eve", "frank", "grace", "henry", "john", "jane", "smith", "jones", "brown", "wilson", "taylor", "davis", "secret", "cipher", "decode", "hidden", "mystery", "puzzle", "crypto", "encrypt"]:
                print(f"      *** RECOGNIZED WORD: {result} ***")
    
    return first_letters

def try_all_split_chars(ciphertext):
    """Try splitting by all characters that appear multiple times"""
    print("Trying all possible split characters:")
    print("=" * 50)
    
    # Count character frequencies
    char_freq = {}
    for char in ciphertext:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Try characters that appear multiple times but not too frequently
    candidates = [(char, freq) for char, freq in char_freq.items() if 3 <= freq <= 15]
    candidates.sort(key=lambda x: x[1], reverse=True)
    
    print(f"Split candidates (frequency 3-15): {[f'{char}({freq})' for char, freq in candidates]}")
    print()
    
    results = []
    
    for char, freq in candidates:
        first_letters = analyze_split_pattern(ciphertext, char)
        results.append((char, first_letters))
        print()
    
    return results

def check_for_flag_format(text):
    """Check if text contains or could be formatted as a flag"""
    print(f"Checking '{text}' for flag format:")
    
    # Direct check
    if "USCC{" in text or "FLAG{" in text:
        print(f"  Already in flag format: {text}")
        return text
    
    # Try wrapping
    wrapped = f"USCC{{{text}}}"
    print(f"  Wrapped: {wrapped}")
    
    # Try with common flag words
    flag_words = ["CONGRATULATIONS", "WELLDONE", "GOODJOB", "SUCCESS", "WINNER", "SOLVED", "CORRECT", "DECODED"]
    
    for word in flag_words:
        if word in text.upper().replace(" ", ""):
            print(f"  Contains flag word '{word}': {text}")
            return f"USCC{{{text}}}"
    
    return None

def main():
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    print("INVESTIGATING SPLIT PATTERNS")
    print("=" * 60)
    
    # Try all split characters
    results = try_all_split_chars(ciphertext)
    
    print("\nSUMMARY OF INTERESTING RESULTS:")
    print("=" * 40)
    
    # Look for the most promising results
    for char, first_letters in results:
        if len(first_letters) >= 6:
            print(f"Split by '{char}': {first_letters}")
            
            # Check each transformation for this split
            for rot in [13, 1, 25]:  # Common rotations
                result = ""
                for c in first_letters:
                    if c.isalpha():
                        result += chr((ord(c) - ord('A') + rot) % 26 + ord('A'))
                    else:
                        result += c
                
                print(f"  ROT{rot}: {result}")
                
                # Check if this could be a flag
                flag_result = check_for_flag_format(result)
                if flag_result:
                    print(f"  *** POTENTIAL FLAG: {flag_result} ***")
                    return flag_result
    
    print("\nNo clear flag found in split patterns.")
    return None

if __name__ == "__main__":
    result = main()
    if result:
        print(f"\nFINAL ANSWER: {result}")
    else:
        print("\nContinue investigating other approaches.")