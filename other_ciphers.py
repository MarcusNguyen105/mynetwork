#!/usr/bin/env python3

def try_other_ciphers():
    """Try other classical cipher types"""
    
    ciphertext = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"
    
    print("Trying other cipher types...")
    print(f"Ciphertext length: {len(ciphertext)}")
    
    # Try Playfair cipher with various keys
    print(f"\n{'='*50}")
    print("Trying Playfair-like approaches...")
    
    # Try Rail Fence cipher
    print(f"\n{'='*50}")
    print("Trying Rail Fence cipher...")
    
    for rails in range(2, 10):
        result = rail_fence_decrypt(ciphertext, rails)
        print(f"Rails {rails}: {result[:50]}...")
        if 'USCC' in result:
            print(f"*** USCC FOUND with {rails} rails! ***")
            print(f"Full result: {result}")
            if '{' in result and '}' in result:
                start = result.find('USCC')
                end = result.find('}', start) + 1
                flag = result[start:end]
                print(f"*** FLAG: {flag} ***")
                return flag
    
    # Try Columnar Transposition
    print(f"\n{'='*50}")
    print("Trying Columnar Transposition...")
    
    # Try different column numbers
    for cols in range(2, 12):
        if len(ciphertext) % cols == 0:  # Only try if it divides evenly
            result = columnar_transpose_decrypt(ciphertext, cols)
            print(f"Columns {cols}: {result[:50]}...")
            if 'USCC' in result:
                print(f"*** USCC FOUND with {cols} columns! ***")
                print(f"Full result: {result}")
                if '{' in result and '}' in result:
                    start = result.find('USCC')
                    end = result.find('}', start) + 1
                    flag = result[start:end]
                    print(f"*** FLAG: {flag} ***")
                    return flag
    
    # Try Polybius Square
    print(f"\n{'='*50}")
    print("Trying Polybius Square...")
    
    # Standard Polybius square (I/J combined)
    polybius = {
        'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
        'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24', 'K': '25',
        'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35',
        'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45',
        'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'
    }
    
    # Reverse mapping
    reverse_polybius = {v: k for k, v in polybius.items()}
    
    # Convert to numbers
    numbers = ""
    for char in ciphertext:
        if char in polybius:
            numbers += polybius[char]
    
    print(f"As Polybius numbers: {numbers[:50]}...")
    
    # Try to decode back (if even length)
    if len(numbers) % 2 == 0:
        polybius_result = ""
        for i in range(0, len(numbers), 2):
            pair = numbers[i:i+2]
            if pair in reverse_polybius:
                polybius_result += reverse_polybius[pair]
        
        print(f"Polybius decode: {polybius_result[:50]}...")
        if 'USCC' in polybius_result:
            print(f"*** USCC FOUND in Polybius! ***")
            print(f"Full result: {polybius_result}")
    
    # Try Four Square cipher (simplified approach)
    print(f"\n{'='*50}")
    print("Trying simple substitution ciphers...")
    
    # Try keyboard shift
    keyboard = "QWERTYUIOPASDFGHJKLZXCVBNM"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Map each letter to the next one on keyboard
    keyboard_result = ""
    for char in ciphertext:
        if char in alphabet:
            pos = alphabet.index(char)
            if pos < len(keyboard):
                keyboard_result += keyboard[pos]
            else:
                keyboard_result += char
        else:
            keyboard_result += char
    
    print(f"Keyboard shift: {keyboard_result[:50]}...")
    if 'USCC' in keyboard_result:
        print(f"*** USCC FOUND in keyboard shift! ***")
        print(f"Full result: {keyboard_result}")
    
    # Try Morse code interpretation (if applicable)
    print(f"\n{'='*50}")
    print("Trying other interpretations...")
    
    # Maybe the cipher is a simple book cipher using positions from the header
    # 1209 could be page 12, line 09, or position 1209
    
    # Try using the numbers from header as a key
    header_numbers = "120911"  # From 1209 and 111
    
    result = vigenere_decrypt(ciphertext, header_numbers)
    print(f"Header numbers as key: {result[:50]}...")
    if 'USCC' in result:
        print(f"*** USCC FOUND with header numbers! ***")
        print(f"Full result: {result}")
    
    # Try treating it as a simple substitution where each letter is shifted by its position
    print(f"\nTrying position-based shifts...")
    position_result = ""
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = i % 26  # Use position as shift
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            position_result += shifted
        else:
            position_result += char
    
    print(f"Position shifts: {position_result[:50]}...")
    if 'USCC' in position_result:
        print(f"*** USCC FOUND with position shifts! ***")
        print(f"Full result: {position_result}")
    
    return None

def rail_fence_decrypt(ciphertext, rails):
    """Decrypt Rail Fence cipher"""
    if rails == 1:
        return ciphertext
    
    # Create the rail pattern
    fence = [[None for _ in range(len(ciphertext))] for _ in range(rails)]
    
    # Mark positions
    rail = 0
    direction = 1
    
    for i in range(len(ciphertext)):
        fence[rail][i] = True
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    # Fill in the characters
    index = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if fence[r][c] and index < len(ciphertext):
                fence[r][c] = ciphertext[index]
                index += 1
    
    # Read off the result
    result = ""
    rail = 0
    direction = 1
    
    for i in range(len(ciphertext)):
        if fence[rail][i]:
            result += fence[rail][i]
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    return result

def columnar_transpose_decrypt(ciphertext, cols):
    """Decrypt Columnar Transposition cipher"""
    rows = len(ciphertext) // cols
    
    # Create grid
    grid = []
    index = 0
    
    for col in range(cols):
        column = []
        for row in range(rows):
            if index < len(ciphertext):
                column.append(ciphertext[index])
                index += 1
        grid.append(column)
    
    # Read row by row
    result = ""
    for row in range(rows):
        for col in range(cols):
            if row < len(grid[col]):
                result += grid[col][row]
    
    return result

def vigenere_decrypt(ciphertext, key):
    """Decrypt using Vigenère cipher"""
    if not key:
        return ciphertext
        
    result = ""
    key_upper = str(key).upper()
    key_len = len(key_upper)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = key_upper[i % key_len]
            if key_char.isalpha():
                shift = ord(key_char) - ord('A')
            else:
                shift = int(key_char) if key_char.isdigit() else 0
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result += decrypted_char
        else:
            result += char
    
    return result

if __name__ == "__main__":
    flag = try_other_ciphers()
    if flag:
        print(f"\n{'='*60}")
        print(f"CORRECT FLAG: {flag}")
    else:
        print("\nNeed to try more approaches...")