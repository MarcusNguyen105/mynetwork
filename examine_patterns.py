#!/usr/bin/env python3

def examine_patterns():
    """Examine the patterns that showed USCC"""
    
    groups = ['XLWHF', 'DJKUC', 'ZONWZ', 'UFDGB', 'SIILK',
              'GSOBR', 'NPPMF', 'BWFTU', 'CHPCO', 'UUBMB',
              'NUUMW', 'HMPJG', 'JGJPM', 'AXKPY', 'FENEP',
              'LKHGM', 'LUPUJ', 'WWCZO', 'YATTS', 'CBSKI',
              'QFKSG', 'ADRPZ', 'J']
    
    print("Examining the patterns that contained USCC...")
    
    # Pattern 4: every 4th group starting from different positions
    print(f"\nPattern 4 analysis:")
    pattern4_text = ""
    for start in range(4):
        for i in range(start, len(groups), 4):
            pattern4_text += groups[i]
    
    print(f"Pattern 4 text: {pattern4_text}")
    
    # Apply Caesar shift 3
    result4 = ""
    for char in pattern4_text:
        if char.isalpha():
            shifted = chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
            result4 += shifted
    
    print(f"Pattern 4 + Caesar 3: {result4}")
    
    # Find USCC and extract context
    uscc_pos = result4.find('USCC')
    if uscc_pos != -1:
        print(f"USCC found at position {uscc_pos}")
        context = result4[max(0, uscc_pos-10):uscc_pos+40]
        print(f"Context: ...{context}...")
        
        # Look for flag pattern
        after_uscc = result4[uscc_pos+4:]
        print(f"After USCC: {after_uscc}")
        
        # Try to find a reasonable flag ending
        flag_content = ""
        for char in after_uscc:
            if char.isalnum() or char in '_-':
                flag_content += char
            else:
                break
        
        if len(flag_content) > 5:
            potential_flag = f"USCC{{{flag_content}}}"
            print(f"Potential flag from pattern 4: {potential_flag}")
    
    # Pattern 5: every 5th group starting from different positions  
    print(f"\nPattern 5 analysis:")
    pattern5_text = ""
    for start in range(5):
        for i in range(start, len(groups), 5):
            pattern5_text += groups[i]
    
    print(f"Pattern 5 text: {pattern5_text}")
    
    # Apply Caesar shift 3
    result5 = ""
    for char in pattern5_text:
        if char.isalpha():
            shifted = chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
            result5 += shifted
    
    print(f"Pattern 5 + Caesar 3: {result5}")
    
    # Find USCC and extract context
    uscc_pos = result5.find('USCC')
    if uscc_pos != -1:
        print(f"USCC found at position {uscc_pos}")
        context = result5[max(0, uscc_pos-10):uscc_pos+40]
        print(f"Context: ...{context}...")
        
        # Look for flag pattern
        after_uscc = result5[uscc_pos+4:]
        print(f"After USCC: {after_uscc}")
        
        # Try to find a reasonable flag ending
        flag_content = ""
        for char in after_uscc:
            if char.isalnum() or char in '_-':
                flag_content += char
            else:
                break
        
        if len(flag_content) > 5:
            potential_flag = f"USCC{{{flag_content}}}"
            print(f"Potential flag from pattern 5: {potential_flag}")
    
    # Let me also try other Caesar shifts on these patterns
    print(f"\nTrying other Caesar shifts on pattern 4:")
    
    for shift in range(1, 26):
        result = ""
        for char in pattern4_text:
            if char.isalpha():
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result += shifted
        
        if 'USCC{' in result and '}' in result:
            print(f"*** COMPLETE FLAG found with shift {shift}! ***")
            start = result.find('USCC{')
            end = result.find('}', start) + 1
            flag = result[start:end]
            print(f"FLAG: {flag}")
            return flag
        elif 'USCC' in result:
            uscc_pos = result.find('USCC')
            context = result[uscc_pos:uscc_pos+20]
            print(f"Shift {shift:2d}: USCC found - {context}")
    
    print(f"\nTrying other Caesar shifts on pattern 5:")
    
    for shift in range(1, 26):
        result = ""
        for char in pattern5_text:
            if char.isalpha():
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result += shifted
        
        if 'USCC{' in result and '}' in result:
            print(f"*** COMPLETE FLAG found with shift {shift}! ***")
            start = result.find('USCC{')
            end = result.find('}', start) + 1
            flag = result[start:end]
            print(f"FLAG: {flag}")
            return flag
        elif 'USCC' in result:
            uscc_pos = result.find('USCC')
            context = result[uscc_pos:uscc_pos+20]
            print(f"Shift {shift:2d}: USCC found - {context}")
    
    return None

if __name__ == "__main__":
    flag = examine_patterns()
    if flag:
        print(f"\n{'='*60}")
        print(f"FINAL FLAG: {flag}")
    else:
        print("\nNeed to examine the USCC contexts more carefully...")