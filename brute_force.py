#!/usr/bin/env python3
"""
Brute force all days with GZV starting position
"""

from enigma.machine import EnigmaMachine

full_encrypted = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"

codebook = {
    30: ("II VI VIII", "20 12 15", "AE BX CU DF HZ JO LS MN QY VW"),
    29: ("V IV VIII", "08 23 20", "AS BW CF DT EM IZ JQ LV PY RU"),
    28: ("VII VI IV", "13 21 12", "AU CP DK HY IW JX MQ OZ RS TV"),
    27: ("VII IV VI", "13 17 01", "AB CJ DZ EL FM GY HX IK RU VW"),
    26: ("VIII II IV", "24 10 23", "AX BZ CI DU FY GH KO LP MW NR"),
    25: ("IV V I", "12 16 08", "AL DV EX FP HN JU KS MR QY WZ"),
    24: ("IV III II", "11 03 22", "CH DU EX FZ JT KP LY MR OW QS"),
    23: ("VII II I", "19 23 08", "AX BH CM DY FZ IJ KW LP QV RU"),
    22: ("VIII III VI", "20 03 17", "BD CP EH FO JW KX LU NQ RZ SV"),
    21: ("I VI II", "13 06 10", "AX BU CK EL GN HP IO JY MR QV"),
    20: ("VIII IV VI", "10 22 06", "AR BN DI GP HQ KZ LU MS TX WY"),
    19: ("II VII I", "01 21 24", "BH CM DU FP GL IO KT QY RW VX"),
    18: ("VIII VI VII", "13 02 15", "AT BV CJ DO EP FY GZ LW MQ NU"),
    17: ("VI II IV", "05 13 26", "AO BS CQ DP EF GN JL KW TY UZ"),
    16: ("II IV VII", "09 02 19", "AE BS CQ FU GX IT JV KL MW OR"),
    15: ("III IV I", "07 19 08", "AN CS DY FT HZ IM JL OX QW RU"),
    14: ("III VII IV", "15 17 04", "AD BO FK GI HW LY MP NS RX TZ"),
    13: ("VI I II", "19 15 01", "AN BL DR EO FQ GS HP IJ TY VW"),
    12: ("II VI I", "25 23 20", "AG EM FY IX JO KR LU NW QS TZ"),
    11: ("II VI VIII", "23 19 15", "CQ DS EZ FL GJ HK MX NY OT PR"),
    10: ("VII VIII II", "14 20 06", "AR BO CF EK GM HZ JN PX QV WY"),
    9: ("IV III VI", "15 08 13", "AQ BI CL DM EV FK JP NS OZ TU"),
    8: ("VIII II VI", "12 02 23", "AD BN CP EG HO JW KQ LX TY VZ"),
    7: ("II VI III", "05 13 20", "AQ CU DN ES GO IL JV MZ RX WY"),
    6: ("V VI VII", "18 01 24", "AN CK DX FQ GL HY IU JR OZ PV"),
    5: ("IV VII II", "01 26 09", "AG BM CW ER FJ IT KO PS UY VX"),
    4: ("VIII VII VI", "08 21 12", "AU BW DX EI FJ HS KP MQ NV RT"),
    3: ("VII IV I", "03 18 09", "AJ CZ DL EO FK GS HW NU PR VX"),
    2: ("V IV II", "18 25 15", "AW CI DY EF GV HT JL KO NS UZ"),
    1: ("VIII II III", "24 09 04", "CY DQ EP FH GW JL NV OU RX SZ"),
}

print("Trying all days with GZV starting position...")
print("="*80)

for day in range(1, 31):
    rotors, ring_settings, plugboard = codebook[day]
    
    machine = EnigmaMachine.from_key_sheet(
        rotors=rotors,
        reflector='B',
        ring_settings=ring_settings,
        plugboard_settings=plugboard
    )
    
    machine.set_display("GZV")
    text = machine.process_text(full_encrypted)
    
    # Check for readable English patterns
    common_words = ["THE", "AND", "YOU", "HAVE", "THAT", "THIS", "WITH", "FROM", "CONGRATULATIONS", "FLAG", "WELL", "DONE"]
    found_words = [w for w in common_words if w in text.upper()]
    
    if found_words or any(c.isdigit() for c in text):  # Also check for digits
        print(f"\nDay {day}: {text}")
        if found_words:
            print(f"  Words found: {found_words}")
    
    # Also check for high concentration of common letters
    letter_freq = {}
    for c in text.upper():
        if c.isalpha():
            letter_freq[c] = letter_freq.get(c, 0) + 1
    
    # Most common letters in English: E, T, A, O, I, N
    common_letter_count = sum(letter_freq.get(c, 0) for c in "ETAOIN")
    total_letters = sum(letter_freq.values())
    if total_letters > 0 and (common_letter_count / total_letters) > 0.5:
        # More than 50% common letters might indicate English
        if day not in [d for d in range(1, 31) if any(w in codebook[d] for w in ["VIII VII VI", "II VI VIII"])]:  # Skip if already printed
            print(f"\nDay {day} (high common letter frequency {common_letter_count/total_letters:.1%}):")
            print(f"  {text[:80]}...")

print("\n" + "="*80)
print("Now trying with standard indicator procedure for all days...")
print("="*80)

for day in range(1, 31):
    rotors, ring_settings, plugboard = codebook[day]
    
    # Try decoding first 6 letters with AAA, then use result
    machine1 = EnigmaMachine.from_key_sheet(
        rotors=rotors,
        reflector='B',
        ring_settings=ring_settings,
        plugboard_settings=plugboard
    )
    
    machine1.set_display("AAA")
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
    
    common_words = ["THE", "AND", "YOU", "HAVE", "CONGRATULATIONS", "FLAG", "WELL", "DONE", "THIS", "THAT"]
    found_words = [w for w in common_words if w in text.upper()]
    
    if found_words:
        print(f"\nDay {day}, Ground=AAA, Key={msg_key}:")
        print(f"  {text}")
        print(f"  Words: {found_words}")
