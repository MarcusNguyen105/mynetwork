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

def analyze_descriptions():
    print("Analyzing access level descriptions for hidden patterns:")
    print("=" * 60)
    
    # Extract first letters of each word
    print("\n1. First letters of each word:")
    for i, desc in enumerate(descriptions, 1):
        words = desc.split()
        first_letters = ''.join([word[0] for word in words])
        print(f"Level {i}: {first_letters}")
    
    # Extract first letters of job titles only
    print("\n2. First letters of job titles:")
    for i, desc in enumerate(descriptions, 1):
        job_title = desc.split(' — ')[0]
        first_letters = ''.join([word[0] for word in job_title.split()])
        print(f"Level {i}: {first_letters}")
    
    # Extract first letters of descriptions only
    print("\n3. First letters of descriptions:")
    for i, desc in enumerate(descriptions, 1):
        description = desc.split(' — ')[1]
        first_letters = ''.join([word[0] for word in description.split()])
        print(f"Level {i}: {first_letters}")
    
    # Check for common CTF flag patterns
    print("\n4. Looking for flag patterns:")
    all_text = ' '.join(descriptions)
    print(f"All text: {all_text}")
    
    # Check if any description contains common flag indicators
    flag_indicators = ['flag', 'FLAG', 'ctf', 'CTF', 'uscc', 'USCC', 'cyberbowl', 'CYBERBOWL']
    for i, desc in enumerate(descriptions, 1):
        for indicator in flag_indicators:
            if indicator in desc:
                print(f"Level {i} contains '{indicator}': {desc}")
    
    # Check for hidden characters or encoding
    print("\n5. Character analysis:")
    for i, desc in enumerate(descriptions, 1):
        print(f"Level {i}: {len(desc)} chars")
        # Check for non-printable characters
        non_printable = [c for c in desc if ord(c) < 32 or ord(c) > 126]
        if non_printable:
            print(f"  Non-printable chars: {non_printable}")

if __name__ == "__main__":
    analyze_descriptions()