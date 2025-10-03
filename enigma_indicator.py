#!/usr/bin/env python3

from enigma.machine import EnigmaMachine

def decode_indicators_and_message():
    """
    Try the proper Enigma procedure:
    1. Use Grundstellung (basic position) to decode indicator groups
    2. Use decoded indicators as rotor positions for the actual message
    """
    
    # Day 30 settings: II VI VIII | 20 12 15 | AE BX CU DF HZ JO LS MN QY VW
    
    print("Trying Enigma indicator procedure...")
    
    # Set up machine with day 30 settings
    machine = EnigmaMachine.from_key_sheet(
        rotors='II VI VIII',
        reflector='B', 
        ring_settings='20 12 15',
        plugboard_settings='AE BX CU DF HZ JO LS MN QY VW'
    )
    
    # Try different Grundstellung positions to decode indicators
    grundstellungen = ['AAA', 'ABC', 'XYZ', 'QWE']
    
    for grund in grundstellungen:
        print(f"\nTrying Grundstellung: {grund}")
        
        # Reset machine to Grundstellung
        machine.set_display(grund)
        
        # Decode the indicator groups GZV and DBR
        decoded_gzv = machine.process_text('GZV')
        machine.set_display(grund)  # Reset for second indicator
        decoded_dbr = machine.process_text('DBR')
        
        print(f"GZV -> {decoded_gzv}")
        print(f"DBR -> {decoded_dbr}")
        
        # Try using decoded indicators as rotor positions
        for indicator in [decoded_gzv, decoded_dbr]:
            print(f"\nTrying rotor position: {indicator}")
            
            # Reset machine and set to decoded indicator position
            machine = EnigmaMachine.from_key_sheet(
                rotors='II VI VIII',
                reflector='B',
                ring_settings='20 12 15', 
                plugboard_settings='AE BX CU DF HZ JO LS MN QY VW'
            )
            machine.set_display(indicator)
            
            # Decode the message
            ciphertext = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"
            plaintext = machine.process_text(ciphertext)
            
            print(f"Plaintext: {plaintext}")
            
            # Check for readable text
            if any(word in plaintext.upper() for word in ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'CAN', 'HER', 'WAS', 'ONE', 'OUR', 'HAD', 'USE', 'USCC', 'FLAG']):
                print("*** POTENTIALLY READABLE TEXT FOUND! ***")
                return plaintext
    
    return None

if __name__ == "__main__":
    result = decode_indicators_and_message()
    if not result:
        print("\nNo readable text found with indicator procedure. Trying direct approach with other days...")
        
        # Maybe it's a different day entirely - let's try some other days
        days_to_try = [1, 2, 3, 4, 5, 15, 20, 25]
        
        configs = {
            1: {'rotors': 'VIII II III', 'rings': '24 09 04', 'plugs': 'CY DQ EP FH GW JL NV OU RX SZ'},
            2: {'rotors': 'V IV II', 'rings': '18 25 15', 'plugs': 'AW CI DY EF GV HT JL KO NS UZ'},
            3: {'rotors': 'VII IV I', 'rings': '03 18 09', 'plugs': 'AJ CZ DL EO FK GS HW NU PR VX'},
            4: {'rotors': 'VIII VII VI', 'rings': '08 21 12', 'plugs': 'AU BW DX EI FJ HS KP MQ NV RT'},
            5: {'rotors': 'IV VII II', 'rings': '01 26 09', 'plugs': 'AG BM CW ER FJ IT KO PS UY VX'},
            15: {'rotors': 'III IV I', 'rings': '07 19 08', 'plugs': 'AN CS DY FT HZ IM JL OX QW RU'},
            20: {'rotors': 'VIII IV VI', 'rings': '10 22 06', 'plugs': 'AR BN DI GP HQ KZ LU MS TX WY'},
            25: {'rotors': 'IV V I', 'rings': '12 16 08', 'plugs': 'AL DV EX FP HN JU KS MR QY WZ'},
        }
        
        for day in days_to_try:
            if day in configs:
                config = configs[day]
                for pos in ['GZV', 'DBR', 'AAA']:
                    machine = EnigmaMachine.from_key_sheet(
                        rotors=config['rotors'],
                        reflector='B',
                        ring_settings=config['rings'],
                        plugboard_settings=config['plugs']
                    )
                    machine.set_display(pos)
                    
                    ciphertext = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"
                    plaintext = machine.process_text(ciphertext)
                    
                    print(f"\nDay {day}, Position {pos}: {plaintext[:50]}...")
                    
                    if any(word in plaintext.upper() for word in ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'CAN', 'HER', 'WAS', 'ONE', 'OUR', 'HAD', 'USE', 'USCC', 'FLAG']):
                        print(f"*** READABLE TEXT FOUND! Day {day}, Position {pos} ***")
                        print(f"Full text: {plaintext}")
        
        print("No readable text found in additional day tests.")