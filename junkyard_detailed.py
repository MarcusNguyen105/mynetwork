#!/usr/bin/env python3
import socket
import time

def detailed_connection(access_level):
    """Make a detailed connection showing all data received"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(15)
        
        print(f"=== DETAILED CONNECTION TO LEVEL {access_level} ===")
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        
        # Receive initial data in chunks
        all_data = b""
        print("Initial connection data:")
        while True:
            try:
                sock.settimeout(2)
                chunk = sock.recv(1024)
                if not chunk:
                    break
                all_data += chunk
                print(f"Received chunk: {repr(chunk)}")
            except socket.timeout:
                break
        
        print(f"Total initial data: {repr(all_data)}")
        print(f"Decoded: {all_data.decode('utf-8', errors='replace')}")
        
        # Send access level
        print(f"\nSending access level: {access_level}")
        sock.send(f"{access_level}\n".encode('utf-8'))
        
        # Receive response data in chunks
        response_data = b""
        print("Response data:")
        while True:
            try:
                sock.settimeout(3)
                chunk = sock.recv(1024)
                if not chunk:
                    break
                response_data += chunk
                print(f"Received chunk: {repr(chunk)}")
            except socket.timeout:
                break
        
        print(f"Total response data: {repr(response_data)}")
        print(f"Decoded: {response_data.decode('utf-8', errors='replace')}")
        
        # Check if connection is still alive
        print(f"\nConnection status: {'alive' if sock.fileno() != -1 else 'closed'}")
        
        sock.close()
        print("=" * 60)
        
    except Exception as e:
        print(f"Error: {e}")

def test_special_inputs():
    """Test some special inputs that might reveal hidden functionality"""
    special_inputs = [
        "999",           # Very high number
        "%s%s%s%s",      # Format string
        "A" * 100,       # Long string
        "\x00",          # Null byte
        "\xff\xfe\xfd",  # Binary data
        "6\x00flag",     # Null byte injection
    ]
    
    for test_input in special_inputs:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            
            # Skip initial prompt
            sock.recv(4096)
            
            # Send special input
            sock.send(test_input.encode('utf-8', errors='replace') + b'\n')
            
            # Get response
            response = sock.recv(4096)
            
            print(f"Special input: {repr(test_input)}")
            print(f"Response: {repr(response)}")
            print("-" * 40)
            
            sock.close()
            
        except Exception as e:
            print(f"Error with {repr(test_input)}: {e}")

if __name__ == "__main__":
    # Test level 6 in detail
    detailed_connection(6)
    
    print("\n" + "=" * 60)
    print("TESTING SPECIAL INPUTS")
    print("=" * 60)
    
    test_special_inputs()