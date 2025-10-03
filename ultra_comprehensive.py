#!/usr/bin/env python3
"""
Ultra comprehensive search for readable English text
"""

from enigma.machine import EnigmaMachine

full_encrypted = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"

codebook_with_kenn = {
    30: ("II VI VIII", "20 12 15", "AE BX CU DF HZ JO LS MN QY VW", ["AZG", "IGN", "UKY", "YPL"]),
    29: ("V IV VIII", "08 23 20", "AS BW CF DT EM IZ JQ LV PY RU", ["PDZ", "DJE", "AFY", "ABJ"]),
    28: ("VII VI IV", "13 21 12", "AU CP DK HY IW JX MQ OZ RS TV", ["VQF", "TKL", "BQV", "DJU"]),
    27: ("VII IV VI", "13 17 01", "AB CJ DZ EL FM GY HX IK RU VW", ["IND", "PNB", "EPL", "CFH"]),
    26: ("VIII II IV", "24 10 23", "AX BZ CI DU FY GH KO LP MW NR", ["QRN", "TOX", "GRT", "BNQ"]),
    25: ("IV V I", "12 16 08", "AL DV EX FP HN JU KS MR QY WZ", ["HIP", "UMA", "PBQ", "MJE"]),
    24: ("IV III II", "11 03 22", "CH DU EX FZ JT KP LY MR OW QS", ["OVE", "FSQ", "WDQ", "CGQ"]),
    23: ("VII II I", "19 23 08", "AX BH CM DY FZ IJ KW LP QV RU", ["ANG", "IRG", "HLO", "UHZ"]),
    22: ("VIII III VI", "20 03 17", "BD CP EH FO JW KX LU NQ RZ SV", ["QME", "ARA", "PRP", "BRA"]),
    21: ("I VI II", "13 06 10", "AX BU CK EL GN HP IO JY MR QV", ["BCI", "VKY", "FIH", "FAC"]),
    20: ("VIII IV VI", "10 22 06", "AR BN DI GP HQ KZ LU MS TX WY", ["YGC", "WHF", "YDK", "UML"]),
    19: ("II VII I", "01 21 24", "BH CM DU FP GL IO KT QY RW VX", ["GPP", "SHJ", "OQW", "ETU"]),
    18: ("VIII VI VII", "13 02 15", "AT BV CJ DO EP FY GZ LW MQ NU", ["LCE", "VZK", "WPV", "EVM"]),
    17: ("VI II IV", "05 13 26", "AO BS CQ DP EF GN JL KW TY UZ", ["BWW", "HZE", "QQZ", "CFK"]),
    16: ("II IV VII", "09 02 19", "AE BS CQ FU GX IT JV KL MW OR", ["OKU", "GAE", "JDZ", "TJQ"]),
    15: ("III IV I", "07 19 08", "AN CS DY FT HZ IM JL OX QW RU", ["XMO", "EBZ", "SLT", "TML"]),
    14: ("III VII IV", "15 17 04", "AD BO FK GI HW LY MP NS RX TZ", ["CMV", "XSW", "XDS", "VQO"]),
    13: ("VI I II", "19 15 01", "AN BL DR EO FQ GS HP IJ TY VW", ["KHL", "MLP", "LIB", "QAV"]),
    12: ("II VI I", "25 23 20", "AG EM FY IX JO KR LU NW QS TZ", ["HNR", "PQV", "HMN", "GLW"]),
    11: ("II VI VIII", "23 19 15", "CQ DS EZ FL GJ HK MX NY OT PR", ["DUQ", "ONH", "VWG", "BRY"]),
    10: ("VII VIII II", "14 20 06", "AR BO CF EK GM HZ JN PX QV WY", ["TFZ", "UQH", "UMO", "MPA"]),
    9: ("IV III VI", "15 08 13", "AQ BI CL DM EV FK JP NS OZ TU", ["CXZ", "ORI", "ISE", "IFC"]),
    8: ("VIII II VI", "12 02 23", "AD BN CP EG HO JW KQ LX TY VZ", ["ZAS", "UDW", "EDA", "FDZ"]),
    7: ("II VI III", "05 13 20", "AQ CU DN ES GO IL JV MZ RX WY", ["EZU", "YZQ", "RTP", "ENI"]),
    6: ("V VI VII", "18 01 24", "AN CK DX FQ GL HY IU JR OZ PV", ["IGG", "CRF", "BIL", "HHF"]),
    5: ("IV VII II", "01 26 09", "AG BM CW ER FJ IT KO PS UY VX", ["YFS", "ZDZ", "QAW", "VZM"]),
    4: ("VIII VII VI", "08 21 12", "AU BW DX EI FJ HS KP MQ NV RT", ["ABF", "QON", "QDK", "CBR"]),
    3: ("VII IV I", "03 18 09", "AJ CZ DL EO FK GS HW NU PR VX", ["POQ", "EPJ", "LLZ", "FYL"]),
    2: ("V IV II", "18 25 15", "AW CI DY EF GV HT JL KO NS UZ", ["PDG", "VMK", "UBM", "FMX"]),
    1: ("VIII II III", "24 09 04", "CY DQ EP FH GW JL NV OU RX SZ", ["LQC", "ZRR", "NOW", "AIO"]),
}

def count_common_trigrams(text):
    """Count common English trigrams"""
    common_trigrams = ['THE', 'AND', 'ING', 'HER', 'HAT', 'HIS', 'THA', 'ERE', 'FOR', 'ENT', 'ION', 'TER', 'WAS', 'YOU', 'ITH', 'VER', 'ALL', 'WIT', 'THI', 'TIO']
    return sum(1 for trig in common_trigrams if trig in text.upper())

print("Searching for most English-like plaintext...")
print("="*80)

best_score = 0
best_results = []

for day in range(1, 31):
    rotors, ring_settings, plugboard, kenngruppen = codebook_with_kenn[day]
    
    # Test with Kenngruppen
    for ground in kenngruppen:
        # Indicator method
        try:
            machine1 = EnigmaMachine.from_key_sheet(
                rotors=rotors,
                reflector='B',
                ring_settings=ring_settings,
                plugboard_settings=plugboard
            )
            
            machine1.set_display(ground)
            indicator = machine1.process_text(full_encrypted[:6])
            msg_key = indicator[:3]
            
            machine2 = EnigmaMachine.from_key_sheet(
                rotors=rotors,
                reflector='B',
                ring_settings=ring_settings,
                plugboard_settings=plugboard
            )
            
            machine2.set_display(msg_key)
            text = machine2.process_text(full_encrypted[6:])
            
            score = count_common_trigrams(text)
            
            if score >= best_score:
                best_score = score
                best_results.append((score, day, ground, msg_key, text))
                if score > 0:
                    print(f"Day {day}, Ground={ground}, Key={msg_key}, Score={score}")
                    print(f"  {text[:80]}...")
        except:
            pass

# Sort and show top results
best_results.sort(reverse=True, key=lambda x: x[0])

print("\n" + "="*80)
print("TOP 5 RESULTS:")
print("="*80)

for i, (score, day, ground, key, text) in enumerate(best_results[:5]):
    print(f"\n#{i+1}: Score={score}, Day={day}, Ground={ground}, Key={key}")
    print(f"Full text: {text}")
    
    # Check for actual words
    if 'CONGRATULATIONS' in text or 'WELL DONE' in text or 'SUCCESS' in text:
        print("*** THIS LOOKS LIKE THE RIGHT ONE! ***")
