#!/usr/bin/env python3
import socket
import time

def analyze_response_lag():
    """Analyze the lag/delay in responses - previous level shown"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        
        print("=== RESPONSE LAG ANALYSIS ===")
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        
        # Skip banner
        banner = sock.recv(4096)
        print(f"Banner: {banner.decode('utf-8', errors='replace')}")
        
        # Test the lag pattern systematically
        test_sequence = [1, 2, 3, 4, 5, 6, 1, 6, 2, 5, 3, 4]
        
        for i, level in enumerate(test_sequence):
            print(f"\n--- Step {i+1}: Sending level {level} ---")
            
            sock.send(f"{level}\n".encode('utf-8'))
            
            # Get immediate response
            response = sock.recv(4096)
            decoded = response.decode('utf-8', errors='replace')
            
            print(f"Sent: {level}")
            print(f"Response: {repr(decoded)}")
            
            # Try to map what we're seeing
            if "SCAVENGER" in decoded:
                print("  -> Shows SCAVENGER (Level 1)")
            elif "HAULER" in decoded:
                print("  -> Shows HAULER (Level 2)")
            elif "MECHANIC" in decoded:
                print("  -> Shows MECHANIC (Level 3)")
            elif "QUARRY FOREMAN" in decoded:
                print("  -> Shows QUARRY FOREMAN (Level 4)")
            elif "YARD MANAGER" in decoded:
                print("  -> Shows YARD MANAGER (Level 5)")
            elif "BOSS" in decoded:
                print("  -> Shows BOSS (Level 6)")
            elif "Enter access band" in decoded:
                print("  -> Shows prompt (initial state)")
            else:
                print(f"  -> Unknown response: {decoded}")
        
        sock.close()
        
    except Exception as e:
        print(f"Error: {e}")

def test_specific_lag_sequence():
    """Test if there's a specific sequence that reveals the flag due to lag"""
    
    # Theory: If the system shows the previous level's description,
    # maybe there's a "level 0" or "level 7" that contains the flag
    # and we can access it by sending the right sequence
    
    sequences_to_test = [
        # Try to access a hypothetical "level 0" by going 1->0
        ([1, 0], "Trying to access level 0 via 1->0"),
        # Try to access a hypothetical "level 7" by going 6->7  
        ([6, 7], "Trying to access level 7 via 6->7"),
        # Try other out-of-bounds
        ([6, 8], "Trying to access level 8 via 6->8"),
        ([5, -1], "Trying to access level -1 via 5->-1"),
        # Try going to 6 then back to 1, then to an invalid level
        ([6, 1, 0], "6->1->0 sequence"),
        ([6, 1, 7], "6->1->7 sequence"),
        # Try accessing all levels then an invalid one
        ([1, 2, 3, 4, 5, 6, 7], "All levels then 7"),
        ([1, 2, 3, 4, 5, 6, 0], "All levels then 0"),
    ]
    
    for sequence, description in sequences_to_test:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            
            print(f"\n=== {description} ===")
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            
            # Skip banner
            sock.recv(4096)
            
            for i, level in enumerate(sequence):
                print(f"Step {i+1}: Sending {level}")
                sock.send(f"{level}\n".encode('utf-8'))
                
                try:
                    response = sock.recv(4096)
                    decoded = response.decode('utf-8', errors='replace')
                    print(f"  Response: {repr(decoded)}")
                    
                    # Check for flag patterns
                    if ('uscc{' in decoded.lower() or 'flag{' in decoded.lower() or 
                        ('{' in decoded and '}' in decoded and len(decoded.strip()) > 20)):
                        print(f"*** POTENTIAL FLAG FOUND: {decoded} ***")
                        return decoded
                        
                    # Check for any unusual responses
                    if ("Enter access band" not in decoded and 
                        "SCAVENGER" not in decoded and "HAULER" not in decoded and
                        "MECHANIC" not in decoded and "QUARRY FOREMAN" not in decoded and
                        "YARD MANAGER" not in decoded and "BOSS" not in decoded and
                        decoded.strip() != ""):
                        print(f"*** UNUSUAL RESPONSE: {decoded} ***")
                        
                except socket.timeout:
                    print("  No response (timeout)")
                except Exception as e:
                    print(f"  Error: {e}")
                    break
            
            sock.close()
            
        except Exception as e:
            print(f"Error with sequence {sequence}: {e}")
    
    return None

def test_buffer_overflow_approach():
    """Test if we can cause buffer overflow to reveal flag"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        
        print("\n=== BUFFER OVERFLOW TEST ===")
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        
        # Skip banner
        sock.recv(4096)
        
        # Try very long inputs
        long_inputs = [
            "6" + "A" * 1000,
            "6" + "\x00" * 100,
            "6" + "1" * 100,
            "A" * 1000,
            "1" * 1000,
            "6\n" * 100,
        ]
        
        for long_input in long_inputs:
            try:
                print(f"Sending long input (length {len(long_input)})")
                sock.send(long_input.encode('utf-8', errors='replace'))
                
                response = sock.recv(4096)
                decoded = response.decode('utf-8', errors='replace')
                
                if decoded and "Enter access band" not in decoded:
                    print(f"Unusual response to long input: {repr(decoded)}")
                    
                    if 'uscc{' in decoded.lower() or 'flag{' in decoded.lower():
                        print(f"*** FLAG FOUND: {decoded} ***")
                        return decoded
                        
            except Exception as e:
                print(f"Error with long input: {e}")
                break
        
        sock.close()
        
    except Exception as e:
        print(f"Buffer overflow test error: {e}")
    
    return None

if __name__ == "__main__":
    analyze_response_lag()
    
    result = test_specific_lag_sequence()
    if result:
        print(f"\n*** FLAG FOUND: {result} ***")
    else:
        result = test_buffer_overflow_approach()
        if result:
            print(f"\n*** FLAG FOUND: {result} ***")
        else:
            print("\nNo flag found with lag analysis approach.")