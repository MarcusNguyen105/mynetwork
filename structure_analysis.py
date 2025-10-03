#!/usr/bin/env python3
import socket

s = socket.socket()
s.settimeout(10)
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))
s.shutdown(socket.SHUT_WR)

# Read chunk
data = s.recv(100000)
s.close()

text = data.decode(errors='replace')

# Get just the jail section
idx = text.find('jail>')
jail_part = text[idx:idx+1000]

print("=== Raw jail section (first 1000 chars) ===")
print(repr(jail_part))

print("\n=== Character analysis ===")
unique_chars = set(jail_part)
print(f"Unique characters: {sorted(unique_chars)}")
print(f"As ASCII codes: {[ord(c) for c in sorted(unique_chars)]}")

# Count occurrences
from collections import Counter
counts = Counter(jail_part)
print(f"\nCharacter counts:")
for char, count in counts.most_common():
    print(f"  {repr(char)}: {count}")

# Look for patterns
print("\n=== Looking for line patterns ===")
lines = jail_part.split('\n')
for i, line in enumerate(lines[:20]):
    print(f"Line {i} ({len(line)} chars): {repr(line[:100])}")
