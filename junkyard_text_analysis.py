#!/usr/bin/env python3
import socket
import re

def analyze_exact_text():
    """Analyze the exact text responses for hidden patterns"""
    
    print("=== ANALYZING EXACT TEXT FOR HIDDEN PATTERNS ===")
    
    # Get all the exact responses
    level_responses = {}
    
    for level in range(1, 7):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            # Use lag behavior to get exact response
            sock.send(f"{level}\n".encode('utf-8'))
            sock.recv(4096)  # Skip prompt
            
            sock.send("1\n".encode('utf-8'))  # Trigger lag
            response = sock.recv(4096)
            
            level_responses[level] = response
            print(f"Level {level} raw bytes: {response}")
            print(f"Level {level} decoded: {repr(response.decode('utf-8', errors='replace'))}")
            
            sock.close()
            
        except Exception as e:
            print(f"Error getting level {level}: {e}")
    
    # Analyze the raw bytes for hidden data
    print(f"\n=== ANALYZING RAW BYTES ===")
    
    all_bytes = b""
    for level in range(1, 7):
        if level in level_responses:
            all_bytes += level_responses[level]
    
    print(f"All bytes combined: {all_bytes}")
    print(f"All bytes hex: {all_bytes.hex()}")
    
    # Look for patterns in the hex
    hex_str = all_bytes.hex()
    print(f"Hex string: {hex_str}")
    
    # Check if there are any flag patterns in hex
    # uscc{ in hex would be: 75736363 7b
    if '757363637b' in hex_str:
        print("Found 'uscc{' pattern in hex!")
    
    # Look for other common patterns
    patterns = {
        'flag': '666c6167',
        'ctf': '637466',
        'cyberbowl': '6379626572626f776c',
    }
    
    for pattern_name, pattern_hex in patterns.items():
        if pattern_hex in hex_str:
            print(f"Found '{pattern_name}' pattern in hex!")
    
    return None

def test_exact_sequences():
    """Test very specific sequences that might work"""
    
    print(f"\n=== TESTING EXACT SEQUENCES ===")
    
    # Maybe the flag is revealed by a very specific sequence
    sequences_to_test = [
        # Try the exact order from your manual testing
        [6, 6],  # You tried 66, maybe it's 6 then 6
        [6, "6"],  # String version
        
        # Try all levels in exact order
        [1, 2, 3, 4, 5, 6],
        
        # Try reverse order  
        [6, 5, 4, 3, 2, 1],
        
        # Try the first letters as numbers: SHMQYB = 19,8,13,17,25,2
        [19, 8, 13, 17, 25, 2],
        
        # Try some other patterns
        ["admin", "6"],
        ["root", "6"], 
        ["debug", "6"],
        ["flag", "6"],
        
        # Try accessing 6 multiple times
        [6, 6, 6],
        [6, 6, 6, 6, 6, 6],
        
        # Try some mathematical sequences
        [1, 1, 2, 3, 5, 6],  # Fibonacci-like ending in 6
        [2, 4, 6],  # Even numbers
        [1, 3, 5],  # Odd numbers
    ]
    
    for sequence in sequences_to_test:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            
            print(f"Testing sequence: {sequence}")
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            for i, item in enumerate(sequence):
                sock.send(f"{item}\n".encode('utf-8'))
                response = sock.recv(4096).decode('utf-8', errors='replace')
                
                print(f"  Step {i+1} ({item}): {repr(response.strip())}")
                
                if 'uscc{' in response.lower() or 'flag{' in response.lower():
                    print(f"*** FLAG FOUND: {response} ***")
                    return response
            
            # Try one final command after the sequence
            sock.send("flag\n".encode('utf-8'))
            final_response = sock.recv(4096).decode('utf-8', errors='replace')
            if final_response.strip() and 'Enter access band' not in final_response:
                print(f"  Final response: {repr(final_response)}")
                if 'uscc{' in final_response.lower():
                    return final_response
            
            sock.close()
            
        except Exception as e:
            print(f"  Error: {e}")
    
    return None

def test_steganography():
    """Look for steganographic patterns in the text"""
    
    print(f"\n=== TESTING STEGANOGRAPHIC PATTERNS ===")
    
    # The level descriptions
    descriptions = [
        "SCAVENGER — Yard floor access",
        "HAULER — Broken-but-usable stock", 
        "MECHANIC — Engine bays & bins",
        "QUARRY FOREMAN — Heavy salvage ops",
        "YARD MANAGER — Central yard systems",
        "BOSS — Secure compound & vaults"
    ]
    
    print("Level descriptions:")
    for i, desc in enumerate(descriptions, 1):
        print(f"  {i}: {desc}")
    
    # Check various patterns
    print(f"\nFirst letters: {''.join([desc[0] for desc in descriptions])}")
    print(f"Last letters: {''.join([desc[-1] for desc in descriptions])}")
    
    # Check first letter of each word
    all_words = []
    for desc in descriptions:
        words = desc.replace('—', ' ').split()
        all_words.extend(words)
    
    first_letters_all_words = ''.join([word[0] for word in all_words])
    print(f"First letters of all words: {first_letters_all_words}")
    
    # Check if any of these spell something
    # Maybe we need to convert to numbers or use as input
    
    # Try using first letters as input
    first_letters = "SHMQYB"
    print(f"\nTrying first letters as input: {first_letters}")
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        sock.recv(4096)  # Skip banner
        
        sock.send(f"{first_letters}\n".encode('utf-8'))
        response = sock.recv(4096).decode('utf-8', errors='replace')
        
        print(f"Response to SHMQYB: {repr(response)}")
        
        if 'uscc{' in response.lower():
            return response
        
        sock.close()
        
    except Exception as e:
        print(f"Error testing SHMQYB: {e}")
    
    return None

if __name__ == "__main__":
    result = analyze_exact_text()
    
    if not result:
        result = test_exact_sequences()
    
    if not result:
        result = test_steganography()
    
    if result:
        print(f"\n*** FLAG FOUND: {result} ***")
    else:
        print(f"\n*** STILL NO FLAG FOUND ***")
        print("Let me try one more approach - maybe the flag is constructed differently...")
        
        # Maybe the flag is based on the exact text or a hash of it
        descriptions = [
            "SCAVENGER — Yard floor access",
            "HAULER — Broken-but-usable stock", 
            "MECHANIC — Engine bays & bins",
            "QUARRY FOREMAN — Heavy salvage ops",
            "YARD MANAGER — Central yard systems",
            "BOSS — Secure compound & vaults"
        ]
        
        # Try various constructions
        constructions = [
            f"uscc{{{descriptions[5].lower().replace(' ', '_').replace('—', '')}}}",  # BOSS description
            f"uscc{{{descriptions[5].split()[0].lower()}}}",  # Just "boss"
            "uscc{secure_compound_vaults}",
            "uscc{compound_vaults}",
            "uscc{vaults}",
            "uscc{secure_compound}",
            "uscc{compound}",
            "uscc{secure_vaults}",
            "uscc{boss_secure_compound_vaults}",
        ]
        
        print("Potential flag constructions based on BOSS description:")
        for construction in constructions:
            print(f"  {construction}")
        
        print(f"\nMy best new guess: uscc{{secure_compound_vaults}}")