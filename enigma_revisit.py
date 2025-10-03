#!/usr/bin/env python3

from enigma.machine import EnigmaMachine

def enigma_revisit():
    """Revisit Enigma with different interpretations"""
    
    ciphertext = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"
    
    print("Revisiting Enigma machine approach...")
    
    # Let me try the proper Enigma procedure more carefully
    # The message header is: 5JT DE SJ2 1209 = 111 = GZV DBR =
    
    # Maybe 1209 refers to September 12th (month 09, day 12)
    # Or December 9th
    # Let me try both day 9 and day 12 more systematically
    
    configs = {
        9: {'rotors': 'IV III VI', 'rings': '15 08 13', 'plugs': 'AQ BI CL DM EV FK JP NS OZ TU'},
        12: {'rotors': 'II VI I', 'rings': '25 23 20', 'plugs': 'AG EM FY IX JO KR LU NW QS TZ'},
        30: {'rotors': 'II VI VIII', 'rings': '20 12 15', 'plugs': 'AE BX CU DF HZ JO LS MN QY VW'},
    }
    
    # Try different procedures for handling the indicator groups
    for day in [9, 12, 30]:
        if day not in configs:
            continue
            
        config = configs[day]
        print(f"\nTrying day {day} configuration:")
        print(f"  Rotors: {config['rotors']}")
        print(f"  Rings: {config['rings']}")
        print(f"  Plugs: {config['plugs']}")
        
        # Method 1: Use GZV directly as rotor positions
        try:
            machine = EnigmaMachine.from_key_sheet(
                rotors=config['rotors'],
                reflector='B',
                ring_settings=config['rings'],
                plugboard_settings=config['plugs']
            )
            machine.set_display('GZV')
            
            plaintext = machine.process_text(ciphertext)
            print(f"  Method 1 (GZV): {plaintext[:50]}...")
            
            if 'USCC' in plaintext:
                print(f"  *** USCC FOUND! ***")
                print(f"  Full text: {plaintext}")
                if '{' in plaintext and '}' in plaintext:
                    start = plaintext.find('USCC')
                    end = plaintext.find('}', start) + 1
                    flag = plaintext[start:end]
                    print(f"  *** FLAG: {flag} ***")
                    return flag
        except Exception as e:
            print(f"  Method 1 error: {e}")
        
        # Method 2: Use DBR as rotor positions
        try:
            machine = EnigmaMachine.from_key_sheet(
                rotors=config['rotors'],
                reflector='B',
                ring_settings=config['rings'],
                plugboard_settings=config['plugs']
            )
            machine.set_display('DBR')
            
            plaintext = machine.process_text(ciphertext)
            print(f"  Method 2 (DBR): {plaintext[:50]}...")
            
            if 'USCC' in plaintext:
                print(f"  *** USCC FOUND! ***")
                print(f"  Full text: {plaintext}")
                if '{' in plaintext and '}' in plaintext:
                    start = plaintext.find('USCC')
                    end = plaintext.find('}', start) + 1
                    flag = plaintext[start:end]
                    print(f"  *** FLAG: {flag} ***")
                    return flag
        except Exception as e:
            print(f"  Method 2 error: {e}")
        
        # Method 3: Decode GZV first with a Grundstellung, then use result
        try:
            # Use AAA as Grundstellung to decode GZV
            machine = EnigmaMachine.from_key_sheet(
                rotors=config['rotors'],
                reflector='B',
                ring_settings=config['rings'],
                plugboard_settings=config['plugs']
            )
            machine.set_display('AAA')
            
            decoded_gzv = machine.process_text('GZV')
            print(f"  Decoded GZV with AAA: {decoded_gzv}")
            
            # Now use decoded GZV as rotor positions
            machine.set_display(decoded_gzv)
            plaintext = machine.process_text(ciphertext)
            print(f"  Method 3 ({decoded_gzv}): {plaintext[:50]}...")
            
            if 'USCC' in plaintext:
                print(f"  *** USCC FOUND! ***")
                print(f"  Full text: {plaintext}")
                if '{' in plaintext and '}' in plaintext:
                    start = plaintext.find('USCC')
                    end = plaintext.find('}', start) + 1
                    flag = plaintext[start:end]
                    print(f"  *** FLAG: {flag} ***")
                    return flag
        except Exception as e:
            print(f"  Method 3 error: {e}")
    
    # Try without plugboard (training Enigma)
    print(f"\n{'='*50}")
    print("Trying without plugboard...")
    
    for day in [9, 12, 30]:
        config = configs[day]
        
        for pos in ['GZV', 'DBR', 'AAA']:
            try:
                machine = EnigmaMachine.from_key_sheet(
                    rotors=config['rotors'],
                    reflector='B',
                    ring_settings=config['rings'],
                    plugboard_settings=''  # No plugboard
                )
                machine.set_display(pos)
                
                plaintext = machine.process_text(ciphertext)
                
                if 'USCC' in plaintext:
                    print(f"Day {day}, No plugs, Pos {pos}: *** USCC FOUND! ***")
                    print(f"Full text: {plaintext}")
                    if '{' in plaintext and '}' in plaintext:
                        start = plaintext.find('USCC')
                        end = plaintext.find('}', start) + 1
                        flag = plaintext[start:end]
                        print(f"*** FLAG: {flag} ***")
                        return flag
                elif any(word in plaintext for word in ['FLAG', 'CIPHER', 'SECRET']):
                    print(f"Day {day}, No plugs, Pos {pos}: Promising - {plaintext[:40]}...")
                    
            except Exception as e:
                print(f"Day {day}, No plugs, Pos {pos} error: {e}")
    
    return None

if __name__ == "__main__":
    flag = enigma_revisit()
    if flag:
        print(f"\n{'='*60}")
        print(f"CORRECT FLAG: {flag}")
    else:
        print("\nStill need to find the correct approach...")