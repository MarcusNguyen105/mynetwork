#!/usr/bin/env python3

from enigma.machine import EnigmaMachine

def comprehensive_enigma_test():
    """Test all possible configurations more systematically"""
    
    # All day configurations from the codebook
    all_configs = {
        1: {'rotors': 'VIII II III', 'rings': '24 09 04', 'plugs': 'CY DQ EP FH GW JL NV OU RX SZ'},
        2: {'rotors': 'V IV II', 'rings': '18 25 15', 'plugs': 'AW CI DY EF GV HT JL KO NS UZ'},
        3: {'rotors': 'VII IV I', 'rings': '03 18 09', 'plugs': 'AJ CZ DL EO FK GS HW NU PR VX'},
        4: {'rotors': 'VIII VII VI', 'rings': '08 21 12', 'plugs': 'AU BW DX EI FJ HS KP MQ NV RT'},
        5: {'rotors': 'IV VII II', 'rings': '01 26 09', 'plugs': 'AG BM CW ER FJ IT KO PS UY VX'},
        6: {'rotors': 'V VI VII', 'rings': '18 01 24', 'plugs': 'AN CK DX FQ GL HY IU JR OZ PV'},
        7: {'rotors': 'II VI III', 'rings': '05 13 20', 'plugs': 'AQ CU DN ES GO IL JV MZ RX WY'},
        8: {'rotors': 'VIII II VI', 'rings': '12 02 23', 'plugs': 'AD BN CP EG HO JW KQ LX TY VZ'},
        9: {'rotors': 'IV III VI', 'rings': '15 08 13', 'plugs': 'AQ BI CL DM EV FK JP NS OZ TU'},
        10: {'rotors': 'VII VIII II', 'rings': '14 20 06', 'plugs': 'AR BO CF EK GM HZ JN PX QV WY'},
        11: {'rotors': 'II VI VIII', 'rings': '23 19 15', 'plugs': 'CQ DS EZ FL GJ HK MX NY OT PR'},
        12: {'rotors': 'II VI I', 'rings': '25 23 20', 'plugs': 'AG EM FY IX JO KR LU NW QS TZ'},
        13: {'rotors': 'VI I II', 'rings': '19 15 01', 'plugs': 'AN BL DR EO FQ GS HP IJ TY VW'},
        14: {'rotors': 'III VII IV', 'rings': '15 17 04', 'plugs': 'AD BO FK GI HW LY MP NS RX TZ'},
        15: {'rotors': 'III IV I', 'rings': '07 19 08', 'plugs': 'AN CS DY FT HZ IM JL OX QW RU'},
        16: {'rotors': 'II IV VII', 'rings': '09 02 19', 'plugs': 'AE BS CQ FU GX IT JV KL MW OR'},
        17: {'rotors': 'VI II IV', 'rings': '05 13 26', 'plugs': 'AO BS CQ DP EF GN JL KW TY UZ'},
        18: {'rotors': 'VIII VI VII', 'rings': '13 02 15', 'plugs': 'AT BV CJ DO EP FY GZ LW MQ NU'},
        19: {'rotors': 'II VII I', 'rings': '01 21 24', 'plugs': 'BH CM DU FP GL IO KT QY RW VX'},
        20: {'rotors': 'VIII IV VI', 'rings': '10 22 06', 'plugs': 'AR BN DI GP HQ KZ LU MS TX WY'},
        21: {'rotors': 'I VI II', 'rings': '13 06 10', 'plugs': 'AX BU CK EL GN HP IO JY MR QV'},
        22: {'rotors': 'VIII III VI', 'rings': '20 03 17', 'plugs': 'BD CP EH FO JW KX LU NQ RZ SV'},
        23: {'rotors': 'VII II I', 'rings': '19 23 08', 'plugs': 'AX BH CM DY FZ IJ KW LP QV RU'},
        24: {'rotors': 'IV III II', 'rings': '11 03 22', 'plugs': 'CH DU EX FZ JT KP LY MR OW QS'},
        25: {'rotors': 'IV V I', 'rings': '12 16 08', 'plugs': 'AL DV EX FP HN JU KS MR QY WZ'},
        26: {'rotors': 'VIII II IV', 'rings': '24 10 23', 'plugs': 'AX BZ CI DU FY GH KO LP MW NR'},
        27: {'rotors': 'VII IV VI', 'rings': '13 17 01', 'plugs': 'AB CJ DZ EL FM GY HX IK RU VW'},
        28: {'rotors': 'VII VI IV', 'rings': '13 21 12', 'plugs': 'AU CP DK HY IW JX MQ OZ RS TV'},
        29: {'rotors': 'V IV VIII', 'rings': '08 23 20', 'plugs': 'AS BW CF DT EM IZ JQ LV PY RU'},
        30: {'rotors': 'II VI VIII', 'rings': '20 12 15', 'plugs': 'AE BX CU DF HZ JO LS MN QY VW'},
    }
    
    ciphertext = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"
    
    # Test positions that might be relevant
    positions_to_try = ['GZV', 'DBR', 'AAA', 'ABC', 'XYZ']
    
    best_results = []
    
    print("Testing all day configurations...")
    
    for day in range(1, 31):
        if day not in all_configs:
            continue
            
        config = all_configs[day]
        
        for pos in positions_to_try:
            try:
                machine = EnigmaMachine.from_key_sheet(
                    rotors=config['rotors'],
                    reflector='B',
                    ring_settings=config['rings'],
                    plugboard_settings=config['plugs']
                )
                machine.set_display(pos)
                
                plaintext = machine.process_text(ciphertext)
                
                # Score the text based on English-like characteristics
                score = score_english_text(plaintext)
                
                if score > 5:  # Threshold for potentially readable text
                    best_results.append((day, pos, score, plaintext))
                    print(f"Day {day:2d}, Pos {pos}, Score {score:2d}: {plaintext[:50]}...")
                    
            except Exception as e:
                print(f"Error with day {day}, pos {pos}: {e}")
    
    # Sort by score and show best results
    best_results.sort(key=lambda x: x[2], reverse=True)
    
    print(f"\n{'='*60}")
    print("BEST RESULTS:")
    
    for day, pos, score, plaintext in best_results[:5]:
        print(f"\nDay {day}, Position {pos}, Score {score}")
        print(f"Text: {plaintext}")
        
        # Look for flag pattern
        if 'USCC' in plaintext or any(word in plaintext for word in ['FLAG', 'CIPHER', 'ENIGMA']):
            print("*** POTENTIAL FLAG FOUND! ***")

