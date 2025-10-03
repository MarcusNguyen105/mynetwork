#!/usr/bin/env python3
from pwn import *

context.log_level = 'info'

host = "chals.uscc-cyberbowl-2025.ctf.institute"
port = 3015

# Looking at the binary, I see "=9  " which could be hex 0x3d393020
# Let's try this and other hex values that appear in the binary

test_values = [
    1027481632,  # 0x3d393020 ("=9  " as little-endian int)
    0x3939,      # "99" in hex
    14649,       # 0x3939 in decimal
    57337,       # 0xDFE9
    # Try the value as if each character position matters
]

def try_value(val):
    print(f"\n{'='*60}")
    print(f"Trying: {val} (0x{val:x})")
    print(f"{'='*60}")
    
    try:
        conn = remote(host, port, timeout=10)
        conn.recvuntil(b":")
        conn.sendline(str(val).encode())
        sleep(0.5)
        
        try:
            data = conn.recvall(timeout=3)
            output = data.decode('utf-8', errors='ignore')
            print(output)
            
            if 'USCC{' in output or 'RAIDER' in output or 'flag' in output.lower():
                print("\n" + "!"*60)
                print("POTENTIAL FLAG OR RAIDER KING FOUND!")
                print("!"*60)
                return True
        except:
            pass
        
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
    
    return False

for val in test_values:
    if try_value(val):
        break
