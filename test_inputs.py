#!/usr/bin/env python3
import socket

host = "chals.uscc-cyberbowl-2025.ctf.institute"
port = 3015

def test_input(value):
    print(f"\n=== Testing input: {value} ===")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    # Receive initial data
    data = s.recv(4096)
    print(data.decode('utf-8', errors='ignore'))
    
    # Send input
    s.send(f"{value}\n".encode())
    
    # Receive response
    data = s.recv(4096)
    print(data.decode('utf-8', errors='ignore'))
    
    s.close()

# Test normal inputs
for i in range(1, 8):
    test_input(i)

# Test some edge cases
test_input(0)
test_input(9)
test_input(57337)  # 0xDFE9 - might be a magic number
