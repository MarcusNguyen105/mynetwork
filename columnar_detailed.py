#!/usr/bin/env python3
"""
Detailed columnar transposition analysis
"""

def columnar_transposition_decrypt(ciphertext, key):
    """Decrypt columnar transposition cipher"""
    key = key.upper()
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    
    cols = len(key)
    rows = len(ciphertext) // cols
    remainder = len(ciphertext) % cols
    
    # Create matrix
    matrix = [[''] * cols for _ in range(rows + (1 if remainder > 0 else 0))]
    
    # Fill matrix column by column in key order
    index = 0
    for col_idx in key_order:
        col_height = rows + (1 if col_idx < remainder else 0)
        for row in range(col_height):
            if index < len(ciphertext):
                matrix[row][col_idx] = ciphertext[index]
                index += 1
    
    # Read row by row
    result = ""
    for row in range(len(matrix)):
        for col in range(cols):
            if matrix[row][col]:
                result += matrix[row][col]
    
    return result.rstrip()

def is_readable_english(text):
    """Check if text contains readable English patterns"""
    text = text.upper()
    
    # Common English words
    common_words = [
        "THE", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL", "CAN", "HER", 
        "WAS", "ONE", "OUR", "HAD", "BY", "UP", "DO", "NO", "IF", "MY", "HE", 
        "AS", "TO", "GO", "WE", "AM", "IS", "OR", "BE", "IT", "IN", "AT", "ON", 
        "SO", "US", "AN", "OF", "FLAG", "USCC", "CONGRATULATIONS", "WELL", 
        "DONE", "GOOD", "JOB", "FOUND", "SOLVED", "CORRECT", "SECRET", "CIPHER", 
        "DECODE", "HIDDEN", "MYSTERY", "CHALLENGE", "COMPETITION", "CYBER", 
        "SECURITY", "CTF"
    ]
    
    # Common English patterns
    common_patterns = ["TH", "ER", "ON", "AN", "RE", "HE", "IN", "ED", "ND", "HA", "AT", "EN", "ES", "OF", "OR", "NT", "EA", "TI", "TO", "IT", "ST", "IO", "LE", "IS", "OU", "AR", "AS", "DE", "RT", "VE"]
    
    words = text.split()
    if len(words) < 2:
        return False, 0
    
    # Count common words
    word_score = sum(1 for word in words[:20] if word in common_words)
    
    # Count common patterns
    pattern_score = sum(1 for pattern in common_patterns if pattern in text)
    
    total_score = word_score * 3 + pattern_score  # Weight words more heavily
    
    return total_score > 5, total_score

def main():
    ciphertext = "JJIFETMTOJTHXRJLNNFMYKCDNXECRDGAJGSOAQZHCOTJAMMDNEOCWVGHZVHOXMMFJSSIGBGKNIRIXVMTOJTUAXNSNNFEUKCMYWROXAIFANWILKRWVSEFEPISRGFTMRUDHBLMRIELUVADLAUDUBIONLESJJEDXRUFWKNK"
    
    print("Detailed Columnar Transposition Analysis")
    print("=" * 60)
    
    # Try various keys
    keys_to_try = [
        # Competition related
        "USCC", "CTF", "FLAG", "CYBER", "SECURITY", "COMPETITION",
        
        # Common cipher keys
        "SECRET", "CIPHER", "DECODE", "HIDDEN", "MYSTERY", "PUZZLE",
        "KEY", "CODE", "PASS", "WORD", "CRYPTO",
        
        # Based on hint
        "NAME", "MYNAME", "SECRETS", "KNOW", "JUST", "BECAUSE",
        
        # Try some longer keys
        "SECRETKEY", "FLAGKEY", "USCCFLAG", "CIPHERKEY", "MYSTERYKEY",
        
        # Try some names
        "ALICE", "BOB", "CHARLIE", "DAVID", "EVE"
    ]
    
    best_results = []
    
    for key in keys_to_try:
        try:
            decrypted = columnar_transposition_decrypt(ciphertext, key)
            is_readable, score = is_readable_english(decrypted)
            
            print(f"Key '{key}' (len {len(key)}):")
            print(f"  Score: {score}")
            print(f"  Text: {decrypted[:100]}...")
            
            if is_readable or score > 3:
                print(f"  *** HIGH SCORE! ***")
                best_results.append((key, decrypted, score))
                print(f"  Full text: {decrypted}")
            
            print()
            
        except Exception as e:
            print(f"Key '{key}': Error - {e}")
            print()
    
    # Show best results
    if best_results:
        print("\nBEST RESULTS:")
        print("=" * 40)
        best_results.sort(key=lambda x: x[2], reverse=True)
        
        for key, text, score in best_results[:5]:  # Top 5
            print(f"Key '{key}' (Score: {score}):")
            print(f"  {text}")
            print()
            
            # Check for flag format
            if "USCC{" in text or "FLAG{" in text:
                print(f"  *** FOUND FLAG FORMAT! ***")
                return text
    
    return None

if __name__ == "__main__":
    result = main()
    if result:
        print(f"\nFINAL ANSWER: {result}")
    else:
        print("\nNo clear solution found with columnar transposition.")