#!/usr/bin/env python3
import socket
import sys
import select

HOST = 'chals.uscc-cyberbowl-2025.ctf.institute'
PORT = 3005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.setblocking(False)

print("Connected to the service. Type your input:")

import time
while True:
    # Check if there's data from the server
    ready = select.select([s], [], [], 0.1)
    if ready[0]:
        try:
            data = s.recv(4096)
            if data:
                print(data.decode(errors='replace'), end='', flush=True)
            else:
                print("\n[Connection closed]")
                break
        except:
            pass
    
    # Check if there's input from stdin
    ready = select.select([sys.stdin], [], [], 0.1)
    if ready[0]:
        line = sys.stdin.readline()
        if not line:
            break
        s.sendall(line.encode())

s.close()
