#!/usr/bin/env python3

def extract_flag():
    """Extract the flag from the decrypted text"""
    
    ciphertext = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"
    key = "SJ2"
    
    # Decrypt using Vigenère with key SJ2
    result = vigenere_decrypt(ciphertext, key)
    
    print(f"Decrypted text with key '{key}':")
    print(result)
    print()
    
    # Look for USCC and extract flag
    if 'USCC' in result:
        uscc_pos = result.find('USCC')
        print(f"Found 'USCC' at position {uscc_pos}")
        
        # Look for opening brace
        brace_start = result.find('{', uscc_pos)
        if brace_start != -1:
            print(f"Found opening brace at position {brace_start}")
            
            # Look for closing brace
            brace_end = result.find('}', brace_start)
            if brace_end != -1:
                print(f"Found closing brace at position {brace_end}")
                
                # Extract complete flag
                flag = result[uscc_pos:brace_end+1]
                print(f"\n*** COMPLETE FLAG FOUND: {flag} ***")
                return flag
            else:
                print("No closing brace found, looking for flag content...")
                # Maybe the flag doesn't have braces, let's look at the context
                flag_context = result[uscc_pos:uscc_pos+50]
                print(f"Flag context: {flag_context}")
        else:
            print("No opening brace found after USCC, looking for flag content...")
            flag_context = result[uscc_pos:uscc_pos+50]
            print(f"Flag context: {flag_context}")
    
    # Let's also check if there are braces elsewhere that might contain the flag content
    print(f"\nLooking for braces in the full text...")
    if '{' in result:
        brace_start = result.find('{')
        print(f"Found opening brace at position {brace_start}")
        if '}' in result:
            brace_end = result.find('}')
            print(f"Found closing brace at position {brace_end}")
            if brace_end > brace_start:
                potential_flag = result[brace_start-4:brace_end+1]  # Include some context before
                print(f"Potential flag with context: {potential_flag}")
    
    # Let's format what we have as a flag
    print(f"\nFormatting as flag...")
    
    # Find the part after USCC
    uscc_pos = result.find('USCC')
    if uscc_pos != -1:
        # Look for the next meaningful content
        flag_content = result[uscc_pos+4:uscc_pos+30]  # Get next 26 chars after USCC
        
        # Clean up the flag content - remove non-alphanumeric except common flag chars
        clean_content = ""
        for char in flag_content:
            if char.isalnum() or char in '_-':
                clean_content += char
        
        formatted_flag = f"USCC{{{clean_content}}}"
        print(f"Formatted flag attempt: {formatted_flag}")
        
        # Try different lengths
        for length in [10, 15, 20, 25, 30]:
            flag_content = result[uscc_pos+4:uscc_pos+4+length]
            clean_content = ""
            for char in flag_content:
                if char.isalnum() or char in '_-':
                    clean_content += char
            formatted_flag = f"USCC{{{clean_content}}}"
            print(f"Length {length}: {formatted_flag}")
    
    return None

def vigenere_decrypt(ciphertext, key):
    """Decrypt using Vigenère cipher"""
    result = ""
    key_upper = key.upper()
    key_len = len(key_upper)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = key_upper[i % key_len]
            shift = ord(key_char) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result += decrypted_char
        else:
            result += char
    
    return result

if __name__ == "__main__":
    flag = extract_flag()
    if flag:
        print(f"\n{'='*60}")
        print(f"FINAL FLAG: {flag}")
    else:
        print("\nFlag extraction needs manual review of the decrypted text.")