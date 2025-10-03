#!/usr/bin/env python3
import socket
import time

def recv_all(s, timeout=2):
    s.settimeout(timeout)
    data = b""
    try:
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            data += chunk
    except socket.timeout:
        pass
    return data

def send_and_recv(s, msg):
    if msg:
        s.sendall(msg.encode() + b'\n')
    time.sleep(0.3)
    return recv_all(s, 1).decode()

s = socket.socket()
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))

# Get initial data
print("=== Initial Response ===")
resp = recv_all(s, 2).decode()
print(resp)

# Try various inputs
test_inputs = [
    "",
    "help",
    "flag",
    "(+ 1 1)",
    "(println \"hello\")",
    "ls",
    "cat flag.txt",
    "source",
    "code",
    "eval",
]

for inp in test_inputs:
    print(f"\n=== Sending: '{inp}' ===")
    s = socket.socket()
    s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))
    resp = send_and_recv(s, inp)
    print(resp)
    s.close()
    time.sleep(0.2)
