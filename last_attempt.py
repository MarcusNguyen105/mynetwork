#!/usr/bin/env python3
"""
Last comprehensive attempt - try everything simple first
"""

def try_all_simple_shifts(ciphertext):
    """Try all possible simple shifts"""
    print("Trying all ROT shifts:")
    
    for shift in range(1, 26):
        result = ""
        for char in ciphertext:
            if char.isalpha():
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result += shifted
            else:
                result += char
        
        # Check for common English words or flag patterns
        upper_result = result.upper()
        if any(word in upper_result for word in ["CONGRATULATIONS", "WELL DONE", "GOOD JOB", "FLAG", "USCC", "SECRET", "CIPHER", "DECODED", "SOLVED", "CORRECT", "SUCCESS", "WINNER"]):
            print(f"ROT{shift}: {result}")
            print("*** POTENTIAL SOLUTION FOUND! ***")
            return result
        
        # Also check for common English patterns
        if "THE " in result or " AND " in result or "YOU " in result:
            print(f"ROT{shift} (has English words): {result[:100]}...")
    
    return None

def try_reverse_then_shift(ciphertext):
    """Try reversing then shifting"""
    print("\nTrying reverse + shift:")
    
    reversed_text = ciphertext[::-1]
    
    for shift in range(1, 26):
        result = ""
        for char in reversed_text:
            if char.isalpha():
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result += shifted
            else:
                result += char
        
        upper_result = result.upper()
        if any(word in upper_result for word in ["CONGRATULATIONS", "WELL DONE", "GOOD JOB", "FLAG", "USCC", "SECRET", "CIPHER", "DECODED", "SOLVED", "CORRECT", "SUCCESS", "WINNER"]):
            print(f"Reverse + ROT{shift}: {result}")
            print("*** POTENTIAL SOLUTION FOUND! ***")
            return result
    
    return None

def try_alternating_shifts(ciphertext):
    """Try alternating between two shifts"""
    print("\nTrying alternating shifts:")
    
    for shift1 in range(1, 13):
        for shift2 in range(shift1 + 1, 26):
            result = ""
            for i, char in enumerate(ciphertext):
                if char.isalpha():
                    shift = shift1 if i % 2 == 0 else shift2
                    shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                    result += shifted
                else:
                    result += char
            
            upper_result = result.upper()
            if any(word in upper_result for word in ["CONGRATULATIONS", "WELL DONE", "FLAG", "USCC", "SECRET"]):
                print(f"Alternating ROT{shift1}/{shift2}: {result}")
                print("*** POTENTIAL SOLUTION FOUND! ***")
                return result
    
    return None

def try_keyword_cipher_simple(ciphertext):
    """Try simple keyword cipher with common words"""
    print("\nTrying simple keyword substitution:")
    
    keywords = ["SECRET", "CIPHER", "USCC", "FLAG", "COMPETITION", "CYBER", "SECURITY"]
    
    for keyword in keywords:
        # Create substitution alphabet
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key_alphabet = ""
        used = set()
        
        # Add keyword letters first
        for char in keyword.upper():
            if char not in used and char.isalpha():
                key_alphabet += char
                used.add(char)
        
        # Add remaining letters
        for char in alphabet:
            if char not in used:
                key_alphabet += char
        
        # Decrypt
        result = ""
        for char in ciphertext:
            if char.isalpha():
                pos = key_alphabet.index(char)
                result += alphabet[pos]
            else:
                result += char
        
        upper_result = result.upper()
        if any(word in upper_result for word in ["CONGRATULATIONS", "WELL DONE", "FLAG", "USCC", "SECRET", "THE", "AND"]):
            print(f"Keyword '{keyword}': {result}")
            print("*** POTENTIAL SOLUTION FOUND! ***")
            return result
    
    return None

def try_reading_every_nth(ciphertext):
    """Try reading every nth character"""
    print("\nTrying to read every nth character:")
    
    for n in range(2, 20):
        for start in range(n):
            result = ""
            pos = start
            while pos < len(ciphertext):
                result += ciphertext[pos]
                pos += n
            
            if len(result) >= 10:  # Only check if we have enough characters
                upper_result = result.upper()
                if any(word in upper_result for word in ["FLAG", "USCC", "SECRET", "CONGRATULATIONS", "WELL", "DONE"]):
                    print(f"Every {n}th char starting at {start}: {result}")
                    print("*** POTENTIAL SOLUTION FOUND! ***")
                    return result
    
    return None

def try_simple_transposition(ciphertext):
    """Try simple transposition patterns"""
    print("\nTrying simple transposition:")
    
    # Try swapping adjacent pairs
    result = ""
    for i in range(0, len(ciphertext) - 1, 2):
        result += ciphertext[i + 1] + ciphertext[i]
    if len(ciphertext) % 2 == 1:
        result += ciphertext[-1]
    
    print(f"Swap adjacent pairs: {result[:80]}...")
    if any(word in result.upper() for word in ["FLAG", "USCC", "SECRET", "CONGRATULATIONS"]):
        print("*** POTENTIAL SOLUTION FOUND! ***")
        return result
    
    return None

def main():
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    print("FINAL COMPREHENSIVE ATTEMPT")
    print("=" * 60)
    print("Trying all simple approaches systematically...")
    print()
    
    # Try each method
    methods = [
        ("Simple ROT shifts", try_all_simple_shifts),
        ("Reverse + ROT", try_reverse_then_shift),
        ("Alternating shifts", try_alternating_shifts),
        ("Keyword cipher", try_keyword_cipher_simple),
        ("Every nth character", try_reading_every_nth),
        ("Simple transposition", try_simple_transposition)
    ]
    
    for method_name, method_func in methods:
        print(f"=== {method_name} ===")
        result = method_func(ciphertext)
        if result:
            print(f"\nSOLUTION FOUND with {method_name}:")
            print(result)
            
            # Check if it contains a flag format
            if "USCC{" in result or "FLAG{" in result:
                print("\nFlag format detected!")
                return result
            else:
                # Maybe we need to wrap it
                print(f"\nTrying to wrap in USCC{{}} format:")
                print(f"USCC{{{result}}}")
                return f"USCC{{{result}}}"
        print()
    
    print("No solution found with simple methods.")
    print("This may require a more complex approach or the cipher type is not standard.")
    
    return None

if __name__ == "__main__":
    result = main()
    if result:
        print(f"\n{'='*60}")
        print(f"FINAL ANSWER: {result}")
    else:
        print(f"\n{'='*60}")
        print("Unable to solve with current methods.")
        print("Consider: steganography, book cipher, or custom encoding.")