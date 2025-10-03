#!/usr/bin/env python3
import socket

host = "chals.uscc-cyberbowl-2025.ctf.institute"
port = 3015

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Receive initial data
data = s.recv(4096)
print(data.decode('utf-8', errors='ignore'))

# Send input
s.send(b"3\n")

# Receive response
data = s.recv(4096)
print(data.decode('utf-8', errors='ignore'))

s.close()
