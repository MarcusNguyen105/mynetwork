#!/usr/bin/env python3
from pwn import *

context.log_level = 'info'

host = "chals.uscc-cyberbowl-2025.ctf.institute"
port = 3015

def try_value(val):
    print(f"\n{'='*60}")
    print(f"Trying: {repr(val)}")
    print(f"{'='*60}")
    
    try:
        conn = remote(host, port, timeout=10)
        conn.recvuntil(b":")
        conn.send(val + b"\n")
        sleep(0.5)
        
        try:
            data = conn.recvall(timeout=3)
            output = data.decode('utf-8', errors='ignore')
            print(output)
            
            if 'USCC{' in output or 'RAIDER' in output:
                print("\n" + "!"*60)
                print("FLAG OR RAIDER KING FOUND!")
                print("!"*60)
                return True
        except:
            pass
        
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
    
    return False

# Try ASCII characters and special sequences
test_values = [
    b'7',
    b'8',
    b'9',
    b'0',
    b'A',
    b'R',  # For RAIDER
    b'K',  # For KING
    b'|',  # Pipe character (appears in binary)
    b'~',
    b'B',  # Next after 'A'
    b'r',  # lowercase
    # Try special format
    b'%s',
    b'%x',
]

for val in test_values:
    if try_value(val):
        break
