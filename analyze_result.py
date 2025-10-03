#!/usr/bin/env python3

def analyze_plaintext():
    # The potentially readable plaintext we found
    plaintext = "MEOXITLFVMVQDFGYUNLGKXYHPAMTZLVTDPQCHHJKBRUYROOOEKFWRXLPDCAHSOVCULZCHRYHIILSTJECDDVHEMZZEZHZBIDYCZARIHGNUCANJOZ"
    
    print(f"Analyzing plaintext: {plaintext}")
    print(f"Length: {len(plaintext)}")
    
    # Look for common English words
    common_words = ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'CAN', 'HER', 'WAS', 'ONE', 'OUR', 'HAD', 'USE', 'USCC', 'FLAG']
    
    print("\nLooking for common words:")
    for word in common_words:
        if word in plaintext:
            pos = plaintext.find(word)
            print(f"Found '{word}' at position {pos}")
    
    # Look for potential flag patterns
    print("\nLooking for flag patterns:")
    
    # Look for USCC pattern
    if 'USCC' in plaintext:
        pos = plaintext.find('USCC')
        print(f"Found 'USCC' at position {pos}")
        # Look for the rest of the flag
        flag_start = pos
        flag_end = plaintext.find('}', flag_start) if '}' in plaintext[flag_start:] else len(plaintext)
        potential_flag = plaintext[flag_start:flag_end+1] if flag_end < len(plaintext) else plaintext[flag_start:]
        print(f"Potential flag: {potential_flag}")
    
    # Look for other patterns that might be flags
    print("\nLooking for other patterns:")
    
    # Split into chunks to see if there are readable segments
    chunk_size = 10
    chunks = [plaintext[i:i+chunk_size] for i in range(0, len(plaintext), chunk_size)]
    
    print("Text in chunks:")
    for i, chunk in enumerate(chunks):
        print(f"{i*chunk_size:3d}: {chunk}")
    
    # Look for repeated patterns or structure
    print(f"\nLooking for patterns...")
    
    # Check if any 3-letter combinations look like words
    for i in range(len(plaintext) - 2):
        trigram = plaintext[i:i+3]
        if trigram in ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'CAN', 'HER', 'WAS', 'ONE', 'OUR', 'HAD', 'USE']:
            print(f"Found word '{trigram}' at position {i}")

if __name__ == "__main__":
    analyze_plaintext()