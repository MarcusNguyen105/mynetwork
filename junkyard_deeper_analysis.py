#!/usr/bin/env python3
import socket
import time
import string

def test_all_ascii_inputs():
    """Test every ASCII character as input to find hidden functionality"""
    
    print("=== TESTING ALL ASCII CHARACTERS ===")
    
    findings = {}
    
    # Test every printable ASCII character
    for i in range(32, 127):
        char = chr(i)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            # Send the character
            sock.send(f"{char}\n".encode('utf-8'))
            response = sock.recv(4096).decode('utf-8', errors='replace')
            
            # Store unique responses
            if response.strip() and response not in findings.values():
                findings[char] = response
                print(f"'{char}' (ASCII {i}): {repr(response)}")
                
                # Check for flag
                if 'uscc{' in response.lower() or 'flag{' in response.lower():
                    print(f"*** FLAG FOUND: {response} ***")
                    return response
            
            sock.close()
            
        except:
            pass
    
    print(f"\nFound {len(findings)} unique responses for ASCII characters")
    return None

def test_binary_inputs():
    """Test binary data inputs"""
    
    print("\n=== TESTING BINARY INPUTS ===")
    
    # Test various binary patterns
    binary_tests = [
        b'\x00',  # Null byte
        b'\x01',  # SOH
        b'\x02',  # STX  
        b'\x03',  # ETX
        b'\x04',  # EOT
        b'\x1b',  # ESC
        b'\x7f',  # DEL
        b'\xff',  # 255
        b'\x00\x01\x02\x03',  # Sequence
        b'6\x00',  # 6 + null
        b'\x006',  # null + 6
        b'6\x00flag',  # 6 + null + flag
    ]
    
    for binary_data in binary_tests:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            # Send binary data + newline
            sock.send(binary_data + b'\n')
            response = sock.recv(4096).decode('utf-8', errors='replace')
            
            if (response.strip() and 
                "Enter access band" not in response and
                "Access band invalid" not in response):
                print(f"Binary {repr(binary_data)}: {repr(response)}")
                
                if 'uscc{' in response.lower():
                    print(f"*** FLAG FOUND: {response} ***")
                    return response
            
            sock.close()
            
        except:
            pass
    
    return None

def test_long_connection_with_timing():
    """Test keeping connection open longer and trying timing attacks"""
    
    print("\n=== TESTING LONG CONNECTION WITH TIMING ===")
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(30)
        
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        banner = sock.recv(4096).decode('utf-8', errors='replace')
        print(f"Banner: {repr(banner)}")
        
        # Access level 6 (BOSS)
        sock.send("6\n".encode('utf-8'))
        response = sock.recv(4096).decode('utf-8', errors='replace')
        print(f"Level 6 response: {repr(response)}")
        
        # Wait longer to see if anything happens
        print("Waiting 10 seconds after BOSS access...")
        time.sleep(10)
        
        # Try to receive more data
        try:
            sock.settimeout(5)
            additional = sock.recv(4096).decode('utf-8', errors='replace')
            if additional.strip():
                print(f"Additional data after wait: {repr(additional)}")
                if 'uscc{' in additional.lower():
                    return additional
        except socket.timeout:
            print("No additional data after wait")
        
        # Try sending empty lines or special sequences
        test_sequences = [
            "",
            " ",
            "\t",
            "\r",
            "\n",
            "flag",
            "show flag",
            "cat flag",
            "ls",
            "help",
            "?",
            "exit",
            "quit",
            "admin",
            "root",
            "debug",
            "test",
            "vault",
            "secure",
            "compound",
            "boss",
        ]
        
        for seq in test_sequences:
            try:
                print(f"Trying: {repr(seq)}")
                sock.send(f"{seq}\n".encode('utf-8'))
                
                sock.settimeout(3)
                response = sock.recv(4096).decode('utf-8', errors='replace')
                
                if response.strip():
                    print(f"  Response: {repr(response)}")
                    if 'uscc{' in response.lower():
                        print(f"*** FLAG FOUND: {response} ***")
                        return response
                
            except socket.timeout:
                pass
            except Exception as e:
                print(f"  Error: {e}")
                break
        
        sock.close()
        
    except Exception as e:
        print(f"Long connection error: {e}")
    
    return None

def test_protocol_manipulation():
    """Test protocol-level manipulation"""
    
    print("\n=== TESTING PROTOCOL MANIPULATION ===")
    
    # Test sending data without newlines
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        sock.recv(4096)  # Skip banner
        
        # Send "6" without newline and wait
        print("Sending '6' without newline...")
        sock.send("6".encode('utf-8'))
        
        time.sleep(2)
        
        # Now send newline
        sock.send("\n".encode('utf-8'))
        response = sock.recv(4096).decode('utf-8', errors='replace')
        print(f"Response: {repr(response)}")
        
        # Try sending more data
        sock.send("flag\n".encode('utf-8'))
        response2 = sock.recv(4096).decode('utf-8', errors='replace')
        if response2.strip():
            print(f"Additional response: {repr(response2)}")
            if 'uscc{' in response2.lower():
                return response2
        
        sock.close()
        
    except Exception as e:
        print(f"Protocol manipulation error: {e}")
    
    return None

def test_buffer_boundaries():
    """Test buffer boundaries and edge cases"""
    
    print("\n=== TESTING BUFFER BOUNDARIES ===")
    
    # Test various buffer sizes
    buffer_tests = [
        "6" + "A" * 10,
        "6" + "A" * 100,
        "6" + "A" * 1000,
        "6" + "A" * 4096,
        "A" * 4096,
        "6" + "\x00" * 100,
        "6" + "\xff" * 100,
    ]
    
    for test_data in buffer_tests:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            print(f"Testing buffer of size {len(test_data)}")
            sock.send(test_data.encode('utf-8', errors='replace') + b'\n')
            
            response = sock.recv(4096).decode('utf-8', errors='replace')
            
            if (response.strip() and 
                "Enter access band" not in response and
                "Access band invalid" not in response and
                "BOSS" not in response):
                print(f"  Unusual response: {repr(response[:100])}")
                if 'uscc{' in response.lower():
                    return response
            
            sock.close()
            
        except Exception as e:
            if "Connection reset" in str(e):
                print(f"  Connection reset with buffer size {len(test_data)}")
    
    return None

if __name__ == "__main__":
    print("=== DEEPER ANALYSIS FOR HIDDEN FLAG ===")
    
    result = test_all_ascii_inputs()
    
    if not result:
        result = test_binary_inputs()
    
    if not result:
        result = test_long_connection_with_timing()
    
    if not result:
        result = test_protocol_manipulation()
    
    if not result:
        result = test_buffer_boundaries()
    
    if result:
        print(f"\n*** FLAG FOUND: {result} ***")
    else:
        print("\n*** NO HIDDEN FLAG FOUND ***")
        print("The flag might be:")
        print("1. In the challenge description or environment")
        print("2. Require a completely different approach")
        print("3. Be based on some other aspect we haven't considered")
        print("4. Need source code analysis or reverse engineering")