def score_english_text(text):
    """Score text based on English-like characteristics"""
    score = 0
    
    # Common English words
    common_words = ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'CAN', 'HER', 'WAS', 'ONE', 'OUR', 'HAD', 'USE', 'HAVE', 'WILL', 'BEEN', 'FROM', 'THEY', 'KNOW', 'WANT', 'BEEN', 'GOOD', 'MUCH', 'SOME', 'TIME', 'VERY', 'WHEN', 'COME', 'HERE', 'HOW', 'JUST', 'LIKE', 'LONG', 'MAKE', 'MANY', 'OVER', 'SUCH', 'TAKE', 'THAN', 'THEM', 'WELL', 'WERE']
    
    for word in common_words:
        if word in text:
            score += 3
    
    # Flag-related words
    flag_words = ['USCC', 'FLAG', 'CIPHER', 'ENIGMA', 'SECRET', 'CODE', 'MESSAGE']
    for word in flag_words:
        if word in text:
            score += 10
    
    # Common letter patterns
    common_patterns = ['TH', 'HE', 'IN', 'ER', 'AN', 'RE', 'ED', 'ND', 'ON', 'EN', 'AT', 'OU', 'IT', 'IS', 'OR', 'TI', 'AS', 'TO', 'NT', 'NG', 'SE', 'HA', 'VE', 'WA', 'LD', 'LE', 'ST', 'AR', 'TE', 'AL']
    
    for pattern in common_patterns:
        score += text.count(pattern) * 0.5
    
    # Penalize too many repeated characters
    for i in range(len(text) - 2):
        if text[i] == text[i+1] == text[i+2]:
            score -= 2
    
    return int(score)

if __name__ == "__main__":
    comprehensive_enigma_test()