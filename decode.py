#!/usr/bin/env python3
import socket

s = socket.socket()
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))
s.shutdown(socket.SHUT_WR)

# Receive ALL data
all_data = b""
while True:
    data = s.recv(65536)
    if not data:
        break
    all_data += data

s.close()

# Decode and check
text = all_data.decode(errors='replace')

# Look for anything that's NOT "> jail"
lines = text.split('> jail')
unique_parts = set(lines)

print(f"Total data length: {len(text)}")
print(f"Number of '> jail' occurrences: {text.count('> jail')}")
print(f"\nUnique parts (should find flag if different):")
for part in unique_parts:
    if part and part != '> jail':
        print(repr(part))

# Also check for flag format
if 'flag{' in text.lower() or 'uscg{' in text.lower() or 'uscc{' in text.lower():
    print("\n\nFLAG FOUND!")
    # Extract flag
    for pattern in ['flag{', 'uscg{', 'uscc{', 'FLAG{', 'USCG{', 'USCC{']:
        if pattern.lower() in text.lower():
            idx = text.lower().find(pattern.lower())
            print(text[idx:idx+100])
