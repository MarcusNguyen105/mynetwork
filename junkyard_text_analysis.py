#!/usr/bin/env python3
import re

def analyze_level_text():
    """Analyze the level descriptions for hidden flags"""
    
    level_descriptions = {
        1: "SCAVENGER — Yard floor access",
        2: "HAULER — Broken-but-usable stock", 
        3: "MECHANIC — Engine bays & bins",
        4: "QUARRY FOREMAN — Heavy salvage ops",
        5: "YARD MANAGER — Central yard systems",
        6: "BOSS — Secure compound & vaults"
    }
    
    print("=== ANALYZING LEVEL DESCRIPTIONS FOR HIDDEN FLAGS ===")
    
    # Print all descriptions
    for level, desc in level_descriptions.items():
        print(f"Level {level}: {desc}")
    
    # Look for hidden patterns
    print(f"\n=== PATTERN ANALYSIS ===")
    
    # First letters of each word
    all_words = []
    for desc in level_descriptions.values():
        words = desc.replace('—', '').split()
        all_words.extend(words)
    
    first_letters = ''.join([word[0] for word in all_words])
    print(f"First letters of all words: {first_letters}")
    
    # First letters of job titles only
    job_titles = ["SCAVENGER", "HAULER", "MECHANIC", "QUARRY FOREMAN", "YARD MANAGER", "BOSS"]
    job_first_letters = ''.join([title.split()[0][0] for title in job_titles])
    print(f"First letters of job titles: {job_first_letters}")
    
    # Look for acronyms in descriptions
    descriptions_only = [
        "Yard floor access",
        "Broken-but-usable stock", 
        "Engine bays & bins",
        "Heavy salvage ops",
        "Central yard systems",
        "Secure compound & vaults"
    ]
    
    desc_first_letters = ''.join([desc.split()[0][0] for desc in descriptions_only])
    print(f"First letters of descriptions: {desc_first_letters}")
    
    # Try different combinations
    print(f"\n=== TRYING DIFFERENT COMBINATIONS ===")
    
    # Maybe the flag is formed by taking specific letters from each description
    combinations = []
    
    # Try first letter of each description
    combo1 = ''.join([desc.split()[-1][0] for desc in descriptions_only])  # Last word first letter
    print(f"Last word first letters: {combo1}")
    
    # Try last letter of each description  
    combo2 = ''.join([desc[-1] for desc in descriptions_only])
    print(f"Last letters of descriptions: {combo2}")
    
    # Try middle letters
    combo3 = ''.join([desc[len(desc)//2] for desc in descriptions_only])
    print(f"Middle letters of descriptions: {combo3}")
    
    # Look for numbers or special patterns
    print(f"\n=== LOOKING FOR NUMBERS AND SPECIAL PATTERNS ===")
    
    all_text = ' '.join(level_descriptions.values())
    numbers = re.findall(r'\d+', all_text)
    print(f"Numbers found: {numbers}")
    
    special_chars = re.findall(r'[^a-zA-Z0-9\s—]', all_text)
    print(f"Special characters: {special_chars}")
    
    # Maybe the flag is the level descriptions themselves rearranged
    print(f"\n=== CHECKING IF DESCRIPTIONS CONTAIN FLAG DIRECTLY ===")
    
    # Check if any description contains flag-like patterns
    flag_patterns = [
        r'uscc\{[^}]*\}',
        r'flag\{[^}]*\}',
        r'\{[^}]*\}',
        r'[A-Za-z0-9_]{20,}',
    ]
    
    for pattern in flag_patterns:
        matches = re.findall(pattern, all_text, re.IGNORECASE)
        if matches:
            print(f"Pattern {pattern} found: {matches}")
    
    # Try ROT13 or other simple ciphers
    print(f"\n=== TRYING SIMPLE CIPHERS ===")
    
    def rot13(text):
        result = ""
        for char in text:
            if 'a' <= char <= 'z':
                result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                result += char
        return result
    
    for level, desc in level_descriptions.items():
        rot13_desc = rot13(desc)
        if 'uscc' in rot13_desc.lower() or 'flag' in rot13_desc.lower():
            print(f"ROT13 of level {level}: {rot13_desc}")
    
    # Try Caesar cipher with different shifts
    def caesar_cipher(text, shift):
        result = ""
        for char in text:
            if 'a' <= char <= 'z':
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += char
        return result
    
    print(f"\nTrying Caesar cipher shifts:")
    for shift in range(1, 26):
        shifted_text = caesar_cipher(job_first_letters, shift)
        if len(shifted_text) >= 4:  # Only show if substantial
            print(f"Shift {shift}: {shifted_text}")
            if 'flag' in shifted_text.lower() or 'uscc' in shifted_text.lower():
                print(f"  *** POTENTIAL FLAG: {shifted_text} ***")
    
    # Maybe the flag is in the order of access levels needed
    print(f"\n=== CHECKING ACCESS LEVEL ORDER ===")
    print("To get highest access (BOSS level), you need level 6")
    print("Maybe the flag is simply: uscc{6} or uscc{boss} or similar")
    
    potential_flags = [
        "uscc{6}",
        "uscc{boss}",
        "uscc{BOSS}",
        "uscc{secure_compound_vaults}",
        "uscc{highest_access}",
        "uscc{junkyard_boss}",
        f"uscc{{{job_first_letters.lower()}}}",
        f"uscc{{{desc_first_letters.lower()}}}",
    ]
    
    print("Potential flags based on analysis:")
    for flag in potential_flags:
        print(f"  {flag}")
    
    return potential_flags

if __name__ == "__main__":
    potential_flags = analyze_level_text()
    
    print(f"\n=== SUMMARY ===")
    print("Based on text analysis, the most likely flags are:")
    for i, flag in enumerate(potential_flags[:5], 1):
        print(f"{i}. {flag}")
    
    print(f"\nNote: The challenge asks to 'get the highest level of access'")
    print(f"Level 6 (BOSS) is the highest level, so the flag might be related to that.")