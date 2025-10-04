#!/usr/bin/env python3
"""
Stream Cipher Solver - Trying to solve based on the "custom random number generator" hint
"""

import string
import re
from collections import Counter
import itertools

# The encrypted message
encrypted = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

def extract_last_line(text):
    """Extract the last line properly"""
    lines = text.split('*')
    # Remove empty lines
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    if non_empty_lines:
        return non_empty_lines[-1]
    return ""

def try_stream_cipher(text, seed):
    """Try stream cipher with given seed"""
    import random
    random.seed(seed)
    
    result = ""
    for char in text:
        if char.isalpha():
            # Generate random shift
            shift = random.randint(0, 25)
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char
    
    return result

def try_lfsr_cipher(text, seed, taps):
    """Try Linear Feedback Shift Register cipher"""
    # Initialize LFSR
    lfsr = seed
    result = ""
    
    for char in text:
        if char.isalpha():
            # Generate next bit
            bit = lfsr & 1
            lfsr >>= 1
            
            # Apply feedback
            if bit:
                lfsr ^= taps
            
            # Use LFSR value as shift
            shift = lfsr % 26
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char
    
    return result

def try_custom_rng_cipher(text, seed, multiplier, increment, modulus):
    """Try custom random number generator cipher"""
    result = ""
    current = seed
    
    for char in text:
        if char.isalpha():
            # Generate next random number
            current = (current * multiplier + increment) % modulus
            
            # Use as shift
            shift = current % 26
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char
    
    return result

def analyze_numbers_in_text(text):
    """Analyze numbers in the text that might be keys or seeds"""
    print("=== NUMBER ANALYSIS ===")
    
    # Find all numbers
    numbers = re.findall(r'\d+', text)
    unique_numbers = list(set(numbers))
    print(f"Unique numbers found: {unique_numbers}")
    
    # Look for the number 750 (from challenge title)
    if '750' in text:
        print("Found '750' in text!")
    
    # Look for other significant numbers
    significant_numbers = []
    for num in unique_numbers:
        if len(num) >= 2:  # At least 2 digits
            significant_numbers.append(int(num))
    
    print(f"Significant numbers: {significant_numbers}")
    return significant_numbers

def try_different_cipher_approaches(text):
    """Try different cipher approaches"""
    print("\n=== TRYING DIFFERENT CIPHER APPROACHES ===")
    
    # Get significant numbers
    numbers = analyze_numbers_in_text(text)
    
    # Try stream cipher with different seeds
    print("\n1. Stream Cipher:")
    for seed in numbers[:10]:  # Try first 10 numbers
        result = try_stream_cipher(text, seed)
        if 'THE' in result or 'AND' in result or 'FOR' in result:
            print(f"  Seed {seed}: Found English words")
            print(f"    Sample: {result[:100]}...")
        
        # Check for flag pattern
        if 'USCC{' in result:
            print(f"  *** FOUND FLAG: {result} ***")
    
    # Try LFSR cipher
    print("\n2. LFSR Cipher:")
    # Common LFSR taps
    taps_list = [0x80000057, 0x80000062, 0x80000076, 0x8000007A]
    
    for seed in numbers[:5]:
        for taps in taps_list:
            result = try_lfsr_cipher(text, seed, taps)
            if 'THE' in result or 'AND' in result or 'FOR' in result:
                print(f"  Seed {seed}, Taps {hex(taps)}: Found English words")
                print(f"    Sample: {result[:100]}...")
            
            if 'USCC{' in result:
                print(f"  *** FOUND FLAG: {result} ***")
    
    # Try custom RNG cipher
    print("\n3. Custom RNG Cipher:")
    # Common LCG parameters
    lcg_params = [
        (1664525, 1013904223, 2**32),  # Common LCG
        (1103515245, 12345, 2**31),    # Another common LCG
        (134775813, 1, 2**32),         # Another common LCG
    ]
    
    for seed in numbers[:5]:
        for multiplier, increment, modulus in lcg_params:
            result = try_custom_rng_cipher(text, seed, multiplier, increment, modulus)
            if 'THE' in result or 'AND' in result or 'FOR' in result:
                print(f"  Seed {seed}, LCG({multiplier}, {increment}, {modulus}): Found English words")
                print(f"    Sample: {result[:100]}...")
            
            if 'USCC{' in result:
                print(f"  *** FOUND FLAG: {result} ***")

def try_simple_substitution(text):
    """Try simple substitution cipher"""
    print("\n=== SIMPLE SUBSTITUTION ===")
    
    # Try mapping the most frequent character to space
    freq = Counter(text)
    most_frequent = freq.most_common(1)[0][0]
    print(f"Most frequent character: '{most_frequent}' ({freq[most_frequent]} times)")
    
    # Try mapping it to space
    text_with_spaces = text.replace(most_frequent, ' ')
    print(f"With '{most_frequent}' as space: {text_with_spaces[:100]}...")
    
    # Try mapping it to 'E'
    text_with_e = text.replace(most_frequent, 'E')
    print(f"With '{most_frequent}' as 'E': {text_with_e[:100]}...")

def main():
    print("Stream Cipher Solver")
    print("=" * 50)
    
    # Extract last line
    last_line = extract_last_line(encrypted)
    print(f"Last line: '{last_line}'")
    
    # Try different cipher approaches
    try_different_cipher_approaches(encrypted)
    
    # Try simple substitution
    try_simple_substitution(encrypted)
    
    # Try on just the last line
    if last_line:
        print(f"\n=== TRYING ON LAST LINE ONLY ===")
        try_different_cipher_approaches(last_line)

if __name__ == "__main__":
    main()