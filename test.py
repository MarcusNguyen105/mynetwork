#!/usr/bin/env python3
import socket
import time

s = socket.socket()
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))

# Send a newline to trigger response
s.sendall(b'\n')
time.sleep(0.5)

s.settimeout(2)
data = s.recv(8192)
print("Response:")
print(repr(data))
print("\nDecoded:")
print(data.decode())

# Try to continue the conversation
print("\n=== Sending Clojure code ===")
s.sendall(b'(+ 1 1)\n')
time.sleep(0.5)
data = s.recv(8192)
print(repr(data))
print(data.decode())

s.close()
