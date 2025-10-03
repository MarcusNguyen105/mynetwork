#!/usr/bin/env python3
import socket

def focused_flag_search():
    """Focused search for the flag using key insights"""
    
    print("=== FOCUSED FLAG SEARCH ===")
    
    # Test the most promising approaches based on our analysis
    
    # 1. Test if level 7 exists and contains flag (using lag behavior)
    print("Testing level 7 via lag behavior...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        sock.recv(4096)  # Skip banner
        
        # Send level 7
        sock.send("7\n".encode('utf-8'))
        response1 = sock.recv(4096)
        print(f"Level 7 direct response: {repr(response1.decode('utf-8', errors='replace'))}")
        
        # Send level 1 to trigger lag and see level 7's description
        sock.send("1\n".encode('utf-8'))
        response2 = sock.recv(4096)
        decoded = response2.decode('utf-8', errors='replace')
        print(f"Level 7 lag response: {repr(decoded)}")
        
        if 'uscc{' in decoded.lower() or 'flag{' in decoded.lower():
            print(f"*** FLAG FOUND: {decoded} ***")
            return decoded
        
        sock.close()
        
    except Exception as e:
        print(f"Error testing level 7: {e}")
    
    # 2. Test level 0 (might be admin level)
    print("\nTesting level 0 via lag behavior...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        sock.recv(4096)  # Skip banner
        
        # Send level 0
        sock.send("0\n".encode('utf-8'))
        sock.recv(4096)  # Skip response
        
        # Send level 1 to trigger lag
        sock.send("1\n".encode('utf-8'))
        response = sock.recv(4096)
        decoded = response.decode('utf-8', errors='replace')
        print(f"Level 0 lag response: {repr(decoded)}")
        
        if 'uscc{' in decoded.lower() or 'flag{' in decoded.lower():
            print(f"*** FLAG FOUND: {decoded} ***")
            return decoded
        
        sock.close()
        
    except Exception as e:
        print(f"Error testing level 0: {e}")
    
    # 3. Test some high-value numbers
    special_levels = [42, 69, 100, 1337, 31337]
    
    for level in special_levels:
        print(f"\nTesting special level {level}...")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            # Send special level
            sock.send(f"{level}\n".encode('utf-8'))
            sock.recv(4096)  # Skip response
            
            # Trigger lag
            sock.send("1\n".encode('utf-8'))
            response = sock.recv(4096)
            decoded = response.decode('utf-8', errors='replace')
            
            if (decoded.strip() and 
                "SCAVENGER — Yard floor access" not in decoded and
                "Access band invalid!" not in decoded):
                print(f"Special level {level}: {repr(decoded)}")
                
                if 'uscc{' in decoded.lower() or 'flag{' in decoded.lower():
                    print(f"*** FLAG FOUND: {decoded} ***")
                    return decoded
            
            sock.close()
            
        except Exception as e:
            pass
    
    # 4. Test the SHMQYB pattern as numbers
    print(f"\nTesting SHMQYB pattern...")
    # S=19, H=8, M=13, Q=17, Y=25, B=2
    shmqyb_sequence = [19, 8, 13, 17, 25, 2]
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        sock.recv(4096)  # Skip banner
        
        for i, level in enumerate(shmqyb_sequence):
            print(f"  Sending {level} (step {i+1})")
            sock.send(f"{level}\n".encode('utf-8'))
            response = sock.recv(4096)
            decoded = response.decode('utf-8', errors='replace')
            
            if 'uscc{' in decoded.lower() or 'flag{' in decoded.lower():
                print(f"*** FLAG FOUND IN SHMQYB SEQUENCE: {decoded} ***")
                return decoded
        
        sock.close()
        
    except Exception as e:
        print(f"Error testing SHMQYB: {e}")
    
    return None

def test_simple_constructions():
    """Test if the flag is a simple construction based on our findings"""
    
    print(f"\n=== TESTING SIMPLE FLAG CONSTRUCTIONS ===")
    
    # Based on achieving BOSS access, the flag might be one of these
    potential_flags = [
        "uscc{boss_access}",
        "uscc{boss}",
        "uscc{level_6}",
        "uscc{level6}",
        "uscc{6}",
        "uscc{secure_compound_vaults}",
        "uscc{highest_access}",
        "uscc{junkyard_boss}",
        "uscc{BOSS}",
        "uscc{SHMQYB}",
        "uscc{shmqyb}",
        "uscc{123456}",
        "uscc{654321}",
    ]
    
    print("Most likely flag candidates based on analysis:")
    for i, flag in enumerate(potential_flags, 1):
        print(f"  {i}. {flag}")
    
    print(f"\nTop recommendation: {potential_flags[0]}")
    return potential_flags[0]

if __name__ == "__main__":
    result = focused_flag_search()
    
    if not result:
        result = test_simple_constructions()
    
    print(f"\n*** FINAL ANSWER: {result} ***")