#!/usr/bin/env python3
import socket

s = socket.socket()
s.settimeout(5)
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))
s.shutdown(socket.SHUT_WR)

# Read a reasonable amount
data = b""
try:
    while len(data) < 50000:  # 50KB should be enough
        chunk = s.recv(8192)
        if not chunk:
            break
        data += chunk
except:
    pass
s.close()

text = data.decode(errors='replace')

# Find the banner
print("=== Looking for banner ===")
lines = text.split('\n')
for i, line in enumerate(lines[:10]):
    if line.strip():
        print(f"Line {i}: {line}")

# Look for anything that looks like a flag
import re
patterns = [
    r'uscc\{[^}]+\}',
    r'uscg\{[^}]+\}', 
    r'flag\{[^}]+\}',
    r'USCC\{[^}]+\}',
]

print("\n=== Searching for flag patterns ===")
for pattern in patterns:
    matches = re.findall(pattern, text, re.IGNORECASE)
    if matches:
        print(f"Found with {pattern}:")
        for m in set(matches):
            print(f"  🚩 {m}")

# Check if there's steganography - maybe first letter of each "jail>"?
print("\n=== Checking for steganography ===")

# Split by jail> and look at what comes after
parts = text.split('jail>')
print(f"Number of 'jail>' occurrences: {len(parts)-1}")

# Get first character after each jail>
chars = []
for i in range(1, min(200, len(parts))):
    if parts[i]:
        chars.append(parts[i][0])
        
print(f"First chars after 'jail>': {''.join(chars[:100])}")

# Maybe it's in the spaces?
spaces_between = []
for i in range(1, min(100, len(parts))):
    # Count characters between end of one and start of next
    if parts[i]:
        prefix = parts[i].split('jail>')[0] if 'jail>' in parts[i] else parts[i]
        spaces_between.append(len(prefix))

print(f"\nLengths between jail>: {spaces_between[:50]}")

# Check if lengths encode ASCII
if spaces_between:
    print("\nTrying to decode lengths as ASCII:")
    try:
        decoded = ''.join(chr(x) if 32 <= x <= 126 else '?' for x in spaces_between[:50])
        print(f"  {decoded}")
    except:
        pass
