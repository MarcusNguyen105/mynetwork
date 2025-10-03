#!/usr/bin/env python3
import socket
import time

def final_flag_attempt():
    """Final comprehensive attempt to find the flag"""
    
    print("=== FINAL FLAG HUNTING ATTEMPT ===")
    
    # Maybe the flag is revealed by accessing levels in the order of their numbers
    # but using the lag behavior in a specific way
    
    approaches = [
        # Try accessing each level twice
        ("double_access", [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]),
        
        # Try the first letters pattern: SHMQYB might be a clue
        # S=19, H=8, M=13, Q=17, Y=25, B=2 (if we map to numbers)
        ("first_letters_numeric", [19, 8, 13, 17, 25, 2]),
        
        # Try reverse order multiple times
        ("reverse_triple", [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]),
        
        # Try binary pattern (1-6 in binary: 001, 010, 011, 100, 101, 110)
        ("binary_pattern", [1, 2, 3, 4, 5, 6, 0, 1, 0, 0, 1, 0]),
        
        # Try Fibonacci-like pattern
        ("fibonacci", [1, 1, 2, 3, 5, 6, 1, 1, 2, 3, 5, 6]),
        
        # Try accessing in the order of description lengths
        ("by_length", [1, 3, 6, 2, 4, 5, 1, 3, 6, 2, 4, 5]),
        
        # Try a long sequence to see if something unlocks after many accesses
        ("long_sequence", list(range(1, 7)) * 10),  # 1-6 repeated 10 times
        
        # Try the "boss" level multiple times
        ("boss_focus", [6] * 20),
        
        # Try alternating between 1 and 6
        ("alternating_1_6", [1, 6] * 10),
        
        # Try going up then down repeatedly
        ("up_down", [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1] * 3),
    ]
    
    for approach_name, sequence in approaches:
        print(f"\n--- Testing approach: {approach_name} ---")
        result = test_extended_sequence(sequence, approach_name)
        if result:
            return result
    
    # Try some special edge cases with the lag behavior
    print(f"\n--- Testing edge cases ---")
    
    edge_cases = [
        # Try to cause buffer overflow with the lag
        ([6] + [1] * 100, "buffer_test_1"),
        ([1] + [6] * 100, "buffer_test_6"),
        
        # Try invalid levels in specific patterns
        ([0, 1, 7, 2, 8, 3], "invalid_pattern_1"),
        ([6, 0, 5, 7, 4, 8], "invalid_pattern_2"),
        
        # Try very high numbers
        ([999, 1, 1000, 2, 9999, 3], "high_numbers"),
        
        # Try negative numbers in pattern
        ([-1, 1, -2, 2, -3, 3], "negative_pattern"),
    ]
    
    for sequence, name in edge_cases:
        print(f"Testing edge case: {name}")
        result = test_extended_sequence(sequence, name)
        if result:
            return result
    
    # Final desperate attempt - try to find any non-standard response
    print(f"\n--- Final scan for any unusual responses ---")
    return final_scan()

def test_extended_sequence(sequence, name):
    """Test an extended sequence and look for flags"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(30)  # Longer timeout for long sequences
        
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        sock.recv(4096)  # Skip banner
        
        responses = []
        
        for i, level in enumerate(sequence):
            try:
                sock.send(f"{level}\n".encode('utf-8'))
                
                # Get response
                sock.settimeout(3)
                response = sock.recv(4096)
                decoded = response.decode('utf-8', errors='replace')
                
                # Check for flag immediately
                if ('uscc{' in decoded.lower() or 'flag{' in decoded.lower() or 
                    'cyberbowl{' in decoded.lower()):
                    print(f"*** FLAG FOUND in {name} at step {i+1}: {decoded} ***")
                    return decoded
                
                # Store unusual responses
                if (decoded.strip() and 'Enter access band' not in decoded and 
                    len(decoded.strip()) > 5):
                    responses.append((i, level, decoded))
                
                # Every 10 steps, check if we got something interesting
                if i > 0 and i % 10 == 0:
                    print(f"  Step {i}: {len(responses)} unusual responses so far")
                
            except socket.timeout:
                pass
            except Exception as e:
                print(f"  Error at step {i}: {e}")
                break
        
        # Check if we got any interesting accumulated responses
        if responses:
            print(f"  {name} produced {len(responses)} unusual responses:")
            for i, level, resp in responses[-5:]:  # Show last 5
                print(f"    Step {i} (level {level}): {repr(resp[:50])}...")
        
        sock.close()
        
    except Exception as e:
        print(f"Error testing {name}: {e}")
    
    return None

def final_scan():
    """Final scan trying everything we can think of"""
    
    # Try every possible single character input
    for char_code in range(256):
        if char_code in [10, 13]:  # Skip newlines
            continue
            
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            # Send the character
            sock.send(bytes([char_code, 10]))  # char + newline
            
            response = sock.recv(4096)
            decoded = response.decode('utf-8', errors='replace')
            
            if ('uscc{' in decoded.lower() or 'flag{' in decoded.lower()):
                print(f"*** FLAG FOUND with char {char_code}: {decoded} ***")
                return decoded
            
            # Check for any non-standard response
            if (decoded.strip() and 'Enter access band' not in decoded and 
                'Access band invalid' not in decoded and len(decoded.strip()) > 10):
                print(f"Unusual response for char {char_code}: {repr(decoded)}")
            
            sock.close()
            
        except:
            pass
    
    return None

if __name__ == "__main__":
    result = final_flag_attempt()
    
    if result:
        print(f"\n*** FINAL FLAG FOUND: {result} ***")
    else:
        print("\n*** NO FLAG FOUND ***")
        print("The flag might be:")
        print("1. Hidden in the service in a way we haven't discovered")
        print("2. Require a different approach (like source code analysis)")
        print("3. Be in the challenge description or environment")
        print("4. Require exploitation of a vulnerability we haven't found")