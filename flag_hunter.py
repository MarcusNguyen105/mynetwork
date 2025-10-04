#!/usr/bin/env python3

def analyze_end_pattern(ciphertext):
    """Analyze the end of the ciphertext which might contain the flag"""
    
    print("=== END PATTERN ANALYSIS ===")
    
    # Get the last part of the ciphertext
    lines = ciphertext.strip().split('\n')
    last_line = lines[-1]
    print(f"Last line: '{last_line}'")
    
    # Look for patterns that might be USCC{...}
    # The pattern seems to be: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    
    # Let's try to see if this is a simple substitution
    # Looking at the pattern, it seems like there might be some readable text
    
    # Let's try different approaches to decode this part
    print("\nTrying different decoding approaches...")
    
    # Approach 1: Simple character shift
    print("\n1. Character shift analysis:")
    for shift in range(1, 26):
        decoded = ""
        for char in last_line:
            if char.isalpha():
                if char.isupper():
                    decoded += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    decoded += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                decoded += char
        if 'USCC' in decoded or 'flag' in decoded.lower() or 'ctf' in decoded.lower():
            print(f"  Shift {shift}: {decoded}")
    
    # Approach 2: Look for the flag pattern more directly
    print("\n2. Direct pattern matching:")
    
    # The pattern looks like it might be: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    # Let's try to map characters that might make sense
    
    # If this is USCC{...}, let's see what the mapping might be
    # U -> <, S -> Q, C -> ;, C -> ;, { -> ), etc.
    
    potential_mapping = {
        '<': 'U',
        'Q': 'S', 
        ';': 'C',
        ')': '{',
        'g': 'f',
        '5': 'l',
        'B': 'a',
        'R': 'g',
        '%': '}',
        ':': ' ',
        '_': ' ',
        'Z': 'T',
        'E': 'h',
        'o': 'e',
        '|': ' ',
        'J': 'k',
        's': 'y',
        '*': ''
    }
    
    decoded_end = ""
    for char in last_line:
        if char in potential_mapping:
            decoded_end += potential_mapping[char]
        else:
            decoded_end += char
    
    print(f"  Potential decoded end: '{decoded_end}'")

def try_vigenere_decrypt(ciphertext, key):
    """Try to decrypt using Vigenère cipher with given key"""
    
    clean_text = ciphertext.replace('\n', '').replace(' ', '').replace('^', ' ')
    
    result = ""
    key_index = 0
    
    for char in clean_text:
        if char.isalpha():
            if char.isupper():
                shift = ord(key[key_index % len(key)].upper()) - ord('A')
                decrypted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                result += decrypted
            else:
                shift = ord(key[key_index % len(key)].lower()) - ord('a')
                decrypted = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                result += decrypted
            key_index += 1
        else:
            result += char
    
    return result

def analyze_full_cipher(ciphertext):
    """Try to analyze the full cipher with different approaches"""
    
    print("\n=== FULL CIPHER ANALYSIS ===")
    
    # Let's try some common keys for Vigenère
    common_keys = ['KEY', 'CIPHER', 'SECRET', 'PASSWORD', 'CRYPTO', 'DECODE', 'SOLVE']
    
    print("Trying common Vigenère keys:")
    for key in common_keys:
        decrypted = try_vigenere_decrypt(ciphertext, key)
        # Look for readable words
        words = decrypted.split()
        readable_words = [w for w in words if len(w) > 2 and w.isalpha()]
        if len(readable_words) > 5:  # If we get several readable words
            print(f"\nKey '{key}':")
            print(f"  {decrypted[:200]}...")
            print(f"  Readable words found: {len(readable_words)}")

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
    analyze_end_pattern(ciphertext)
    analyze_full_cipher(ciphertext)