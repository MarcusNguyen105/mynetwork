#!/usr/bin/env python3
import socket
import time

def capture_interaction(level):
    host = "chals.uscc-cyberbowl-2025.ctf.institute"
    port = 3015
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        print(f"Testing level {level}:")
        print("-" * 30)
        
        # Receive banner
        banner = sock.recv(1024).decode('utf-8')
        print(f"Banner received: {repr(banner)}")
        
        # Send access level
        sock.send(f"{level}\n".encode('utf-8'))
        print(f"Sent: {level}")
        
        # Wait a moment
        time.sleep(0.5)
        
        # Try to receive more data
        try:
            sock.settimeout(3)
            data = sock.recv(1024).decode('utf-8')
            print(f"Additional data: {repr(data)}")
        except socket.timeout:
            print("No additional data received (timeout)")
        except Exception as e:
            print(f"Error receiving additional data: {e}")
        
        sock.close()
        print()
        
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Test levels 1-6
    for level in range(1, 7):
        capture_interaction(level)
        time.sleep(1)

if __name__ == "__main__":
    main()