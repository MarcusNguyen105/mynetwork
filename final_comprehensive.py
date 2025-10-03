#!/usr/bin/env python3

from enigma.machine import EnigmaMachine

def final_comprehensive():
    """Final comprehensive attempt with all possible interpretations"""
    
    ciphertext = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"
    
    print("Final comprehensive attempt...")
    print("Trying all possible date interpretations and procedures...")
    
    # All possible date interpretations
    # 1209 could be:
    # - December 9th (day 9)
    # - September 12th (day 12) 
    # - Day 12, month 09
    # - Or even a different interpretation
    
    # Let me try ALL days from the codebook systematically
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
    
    # Try every possible combination more systematically
    positions_to_try = [
        'GZV', 'DBR', 'AAA', 'ABC', 'XYZ', 'QWE', 'ASD', 'ZXC',
        'SJT', 'SJB', 'SJC', 'SJD', 'SJE', 'SJF', 'SJG', 'SJH', 'SJI', 'SJJ', 'SJK', 'SJL', 'SJM', 'SJN', 'SJO', 'SJP', 'SJQ', 'SJR', 'SJS', 'SJU', 'SJV', 'SJW', 'SJX', 'SJY', 'SJZ'
    ]
    
    print(f"Testing {len(all_configs)} days with {len(positions_to_try)} positions...")
    
    for day in range(1, 31):
        if day not in all_configs:
            continue
            
        config = all_configs[day]
        
        for pos in positions_to_try:
            # Try with plugboard
            try:
                machine = EnigmaMachine.from_key_sheet(
                    rotors=config['rotors'],
                    reflector='B',
                    ring_settings=config['rings'],
                    plugboard_settings=config['plugs']
                )
                machine.set_display(pos)
                
                plaintext = machine.process_text(ciphertext)
                
                # Check for complete flag
                if 'USCC{' in plaintext and '}' in plaintext:
                    start = plaintext.find('USCC{')
                    end = plaintext.find('}', start) + 1
                    flag = plaintext[start:end]
                    print(f"*** COMPLETE FLAG FOUND! ***")
                    print(f"Day: {day}, Position: {pos}, Plugboard: Yes")
                    print(f"FLAG: {flag}")
                    print(f"Full text: {plaintext}")
                    return flag
                
                # Check for readable English text that might contain the flag
                if contains_english_words(plaintext):
                    print(f"Day {day}, Pos {pos}, Plugs: Contains English - {plaintext[:50]}...")
                    if 'USCC' in plaintext:
                        print(f"  -> Also contains USCC!")
                        uscc_pos = plaintext.find('USCC')
                        context = plaintext[uscc_pos:uscc_pos+40]
                        print(f"  -> Context: {context}")
                        
                        # Try to manually construct flag
                        after_uscc = plaintext[uscc_pos+4:]
                        clean_content = ""
                        for char in after_uscc:
                            if char.isalnum():
                                clean_content += char
                            else:
                                break
                        
                        if len(clean_content) >= 10:
                            manual_flag = f"USCC{{{clean_content}}}"
                            print(f"  -> Manual flag: {manual_flag}")
                
            except Exception as e:
                continue
            
            # Try without plugboard
            try:
                machine = EnigmaMachine.from_key_sheet(
                    rotors=config['rotors'],
                    reflector='B',
                    ring_settings=config['rings'],
                    plugboard_settings=''
                )
                machine.set_display(pos)
                
                plaintext = machine.process_text(ciphertext)
                
                # Check for complete flag
                if 'USCC{' in plaintext and '}' in plaintext:
                    start = plaintext.find('USCC{')
                    end = plaintext.find('}', start) + 1
                    flag = plaintext[start:end]
                    print(f"*** COMPLETE FLAG FOUND! ***")
                    print(f"Day: {day}, Position: {pos}, Plugboard: No")
                    print(f"FLAG: {flag}")
                    print(f"Full text: {plaintext}")
                    return flag
                
                # Check for readable English text
                if contains_english_words(plaintext):
                    print(f"Day {day}, Pos {pos}, No Plugs: Contains English - {plaintext[:50]}...")
                    if 'USCC' in plaintext:
                        print(f"  -> Also contains USCC!")
                        uscc_pos = plaintext.find('USCC')
                        context = plaintext[uscc_pos:uscc_pos+40]
                        print(f"  -> Context: {context}")
                
            except Exception as e:
                continue
    
    print("No complete flag found with Enigma. Trying one final Vigenère approach...")
    
    # Try all possible 3-letter keys from the message
    three_letter_keys = []
    for i in range(len(ciphertext) - 2):
        three_letter_keys.append(ciphertext[i:i+3])
    
    # Remove duplicates
    three_letter_keys = list(set(three_letter_keys))
    
    print(f"Trying {len(three_letter_keys)} three-letter keys from the ciphertext...")
    
    for key in three_letter_keys[:50]:  # Try first 50 to avoid too much output
        result = vigenere_decrypt(ciphertext, key)
        
        if 'USCC{' in result and '}' in result:
            start = result.find('USCC{')
            end = result.find('}', start) + 1
            flag = result[start:end]
            print(f"*** FLAG FOUND with key '{key}': {flag} ***")
            return flag
    
    return None

def contains_english_words(text):
    """Check if text contains common English words"""
    common_words = ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'CAN', 'HER', 'WAS', 'ONE', 'OUR', 'HAD', 'USE', 'HAVE', 'WILL', 'BEEN', 'FROM', 'THEY', 'KNOW', 'WANT', 'GOOD', 'MUCH', 'SOME', 'TIME', 'VERY', 'WHEN', 'COME', 'HERE', 'HOW', 'JUST', 'LIKE', 'LONG', 'MAKE', 'MANY', 'OVER', 'SUCH', 'TAKE', 'THAN', 'THEM', 'WELL', 'WERE', 'WITH']
    
    count = 0
    for word in common_words:
        if word in text.upper():
            count += 1
    
    return count >= 2  # At least 2 common English words

def vigenere_decrypt(ciphertext, key):
    """Decrypt using Vigenère cipher"""
    result = ""
    key_upper = key.upper()
    key_len = len(key_upper)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = key_upper[i % key_len]
            shift = ord(key_char) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result += decrypted_char
        else:
            result += char
    
    return result

if __name__ == "__main__":
    flag = final_comprehensive()
    if flag:
        print(f"\n{'='*60}")
        print(f"FINAL FLAG: {flag}")
    else:
        print("\nUnable to find the correct flag. The cipher may require a different approach or additional information.")