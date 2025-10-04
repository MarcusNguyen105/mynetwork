#!/usr/bin/env python3

def analyze_word_patterns(ciphertext):
    """Analyze the ciphertext for word-like patterns"""
    
    # Split by ^ which seems to be a separator
    segments = ciphertext.replace('\n', '').split('^')
    
    print("=== WORD-LIKE SEGMENTS (split by ^) ===")
    segment_lengths = {}
    for i, segment in enumerate(segments):
        if len(segment) > 0:
            length = len(segment)
            if length not in segment_lengths:
                segment_lengths[length] = []
            segment_lengths[length].append(segment)
    
    # Show segments by length
    for length in sorted(segment_lengths.keys()):
        segments_of_length = segment_lengths[length]
        print(f"\nLength {length} ({len(segments_of_length)} segments):")
        for segment in segments_of_length[:10]:  # Show first 10 of each length
            print(f"  '{segment}'")
        if len(segments_of_length) > 10:
            print(f"  ... and {len(segments_of_length) - 10} more")
    
    return segments

def try_pattern_matching(ciphertext):
    """Try to identify common English word patterns"""
    
    print("\n=== PATTERN MATCHING ===")
    
    # Look for patterns that might be common words
    # Common 2-letter words: of, to, in, it, is, be, as, at, so, we, he, by, or, on, do, if, me, my, up, an, go, no, us, am
    
    # Look for single characters that might be 'a' or 'I'
    single_chars = []
    segments = ciphertext.replace('\n', '').split('^')
    for segment in segments:
        if len(segment) == 1 and segment.isalpha():
            single_chars.append(segment)
    
    print("Single character segments (potential 'a' or 'I'):")
    from collections import Counter
    single_char_freq = Counter(single_chars)
    for char, count in single_char_freq.most_common():
        print(f"  '{char}': {count} times")
    
    # Look for 2-character segments
    two_chars = []
    for segment in segments:
        if len(segment) == 2 and segment.isalpha():
            two_chars.append(segment)
    
    print("\nTwo character segments (potential short words):")
    two_char_freq = Counter(two_chars)
    for char, count in two_char_freq.most_common(10):
        print(f"  '{char}': {count} times")

def analyze_repeated_sequences(ciphertext):
    """Look for longer repeated sequences that might be common words"""
    
    print("\n=== REPEATED SEQUENCES ===")
    
    clean_text = ciphertext.replace('\n', '').replace(' ', '')
    
    # Look for 4+ character repeated sequences
    sequences = {}
    for length in range(4, 8):
        for i in range(len(clean_text) - length + 1):
            seq = clean_text[i:i+length]
            if seq in sequences:
                sequences[seq] += 1
            else:
                sequences[seq] = 1
    
    # Show most common sequences
    common_seqs = sorted(sequences.items(), key=lambda x: x[1], reverse=True)
    for seq, count in common_seqs[:15]:
        if count > 1:
            print(f"'{seq}': {count} times")

def try_vigenere_analysis(ciphertext):
    """Try to analyze if this might be a Vigenère cipher"""
    
    print("\n=== VIGENÈRE ANALYSIS ===")
    
    clean_text = ciphertext.replace('\n', '').replace(' ', '')
    
    # Look for repeated patterns to find key length
    # This is a simplified approach - look for patterns that repeat at regular intervals
    
    for key_length in range(2, 20):
        # Check if characters at positions separated by key_length have similar frequencies
        positions = {}
        for i in range(key_length):
            positions[i] = []
        
        for i, char in enumerate(clean_text):
            positions[i % key_length].append(char)
        
        # Calculate frequency distribution for each position
        freq_diffs = []
        for pos in range(key_length):
            freq = {}
            for char in positions[pos]:
                freq[char] = freq.get(char, 0) + 1
            
            # Calculate how far this distribution is from uniform
            total = len(positions[pos])
            max_freq = max(freq.values()) if freq else 0
            freq_diffs.append(max_freq / total if total > 0 else 0)
        
        avg_freq_diff = sum(freq_diffs) / len(freq_diffs)
        if avg_freq_diff > 0.15:  # Threshold for non-uniform distribution
            print(f"Key length {key_length}: avg max frequency = {avg_freq_diff:.3f}")

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
    segments = analyze_word_patterns(ciphertext)
    try_pattern_matching(ciphertext)
    analyze_repeated_sequences(ciphertext)
    try_vigenere_analysis(ciphertext)