#!/usr/bin/env python3
"""
Investigate the J pattern more deeply
"""

def analyze_j_splits_detailed(ciphertext):
    """Detailed analysis of J-split patterns"""
    print("Detailed J-split analysis:")
    print("=" * 40)
    
    j_positions = [i for i, char in enumerate(ciphertext) if char == 'J']
    print(f"J positions: {j_positions}")
    
    parts = ciphertext.split('J')
    print(f"\nParts after splitting by J:")
    
    first_letters = ""
    for i, part in enumerate(parts):
        if part:
            print(f"  Part {i}: '{part}' (length: {len(part)}, first: '{part[0]}')")
            first_letters += part[0]
        else:
            print(f"  Part {i}: (empty)")
    
    print(f"\nFirst letters combined: '{first_letters}'")
    
    # Try treating this as a message
    if len(first_letters) >= 8:
        print(f"Could '{first_letters}' be a message?")
        
        # Try common cipher techniques on this shorter string
        print("\nTrying ciphers on the first letters:")
        
        # ROT cipher
        for rot in range(1, 26):
            decoded = ""
            for char in first_letters:
                if char.isalpha():
                    decoded += chr((ord(char) - ord('A') + rot) % 26 + ord('A'))
                else:
                    decoded += char
            
            if any(word in decoded for word in ["FLAG", "USCC", "THE", "AND", "SECRET", "WELL", "DONE", "GOOD"]):
                print(f"  ROT{rot}: {decoded} *** POTENTIAL MATCH ***")
            elif rot <= 5:  # Show first few anyway
                print(f"  ROT{rot}: {decoded}")
        
        # Try Atbash
        atbash = ""
        for char in first_letters:
            if char.isalpha():
                atbash += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                atbash += char
        print(f"  Atbash: {atbash}")
        
        # Try reversing
        print(f"  Reversed: {first_letters[::-1]}")
    
    return first_letters

def try_other_split_characters(ciphertext):
    """Try splitting by other characters"""
    print("\nTrying other split characters:")
    
    # Count frequency of each character
    char_freq = {}
    for char in ciphertext:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Try characters that appear multiple times
    for char, freq in sorted(char_freq.items(), key=lambda x: x[1], reverse=True):
        if freq > 2 and freq < 20:  # Not too common, not too rare
            parts = ciphertext.split(char)
            if len(parts) > 3:  # At least a few parts
                first_letters = ''.join(part[0] if part else '' for part in parts if part)
                print(f"  Split by '{char}' (freq: {freq}): first letters = '{first_letters}'")
                
                # Quick check for English patterns
                if len(first_letters) >= 6:
                    # Try ROT13 on this
                    rot13 = ""
                    for c in first_letters:
                        if c.isalpha():
                            rot13 += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
                        else:
                            rot13 += c
                    
                    if any(word in rot13 for word in ["FLAG", "USCC", "THE", "SECRET"]):
                        print(f"    ROT13 of first letters: {rot13} *** POTENTIAL MATCH ***")

def try_positional_extraction(ciphertext):
    """Try extracting characters at specific positions"""
    print("\nPositional extraction attempts:")
    
    # Try extracting every nth character starting from different positions
    for start in range(5):
        for step in range(2, 12):
            extracted = ""
            pos = start
            while pos < len(ciphertext):
                extracted += ciphertext[pos]
                pos += step
            
            if len(extracted) >= 8:
                # Check if this looks like a message
                if any(pattern in extracted.upper() for pattern in ["FLAG", "USCC", "THE", "SECRET", "WELL", "DONE"]):
                    print(f"  Start {start}, step {step}: {extracted} *** POTENTIAL MATCH ***")
                elif len(extracted) <= 20:  # Show shorter ones
                    print(f"  Start {start}, step {step}: {extracted}")

def try_matrix_approach(ciphertext):
    """Try arranging in a matrix and reading differently"""
    print("\nMatrix approach:")
    
    # Try different matrix dimensions
    length = len(ciphertext)
    factors = []
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            factors.append((i, length // i))
    
    print(f"Possible matrix dimensions: {factors[:5]}")  # Show first 5
    
    for rows, cols in factors[:3]:  # Try first 3
        print(f"\nTrying {rows}x{cols} matrix:")
        
        # Fill matrix row by row
        matrix = []
        for r in range(rows):
            row = ciphertext[r*cols:(r+1)*cols]
            matrix.append(row)
        
        # Read column by column
        column_reading = ""
        for c in range(cols):
            for r in range(rows):
                if c < len(matrix[r]):
                    column_reading += matrix[r][c]
        
        print(f"  Column reading: {column_reading[:80]}...")
        
        if any(word in column_reading.upper() for word in ["FLAG", "USCC", "THE", "SECRET"]):
            print(f"    *** POTENTIAL MATCH: {column_reading}")
        
        # Try reading diagonally
        diagonal = ""
        for i in range(min(rows, cols)):
            if i < len(matrix) and i < len(matrix[i]):
                diagonal += matrix[i][i]
        
        if len(diagonal) >= 6:
            print(f"  Diagonal: {diagonal}")

def main():
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    print("J-Pattern Deep Dive Analysis")
    print("=" * 60)
    
    # Analyze J splits in detail
    first_letters = analyze_j_splits_detailed(ciphertext)
    
    # Try other split characters
    try_other_split_characters(ciphertext)
    
    # Try positional extraction
    try_positional_extraction(ciphertext)
    
    # Try matrix approach
    try_matrix_approach(ciphertext)
    
    # Final attempt: maybe the solution is simpler
    print("\nFinal simple attempts:")
    
    # What if we just need to find a hidden word?
    # Look for common flag formats
    for i in range(len(ciphertext) - 4):
        if ciphertext[i:i+4] == "USCC":
            print(f"Found 'USCC' at position {i}")
        if ciphertext[i:i+4] == "FLAG":
            print(f"Found 'FLAG' at position {i}")
    
    # Try reading backwards
    backwards = ciphertext[::-1]
    for i in range(len(backwards) - 4):
        if backwards[i:i+4] == "USCC":
            print(f"Found 'USCC' in reverse at position {i}")
        if backwards[i:i+4] == "FLAG":
            print(f"Found 'FLAG' in reverse at position {i}")

if __name__ == "__main__":
    main()