#!/usr/bin/env python3

from enigma.machine import EnigmaMachine

def try_alternative_approaches():
    """Try alternative interpretations of the Enigma message"""
    
    print("Trying alternative Enigma approaches...")
    
    # Day 9 configuration (December 9th interpretation)
    day9_config = {
        'rotors': 'IV III VI',
        'rings': '15 08 13', 
        'plugs': 'AQ BI CL DM EV FK JP NS OZ TU'
    }
    
    ciphertext = "XLWHFDJKUCZONWZUFDGBSIILKGSOBRNPPMFBWFTUCHPCOUUBMBNUUMWHMPJGJGJPMAXKPYFENEPLKHGMLUPUJWWCZOYATTSCBSKIQFKSGADRPZJ"
    
    # Try different reflectors
    reflectors = ['A', 'B', 'C']
    
    # Try different position interpretations
    position_interpretations = [
        ('AAA', '111 = position 1,1,1'),
        ('GZV', 'GZV from header'),
        ('DBR', 'DBR from header'),
        ('SJT', 'From call sign 5JT'),
        ('SJB', 'From call sign SJ2 -> SJB'),
    ]
    
    best_results = []
    
    for reflector in reflectors:
        for pos, desc in position_interpretations:
            try:
                machine = EnigmaMachine.from_key_sheet(
                    rotors=day9_config['rotors'],
                    reflector=reflector,
                    ring_settings=day9_config['rings'],
                    plugboard_settings=day9_config['plugs']
                )
                machine.set_display(pos)
                
                plaintext = machine.process_text(ciphertext)
                score = score_text(plaintext)
                
                print(f"Reflector {reflector}, Pos {pos}: Score {score}")
                print(f"  {desc}")
                print(f"  Text: {plaintext[:60]}...")
                
                if score > 10:
                    best_results.append((reflector, pos, score, plaintext, desc))
                    
            except Exception as e:
                print(f"Error with reflector {reflector}, pos {pos}: {e}")
    
    # Also try without plugboard (maybe it's a training Enigma)
    print(f"\n{'='*50}")
    print("Trying without plugboard...")
    
    for reflector in reflectors:
        for pos, desc in position_interpretations:
            try:
                machine = EnigmaMachine.from_key_sheet(
                    rotors=day9_config['rotors'],
                    reflector=reflector,
                    ring_settings=day9_config['rings'],
                    plugboard_settings=''  # No plugboard
                )
                machine.set_display(pos)
                
                plaintext = machine.process_text(ciphertext)
                score = score_text(plaintext)
                
                print(f"No Plugs, Reflector {reflector}, Pos {pos}: Score {score}")
                print(f"  Text: {plaintext[:60]}...")
                
                if score > 10:
                    best_results.append((reflector, pos, score, plaintext, f"No plugs, {desc}"))
                    
            except Exception as e:
                print(f"Error with no plugs, reflector {reflector}, pos {pos}: {e}")
    
    # Try simple Caesar cipher as backup
    print(f"\n{'='*50}")
    print("Trying simple Caesar cipher as backup...")
    
    clean_cipher = ciphertext.replace(' ', '').replace('\n', '')
    
    for shift in range(1, 26):
        caesar_result = ""
        for char in clean_cipher:
            if char.isalpha():
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                caesar_result += shifted
            else:
                caesar_result += char
        
        if 'USCC' in caesar_result or any(word in caesar_result for word in ['FLAG', 'CIPHER', 'SECRET']):
            print(f"Caesar shift {shift}: {caesar_result}")
            best_results.append(('Caesar', shift, 100, caesar_result, f"Caesar cipher shift {shift}"))
    
    if best_results:
        print(f"\n{'='*60}")
        print("BEST RESULTS FOUND:")
        best_results.sort(key=lambda x: x[2], reverse=True)
        
        for method, pos, score, text, desc in best_results[:3]:
            print(f"\nMethod: {method}, Position: {pos}, Score: {score}")
            print(f"Description: {desc}")
            print(f"Text: {text}")
            
            if 'USCC' in text:
                # Extract flag
                start = text.find('USCC')
                end = text.find('}', start) if '}' in text[start:] else len(text)
                flag = text[start:end+1] if end < len(text) else text[start:]
                print(f"*** FLAG FOUND: {flag} ***")

def score_text(text):
    """Score text for English-like characteristics"""
    score = 0
    
    # High value words
    high_value = ['USCC', 'FLAG', 'CIPHER', 'ENIGMA', 'SECRET', 'CODE', 'MESSAGE', 'BLETCHLEY', 'PARK']
    for word in high_value:
        score += text.count(word) * 20
    
    # Common English words
    common_words = ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'CAN', 'HER', 'WAS', 'ONE', 'OUR', 'HAD', 'USE', 'HAVE', 'WILL', 'BEEN', 'FROM', 'THEY', 'KNOW', 'WANT', 'GOOD', 'MUCH', 'SOME', 'TIME', 'VERY', 'WHEN', 'COME', 'HERE', 'HOW', 'JUST', 'LIKE', 'LONG', 'MAKE', 'MANY', 'OVER', 'SUCH', 'TAKE', 'THAN', 'THEM', 'WELL', 'WERE', 'WITH', 'WORK', 'YEAR', 'YOUR', 'BACK', 'CALL', 'CAME', 'EACH', 'EVEN', 'FIND', 'GIVE', 'HAND', 'HIGH', 'KEEP', 'LAST', 'LEFT', 'LIFE', 'LIVE', 'LOOK', 'MADE', 'MOST', 'MOVE', 'MUST', 'NAME', 'NEED', 'NEXT', 'OPEN', 'PART', 'PLAY', 'RIGHT', 'SAID', 'SAME', 'SEEM', 'SHOW', 'SIDE', 'TELL', 'TURN', 'USED', 'WANT', 'WAYS', 'WEEK', 'WENT', 'WHAT', 'WHERE', 'WHICH', 'WHILE', 'WHO', 'WHY', 'WORD', 'WORK', 'WORLD', 'WOULD', 'WRITE', 'YEAR', 'YOUNG']
    
    for word in common_words:
        score += text.count(word) * 2
    
    # Common digrams
    common_digrams = ['TH', 'HE', 'IN', 'ER', 'AN', 'RE', 'ED', 'ND', 'ON', 'EN', 'AT', 'OU', 'IT', 'IS', 'OR', 'TI', 'AS', 'TO', 'NT', 'NG', 'SE', 'HA', 'VE', 'WA', 'LD', 'LE', 'ST', 'AR', 'TE', 'AL']
    
    for digram in common_digrams:
        score += text.count(digram) * 0.5
    
    return int(score)

if __name__ == "__main__":
    try_alternative_approaches()