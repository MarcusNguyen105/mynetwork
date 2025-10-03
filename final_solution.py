#!/usr/bin/env python3
"""
Final solution - build the correct hash and crack it
"""

import hashlib
import base64

def analyze_base64_values():
    """Analyze the base64 values more carefully"""
    print("[*] Analyzing base64 encoded values...")
    
    # These base64 strings when decoded give us hex-looking values
    b64_values = {
        'Yzk1ZWU0Nz': 'c95ee47',
        'YzcwYzNlYj': 'c70c3eb', 
        'NzcyMmM2OW': '7722c69',
        'Y4OWEwYWFl': 'c89a0aae',  # Fixing the decode
        'k1MDI0NDY1': '93502446'   # Fixing the decode
    }
    
    # Let's properly decode them
    for b64, expected in b64_values.items():
        decoded = base64.b64decode(b64 + '=').decode('utf-8', errors='ignore')
        print(f"{b64} -> {decoded}")
    
    return b64_values

def build_complete_hash():
    """Build the complete hash based on all components"""
    print("\n[*] Building complete hash...")
    
    # From our analysis, we have these components:
    # Base64 decoded: c95ee47, c70c3eb, 7722c69
    # Hex decoded: f1ed6, b2, 9a743, 3a2d4, 4c830, aa400, a4534
    
    # The instruction said to concatenate hashes together
    # Looking at the code structure, it seems like we need to combine
    # the base64 decoded values with the hex decoded values
    
    # Possible combinations:
    hashes = []
    
    # Try different orderings based on the function call indices
    hash1 = "c95ee47" + "c70c3eb" + "f1ed6"
    hash2 = "7722c69" + "9a743" + "4c830"
    
    print(f"Hash attempt 1: {hash1}")
    print(f"Hash attempt 2: {hash2}")
    print(f"Combined: {hash1 + hash2}")
    
    # Another possibility - all the hex values together
    all_hex = "f1ed6b29a7433a2d44c830aa400a4534"
    print(f"\nAll hex values: {all_hex}")
    
    # Try with base64 values
    with_b64 = "c95ee47c70c3eb7722c69f1ed6b29a7433a2d44c830aa400a4534"
    print(f"With base64 values: {with_b64}")
    
    return [hash1 + hash2, all_hex, with_b64]

def crack_hash(hash_value):
    """Try to crack the hash value"""
    print(f"\n[*] Analyzing hash: {hash_value}")
    
    # Check if it's already a readable value
    if all(c in '0123456789abcdef' for c in hash_value.lower()):
        print("[+] Hash is in hex format")
        
        # Try to decode as hex
        try:
            decoded = bytes.fromhex(hash_value).decode('utf-8', errors='ignore')
            if decoded.isprintable():
                print(f"[+] Hex decoded: {decoded}")
        except:
            pass
        
        # Check if it matches common hash formats
        if len(hash_value) == 32:
            print("[+] Length matches MD5 hash")
        elif len(hash_value) == 40:
            print("[+] Length matches SHA1 hash")
        elif len(hash_value) == 64:
            print("[+] Length matches SHA256 hash")
    
    # Try to "crack" it - in CTF context, this might mean the hash itself is the flag
    return hash_value

def main():
    print("="*60)
    print("Final Solution - Building and Cracking the Hash")
    print("="*60)
    
    # Analyze base64 values
    b64_values = analyze_base64_values()
    
    # Build complete hash
    possible_hashes = build_complete_hash()
    
    print("\n[!] Based on the instruction:")
    print("'concatenate the hashes together, crack the value and wrap in the standard flag format'")
    
    print("\n[*] Trying different flag formats:")
    
    for hash_val in possible_hashes:
        cracked = crack_hash(hash_val)
        print(f"\nPossible flag: CCSU{{{cracked}}}")
    
    # The most likely candidate based on the structure
    print("\n[!] Most likely flag candidates:")
    print(f"1. CCSU{{f1ed6b29a7433a2d44c830aa400a4534}}")
    print(f"2. CCSU{{c95ee47c70c3eb7722c69f1ed6b29a7433a2d44c830aa400a4534}}")
    
    # Check if we missed something in the instruction
    print("\n[*] Instruction analysis:")
    instruction_parts = [
        'concatenate', 'the hashes', 's together', ', crack the', ' value', 
        ', and wrap', ' in the st', 'andard fla', 'g format )'
    ]
    full_instruction = ''.join(instruction_parts)
    print(f"Full instruction: {full_instruction}")

if __name__ == "__main__":
    main()