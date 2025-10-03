#!/usr/bin/env python3
import socket

s = socket.socket()
s.settimeout(15)
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))
s.shutdown(socket.SHUT_WR)

# Read lots of data
data = b""
try:
    while len(data) < 2000000:  # 2MB should be enough
        chunk = s.recv(65536)
        if not chunk:
            break
        data += chunk
except:
    pass
s.close()

text = data.decode(errors='replace')
print(f"Total: {len(text)} chars\n")

# Find where the jail loop starts
banner_end = text.find('\njail>')
if banner_end < 0:
    banner_end = text.find('jail>')
print(f"Banner ends at position: {banner_end}")
print(f"Banner:\n{text[:banner_end]}\n")

jail_section = text[banner_end:]

# The pattern is "jail> jail> jail>" with spaces between
# Let's look at what characters appear between "jail>" and the next ">"
parts = jail_section.split('jail>')

print(f"Number of 'jail>' splits: {len(parts)}")

# Look at what's between each jail>
chars_between = []
for i in range(1, min(5000, len(parts))):
    if parts[i]:
        # Get the content before the next ">" or end
        content = parts[i].split('>')[0] if '>' in parts[i] else parts[i]
        if content:
            chars_between.append(content)

print(f"\nFirst 100 segments between 'jail>' and next '>':")
for i, seg in enumerate(chars_between[:100]):
    print(f"{i}: {repr(seg)}")

# Try to extract hidden message
print("\n=== Extracting possible hidden message ===")
hidden = []
for seg in chars_between:
    if seg and seg != ' ':
        # Not just a space - might be a message character
        hidden.append(seg.strip())

message = ''.join(hidden)
print(f"Hidden message ({len(message)} chars):")
print(message)

# Also try: maybe it's in the last character before each >
alt_message = []
for i in range(1, min(5000, len(parts))):
    if parts[i] and len(parts[i]) > 0:
        # Last char before next >
        before_gt = parts[i].split('>')[0]
        if before_gt:
            alt_message.append(before_gt[-1])

alt = ''.join(alt_message[:500])
print(f"\n=== Last char before each '>' (first 500) ===")
print(alt)
