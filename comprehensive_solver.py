#!/usr/bin/env python3

def try_vigenere_decrypt(ciphertext, key):
    """Try Vigenère decryption"""
    result = ""
    key_index = 0
    
    for char in ciphertext:
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

def analyze_key_length(ciphertext):
    """Analyze potential key lengths using Kasiski examination"""
    clean_text = ''.join([c for c in ciphertext if c.isalpha()])
    
    # Look for repeated 3-character sequences
    sequences = {}
    for i in range(len(clean_text) - 2):
        seq = clean_text[i:i+3]
        if seq in sequences:
            sequences[seq].append(i)
        else:
            sequences[seq] = [i]
    
    # Calculate distances between repeated sequences
    distances = []
    for seq, positions in sequences.items():
        if len(positions) > 1:
            for i in range(len(positions) - 1):
                distance = positions[i+1] - positions[i]
                distances.append(distance)
    
    # Find common factors
    if distances:
        from math import gcd
        from functools import reduce
        
        # Find GCD of all distances
        common_factor = reduce(gcd, distances)
        
        # Find factors of the GCD
        factors = []
        for i in range(2, min(common_factor + 1, 20)):
            if common_factor % i == 0:
                factors.append(i)
        
        return factors[:10]  # Return top 10 potential key lengths
    
    return []

def try_common_words_as_keys():
    """Try common words as Vigenère keys"""
    
    ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""
    
    # Common words that might be used as keys
    common_keys = [
        'KEY', 'CIPHER', 'SECRET', 'PASSWORD', 'CRYPTO', 'DECODE', 'SOLVE',
        'FLAG', 'HACK', 'CODE', 'BREAK', 'CRACK', 'FIND', 'SOLVE', 'ANSWER',
        'RANDOM', 'CUSTOM', 'GENERATOR', 'NUMBER', 'ENCRYPT', 'DECRYPT',
        'MESSAGE', 'TEXT', 'DATA', 'INFO', 'CLUE', 'HINT', 'SOLUTION'
    ]
    
    print("=== TRYING COMMON KEYS ===")
    
    for key in common_keys:
        decrypted = try_vigenere_decrypt(ciphertext, key)
        
        # Look for readable words
        words = decrypted.split()
        readable_words = []
        for word in words:
            clean_word = ''.join([c for c in word if c.isalpha()])
            if len(clean_word) > 2 and clean_word.isalpha():
                readable_words.append(clean_word)
        
        if len(readable_words) > 10:  # If we get several readable words
            print(f"\nKey '{key}':")
            print(f"Decrypted: {decrypted[:300]}...")
            print(f"Readable words: {readable_words[:10]}")
            
            # Look for flag pattern
            if 'USCC' in decrypted or 'flag' in decrypted.lower():
                print(f"*** POTENTIAL FLAG FOUND WITH KEY '{key}' ***")
                return key, decrypted
    
    return None, None

def try_key_length_analysis():
    """Try to find the key length and then brute force"""
    
    ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""
    
    print("=== KEY LENGTH ANALYSIS ===")
    
    potential_lengths = analyze_key_length(ciphertext)
    print(f"Potential key lengths: {potential_lengths}")
    
    # Try brute force with short keys
    print("\n=== BRUTE FORCE WITH SHORT KEYS ===")
    
    for length in [3, 4, 5, 6]:
        print(f"\nTrying keys of length {length}:")
        
        # Generate all possible keys of this length
        import itertools
        import string
        
        # Try common letter combinations
        common_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        # Try all combinations (this might be slow for longer keys)
        if length <= 4:
            for key_tuple in itertools.product(common_letters, repeat=length):
                key = ''.join(key_tuple)
                decrypted = try_vigenere_decrypt(ciphertext, key)
                
                # Look for flag pattern
                if 'USCC{' in decrypted:
                    print(f"*** FLAG FOUND WITH KEY '{key}' ***")
                    print(f"Decrypted: {decrypted}")
                    return key, decrypted
                
                # Look for readable text
                words = decrypted.split()
                readable_count = 0
                for word in words:
                    clean_word = ''.join([c for c in word if c.isalpha()])
                    if len(clean_word) > 2 and clean_word.isalpha():
                        readable_count += 1
                
                if readable_count > 15:  # If we get many readable words
                    print(f"Key '{key}': {readable_count} readable words")
                    print(f"Sample: {decrypted[:100]}...")
    
    return None, None

def try_end_pattern_decoding():
    """Try to decode just the end pattern which likely contains the flag"""
    
    print("\n=== END PATTERN DECODING ===")
    
    end_pattern = "<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"
    print(f"End pattern: {end_pattern}")
    
    # Try different interpretations
    # Maybe the flag is: USCC{...} and it's encoded as: <Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*
    
    # Let's try to map this systematically
    # If USCC{ maps to <Q;;), then:
    # U -> <, S -> Q, C -> ;, C -> ;, { -> )
    
    # Let's try to continue this pattern
    # Maybe the flag text is: ZEo|gBoRoJogE g5oEJgs
    
    flag_text = "ZEo|gBoRoJogE g5oEJgs"
    
    # Try different Caesar shifts on this part
    print(f"\nTrying Caesar shifts on flag text: {flag_text}")
    
    for shift in range(26):
        decoded = ""
        for char in flag_text:
            if char.isalpha():
                if char.isupper():
                    decoded += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    decoded += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                decoded += char
        
        # Look for meaningful text
        if 'flag' in decoded.lower() or 'key' in decoded.lower() or 'text' in decoded.lower():
            print(f"Shift {shift}: {decoded}")
            
            # If this looks like a flag, construct the full flag
            if 'flag' in decoded.lower():
                full_flag = f"USCC{{{decoded}}}"
                print(f"*** POTENTIAL FLAG: {full_flag} ***")
                return full_flag
    
    return None

if __name__ == "__main__":
    # Try different approaches
    key, decrypted = try_common_words_as_keys()
    if key:
        print(f"\n*** SOLUTION FOUND ***")
        print(f"Key: {key}")
        print(f"Decrypted message: {decrypted}")
    else:
        print("\nCommon keys didn't work, trying key length analysis...")
        key, decrypted = try_key_length_analysis()
        if key:
            print(f"\n*** SOLUTION FOUND ***")
            print(f"Key: {key}")
            print(f"Decrypted message: {decrypted}")
        else:
            print("\nTrying end pattern decoding...")
            flag = try_end_pattern_decoding()
            if flag:
                print(f"\n*** FLAG FOUND ***")
                print(f"Flag: {flag}")
            else:
                print("\nStill working on it...")