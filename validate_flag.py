#!/usr/bin/env python3

# The two potential flags we found
flag1 = "USCC{g5BRRZEogBoRoJogEg5oEJgs}"
flag2 = "USCC{t5OEEMRbtObEbWbtRt5bRWtf}"

def analyze_decoded_message():
    """Analyze the decoded message for clues about which flag is correct"""
    
    decoded_message = """C^8(#E|K^tU#=KuE#P(|8^=E#EK|PUK^(}^|#^|8=UK(Po]^Po|P^>(E8-}^|^}E3uE#tE^Uj^z}Eu-UqK|#-U](pE-^Po|P^>(E8-}^|^}E3uE#tE^Uj^z}Eu-UqK|#-U]^#u]OEK}^t|8tu8|PE-^F(Po^|^-(}tU#P(#uUu}^z(EtEF(}E^8(#E|K^E3u|P(U#*
ioE^]EPoU-^KEzKE}E#P}^U#E^Uj^PoE^U8-E}P^|#-^OE}Pqe#UF#^z}Eu-UK|#-U]^#u]OEK^=E#EK|PUK^|8=UK(Po]}*
ioE^PoEUK>^OEo(#-^PoE]^(}^KE8|P(.E8>^E|}>^PU^u#-EK}P|#-?^|#-^PoE>^|KE^E|}(8>^(]z8E]E#PE-^|#-^j|}P?^E}zEt(|88>^U#^tU]zuPEK^o|K-F|KE^Fo(to^t|#^zKU.(-E^]U-u8|K^|K(Po]EP(t^O>^}PUK|=EqO(P^PKu#t|P(U#*
x;c}^|KE^j|}P^|#-^KE3u(KE^](#(]|8^]E]UK>^vU#E^]U-u8Uq]^#u]OEK?^UjPE#^%_^UK^5W^O(P}/^PU^KEP|(#^}P|PE*
io(}^]|eE}^PoE]^.|8u|O8E^jUK^}(]u8|P(#=^]u8P(z8E^(#-EzE#-E#P^}PKE|]}*
x;c}^|KE^#UP^(#PE#-E-?^|#-^]u}P^#UP^OE^u}E-?^jUK^tK>zPU=K|zo(t^|zz8(t|P(U#}0^u}E^|^tK>zPU=K|zo(t|88>^}EtuKE^z}Eu-UK|#-U]^#u]OEK^=E#EK|PUK^jUK^}uto^|zz8(t|P(U#}*
C8PoUu=o^x;c}^o|.E^|^jEF^}zEt(j(t^FE|e#E}}E}?^]|#>^Uj^PoE(K^j8|F}^tU]E^jKU]^o|.(#=^PUU^}]|88^|^}P|PE*^ioE^j|tP^Po|P^zEUz8E^o|.E^OEE#^8u88E-^jUK^}U^]|#>^>E|K}^(#PU^u}(#=^PoE]^F(Po^}uto^}]|88^]U-u8(^t|#^OE^}EE#^|}^|^PE}P|]E#P^PU^}PKE#=Po^Uj^PoE^PEto#(3uE*^C^x;c^F(Po^8|K=E^E#Uu=o^}P|PE^t|#^z|}}^E.E#^}PK(#=E#P^}P|P(}P(t|8^PE}P}0^|^]U-u8Uq_^x;c^Fo(to^KEPuK#}^PoE^o(=o^%_^O(P}^z|}}E}^iE}P<g:Q}^D]|88;Ku}o^}u(PE?^|#-^|^R5qO(P^x;c^z|}}E}^PoE^]U}P^}PK(#=E#P^h(=;Ku}o^}u(PE*
ioE^j8|=^(}^<D;;)t5OEE% :%:_ MRb|tObEbWbtR t5bRWtf*"""
    
    print("=== Analyzing Decoded Message ===")
    
    # Clean up the message by replacing ^ with spaces
    clean_message = decoded_message.replace('^', ' ')
    print("Cleaned message:")
    print(clean_message)
    
    print("\n" + "="*50)
    
    # Look for key information
    if "linear" in clean_message.lower():
        print("✓ Message mentions 'linear' (linear congruential generator)")
    
    if "generator" in clean_message.lower():
        print("✓ Message mentions 'generator'")
    
    if "pseudorandom" in clean_message.lower():
        print("✓ Message mentions 'pseudorandom'")
    
    # The message seems to be about RNG/PRNG theory
    
def check_flag_formats():
    """Check which flag format makes more sense"""
    
    print("\n=== Flag Format Analysis ===")
    
    print(f"Flag 1: {flag1}")
    print(f"Flag 2: {flag2}")
    
    # Flag format should be USCC{...}
    # The content should be meaningful
    
    # Let's analyze the content of each flag
    content1 = flag1[5:-1]  # Remove USCC{ and }
    content2 = flag2[5:-1]  # Remove USCC{ and }
    
    print(f"\nFlag 1 content: {content1}")
    print(f"Flag 2 content: {content2}")
    
    # Check if either contains recognizable patterns
    # Flag content often contains readable words or meaningful patterns
    
    # The first flag has mixed case and numbers: g5BRRZEogBoRoJogEg5oEJgs
    # The second flag has mixed case and numbers: t5OEEMRbtObEbWbtRt5bRWtf
    
    # Neither looks immediately readable, but let's see if we can find patterns
    
    # Maybe we need to look at the structure differently
    # What if the numbers are separators?
    
    import re
    
    # Split by numbers
    parts1 = re.split(r'\d+', content1)
    parts2 = re.split(r'\d+', content2)
    
    print(f"\nFlag 1 parts (split by numbers): {[p for p in parts1 if p]}")
    print(f"Flag 2 parts (split by numbers): {[p for p in parts2 if p]}")

def final_decision():
    """Make a final decision on which flag to submit"""
    
    print("\n=== Final Decision ===")
    
    # Based on the analysis:
    # 1. We correctly identified the flag structure using substitution cipher
    # 2. We have two candidates based on whether to apply ROT13 to the content
    # 3. The decoded message is about linear congruential generators and RNGs
    
    # Let's think about this logically:
    # - The outer structure used substitution: < = U, Q = S, ; = C, ) = {, * = }
    # - The inner content might use a different cipher (ROT13) or might be as-is
    
    # Given that this is a crypto challenge about RNGs, and the flag format is USCC{...},
    # let's try both flags but lean towards the one that makes more cryptographic sense
    
    print("Based on the analysis:")
    print("1. The message is clearly about linear congruential generators (LCGs)")
    print("2. The flag structure USCC{...} was correctly identified")
    print("3. We have two candidates:")
    print(f"   - Original: {flag1}")
    print(f"   - ROT13:    {flag2}")
    
    print("\nRecommendation: Try both flags, starting with the ROT13 version")
    print("since the rest of the message used ROT13 for decoding.")
    
    return flag2, flag1

if __name__ == "__main__":
    analyze_decoded_message()
    check_flag_formats()
    primary_flag, secondary_flag = final_decision()
    
    print(f"\n🎯 PRIMARY FLAG TO TRY: {primary_flag}")
    print(f"🎯 SECONDARY FLAG TO TRY: {secondary_flag}")