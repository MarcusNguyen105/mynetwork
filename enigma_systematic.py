#!/usr/bin/env python3

from enigma.machine import EnigmaMachine

def test_enigma_config(day, rotor_pos, description):
    """Test a specific Enigma configuration"""
    
    # Configuration mapping from the codebook
    configs = {
        30: {'rotors': 'II VI VIII', 'rings': '20 12 15', 'plugs': 'AE BX CU DF HZ JO LS MN QY VW'},
        12: {'rotors': 'II VI I', 'rings': '25 23 20', 'plugs': 'AG EM FY IX JO KR LU NW QS TZ'},
        9: {'rotors': 'IV III VI', 'rings': '15 08 13', 'plugs': 'AQ BI CL DM EV FK JP NS OZ TU'},
    }
    
    if day not in configs:
        print(f"Day {day} not in test configurations")
        return None
    
    config = configs[day]
    
    # Set up the Enigma machine
    machine = EnigmaMachine.from_key_sheet(
        rotors=config['rotors'],
        reflector='B',
        ring_settings=config['rings'],
        plugboard_settings=config['plugs']
    )
    
    # Set rotor positions
    machine.set_display(rotor_pos)
    
    # The encrypted message
    ciphertext = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"
    
    # Decode
    plaintext = machine.process_text(ciphertext)
    
    print(f"\n{description}")
    print(f"Day {day}, Rotors: {config['rotors']}, Position: {rotor_pos}")
    print(f"Plaintext: {plaintext}")
    
    # Check if it looks like readable text (contains common English patterns)
    if any(word in plaintext.upper() for word in ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'CAN', 'HER', 'WAS', 'ONE', 'OUR', 'HAD', 'USE', 'USCC']):
        print("*** POTENTIALLY READABLE TEXT FOUND! ***")
        return plaintext
    
    return None

def main():
    print("Testing different Enigma configurations...")
    
    # Test different day configurations with different rotor positions
    test_cases = [
        (30, 'GZV', 'Day 30 with GZV (from message header)'),
        (30, 'DBR', 'Day 30 with DBR (from message header)'),
        (30, 'AAA', 'Day 30 with AAA (111 might mean position 1,1,1)'),
        (12, 'GZV', 'Day 12 with GZV'),
        (12, 'DBR', 'Day 12 with DBR'),
        (12, 'AAA', 'Day 12 with AAA'),
        (9, 'GZV', 'Day 9 with GZV'),
        (9, 'DBR', 'Day 9 with DBR'),
        (9, 'AAA', 'Day 9 with AAA'),
    ]
    
    results = []
    for day, pos, desc in test_cases:
        result = test_enigma_config(day, pos, desc)
        if result:
            results.append((day, pos, result))
    
    if results:
        print("\n" + "="*50)
        print("READABLE RESULTS FOUND:")
        for day, pos, text in results:
            print(f"Day {day}, Position {pos}: {text}")
    else:
        print("\nNo clearly readable results found. May need to try other approaches.")

if __name__ == "__main__":
    main()