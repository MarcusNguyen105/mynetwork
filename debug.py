#!/usr/bin/env python3
import socket
import sys

s = socket.socket()
s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))

print("Connected. Reading all data...")

# Set a longer timeout and try to read everything
s.settimeout(5)
all_data = b""

try:
    while True:
        data = s.recv(8192)
        if not data:
            print("Connection closed by server")
            break
        all_data += data
        print(f"Received {len(data)} bytes")
        sys.stdout.write(data.decode(errors='replace'))
        sys.stdout.flush()
except socket.timeout:
    print("\n\n=== Timeout reached ===")
except Exception as e:
    print(f"\n\nException: {e}")

print(f"\n\nTotal bytes received: {len(all_data)}")
print("Hex dump:")
print(all_data.hex())

print("\n\nRaw bytes:")
print(repr(all_data))

s.close()
