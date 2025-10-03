#!/usr/bin/env python3
import socket

s = socket.socket()
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))
s.shutdown(socket.SHUT_WR)

# Read enough data to find any pattern
data = s.recv(100000)  # 100KB
s.close()

text = data.decode(errors='replace')

print(f"Total bytes: {len(data)}")
print(f"Total chars: {len(text)}")

# Look for patterns in the jail output
lines = text.split('\n')
print(f"Total lines: {len(lines)}")

# Check if there are any variations in the "jail>" pattern
jail_prompts = text.split('jail>')
print(f"Number of 'jail>' occurrences: {len(jail_prompts) - 1}")

# Check what's between each jail>
unique_separators = set()
for i in range(len(jail_prompts) - 1):
    sep = jail_prompts[i][-10:] if len(jail_prompts[i]) > 0 else ''
    unique_separators.add(repr(sep))

print(f"\nUnique separators before 'jail>': {len(unique_separators)}")
for sep in list(unique_separators)[:20]:
    print(f"  {sep}")

# Look for the actual banner
banner_end = text.find('jail>')
if banner_end > 0:
    banner = text[:banner_end]
    print(f"\n=== BANNER ===")
    print(banner)
    print(f"\n=== After banner (first 200 chars) ===")
    print(text[banner_end:banner_end+200])

# Check if there's any pattern in which characters appear after jail>
chars_after_jail = []
idx = 0
count = 0
while True:
    idx = text.find('jail>', idx)
    if idx == -1 or count > 1000:
        break
    if idx + 5 < len(text):
        chars_after_jail.append(text[idx + 5])
    idx += 5
    count += 1

print(f"\n=== Characters immediately after 'jail>' (first 100) ===")
print(''.join(chars_after_jail[:100]))

# Look for any hidden message
unique_chars_after = set(chars_after_jail)
print(f"\nUnique chars after 'jail>': {unique_chars_after}")
