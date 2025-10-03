#!/usr/bin/env python3
"""
Enigma decoder - trying indicator as first 6 letters
"""

from enigma.machine import EnigmaMachine

# Full encrypted message
full_encrypted = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"

# Codebook settings
codebook = {
    4: ("VIII VII VI", "08 21 12", "AU BW DX EI FJ HS KP MQ NV RT", "ABF QON QDK CBR"),
    20: ("VIII IV VI", "10 22 06", "AR BN DI GP HQ KZ LU MS TX WY", "YGC WHF YDK UML"),
}

def decode_with_procedure(day, ground_setting="AAA"):
    """
    Use proper Enigma procedure:
    1. Decode first 6 letters with ground setting to get message key (encrypted twice)
    2. Use message key to decode the rest
    """
    rotors, ring_settings, plugboard, kenngruppen = codebook[day]
    
    rotor_list = rotors.split()
    ring_list = [int(x) for x in ring_settings.split()]
    
    # Step 1: Decode the indicator (first 6 letters) with ground setting
    machine = EnigmaMachine.from_key_sheet(
        rotors=' '.join(rotor_list),
        reflector='B',
        ring_settings=' '.join([str(r) for r in ring_list]),
        plugboard_settings=plugboard
    )
    
    machine.set_display(ground_setting)
    indicator_decrypted = machine.process_text(full_encrypted[:6])
    
    # The message key should be the first 3 letters (repeated twice for verification)
    message_key = indicator_decrypted[:3]
    message_key_check = indicator_decrypted[3:6]
    
    print(f"Day {day}, Ground setting {ground_setting}:")
    print(f"  Encrypted indicator: {full_encrypted[:6]}")
    print(f"  Decrypted indicator: {indicator_decrypted} -> Message key: {message_key} (check: {message_key_check})")
    
    # Step 2: Decode the actual message with the message key
    machine.set_display(message_key)
    actual_message = full_encrypted[6:]
    plaintext = machine.process_text(actual_message)
    
    print(f"  Plaintext: {plaintext}")
    print()
    
    return plaintext

# Try different days and ground settings
print("Trying proper Enigma procedure with different days and ground settings:")
print("="*80)

for day in [4, 20]:
    for ground in ["AAA", "WHF", "GZV", "DBR"]:
        plaintext = decode_with_procedure(day, ground)
        if any(word in plaintext.upper() for word in ["CONGRATULATIONS", "FLAG", "WELL", "ENIGMA", "SUCCESS", "BLETCHLEY"]):
            print(f"*** POSSIBLE MATCH FOUND ***")
            print()

print("\n" + "="*80)
print("Let me also try all days with AAA ground setting:")
print("="*80)

