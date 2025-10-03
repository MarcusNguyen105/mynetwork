#!/usr/bin/env python3
import socket
import time

def comprehensive_flag_hunt():
    """Comprehensive hunt for the flag using all approaches"""
    
    # Test a wide range of special levels
    special_levels = []
    
    # Negative numbers
    special_levels.extend(range(-10, 0))
    
    # Numbers above 6
    special_levels.extend(range(7, 20))
    special_levels.extend([50, 99, 100, 127, 128, 255, 256, 1000, 9999])
    
    # String inputs that might be special
    string_levels = [
        "admin", "root", "flag", "boss", "secret", "hidden", "debug", "test",
        "super", "master", "god", "dev", "developer", "backdoor", "override",
        "bypass", "unlock", "open", "show", "reveal", "password", "key",
        "vault", "secure", "compound", "junkyard", "terminal", "access",
        "system", "manager", "foreman", "mechanic", "hauler", "scavenger"
    ]
    special_levels.extend(string_levels)
    
    found_flags = []
    unusual_responses = []
    
    for special_level in special_levels:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(8)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            # Send special level
            sock.send(f"{special_level}\n".encode('utf-8'))
            response1 = sock.recv(4096)
            
            # Send trigger level to see the lag response
            sock.send("1\n".encode('utf-8'))
            response2 = sock.recv(4096)
            
            decoded = response2.decode('utf-8', errors='replace')
            
            # Check for flag patterns
            if ('uscc{' in decoded.lower() or 'flag{' in decoded.lower() or 
                ('ctf{' in decoded.lower()) or ('cyberbowl{' in decoded.lower())):
                print(f"*** FLAG FOUND WITH LEVEL {special_level}: {decoded} ***")
                found_flags.append((special_level, decoded))
            
            # Check for unusual responses (not standard level descriptions)
            standard_responses = [
                "SCAVENGER — Yard floor access\n",
                "HAULER — Broken-but-usable stock\n", 
                "MECHANIC — Engine bays & bins\n",
                "QUARRY FOREMAN — Heavy salvage ops\n",
                "YARD MANAGER — Central yard systems\n",
                "BOSS — Secure compound & vaults\n",
                "\nEnter access band (1-6): ",
                "",
                "Access band invalid!\n"
            ]
            
            if decoded not in standard_responses and len(decoded.strip()) > 3:
                print(f"Level {special_level}: {repr(decoded)}")
                unusual_responses.append((special_level, decoded))
                
                # Check if this unusual response might contain encoded flag
                if len(decoded.strip()) > 20:  # Substantial content
                    print(f"  -> Substantial unusual response, might contain flag")
            
            sock.close()
            
        except Exception as e:
            # Skip errors for most invalid inputs
            pass
    
    # Test some specific sequences that might unlock flags
    print("\n=== TESTING SPECIFIC SEQUENCES ===")
    
    sequences = [
        # Try to access a "level 7" which might be admin/flag level
        [7, 1],
        [8, 1], 
        [9, 1],
        [10, 1],
        # Try negative levels
        [-1, 1],
        [-2, 1],
        # Try going from highest to lowest then to special
        [6, 1, 7],
        [6, 1, 0],
        # Try all levels then special
        [1, 2, 3, 4, 5, 6, 7],
        [6, 5, 4, 3, 2, 1, 0],
    ]
    
    for sequence in sequences:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            print(f"Testing sequence: {sequence}")
            
            for i, level in enumerate(sequence):
                sock.send(f"{level}\n".encode('utf-8'))
                response = sock.recv(4096)
                decoded = response.decode('utf-8', errors='replace')
                
                if ('uscc{' in decoded.lower() or 'flag{' in decoded.lower()):
                    print(f"*** FLAG FOUND IN SEQUENCE {sequence} AT STEP {i+1}: {decoded} ***")
                    found_flags.append((f"sequence_{sequence}_step_{i+1}", decoded))
                
                if len(decoded.strip()) > 30 and "Enter access band" not in decoded:
                    print(f"  Step {i+1} ({level}): {repr(decoded)}")
            
            sock.close()
            
        except Exception as e:
            print(f"Error with sequence {sequence}: {e}")
    
    # Summary
    print(f"\n=== SUMMARY ===")
    print(f"Found {len(found_flags)} potential flags:")
    for level, flag in found_flags:
        print(f"  {level}: {flag}")
    
    print(f"\nFound {len(unusual_responses)} unusual responses:")
    for level, response in unusual_responses[:10]:  # Show first 10
        print(f"  {level}: {response.strip()}")
    
    return found_flags

if __name__ == "__main__":
    flags = comprehensive_flag_hunt()
    
    if flags:
        print(f"\n*** BEST FLAG CANDIDATE: {flags[0][1]} ***")
    else:
        print("\nNo flags found. The flag might be hidden in a different way.")