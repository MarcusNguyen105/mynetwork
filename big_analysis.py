#!/usr/bin/env python3
import socket
import re

s = socket.socket()
s.settimeout(10)
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))
s.shutdown(socket.SHUT_WR)

# Read LOTS of data - maybe the flag appears later
data = b""
chunks_read = 0
try:
    while len(data) < 5000000:  # 5MB
        chunk = s.recv(65536)
        if not chunk:
            break
        data += chunk
        chunks_read += 1
        if chunks_read % 10 == 0:
            print(f"Read {len(data)} bytes so far...")
except Exception as e:
    print(f"Stopped reading: {e}")
s.close()

text = data.decode(errors='replace')
print(f"\nTotal data: {len(data)} bytes, {len(text)} chars")

# Search for any flag pattern
print("\n=== Searching for flags ===")
flag_patterns = [
    r'[a-zA-Z]{2,5}\{[^}]{5,50}\}',  # Generic flag format
]

for pattern in flag_patterns:
    matches = re.findall(pattern, text)
    if matches:
        unique = set(matches)
        print(f"Found {len(unique)} unique matches:")
        for m in unique:
            print(f"  {m}")

# Look at spacing variations
parts = text.split('jail>')
spaces = []
for i in range(1, min(1000, len(parts))):
    if parts[i] and len(parts[i]) > 0:
        # Count spaces or newlines before next content
        prefix = parts[i].split('jail>')[0] if 'jail>' in parts[i] else parts[i]
        spaces.append(len(prefix))

print(f"\n=== Space analysis ===")
print(f"Number of segments: {len(spaces)}")
print(f"Unique space counts: {set(spaces)}")

# Maybe every N-th character?
if len(text) > 1000:
    print("\n=== Every 100th character ===")
    print(''.join([text[i] for i in range(0, min(10000, len(text)), 100)]))
