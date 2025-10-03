#!/usr/bin/env python3
import socket
import re

s = socket.socket()
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))
s.shutdown(socket.SHUT_WR)

# Receive first chunk of data and look for flag
data = s.recv(1024*1024).decode(errors='replace')
s.close()

print("=== Looking for flags ===")
print(f"Data length: {len(data)}")

# Search for various flag formats
flag_patterns = [
    r'uscc\{[^}]+\}',
    r'uscg\{[^}]+\}',
    r'flag\{[^}]+\}',
    r'USCC\{[^}]+\}',
    r'USCG\{[^}]+\}',
    r'FLAG\{[^}]+\}',
]

for pattern in flag_patterns:
    matches = re.findall(pattern, data, re.IGNORECASE)
    if matches:
        print(f"\nFound with pattern {pattern}:")
        for match in matches:
            print(f"  {match}")

# Also print the start of the data to see the banner
print("\n=== First 500 characters ===")
print(data[:500])

# Check if there's anything unusual in the data
unique_chars = set(data)
print(f"\n=== Unique characters in data ===")
print(sorted(unique_chars))

# Look for the word "flag" case-insensitively
if 'flag' in data.lower():
    idx = data.lower().find('flag')
    print(f"\n=== Context around 'flag' ===")
    print(data[max(0,idx-50):idx+100])
