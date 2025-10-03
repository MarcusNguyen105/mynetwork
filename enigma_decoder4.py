#!/usr/bin/env python3
"""
Enigma decoder - focusing on Kenngruppen matching
"""

from enigma.machine import EnigmaMachine

full_encrypted = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"

# Day 4 has "CBR" in kenngruppen which is close to "DBR" in the message header
# Day 4: ("VIII VII VI", "08 21 12", "AU BW DX EI FJ HS KP MQ NV RT", "ABF QON QDK CBR")

# Let's try using the Kenngruppen as initial positions
day4_settings = {
    "rotors": "VIII VII VI",
    "ring_settings": "08 21 12",
    "plugboard": "AU BW DX EI FJ HS KP MQ NV RT",
    "kenngruppen": ["ABF", "QON", "QDK", "CBR"]
}

def decode_with_settings(initial_position):
    rotor_list = day4_settings["rotors"].split()
    ring_list = [int(x) for x in day4_settings["ring_settings"].split()]
    
    machine = EnigmaMachine.from_key_sheet(
        rotors=' '.join(rotor_list),
        reflector='B',
        ring_settings=' '.join([str(r) for r in ring_list]),
        plugboard_settings=day4_settings["plugboard"]
    )
    
    machine.set_display(initial_position)
    plaintext = machine.process_text(full_encrypted)
    
    return plaintext

print("Day 4 analysis - trying Kenngruppen positions:")
print("="*80)

# Try each kenngruppe as initial position
for kg in day4_settings["kenngruppen"]:
    plaintext = decode_with_settings(kg)
    print(f"Position {kg}:")
    print(f"  {plaintext[:80]}")
    if any(word in plaintext.upper() for word in ["CONGRATULATIONS", "FLAG", "WELL", "ENIGMA", "SUCCESS", "BLETCHLEY", "DONE"]):
        print(f"  *** POSSIBLE MATCH ***")
    print()

# Try DBR and GZV directly
print("Trying DBR and GZV:")
for pos in ["DBR", "GZV"]:
    plaintext = decode_with_settings(pos)
    print(f"Position {pos}:")
    print(f"  {plaintext[:80]}")
    if any(word in plaintext.upper() for word in ["CONGRATULATIONS", "FLAG", "WELL", "ENIGMA", "SUCCESS", "BLETCHLEY", "DONE"]):
        print(f"  *** POSSIBLE MATCH ***")
    print()

# Let's also try the standard procedure but with Kenngruppen as ground settings
print("\n" + "="*80)
print("Trying standard procedure with Kenngruppen as ground settings:")
print("="*80)

for ground in day4_settings["kenngruppen"]:
    rotor_list = day4_settings["rotors"].split()
    ring_list = [int(x) for x in day4_settings["ring_settings"].split()]
    
    machine = EnigmaMachine.from_key_sheet(
        rotors=' '.join(rotor_list),
        reflector='B',
        ring_settings=' '.join([str(r) for r in ring_list]),
        plugboard_settings=day4_settings["plugboard"]
    )
    
    # Decode indicator with kenngruppe as ground setting
    machine.set_display(ground)
    indicator_decrypted = machine.process_text(full_encrypted[:6])
    message_key = indicator_decrypted[:3]
    
    # Decode message with message key
    machine.set_display(message_key)
    plaintext = machine.process_text(full_encrypted[6:])
    
    print(f"Ground: {ground}, Indicator: {full_encrypted[:6]} -> {indicator_decrypted}, Message key: {message_key}")
    print(f"  {plaintext[:80]}")
    if any(word in plaintext.upper() for word in ["CONGRATULATIONS", "FLAG", "WELL", "ENIGMA", "SUCCESS", "BLETCHLEY", "DONE", "YOU"]):
        print(f"  *** POSSIBLE MATCH ***")
        print(f"  FULL TEXT: {plaintext}")
    print()
