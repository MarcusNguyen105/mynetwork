#!/usr/bin/env python3
import socket

s = socket.socket()
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))

# Send data and close write side
s.sendall(b'(+ 1 1)\n')
s.shutdown(socket.SHUT_WR)

# Now read the response
s.settimeout(3)
data = b""
while True:
    try:
        chunk = s.recv(8192)
        if not chunk:
            break
        data += chunk
    except socket.timeout:
        break

print("Response:")
print(repr(data))
print("\nDecoded:")
print(data.decode())

s.close()
