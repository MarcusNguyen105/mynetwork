#!/usr/bin/env python3

from enigma.machine import EnigmaMachine

def decode_enigma_message():
    # Settings for day 12 from the codebook (trying 1209 as day 12, month 09)
    # Tag 12: II VI I | 25 23 20 | AG EM FY IX JO KR LU NW QS TZ
    
    # Set up the Enigma machine
    machine = EnigmaMachine.from_key_sheet(
        rotors='II VI I',              # Rotor configuration
        reflector='B',                 # Standard reflector B
        ring_settings='25 23 20',      # Ring settings (Y W T in letters)
        plugboard_settings='AG EM FY IX JO KR LU NW QS TZ'  # Plugboard pairs
    )
    
    # Try different rotor positions - maybe DBR instead of GZV
    machine.set_display('DBR')
    
    # The encrypted message (removing spaces and formatting)
    ciphertext = """XLWHF DJKUC ZONWZ UFDGB SIILK
GSOBR NPPMF BWFTU CHPCO UUBMB
NUUMW HMPJG JGJPM AXKPY FENEP
LKHGM LUPUJ WWCZO YATTS CBSKI
QFKSG ADRPZ J"""
    
    # Clean the ciphertext (remove spaces and newlines)
    clean_ciphertext = ''.join(ciphertext.split())
    
    print(f"Ciphertext: {clean_ciphertext}")
    print(f"Length: {len(clean_ciphertext)}")
    
    # Decode the message
    plaintext = machine.process_text(clean_ciphertext)
    
    print(f"Plaintext: {plaintext}")
    
    return plaintext

if __name__ == "__main__":
    decoded = decode_enigma_message()