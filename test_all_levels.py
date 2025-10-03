#!/usr/bin/env python3
import socket
import time

def test_access_level(level):
    host = "chals.uscc-cyberbowl-2025.ctf.institute"
    port = 3015
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        # Receive banner
        banner = sock.recv(1024).decode('utf-8')
        
        # Send access level
        sock.send(f"{level}\n".encode('utf-8'))
        
        # Receive all available data
        full_response = ""
        while True:
            try:
                data = sock.recv(1024).decode('utf-8')
                if not data:
                    break
                full_response += data
            except:
                break
        
        sock.close()
        
        return full_response.strip()
        
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Testing all access levels:")
    print("=" * 50)
    
    for level in range(1, 7):
        print(f"\nLevel {level}:")
        response = test_access_level(level)
        print(response)
        time.sleep(0.5)  # Small delay between requests

if __name__ == "__main__":
    main()