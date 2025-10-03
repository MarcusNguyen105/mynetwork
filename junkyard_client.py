#!/usr/bin/env python3
import socket
import sys

def connect_to_junkyard(access_level):
    """Connect to the junkyard service and test an access level"""
    try:
        # Create socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        
        # Connect to the service
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        
        # Receive initial prompt
        response = sock.recv(4096).decode('utf-8')
        print(f"=== ACCESS LEVEL {access_level} ===")
        print(response)
        
        # Send access level
        sock.send(f"{access_level}\n".encode('utf-8'))
        
        # Receive response
        response = sock.recv(4096).decode('utf-8')
        print(response)
        
        # Try to receive more data in case there's additional output
        sock.settimeout(2)
        try:
            additional = sock.recv(4096).decode('utf-8')
            if additional.strip():
                print(additional)
        except socket.timeout:
            pass
        
        sock.close()
        print("=" * 50)
        
    except Exception as e:
        print(f"Error connecting to level {access_level}: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Test specific level
        level = int(sys.argv[1])
        connect_to_junkyard(level)
    else:
        # Test all levels
        for level in range(1, 7):
            connect_to_junkyard(level)
            print()