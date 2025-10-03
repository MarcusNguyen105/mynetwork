#!/usr/bin/env python3
"""
Extract the actual hash values from the obfuscated JavaScript
"""

import base64

# The arrays from the JavaScript
first_array = [
    'eulav eht ', 'table', '70390zHMDsK', 'object', '966028jCWdrH', 'function', 
    'log', '5YARiXg', 'Yzk1ZWU0Nz', '45JEiLUC', 'YzcwYzNlYj', '6631656436', 
    '863256EtMoYk', 'push', '6589810GTlrab', 'apply', '882245NXpbDV', '43312yxCGot', 
    '4373736qzQvCI', 'toString', 'warn', '6232', '8796768UCpcfR', 'length', 
    'parw dna ,', '3961373433', '3361326434', '11CsMkkl', 'exception', 'NzcyMmM2OW', 
    '3463383330', '31508QVFcbD', 'error', 'undefined', '({...}CCSU', 'alf dradna', 
    'ts eht ni ', 'Y4OWEwYWFl', 'c ,sehsah ', '40556232pbALNU', '736888mBECaR', 
    'shift', 'bind', 'k1MDI0NDY1', '__proto__', 'rehtegot s', '29ekpzDq', 'info', 
    '854YoyEjg', '66nVBDrR', 'console', '6134353334'
]

# The second array references (we need to map the hex indices)
second_array_items = [
    'IxZg==', 'eht kcarc', '9VFwNrg', '287AWNVHd', '6161343030', 'etanetacno', 
    '178842lPRJmm', '1392482zqhnOI', ') tamrof g'
]

# Based on the code pattern, we need to build:
# hash1 = _0x34b85e(0x1f3) + _0x34b85e(0x1fa) + _0x34b85e(0x1e2) + _0x34b85e(0x1f5) + _0x34b85e(0x1ed) + _0x34b85e(0x1f9) + _0x34b85e(0x1f8)
# hash2 = _0x34b85e(0x1fe) + _0x34b85e(0x1f7) + _0x34b85e(0x1f1) + _0x34b85e(0x1e7) + _0x34b85e(0x1e9) + _0x34b85e(0x1e6)

# The _0x34b85e function accesses the _0x32e5 array with offset adjustments
# We need to calculate the actual indices

def decode_base64_strings():
    """Try to decode base64 strings"""
    print("[*] Decoding base64 strings from arrays...")
    
    base64_candidates = ['Yzk1ZWU0Nz', 'YzcwYzNlYj', 'NzcyMmM2OW', 'Y4OWEwYWFl', 'k1MDI0NDY1', 'IxZg==']
    
    for b64 in base64_candidates:
        try:
            # Try adding padding if needed
            padded = b64 + '=' * (4 - len(b64) % 4)
            decoded = base64.b64decode(padded)
            print(f"[+] {b64} -> {decoded.hex()} (hex) -> {decoded}")
        except Exception as e:
            print(f"[-] Failed to decode {b64}: {e}")

def decode_hex_strings():
    """Decode hex strings"""
    print("\n[*] Decoding hex strings...")
    
    hex_strings = ['6631656436', '6232', '3961373433', '3361326434', '3463383330', '6161343030', '6134353334']
    
    decoded_hex = []
    for hex_str in hex_strings:
        try:
            decoded = bytes.fromhex(hex_str).decode('utf-8')
            decoded_hex.append(decoded)
            print(f"[+] {hex_str} -> {decoded}")
        except:
            print(f"[-] Failed to decode {hex_str}")
    
    return decoded_hex

def build_hashes():
    """Try to build the hash values based on the pattern"""
    print("\n[*] Building hash values...")
    
    # Based on the indices in the code, let's manually map them
    # The function calls with hex values need to be mapped to array indices
    
    # From the deobfuscated values, we have:
    # Several hex strings that decode to: f1ed6, b2, 9a743, 3a2d4, 4c830, aa400, a4534
    # Several base64 strings
    
    # Let's also check the specific indices referenced
    print("\n[*] Checking specific array values...")
    
    # The base64 strings that couldn't be decoded might need different handling
    special_b64 = ['Yzk1ZWU0Nz', 'YzcwYzNlYj', 'NzcyMmM2OW', 'Y4OWEwYWFl', 'k1MDI0NDY1']
    
    for b64 in special_b64:
        # These might be base64 encoded hex values
        try:
            decoded = base64.b64decode(b64 + '=').hex()
            print(f"[+] {b64} -> {decoded}")
        except:
            try:
                decoded = base64.b64decode(b64).hex()
                print(f"[+] {b64} -> {decoded}")
            except:
                pass

def main():
    print("="*60)
    print("Hash Extraction from Administrator Panel")
    print("="*60)
    
    decode_base64_strings()
    hex_values = decode_hex_strings()
    build_hashes()
    
    print("\n[!] Summary of decoded values:")
    print("Hex decoded values:", hex_values)
    
    print("\n[*] Based on the instruction, we need to:")
    print("1. Concatenate the hashes together")
    print("2. Crack the resulting value")
    print("3. Wrap in standard flag format (likely CCSU{...})")
    
    # Looking at the patterns, the hashes are likely built from these components
    print("\n[*] Possible hash components:")
    print("- f1ed6")
    print("- 9a743") 
    print("- 3a2d4")
    print("- 4c830")
    print("- aa400")
    print("- a4534")
    print("- b2")
    
    # Try different combinations
    print("\n[*] Trying hash combinations:")
    hash1 = "f1ed6" + "b2" + "9a743"
    hash2 = "3a2d4" + "4c830" + "aa400"
    combined = hash1 + hash2
    print(f"Hash1: {hash1}")
    print(f"Hash2: {hash2}")
    print(f"Combined: {combined}")

if __name__ == "__main__":
    main()