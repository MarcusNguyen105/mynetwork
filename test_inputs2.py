#!/usr/bin/env python3
import socket
import time

host = "chals.uscc-cyberbowl-2025.ctf.institute"
port = 3015

def test_input(value):
    print(f"\n=== Testing input: {value} ===")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    # Receive initial data
    time.sleep(0.2)
    data = s.recv(4096)
    print(data.decode('utf-8', errors='ignore'), end='')
    
    # Send input
    s.send(f"{value}\n".encode())
    
    # Receive response
    time.sleep(0.5)
    try:
        data = s.recv(4096)
        print(data.decode('utf-8', errors='ignore'))
    except:
        pass
    
    s.close()

# Test normal inputs
for i in [1, 3, 6, 7, 57337]:
    test_input(i)