# Expand codebook
all_codebook = {
    30: ("II VI VIII", "20 12 15", "AE BX CU DF HZ JO LS MN QY VW", "AZG IGN UKY YPL"),
    29: ("V IV VIII", "08 23 20", "AS BW CF DT EM IZ JQ LV PY RU", "PDZ DJE AFY ABJ"),
    28: ("VII VI IV", "13 21 12", "AU CP DK HY IW JX MQ OZ RS TV", "VQF TKL BQV DJU"),
    27: ("VII IV VI", "13 17 01", "AB CJ DZ EL FM GY HX IK RU VW", "IND PNB EPL CFH"),
    26: ("VIII II IV", "24 10 23", "AX BZ CI DU FY GH KO LP MW NR", "QRN TOX GRT BNQ"),
    25: ("IV V I", "12 16 08", "AL DV EX FP HN JU KS MR QY WZ", "HIP UMA PBQ MJE"),
    24: ("IV III II", "11 03 22", "CH DU EX FZ JT KP LY MR OW QS", "OVE FSQ WDQ CGQ"),
    23: ("VII II I", "19 23 08", "AX BH CM DY FZ IJ KW LP QV RU", "ANG IRG HLO UHZ"),
    22: ("VIII III VI", "20 03 17", "BD CP EH FO JW KX LU NQ RZ SV", "QME ARA PRP BRA"),
    21: ("I VI II", "13 06 10", "AX BU CK EL GN HP IO JY MR QV", "BCI VKY FIH FAC"),
    20: ("VIII IV VI", "10 22 06", "AR BN DI GP HQ KZ LU MS TX WY", "YGC WHF YDK UML"),
    19: ("II VII I", "01 21 24", "BH CM DU FP GL IO KT QY RW VX", "GPP SHJ OQW ETU"),
    18: ("VIII VI VII", "13 02 15", "AT BV CJ DO EP FY GZ LW MQ NU", "LCE VZK WPV EVM"),
    17: ("VI II IV", "05 13 26", "AO BS CQ DP EF GN JL KW TY UZ", "BWW HZE QQZ CFK"),
    16: ("II IV VII", "09 02 19", "AE BS CQ FU GX IT JV KL MW OR", "OKU GAE JDZ TJQ"),
    15: ("III IV I", "07 19 08", "AN CS DY FT HZ IM JL OX QW RU", "XMO EBZ SLT TML"),
    14: ("III VII IV", "15 17 04", "AD BO FK GI HW LY MP NS RX TZ", "CMV XSW XDS VQO"),
    13: ("VI I II", "19 15 01", "AN BL DR EO FQ GS HP IJ TY VW", "KHL MLP LIB QAV"),
    12: ("II VI I", "25 23 20", "AG EM FY IX JO KR LU NW QS TZ", "HNR PQV HMN GLW"),
    11: ("II VI VIII", "23 19 15", "CQ DS EZ FL GJ HK MX NY OT PR", "DUQ ONH VWG BRY"),
    10: ("VII VIII II", "14 20 06", "AR BO CF EK GM HZ JN PX QV WY", "TFZ UQH UMO MPA"),
    9: ("IV III VI", "15 08 13", "AQ BI CL DM EV FK JP NS OZ TU", "CXZ ORI ISE IFC"),
    8: ("VIII II VI", "12 02 23", "AD BN CP EG HO JW KQ LX TY VZ", "ZAS UDW EDA FDZ"),
    7: ("II VI III", "05 13 20", "AQ CU DN ES GO IL JV MZ RX WY", "EZU YZQ RTP ENI"),
    6: ("V VI VII", "18 01 24", "AN CK DX FQ GL HY IU JR OZ PV", "IGG CRF BIL HHF"),
    5: ("IV VII II", "01 26 09", "AG BM CW ER FJ IT KO PS UY VX", "YFS ZDZ QAW VZM"),
    4: ("VIII VII VI", "08 21 12", "AU BW DX EI FJ HS KP MQ NV RT", "ABF QON QDK CBR"),
    3: ("VII IV I", "03 18 09", "AJ CZ DL EO FK GS HW NU PR VX", "POQ EPJ LLZ FYL"),
    2: ("V IV II", "18 25 15", "AW CI DY EF GV HT JL KO NS UZ", "PDG VMK UBM FMX"),
    1: ("VIII II III", "24 09 04", "CY DQ EP FH GW JL NV OU RX SZ", "LQC ZRR NOW AIO"),
}

def decode_all(day, ground_setting="AAA"):
    rotors, ring_settings, plugboard, kenngruppen = all_codebook[day]
    
    rotor_list = rotors.split()
    ring_list = [int(x) for x in ring_settings.split()]
    
    machine = EnigmaMachine.from_key_sheet(
        rotors=' '.join(rotor_list),
        reflector='B',
        ring_settings=' '.join([str(r) for r in ring_list]),
        plugboard_settings=plugboard
    )
    
    machine.set_display(ground_setting)
    indicator_decrypted = machine.process_text(full_encrypted[:6])
    message_key = indicator_decrypted[:3]
    
    machine.set_display(message_key)
    actual_message = full_encrypted[6:]
    plaintext = machine.process_text(actual_message)
    
    return message_key, plaintext

for day in range(1, 31):
    msg_key, plaintext = decode_all(day, "AAA")
    if any(word in plaintext.upper() for word in ["CONGRATULATIONS", "FLAG", "WELL", "ENIGMA", "SUCCESS", "BLETCHLEY", "DONE", "YOU"]):
        print(f"Day {day}: Message key = {msg_key}")
        print(f"  {plaintext}")
        print()
