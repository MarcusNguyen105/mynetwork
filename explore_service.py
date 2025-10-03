#!/usr/bin/env python3
import socket
import time

def explore_service():
    host = "chals.uscc-cyberbowl-2025.ctf.institute"
    port = 3015
    
    try:
        # Create socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        # Receive initial banner
        banner = sock.recv(1024).decode('utf-8')
        print("Banner received:")
        print(banner)
        
        # Send access level 6 (BOSS)
        sock.send(b"6\n")
        
        # Keep receiving data until connection closes
        print("\nReceiving all available data:")
        while True:
            try:
                data = sock.recv(1024).decode('utf-8')
                if not data:
                    break
                print(data, end='')
            except:
                break
        
        sock.close()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    explore_service()