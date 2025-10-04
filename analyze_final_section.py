#!/usr/bin/env python3

import re
import base64
import codecs

def analyze_final_section():
    # The final section that looks different
    final_section = "vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs"

    print(f"Final section: '{final_section}'")
    print(f"Length: {len(final_section)}")

    # Character frequency
    char_freq = {}
    for char in final_section:
        char_freq[char] = char_freq.get(char, 0) + 1

    print("\nCharacter frequency:")
    for char in sorted(char_freq.keys()):
        print(f"  '{char}': {char_freq[char]}")

    # Try various decoding approaches

    # 1. Try base64
    print("\n1. Base64 decoding attempts:")
    # Remove non-base64 characters
    cleaned = re.sub(r'[^A-Za-z0-9+/=]', '', final_section)
    print(f"Cleaned: '{cleaned}'")

    try:
        # Add padding if needed
        missing_padding = len(cleaned) % 4
        if missing_padding:
            cleaned += '=' * (4 - missing_padding)

        decoded = base64.b64decode(cleaned)
        print(f"Base64 decode: '{decoded.decode('utf-8', errors='ignore')}'")
    except Exception as e:
        print(f"Base64 decode failed: {e}")

    # 2. Try ROT13
    print("\n2. ROT13 decoding:")
    try:
        rot13 = codecs.decode(final_section, 'rot13')
        print(f"ROT13: '{rot13}'")
    except Exception as e:
        print(f"ROT13 failed: {e}")

    # 3. Try other ROT variations
    print("\n3. Other ROT decodings:")
    for rot in range(1, 26):
        try:
            # Simple Caesar cipher
            result = ''
            for char in final_section:
                if char.isalpha():
                    shifted = chr((ord(char.lower()) - ord('a') - rot) % 26 + ord('a'))
                    result += shifted if char.islower() else shifted.upper()
                else:
                    result += char

            # Check if result contains flag-like pattern
            if 'USCC' in result.upper():
                print(f"ROT{rot}: '{result}'")
        except Exception as e:
            print(f"ROT{rot} failed: {e}")

    # 4. Look for patterns that might be flag-like
    print("\n4. Looking for flag-like patterns:")
    # Look for USCC pattern
    uscc_pattern = re.findall(r'[A-Za-z]{4}', final_section)
    print(f"4-letter words: {uscc_pattern}")

    # Look for patterns that might be USCC with substitutions
    print("\n5. Substitution analysis:")
    # Notice patterns like g5BRR and g5oEJgs
    print("Repeated patterns:")
    patterns = {}
    for i in range(len(final_section) - 1):
        pair = final_section[i:i+2]
        if pair in patterns:
            patterns[pair] += 1
        else:
            patterns[pair] = 1

    sorted_patterns = sorted(patterns.items(), key=lambda x: x[1], reverse=True)
    print("Most common 2-char patterns:")
    for pattern, count in sorted_patterns[:10]:
        print(f"  '{pattern}': {count}")

    # Look for longer patterns
    print("\nLonger repeated patterns:")
    for length in range(3, 8):
        pattern_counts = {}
        for i in range(len(final_section) - length + 1):
            pattern = final_section[i:i+length]
            pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1

        repeated = {k: v for k, v in pattern_counts.items() if v > 1}
        if repeated:
            sorted_repeated = sorted(repeated.items(), key=lambda x: x[1], reverse=True)
            print(f"{length}-char patterns:")
            for pattern, count in sorted_repeated[:5]:
                print(f"  '{pattern}': {count}")

    # 6. Try to see if this is a simple substitution
    print("\n6. Character mapping analysis:")
    # The flag format is USCC{}, so let's see what characters could map to U, S, C, {, }
    print("Looking for character positions that might correspond to flag characters...")

    # Try to reverse engineer from the flag format
    # USCC{} is 6 characters, but our section is 47 characters, so maybe it's encoded

    # Look at the structure: vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs
    # Notice the spaces and separators

    parts = final_section.split()
    print(f"\n7. Split by spaces: {parts}")
    for i, part in enumerate(parts):
        print(f"  Part {i}: '{part}' (length {len(part)})")

if __name__ == "__main__":
    analyze_final_section()