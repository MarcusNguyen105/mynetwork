#!/usr/bin/env python3
import socket
import time

def test_input(test_input):
    """Test different inputs to the junkyard service"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        
        # Receive initial prompt
        response = sock.recv(4096).decode('utf-8')
        
        # Send test input
        sock.send(f"{test_input}\n".encode('utf-8'))
        
        # Receive response
        sock.settimeout(5)
        response = sock.recv(4096).decode('utf-8')
        
        print(f"Input: {repr(test_input)}")
        print(f"Response: {repr(response)}")
        print("-" * 50)
        
        sock.close()
        
    except Exception as e:
        print(f"Error with input {repr(test_input)}: {e}")

if __name__ == "__main__":
    # Test various inputs
    test_inputs = [
        "0",      # Below range
        "7",      # Above range
        "10",     # Way above range
        "-1",     # Negative
        "a",      # Letter
        "admin",  # Common admin term
        "root",   # Root access
        "boss",   # Boss level name
        "flag",   # Direct flag request
        "help",   # Help command
        "",       # Empty input
        " ",      # Space
        "1 2 3",  # Multiple numbers
        "6 flag", # Level 6 with flag
        "6\nflag", # Level 6 then flag on new line
    ]
    
    for input_value in test_inputs:
        test_input(input_value)
        time.sleep(0.5)  # Small delay between requests