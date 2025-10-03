#!/usr/bin/env python3
"""
Exhaustive search for the correct Enigma settings
"""

from enigma.machine import EnigmaMachine

full_encrypted = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"

codebook = {
    30: ("II VI VIII", "20 12 15", "AE BX CU DF HZ JO LS MN QY VW", ["AZG", "IGN", "UKY", "YPL"]),
    12: ("II VI I", "25 23 20", "AG EM FY IX JO KR LU NW QS TZ", ["HNR", "PQV", "HMN", "GLW"]),
    20: ("VIII IV VI", "10 22 06", "AR BN DI GP HQ KZ LU MS TX WY", ["YGC", "WHF", "YDK", "UML"]),
    4: ("VIII VII VI", "08 21 12", "AU BW DX EI FJ HS KP MQ NV RT", ["ABF", "QON", "QDK", "CBR"]),
}

def check_readability(text):
    """Check if text looks like readable English"""
    common_words = ["THE", "AND", "THAT", "THIS", "HAVE", "WITH", "FROM", "WILL", "YOUR", "CONGRATULATIONS", "WELLDONE", "FLAG", "USCC"]
    score = sum(1 for word in common_words if word in text.upper())
    return score, [word for word in common_words if word in text.upper()]

print("Exhaustive search across multiple approaches:")
print("="*80)

best_score = 0
best_result = None

for day in codebook.keys():
    rotors, ring_settings, plugboard, kenngruppen = codebook[day]
    
    # Try all combinations of ground settings and message keys
    test_positions = kenngruppen + ["AAA", "GZV", "DBR", "WHF"]
    
    for ground in test_positions:
        for reflector in ["B", "C"]:
            # Approach 1: Direct decryption
            try:
                machine = EnigmaMachine.from_key_sheet(
                    rotors=rotors,
                    reflector=reflector,
                    ring_settings=ring_settings,
                    plugboard_settings=plugboard
                )
                machine.set_display(ground)
                text1 = machine.process_text(full_encrypted)
                score1, words1 = check_readability(text1)
                
                if score1 > best_score:
                    best_score = score1
                    best_result = (day, reflector, ground, "direct", text1, words1)
                    print(f"\nNew best: Day {day}, Ref={reflector}, Pos={ground}, Direct")
                    print(f"  Score={score1}, Words={words1}")
                    print(f"  Text: {text1[:80]}...")
            except:
                pass
            
            # Approach 2: With indicator procedure (first 6 letters)
            try:
                machine1 = EnigmaMachine.from_key_sheet(
                    rotors=rotors,
                    reflector=reflector,
                    ring_settings=ring_settings,
                    plugboard_settings=plugboard
                )
                machine1.set_display(ground)
                indicator = machine1.process_text(full_encrypted[:6])
                msg_key = indicator[:3]
                
                machine2 = EnigmaMachine.from_key_sheet(
                    rotors=rotors,
                    reflector=reflector,
                    ring_settings=ring_settings,
                    plugboard_settings=plugboard
                )
                machine2.set_display(msg_key)
                text2 = machine2.process_text(full_encrypted[6:])
                score2, words2 = check_readability(text2)
                
                if score2 > best_score:
                    best_score = score2
                    best_result = (day, reflector, ground, f"indicator, key={msg_key}", text2, words2)
                    print(f"\nNew best: Day {day}, Ref={reflector}, Ground={ground}, Key={msg_key}")
                    print(f"  Score={score2}, Words={words2}")
                    print(f"  Text: {text2[:80]}...")
            except:
                pass

print("\n" + "="*80)
if best_result:
    day, refl, pos, method, text, words = best_result
    print(f"\nBEST RESULT:")
    print(f"  Day: {day}")
    print(f"  Reflector: {refl}")
    print(f"  Method: {method}")
    print(f"  Position: {pos}")
    print(f"  Words found: {words}")
    print(f"  Full text: {text}")
else:
    print("\nNo good matches found")
