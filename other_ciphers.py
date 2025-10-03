#!/usr/bin/env python3
"""
Try other cipher types
"""

def rail_fence_decrypt(ciphertext, rails):
    """Decrypt rail fence cipher"""
    if rails == 1:
        return ciphertext
    
    fence = [[None for _ in range(len(ciphertext))] for _ in range(rails)]
    
    # Mark the positions
    rail = 0
    direction = 1
    for i in range(len(ciphertext)):
        fence[rail][i] = True
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    # Fill the fence with ciphertext
    index = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if fence[r][c]:
                fence[r][c] = ciphertext[index]
                index += 1
    
    # Read the message
    result = ""
    rail = 0
    direction = 1
    for i in range(len(ciphertext)):
        result += fence[rail][i]
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    return result

def columnar_transposition_decrypt(ciphertext, key):
    """Decrypt columnar transposition cipher"""
    key = key.upper()
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    
    cols = len(key)
    rows = len(ciphertext) // cols
    if len(ciphertext) % cols != 0:
        rows += 1
    
    # Create matrix
    matrix = [[''] * cols for _ in range(rows)]
    
    # Fill matrix column by column in key order
    index = 0
    for col_idx in key_order:
        for row in range(rows):
            if index < len(ciphertext):
                matrix[row][col_idx] = ciphertext[index]
                index += 1
    
    # Read row by row
    result = ""
    for row in range(rows):
        for col in range(cols):
            result += matrix[row][col]
    
    return result.rstrip()

def simple_substitution_decrypt(ciphertext, key_mapping):
    """Decrypt simple substitution cipher"""
    result = ""
    for char in ciphertext:
        if char.upper() in key_mapping:
            result += key_mapping[char.upper()]
        else:
            result += char
    return result

def main():
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    print("Trying other cipher types:")
    print("=" * 50)
    
    # Try rail fence cipher
    print("Rail Fence Cipher:")
    for rails in range(2, 8):
        decrypted = rail_fence_decrypt(ciphertext, rails)
        print(f"  {rails} rails: {decrypted[:80]}...")
        if any(word in decrypted.upper() for word in ["THE", "AND", "FLAG", "USCC", "SECRET"]):
            print(f"    *** POTENTIAL MATCH: {decrypted}")
    print()
    
    # Try columnar transposition
    print("Columnar Transposition:")
    keys = ["FLAG", "USCC", "SECRET", "CIPHER", "KEY", "CODE"]
    for key in keys:
        try:
            decrypted = columnar_transposition_decrypt(ciphertext, key)
            print(f"  Key '{key}': {decrypted[:80]}...")
            if any(word in decrypted.upper() for word in ["THE", "AND", "FLAG", "USCC", "SECRET"]):
                print(f"    *** POTENTIAL MATCH: {decrypted}")
        except:
            pass
    print()
    
    # Try simple substitution with common patterns
    print("Simple Substitution (frequency analysis):")
    # Most common letters in English: ETAOINSHRDLCUMWFGYPBVKJXQZ
    # Most common letters in ciphertext (from earlier analysis): NJMIEROFAT
    
    # Try mapping most frequent cipher letters to most frequent English letters
    cipher_freq = "NJMIEROFAT"
    english_freq = "ETAOINSHRD"
    
    mapping = {}
    for i in range(min(len(cipher_freq), len(english_freq))):
        mapping[cipher_freq[i]] = english_freq[i]
    
    decrypted = simple_substitution_decrypt(ciphertext, mapping)
    print(f"  Frequency mapping: {decrypted[:80]}...")
    if any(word in decrypted.upper() for word in ["THE", "AND", "FLAG", "USCC", "SECRET"]):
        print(f"    *** POTENTIAL MATCH: {decrypted}")
    print()
    
    # Try reverse cipher
    print("Reverse Cipher:")
    reversed_text = ciphertext[::-1]
    print(f"  Reversed: {reversed_text[:80]}...")
    print()
    
    # Try splitting the text and looking for patterns
    print("Pattern Analysis:")
    print(f"Length: {len(ciphertext)}")
    print(f"Length factors: {[i for i in range(1, 21) if len(ciphertext) % i == 0]}")
    
    # Try splitting into chunks and see if there are patterns
    for chunk_size in [2, 3, 4, 6, 8, 12]:
        if len(ciphertext) % chunk_size == 0:
            chunks = [ciphertext[i:i+chunk_size] for i in range(0, len(ciphertext), chunk_size)]
            unique_chunks = set(chunks)
            print(f"  {chunk_size}-char chunks: {len(chunks)} total, {len(unique_chunks)} unique")
            if len(unique_chunks) < len(chunks) * 0.8:  # If many repeats
                print(f"    Repeated chunks found!")
    
    # Since we know the repeat distance is 72, try treating it as a block cipher
    print("\nBlock analysis (72-char blocks):")
    if len(ciphertext) >= 144:  # At least 2 blocks
        block1 = ciphertext[:72]
        block2 = ciphertext[72:144]
        print(f"Block 1: {block1}")
        print(f"Block 2: {block2}")
        
        # Look for differences
        differences = []
        for i in range(min(len(block1), len(block2))):
            if block1[i] != block2[i]:
                differences.append(i)
        print(f"Differences at positions: {differences[:10]}...")  # Show first 10

if __name__ == "__main__":
    main()