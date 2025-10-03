#!/usr/bin/env python3
import socket

s = socket.socket()
s.settimeout(10)
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))
s.shutdown(socket.SHUT_WR)

# Read more data
data = s.recv(500000)
s.close()

text = data.decode(errors='replace')
print(f"Total received: {len(text)} chars\n")

# Show the first 2000 characters to understand structure
print("=== First 2000 chars ===")
print(text[:2000])

# Unique characters in entire text
unique = set(text)
print(f"\n=== All unique characters in text ===")
for char in sorted(unique):
    print(f"  {repr(char)} (ASCII {ord(char)})")

# Look for any flag-like patterns
import re
patterns = [
    r'uscc\{[^}]+\}',
    r'flag\{[^}]+\}',
    r'[A-Z]{3,}\{[^}]+\}',
]

print("\n=== Searching for flags ===")
for pattern in patterns:
    matches = re.findall(pattern, text, re.IGNORECASE)
    if matches:
        print(f"Pattern {pattern}: {matches}")
