#!/usr/bin/env python3
import socket
import time

s = socket.socket()
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))

# Send a newline to trigger response
s.sendall(b'\n')
time.sleep(0.2)

# Read initial response (before the jail flood)
s.settimeout(0.3)
data = b""
try:
    data = s.recv(8192)
except:
    pass

s.close()

text = data.decode(errors='replace')
print("=== Full banner ===")
print(text[:1000])  # First 1000 chars

# Split by newlines and show each line
lines = [l for l in text.split('\n') if l.strip()]
print("\n=== Non-empty lines ===")
for i, line in enumerate(lines[:10]):
    print(f"{i}: {line}")
