#!/usr/bin/env python3
import socket
import time
import base64
import binascii

def try_advanced_techniques():
    host = "chals.uscc-cyberbowl-2025.ctf.institute"
    port = 3015
    
    # Try different encoding/input techniques
    test_cases = [
        # Different number formats
        ("6", "Normal"),
        ("0x6", "Hex"),
        ("0b110", "Binary"),
        ("06", "Zero padded"),
        ("6.0", "Float"),
        
        # Special characters
        ("6\x00", "Null byte"),
        ("6\x0a", "LF"),
        ("6\x0d", "CR"),
        ("6\x0d\x0a", "CRLF"),
        
        # Multiple inputs
        ("6\n", "With newline"),
        ("6\r\n", "With CRLF"),
        ("6 ", "With space"),
        (" 6", "Leading space"),
        (" 6 ", "Spaces around"),
        
        # Try to overflow or underflow
        ("7", "Overflow"),
        ("0", "Underflow"),
        ("-1", "Negative"),
        ("999", "Large number"),
        
        # Try to inject commands
        ("6; ls", "Command injection"),
        ("6 | cat", "Pipe"),
        ("6 && ls", "And operator"),
        ("6 || ls", "Or operator"),
        
        # Try different encodings
        ("6".encode('utf-16').decode('utf-8'), "UTF-16"),
        ("6".encode('ascii'), "ASCII bytes"),
    ]
    
    for test_input, description in test_cases:
        print(f"\n{'='*60}")
        print(f"Testing: {description} - Input: {repr(test_input)}")
        print('='*60)
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            
            # Receive banner
            banner = sock.recv(1024).decode('utf-8')
            print(f"Banner: {banner.strip()}")
            
            # Send test input
            if isinstance(test_input, str):
                sock.send(test_input.encode('utf-8'))
            else:
                sock.send(test_input)
            
            # Try to receive response
            try:
                sock.settimeout(3)
                data = sock.recv(1024).decode('utf-8')
                print(f"Response: {repr(data)}")
                
                # Check if we get more data
                time.sleep(0.5)
                try:
                    more_data = sock.recv(1024).decode('utf-8')
                    if more_data:
                        print(f"Additional data: {repr(more_data)}")
                except:
                    pass
                    
            except socket.timeout:
                print("No response (timeout)")
            except Exception as e:
                print(f"Error receiving response: {e}")
            
            sock.close()
            
        except Exception as e:
            print(f"Connection error: {e}")
        
        time.sleep(0.5)

def analyze_responses_for_hidden_data():
    """Analyze if there's hidden data in the responses"""
    print("\n" + "="*60)
    print("ANALYZING RESPONSES FOR HIDDEN DATA")
    print("="*60)
    
    # Known responses
    responses = [
        "SCAVENGER — Yard floor access",
        "HAULER — Broken-but-usable stock",
        "MECHANIC — Engine bays & bins",
        "QUARRY FOREMAN — Heavy salvage ops",
        "YARD MANAGER — Central yard systems",
        "BOSS — Secure compound & vaults"
    ]
    
    for i, response in enumerate(responses, 1):
        print(f"\nLevel {i}: {response}")
        
        # Check for hidden characters
        hidden_chars = []
        for char in response:
            if ord(char) < 32 or ord(char) > 126:
                hidden_chars.append(f"\\x{ord(char):02x}")
        
        if hidden_chars:
            print(f"  Hidden chars: {hidden_chars}")
        
        # Check for patterns in character codes
        char_codes = [ord(c) for c in response]
        print(f"  Char codes: {char_codes}")
        
        # Check if char codes form a pattern
        if len(char_codes) > 10:
            # Look for arithmetic sequences
            diffs = [char_codes[i+1] - char_codes[i] for i in range(len(char_codes)-1)]
            print(f"  Differences: {diffs}")

if __name__ == "__main__":
    try_advanced_techniques()
    analyze_responses_for_hidden_data()