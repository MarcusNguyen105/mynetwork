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

def analyze_for_flag():
    print("Comprehensive flag analysis:")
    print("=" * 50)
    
    # 1. Extract all first letters
    print("\n1. All first letters:")
    all_first_letters = ""
    for desc in descriptions:
        words = desc.split()
        first_letters = ''.join([word[0] for word in words])
        all_first_letters += first_letters
        print(f"  {desc} -> {first_letters}")
    print(f"Combined: {all_first_letters}")
    
    # 2. Extract job title first letters only
    print("\n2. Job title first letters:")
    job_first_letters = ""
    for desc in descriptions:
        job_title = desc.split(' — ')[0]
        first_letters = ''.join([word[0] for word in job_title.split()])
        job_first_letters += first_letters
        print(f"  {job_title} -> {first_letters}")
    print(f"Combined: {job_first_letters}")
    
    # 3. Extract description first letters only
    print("\n3. Description first letters:")
    desc_first_letters = ""
    for desc in descriptions:
        description = desc.split(' — ')[1]
        first_letters = ''.join([word[0] for word in description.split()])
        desc_first_letters += first_letters
        print(f"  {description} -> {first_letters}")
    print(f"Combined: {desc_first_letters}")
    
    # 4. Try different combinations
    print("\n4. Different combinations:")
    combinations = [
        ("Job titles only", job_first_letters),
        ("Descriptions only", desc_first_letters),
        ("All first letters", all_first_letters),
        ("Job titles reversed", job_first_letters[::-1]),
        ("Descriptions reversed", desc_first_letters[::-1]),
        ("All reversed", all_first_letters[::-1]),
    ]
    
    for name, combo in combinations:
        print(f"  {name}: {combo}")
    
    # 5. Check for common flag formats
    print("\n5. Checking for flag formats:")
    flag_formats = ["uscc{", "USCC{", "flag{", "FLAG{", "ctf{", "CTF{"]
    
    for name, combo in combinations:
        for flag_format in flag_formats:
            if flag_format.lower() in combo.lower():
                print(f"  Found '{flag_format}' in {name}: {combo}")
    
    # 6. Try extracting letters in different orders
    print("\n6. Different letter extraction orders:")
    
    # Extract letters by position in each word
    for pos in range(5):  # Try positions 0-4
        extracted = ""
        for desc in descriptions:
            words = desc.split()
            for word in words:
                if pos < len(word):
                    extracted += word[pos]
        print(f"  Position {pos}: {extracted}")
    
    # 7. Check for hidden patterns in the em dashes
    print("\n7. Em dash analysis:")
    em_dashes = []
    for desc in descriptions:
        if '—' in desc:
            em_dashes.append(desc)
    print(f"  Descriptions with em dashes: {len(em_dashes)}")
    
    # 8. Try reading the descriptions as if they contain encoded text
    print("\n8. Looking for encoded text:")
    for i, desc in enumerate(descriptions, 1):
        # Check if any part looks like encoded text
        words = desc.split()
        for word in words:
            if word.isupper() and len(word) > 1:
                print(f"  Level {i} uppercase word: {word}")

if __name__ == "__main__":
    analyze_for_flag()