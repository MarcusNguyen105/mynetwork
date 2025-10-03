#!/usr/bin/env python3
import socket
import time

def connect():
    s = socket.socket()
    s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))
    return s

s = connect()

# Receive all available data
time.sleep(0.5)
data = b""
while True:
    try:
        s.settimeout(1)
        chunk = s.recv(4096)
        if not chunk:
            break
        data += chunk
        print(chunk.decode(), end='', flush=True)
    except socket.timeout:
        break

print("\n\n=== END OF INITIAL DATA ===")

# Try to interact
try:
    s.sendall(b"\n")
    time.sleep(0.5)
    response = s.recv(4096)
    print("Response:", response.decode())
except Exception as e:
    print(f"Error: {e}")

s.close()
