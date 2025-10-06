#!/usr/bin/env python3

def try_vigenere_with_different_keys():
    """Try Vigenère with different keys"""
    
    print("=== VIGENÈRE WITH DIFFERENT KEYS ===")
    
    ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""
    
    # Try different keys
    keys = ['RANDOM', 'CUSTOM', 'GENERATOR', 'NUMBER', 'ENCRYPT', 'DECRYPT', 'MESSAGE', 'TEXT', 'DATA', 'INFO', 'CLUE', 'HINT', 'SOLUTION', 'ANSWER', 'FLAG', 'HACK', 'CODE', 'BREAK', 'CRACK', 'FIND', 'SOLVE']
    
    for key in keys:
        decrypted = try_vigenere_decrypt(ciphertext, key)
        
        # Look for flag pattern
        if 'USCC{' in decrypted:
            print(f"*** FLAG FOUND WITH KEY '{key}' ***")
            print(f"Decrypted: {decrypted}")
            return key, decrypted
        
        # Look for readable words
        words = decrypted.split()
        readable_words = []
        for word in words:
            clean_word = ''.join([c for c in word if c.isalpha()])
            if len(clean_word) > 2 and clean_word.isalpha():
                readable_words.append(clean_word)
        
        if len(readable_words) > 15:  # If we get many readable words
            print(f"Key '{key}': {len(readable_words)} readable words")
            print(f"Sample: {decrypted[:200]}...")
    
    return None, None

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

def try_different_cipher_types():
    """Try different cipher types"""
    
    print("\n=== DIFFERENT CIPHER TYPES ===")
    
    ciphertext = """P^8(#R|X^gH#=XhR#C(|8^=R#RX|CHX^(}^|#^|8=HX(Cb]^Cb|C^>(R8-}^|^}R3hR#gR^Hw^m}Rh-HdX|#-H](cR-^#h]BRX}^g|8gh8|CR-^S(Cb^|^-(}gH#C(#hHh}^m(RgRS(}R^8(#R|X^R3h|C(H#*
vbR^]RCbH-^XRmXR}R#C}^H#R^Hw^CbR^H8-R}C^|#-^BR}Cdr#HS#^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^|8=HX(Cb]}*
vbR^CbRHX>^BRb(#-^CbR]^(}^XR8|C(.R8>^R|}>^CH^h#-RX}C|#-?^|#-^CbR>^|XR^R|}(8>^(]m8R]R#CR-^|#-^w|}C?^R}mRg(|88>^H#^gH]mhCRX^b|X-S|XR^Sb(gb^g|#^mXH.(-R^]H-h8|X^|X(Cb]RC(g^B>^}CHX|=RdB(C^CXh#g|C(H#*
k;p}^|XR^w|}C^|#-^XR3h(XR^](#(]|8^]R]HX>^iH#R^]H-h8Hd]^#h]BRX?^HwCR#^%_^HX^5J^B(C}/^CH^XRC|(#^}C|CR*
vb(}^]|rR}^CbR]^.|8h|B8R^wHX^}(]h8|C(#=^]h8C(m8R^(#-RmR#-R#C^}CXR|]}*
k;p}^|XR^#HC^(#CR#-R-?^|#-^]h}C^#HC^BR^h}R-?^wHX^gX>mCH=X|mb(g^|mm8(g|C(H#}0^h}R^|^gX>mCH=X|mb(g|88>^}RghXR^m}Rh-HX|#-H]^#h]BRX^=R#RX|CHX^wHX^}hgb^|mm8(g|C(H#}*
P8CbHh=b^k;p}^b|.R^|^wRS^}mRg(w(g^SR|r#R}}R}?^]|#>^Hw^CbR(X^w8|S}^gH]R^wXH]^b|.(#=^CHH^}]|88^|^}C|CR*^vbR^w|gC^Cb|C^mRHm8R^b|.R^BRR#^8h88R-^wHX^}H^]|#>^>R|X}^(#CH^h}(#=^CbR]^S(Cb^}hgb^}]|88^]H-h8(^g|#^BR^}RR#^|}^|^CR}C|]R#C^CH^}CXR#=Cb^Hw^CbR^CRgb#(3hR*^P^k;p^S(Cb^8|X=R^R#Hh=b^}C|CR^g|#^m|}}^R.R#^}CX(#=R#C^}C|C(}C(g|8^CR}C}0^|^]H-h8Hd_^k;p^Sb(gb^XRChX#}^CbR^b(=b^%_^B(C}^m|}}R}^vR}C<t:D}^Q]|88;Xh}b^}h(CR?^|#-^|^E5dB(C^k;p^m|}}R}^CbR^]H}C^}CX(#=R#C^u(=;Xh}b^}h(CR*
vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs*"""
    
    # Try Atbash cipher
    print("Trying Atbash cipher...")
    atbash_result = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                atbash_result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                atbash_result += chr(ord('z') - (ord(char) - ord('a')))
        else:
            atbash_result += char
    
    if 'USCC' in atbash_result or 'flag' in atbash_result.lower():
        print(f"*** ATBASH SUCCESS ***")
        print(f"Atbash result: {atbash_result}")
        return atbash_result
    
    # Try ROT13
    print("Trying ROT13...")
    rot13_result = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                rot13_result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                rot13_result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            rot13_result += char
    
    if 'USCC' in rot13_result or 'flag' in rot13_result.lower():
        print(f"*** ROT13 SUCCESS ***")
        print(f"ROT13 result: {rot13_result}")
        return rot13_result
    
    return None

if __name__ == "__main__":
    # Try different approaches
    key, decrypted = try_vigenere_with_different_keys()
    if key:
        print(f"\n*** SOLUTION FOUND ***")
        print(f"Key: {key}")
        print(f"Decrypted message: {decrypted}")
    else:
        result = try_different_cipher_types()
        if result:
            print(f"\n*** CIPHER SUCCESS ***")
            print(f"Result: {result}")
        else:
            print("\nStill working on it...")