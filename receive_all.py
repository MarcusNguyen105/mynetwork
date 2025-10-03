#!/usr/bin/env python3
import socket
import sys

payload = sys.argv[1] if len(sys.argv) > 1 else ""

s = socket.socket()
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))

if payload:
    s.sendall(payload.encode() + b'\n')

s.shutdown(socket.SHUT_WR)

# Receive ALL data
all_data = b""
while True:
    data = s.recv(4096)
    if not data:
        break
    all_data += data

print("=== Received data ===")
print(all_data.decode())
print("\n=== Hex dump ===")
print(all_data.hex())
print(f"\n=== Total bytes: {len(all_data)} ===")

s.close()
