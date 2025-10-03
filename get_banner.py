#!/usr/bin/env python3
import socket
import time

s = socket.socket()
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))

# Wait a moment for the banner
time.sleep(0.5)

# Read just the banner  
s.settimeout(0.5)
data = b""
try:
    while len(data) < 10000:  # Read first 10KB
        chunk = s.recv(4096)
        if not chunk:
            break
        data += chunk
except:
    pass

s.close()

text = data.decode(errors='replace')
lines = text.split('\n')

print("=== First 20 lines ===")
for i, line in enumerate(lines[:20]):
    print(f"{i}: {repr(line)}")

# Look for the hint
if 'flag' in text.lower():
    print("\n=== Flag-related content ===")
    for line in lines:
        if 'flag' in line.lower():
            print(line)
