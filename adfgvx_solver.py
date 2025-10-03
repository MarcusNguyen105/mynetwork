#!/usr/bin/env python3
"""
Try ADFGVX cipher and other complex ciphers
"""

def adfgvx_decrypt_attempt(ciphertext, key1, key2):
    """
    Attempt ADFGVX decryption
    key1: substitution key (25 chars for 5x5 grid, excluding one letter like J)
    key2: transposition key
    """
    # ADFGVX uses only these 6 letters
    adfgvx_chars = "ADFGVX"
    
    # Check if ciphertext only contains ADFGVX characters
    if not all(c in adfgvx_chars for c in ciphertext):
        return None  # Not an ADFGVX cipher
    
    # This is a simplified attempt - full ADFGVX is quite complex
    return None

def four_square_decrypt_attempt(ciphertext, key1, key2):
    """Attempt Four Square cipher decryption"""
    # Four Square cipher works with pairs of letters
    if len(ciphertext) % 2 != 0:
        return None
    
    # This would require implementing the full Four Square algorithm
    return None

def playfair_decrypt(ciphertext, key):
    """Attempt Playfair cipher decryption"""
    def create_playfair_matrix(key):
        key = key.upper().replace('J', 'I')  # J and I share a cell
        matrix = []
        used = set()
        
        # Add key letters first
        for char in key:
            if char.isalpha() and char not in used:
                matrix.append(char)
                used.add(char)
        
        # Add remaining letters
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # No J
            if char not in used:
                matrix.append(char)
        
        # Convert to 5x5 matrix
        return [matrix[i:i+5] for i in range(0, 25, 5)]
    
    def find_position(matrix, char):
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == char:
                    return i, j
        return None, None
    
    def decrypt_pair(matrix, char1, char2):
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        
        if row1 is None or row2 is None:
            return char1 + char2
        
        if row1 == row2:  # Same row
            return matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:  # Same column
            return matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:  # Rectangle
            return matrix[row1][col2] + matrix[row2][col1]
    
    matrix = create_playfair_matrix(key)
    result = ""
    
    # Process pairs
    for i in range(0, len(ciphertext), 2):
        if i + 1 < len(ciphertext):
            pair = decrypt_pair(matrix, ciphertext[i], ciphertext[i+1])
            result += pair
        else:
            result += ciphertext[i]
    
    return result

def bifid_decrypt(ciphertext, key):
    """Attempt Bifid cipher decryption"""
    def create_polybius_square(key):
        key = key.upper().replace('J', 'I')
        square = []
        used = set()
        
        for char in key:
            if char.isalpha() and char not in used:
                square.append(char)
                used.add(char)
        
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in used:
                square.append(char)
        
        return [square[i:i+5] for i in range(0, 25, 5)]
    
    def char_to_coords(square, char):
        for i, row in enumerate(square):
            for j, cell in enumerate(row):
                if cell == char:
                    return i+1, j+1
        return None, None
    
    def coords_to_char(square, row, col):
        if 1 <= row <= 5 and 1 <= col <= 5:
            return square[row-1][col-1]
        return '?'
    
    square = create_polybius_square(key)
    
    # Convert to coordinates
    rows = []
    cols = []
    for char in ciphertext:
        if char.isalpha():
            r, c = char_to_coords(square, char.upper())
            if r and c:
                rows.append(r)
                cols.append(c)
    
    # Combine coordinates
    combined = rows + cols
    
    # Convert back to letters
    result = ""
    for i in range(0, len(combined), 2):
        if i + 1 < len(combined):
            char = coords_to_char(square, combined[i], combined[i+1])
            result += char
    
    return result

def main():
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    print("Trying Complex Cipher Types")
    print("=" * 50)
    
    # Check if it could be ADFGVX
    adfgvx_chars = set("ADFGVX")
    cipher_chars = set(ciphertext)
    
    print(f"Cipher uses characters: {sorted(cipher_chars)}")
    print(f"ADFGVX uses: {sorted(adfgvx_chars)}")
    
    if cipher_chars.issubset(adfgvx_chars):
        print("Could be ADFGVX cipher!")
    else:
        print("Not ADFGVX cipher (uses characters outside ADFGVX)")
    
    print()
    
    # Try Playfair cipher
    print("Trying Playfair cipher:")
    playfair_keys = ["SECRET", "CIPHER", "USCC", "FLAG", "COMPETITION", "CYBER", "SECURITY", "MYSTERY", "HIDDEN", "DECODE"]
    
    for key in playfair_keys:
        try:
            decrypted = playfair_decrypt(ciphertext, key)
            print(f"  Key '{key}': {decrypted[:80]}...")
            
            # Check for English patterns
            if any(word in decrypted.upper() for word in ["THE", "AND", "FLAG", "USCC", "SECRET", "CONGRATULATIONS"]):
                print(f"    *** POTENTIAL MATCH: {decrypted}")
        except Exception as e:
            print(f"  Key '{key}': Error - {e}")
    
    print()
    
    # Try Bifid cipher
    print("Trying Bifid cipher:")
    bifid_keys = ["SECRET", "CIPHER", "USCC", "FLAG", "KEY", "CODE"]
    
    for key in bifid_keys:
        try:
            decrypted = bifid_decrypt(ciphertext, key)
            print(f"  Key '{key}': {decrypted[:80]}...")
            
            if any(word in decrypted.upper() for word in ["THE", "AND", "FLAG", "USCC", "SECRET", "CONGRATULATIONS"]):
                print(f"    *** POTENTIAL MATCH: {decrypted}")
        except Exception as e:
            print(f"  Key '{key}': Error - {e}")
    
    print()
    
    # Try looking for steganography or hidden patterns
    print("Looking for hidden patterns:")
    
    # Try taking every nth character
    for n in [2, 3, 4, 5, 6, 8, 9, 12]:
        extracted = ""
        for i in range(0, len(ciphertext), n):
            extracted += ciphertext[i]
        print(f"  Every {n}th char: {extracted[:50]}...")
        
        if any(word in extracted.upper() for word in ["FLAG", "USCC", "SECRET"]):
            print(f"    *** FOUND PATTERN: {extracted}")
    
    # Try taking characters at specific positions
    print("\nTrying position-based extraction:")
    
    # Try first letter of each "word" if we split by certain patterns
    for split_char in ['J', 'X', 'Z']:
        if split_char in ciphertext:
            parts = ciphertext.split(split_char)
            first_letters = ''.join(part[0] if part else '' for part in parts)
            print(f"  First letters after '{split_char}': {first_letters}")

if __name__ == "__main__":
    main()