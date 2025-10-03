#!/usr/bin/env python3
import socket
import sys

payload = sys.argv[1] if len(sys.argv) > 1 else ""

s = socket.socket()
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))

if payload:
    s.sendall(payload.encode() + b'\n')

s.shutdown(socket.SHUT_WR)

data = s.recv(4096)
print(data.decode())

s.close()
