#!/usr/bin/env python3

from enigma.machine import EnigmaMachine

def examine_promising():
    """Examine the most promising results more closely"""
    
    ciphertext = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"
    
    # The most promising results from the previous run:
    promising_configs = [
        (30, 'SJO', False, 'II VI VIII', '20 12 15', ''),  # No plugs, contains "THE"
        (27, 'XYZ', True, 'VII IV VI', '13 17 01', 'AB CJ DZ EL FM GY HX IK RU VW'),  # With plugs
        (9, 'GZV', False, 'IV III VI', '15 08 13', ''),  # No plugs
    ]
    
    print("Examining the most promising Enigma results...")
    
    for day, pos, use_plugs, rotors, rings, plugs in promising_configs:
        print(f"\n{'='*50}")
        print(f"Day {day}, Position {pos}, Plugs: {'Yes' if use_plugs else 'No'}")
        print(f"Rotors: {rotors}, Rings: {rings}")
        
        try:
            machine = EnigmaMachine.from_key_sheet(
                rotors=rotors,
                reflector='B',
                ring_settings=rings,
                plugboard_settings=plugs if use_plugs else ''
            )
            machine.set_display(pos)
            
            plaintext = machine.process_text(ciphertext)
            
            print(f"Full plaintext:")
            print(plaintext)
            print()
            
            # Look for any flag-like patterns
            print("Looking for flag patterns...")
            
            # Check for USCC
            if 'USCC' in plaintext:
                uscc_pos = plaintext.find('USCC')
                print(f"Found USCC at position {uscc_pos}")
                context = plaintext[max(0, uscc_pos-10):uscc_pos+50]
                print(f"Context: {context}")
                
                # Try to extract flag
                after_uscc = plaintext[uscc_pos+4:]
                flag_content = ""
                for char in after_uscc:
                    if char.isalnum() or char in '_-':
                        flag_content += char
                    else:
                        break
                
                if len(flag_content) >= 5:
                    potential_flag = f"USCC{{{flag_content}}}"
                    print(f"Potential flag: {potential_flag}")
            
            # Look for common English words
            common_words = ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'CAN', 'HER', 'WAS', 'ONE', 'OUR', 'HAD', 'USE', 'HAVE', 'WILL', 'BEEN', 'FROM', 'THEY', 'KNOW', 'WANT', 'GOOD', 'MUCH', 'SOME', 'TIME', 'VERY', 'WHEN', 'COME', 'HERE', 'HOW', 'JUST', 'LIKE', 'LONG', 'MAKE', 'MANY', 'OVER', 'SUCH', 'TAKE', 'THAN', 'THEM', 'WELL', 'WERE', 'WITH', 'FLAG', 'CIPHER', 'SECRET', 'ENIGMA', 'BLETCHLEY']
            
            found_words = []
            for word in common_words:
                if word in plaintext.upper():
                    pos_word = plaintext.upper().find(word)
                    found_words.append((word, pos_word))
            
            if found_words:
                print(f"Found English words: {[word for word, pos in found_words]}")
                
                # If we found "THE", this might be readable English
                if any(word == 'THE' for word, pos in found_words):
                    print("This looks like readable English text!")
                    
                    # Try to parse it as a message
                    # Maybe the flag is embedded in readable English
                    words = plaintext.split()
                    print(f"As words: {words}")
                    
                    # Look for flag in the words
                    for word in words:
                        if 'USCC' in word.upper():
                            print(f"Found USCC in word: {word}")
            
            # Check if this could be a different format
            # Maybe the entire decrypted text IS the flag content
            if len(plaintext) < 50 and plaintext.isalnum():
                potential_flag = f"USCC{{{plaintext}}}"
                print(f"Entire text as flag: {potential_flag}")
            
        except Exception as e:
            print(f"Error: {e}")
    
    # Let me also try one more approach - what if I need to use different reflectors?
    print(f"\n{'='*60}")
    print("Trying different reflectors on the most promising config...")
    
    # Use day 30, position SJO, no plugs (which contained "THE")
    for reflector in ['A', 'B', 'C']:
        try:
            machine = EnigmaMachine.from_key_sheet(
                rotors='II VI VIII',
                reflector=reflector,
                ring_settings='20 12 15',
                plugboard_settings=''
            )
            machine.set_display('SJO')
            
            plaintext = machine.process_text(ciphertext)
            
            print(f"Reflector {reflector}: {plaintext[:60]}...")
            
            if 'USCC{' in plaintext and '}' in plaintext:
                start = plaintext.find('USCC{')
                end = plaintext.find('}', start) + 1
                flag = plaintext[start:end]
                print(f"*** COMPLETE FLAG FOUND with reflector {reflector}: {flag} ***")
                return flag
            elif 'USCC' in plaintext:
                uscc_pos = plaintext.find('USCC')
                context = plaintext[uscc_pos:uscc_pos+30]
                print(f"  Contains USCC: {context}")
                
        except Exception as e:
            print(f"Reflector {reflector} error: {e}")
    
    return None

if __name__ == "__main__":
    flag = examine_promising()
    if flag:
        print(f"\n{'='*60}")
        print(f"FINAL FLAG: {flag}")
    else:
        print("\nNeed to try a different approach or get more information about the cipher.")