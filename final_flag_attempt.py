#!/usr/bin/env python3

# Access level descriptions
descriptions = [
    "SCAVENGER — Yard floor access",
    "HAULER — Broken-but-usable stock",
    "MECHANIC — Engine bays & bins",
    "QUARRY FOREMAN — Heavy salvage ops",
    "YARD MANAGER — Central yard systems",
    "BOSS — Secure compound & vaults"
]

def try_all_flag_techniques():
    print("Final comprehensive flag analysis:")
    print("=" * 60)
    
    # 1. Try extracting letters by different patterns
    print("\n1. Different letter extraction patterns:")
    
    # Pattern 1: First letter of each word
    pattern1 = ""
    for desc in descriptions:
        words = desc.split()
        for word in words:
            pattern1 += word[0]
    print(f"First letters: {pattern1}")
    
    # Pattern 2: Last letter of each word
    pattern2 = ""
    for desc in descriptions:
        words = desc.split()
        for word in words:
            pattern2 += word[-1]
    print(f"Last letters: {pattern2}")
    
    # Pattern 3: Middle letter of each word (if odd length)
    pattern3 = ""
    for desc in descriptions:
        words = desc.split()
        for word in words:
            if len(word) % 2 == 1:  # Odd length
                middle = len(word) // 2
                pattern3 += word[middle]
    print(f"Middle letters: {pattern3}")
    
    # Pattern 4: Every second letter
    pattern4 = ""
    for desc in descriptions:
        for i in range(0, len(desc), 2):
            pattern4 += desc[i]
    print(f"Every second letter: {pattern4}")
    
    # Pattern 5: Vowels only
    pattern5 = ""
    vowels = "AEIOUaeiou"
    for desc in descriptions:
        for char in desc:
            if char in vowels:
                pattern5 += char
    print(f"Vowels only: {pattern5}")
    
    # Pattern 6: Consonants only
    pattern6 = ""
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    for desc in descriptions:
        for char in desc:
            if char in consonants:
                pattern6 += char
    print(f"Consonants only: {pattern6}")
    
    # 2. Try different combinations of job titles
    print("\n2. Job title combinations:")
    job_titles = ["SCAVENGER", "HAULER", "MECHANIC", "QUARRY FOREMAN", "YARD MANAGER", "BOSS"]
    
    # First letters of job titles
    job_first = "".join([title.split()[0][0] for title in job_titles])
    print(f"Job first letters: {job_first}")
    
    # Last letters of job titles
    job_last = "".join([title.split()[-1][-1] for title in job_titles])
    print(f"Job last letters: {job_last}")
    
    # 3. Try extracting from specific positions
    print("\n3. Position-based extraction:")
    
    # Extract character at position 6 from each description (since we want level 6)
    pos6_chars = ""
    for desc in descriptions:
        if len(desc) > 6:
            pos6_chars += desc[6]
    print(f"Position 6 characters: {pos6_chars}")
    
    # Extract character at position 0 from each description
    pos0_chars = ""
    for desc in descriptions:
        pos0_chars += desc[0]
    print(f"Position 0 characters: {pos0_chars}")
    
    # 4. Try reading the descriptions as if they contain hidden text
    print("\n4. Hidden text analysis:")
    
    # Look for patterns that might be flags
    all_text = " ".join(descriptions)
    print(f"All text: {all_text}")
    
    # Check if any part looks like a flag
    flag_indicators = ["uscc", "USCC", "flag", "FLAG", "ctf", "CTF", "cyberbowl", "CYBERBOWL"]
    for indicator in flag_indicators:
        if indicator in all_text:
            print(f"Found '{indicator}' in text")
    
    # 5. Try interpreting the descriptions as instructions
    print("\n5. Interpreting as instructions:")
    print("Maybe the descriptions are telling us what to do:")
    for i, desc in enumerate(descriptions, 1):
        print(f"Level {i}: {desc}")
    
    # 6. Check if the flag is simply the highest access level
    print("\n6. Simple interpretation:")
    print("The challenge asks for 'the highest level of access'")
    print("Level 6 is BOSS — Secure compound & vaults")
    print("Maybe the flag is just '6' or 'BOSS' or 'BOSS — Secure compound & vaults'")

if __name__ == "__main__":
    try_all_flag_techniques()