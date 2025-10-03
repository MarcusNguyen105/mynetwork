#!/usr/bin/env python3
from pwn import *

# Context settings
context.log_level = 'debug'

host = "chals.uscc-cyberbowl-2025.ctf.institute"
port = 3015

print(f"\n{'='*60}")
print(f"Trying access band: 6 (BOSS)")
print(f"{'='*60}")

try:
    # Connect to the server
    conn = remote(host, port, timeout=10)
    
    # Receive and print everything interactively
    conn.interactive()
    
except Exception as e:
    print(f"Error: {e}")
