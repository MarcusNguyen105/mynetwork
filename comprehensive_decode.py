#!/usr/bin/env python3
"""
Comprehensive Enigma decoder - trying all days with all Kenngruppen
"""

from enigma.machine import EnigmaMachine

full_encrypted = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"

# Full codebook
codebook = {
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

def decode_with_procedure(day, ground_setting):
    """Use proper Enigma procedure"""
    rotors, ring_settings, plugboard, kenngruppen = codebook[day]
    
    rotor_list = rotors.split()
    ring_list = [int(x) for x in ring_settings.split()]
    
    machine = EnigmaMachine.from_key_sheet(
        rotors=' '.join(rotor_list),
        reflector='B',
        ring_settings=' '.join([str(r) for r in ring_list]),
        plugboard_settings=plugboard
    )
    
    # Decode indicator
    machine.set_display(ground_setting)
    indicator_decrypted = machine.process_text(full_encrypted[:6])
    message_key = indicator_decrypted[:3]
    
    # Decode message
    machine.set_display(message_key)
    plaintext = machine.process_text(full_encrypted[6:])
    
    return message_key, plaintext

# Search keywords
keywords = ["CONGRATULATIONS", "FLAG", "WELL", "ENIGMA", "SUCCESS", "BLETCHLEY", "DONE", "YOU", "HAVE", "CRACK", "DECIPHER", "SECRET", "MESSAGE"]

print("Searching all days with all Kenngruppen as ground settings...")
print("="*80)

matches = []

for day in range(1, 31):
    _, _, _, kenngruppen = codebook[day]
    for kg in kenngruppen:
        message_key, plaintext = decode_with_procedure(day, kg)
        
        # Check for English-looking text
        found = [word for word in keywords if word in plaintext.upper()]
        if found:
            print(f"\n*** POTENTIAL MATCH ***")
            print(f"Day {day}, Ground setting: {kg}, Message key: {message_key}")
            print(f"Keywords found: {found}")
            print(f"Plaintext: {plaintext}")
            print()
            matches.append((day, kg, message_key, plaintext))

if not matches:
    print("\nNo obvious matches found with keyword search.")
    print("Let me try a different approach - looking for readable text patterns...")
    print()
    
    # Look for patterns of common letter sequences
    common_patterns = ["TH", "HE", "THE", "AND", "ING", "YOU", "THAT", "FOR", "WITH"]
    
    for day in range(1, 31):
        _, _, _, kenngruppen = codebook[day]
        for kg in kenngruppen:
            message_key, plaintext = decode_with_procedure(day, kg)
            
            # Count how many common patterns appear
            pattern_count = sum(1 for pattern in common_patterns if pattern in plaintext.upper())
            
            if pattern_count >= 3:  # At least 3 common patterns
                print(f"Day {day}, Ground: {kg}, Key: {message_key}, Patterns: {pattern_count}")
                print(f"  {plaintext[:100]}...")
                print()

print("\nDone!")
