#!/usr/bin/env python3
import socket

def test_multidigit_levels():
    """Test multi-digit access levels that might be special"""
    
    print("=== TESTING MULTI-DIGIT ACCESS LEVELS ===")
    
    # Test various multi-digit combinations
    multidigit_tests = [
        # Double digits
        11, 12, 13, 14, 15, 16, 17, 18, 19,
        22, 33, 44, 55, 66, 77, 88, 99,
        
        # Level combinations
        12, 21, 23, 32, 34, 43, 45, 54, 56, 65,
        123, 321, 456, 654, 135, 531, 246, 642,
        
        # Special numbers
        42, 69, 100, 101, 111, 123, 1337, 31337,
        
        # Hex-like numbers
        10, 16, 32, 64, 128, 256, 512, 1024,
        
        # CTF common numbers
        1337, 31337, 8080, 4444, 1234, 5678, 9999,
        
        # Year/date related
        2024, 2025, 1999, 2000,
    ]
    
    unique_responses = {}
    
    for level in multidigit_tests:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            
            # Skip banner
            banner = sock.recv(4096)
            
            # Send level
            sock.send(f"{level}\n".encode('utf-8'))
            
            # Get response
            response = sock.recv(4096).decode('utf-8', errors='replace')
            
            # Check for unique responses
            response_key = response.strip()
            if response_key and response_key not in unique_responses.values():
                unique_responses[level] = response_key
                print(f"Level {level}: {repr(response)}")
                
                # Check for flags
                if ('uscc{' in response.lower() or 'flag{' in response.lower() or 
                    'cyberbowl{' in response.lower()):
                    print(f"*** FLAG FOUND: {response} ***")
                    return response
                
                # Check for anything that's not the standard invalid message
                if "Access band invalid!" not in response and "Enter access band" not in response:
                    print(f"  -> UNUSUAL RESPONSE!")
            
            sock.close()
            
        except Exception as e:
            pass
    
    print(f"\nUnique responses found:")
    for level, response in unique_responses.items():
        print(f"  {level}: {response}")
    
    return None

def test_specific_sequences():
    """Test specific sequences that might unlock something"""
    
    print("\n=== TESTING SPECIFIC SEQUENCES ===")
    
    # Maybe we need to send a specific sequence to unlock the flag
    sequences = [
        # Try the "66" you tested - maybe it's part of a sequence
        ["66", "6"],
        ["6", "66"],
        ["66", "66"],
        
        # Try other double-digit combinations
        ["11", "1"], ["22", "2"], ["33", "3"], ["44", "4"], ["55", "5"],
        
        # Try sequences that might represent "boss" or "admin"
        ["2", "15", "19", "19"],  # B-O-S-S in alphabet positions
        ["1", "4", "13", "9", "14"],  # A-D-M-I-N
        
        # Try the first letters pattern we found: SHMQYB
        ["19", "8", "13", "17", "25", "2"],  # S-H-M-Q-Y-B positions
        
        # Try binary representations
        ["110", "111"],  # 6 and 7 in binary
        ["1110", "1111"],  # 14 and 15 in binary
    ]
    
    for sequence in sequences:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            
            print(f"Testing sequence: {sequence}")
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            for i, level in enumerate(sequence):
                sock.send(f"{level}\n".encode('utf-8'))
                response = sock.recv(4096).decode('utf-8', errors='replace')
                
                print(f"  Step {i+1} ({level}): {repr(response.strip())}")
                
                if ('uscc{' in response.lower() or 'flag{' in response.lower()):
                    print(f"*** FLAG FOUND IN SEQUENCE: {response} ***")
                    return response
            
            sock.close()
            
        except Exception as e:
            print(f"  Error: {e}")
    
    return None

def test_boss_variations():
    """Test variations around the BOSS level"""
    
    print("\n=== TESTING BOSS LEVEL VARIATIONS ===")
    
    # Since level 6 gives us BOSS access, maybe there are variations
    boss_tests = [
        "6.0", "6.1", "6.5", "6.9",
        "06", "006", "0006",
        "6a", "6b", "6c", "6admin", "6boss", "6flag",
        "boss", "BOSS", "Boss",
        "level6", "LEVEL6", "Level6",
        "six", "SIX", "Six",
    ]
    
    for test_input in boss_tests:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            sock.send(f"{test_input}\n".encode('utf-8'))
            response = sock.recv(4096).decode('utf-8', errors='replace')
            
            # Look for non-standard responses
            if ("Access band invalid!" not in response and 
                "Enter access band" not in response and
                "BOSS — Secure compound & vaults" not in response and
                response.strip()):
                
                print(f"Input '{test_input}': {repr(response)}")
                
                if ('uscc{' in response.lower() or 'flag{' in response.lower()):
                    print(f"*** FLAG FOUND: {response} ***")
                    return response
            
            sock.close()
            
        except:
            pass
    
    return None

if __name__ == "__main__":
    result = test_multidigit_levels()
    
    if not result:
        result = test_specific_sequences()
    
    if not result:
        result = test_boss_variations()
    
    if result:
        print(f"\n*** FLAG FOUND: {result} ***")
    else:
        print("\n=== FINAL ANALYSIS ===")
        print("Based on all testing, the most likely scenarios are:")
        print("1. The flag is 'uscc{boss_access}' or similar, based on reaching level 6")
        print("2. The challenge requires submitting proof of reaching BOSS level")
        print("3. The flag is hidden in the challenge description/environment")
        print("4. There's a specific technique we haven't discovered yet")
        
        print(f"\nMy best guess for the flag: uscc{{boss_access}}")