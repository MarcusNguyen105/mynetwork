#!/usr/bin/env python3

def analyze_ciphertext(ciphertext):
    """Analyze the ciphertext for patterns and frequency"""
    
    # Remove whitespace and newlines for analysis
    clean_text = ciphertext.replace('\n', '').replace(' ', '')
    
    print("=== CIPHERTEXT ANALYSIS ===")
    print(f"Total length: {len(clean_text)}")
    print(f"Unique characters: {len(set(clean_text))}")
    print()
    
    # Character frequency analysis
    print("=== CHARACTER FREQUENCY ===")
    freq = {}
    for char in clean_text:
        freq[char] = freq.get(char, 0) + 1
    
    # Sort by frequency
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_freq:
        percentage = (count / len(clean_text)) * 100
        print(f"'{char}': {count} ({percentage:.1f}%)")
    
    print()
    
    # Look for repeated patterns
    print("=== REPEATED PATTERNS ===")
    patterns = {}
    for i in range(len(clean_text) - 2):
        pattern = clean_text[i:i+3]
        if pattern in patterns:
            patterns[pattern] += 1
        else:
            patterns[pattern] = 1
    
    # Show most common 3-character patterns
    common_patterns = sorted(patterns.items(), key=lambda x: x[1], reverse=True)[:10]
    for pattern, count in common_patterns:
        if count > 1:
            print(f"'{pattern}': {count} times")
    
    print()
    
    # Look for potential word boundaries (common separators)
    print("=== POTENTIAL SEPARATORS ===")
    separators = ['^', '#', '(', ')', '|', '}', '{', '[', ']', '-', '=', '>', '<']
    for sep in separators:
        count = clean_text.count(sep)
        if count > 0:
            print(f"'{sep}': {count} occurrences")
    
    return clean_text, freq

def try_simple_substitution(ciphertext, key_mapping):
    """Try a simple substitution cipher with given mapping"""
    result = ""
    for char in ciphertext:
        if char in key_mapping:
            result += key_mapping[char]
        else:
            result += char
    return result

# The ciphertext from the problem
ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""

if __name__ == "__main__":
    clean_text, freq = analyze_ciphertext(ciphertext)
    
    print("\n=== ATTEMPTING DECRYPTION ===")
    
    # Based on frequency analysis, let's try some common mappings
    # Looking at the most frequent characters and common English letter frequencies
    
    # Common English letter frequencies: E, T, A, O, I, N, S, H, R, D, L, C, U, M, W, F, G, Y, P, B, V, K, J, X, Q, Z
    
    # Let's try mapping the most frequent characters to common English letters
    # This is a starting point - we'll need to adjust based on results
    
    print("Attempting frequency-based substitution...")
    
    # Let's try a different approach - look for patterns that might be common words
    print("\nLooking for potential 'THE' patterns...")
    
    # Look for 3-character patterns that might be 'THE'
    for i in range(len(clean_text) - 2):
        pattern = clean_text[i:i+3]
        if pattern in ['^|#', '^|8', '^|X', '^|C']:  # Common patterns we see
            print(f"Potential 'THE' at position {i}: '{pattern}'")