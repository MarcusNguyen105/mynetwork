#!/usr/bin/env python3
import socket
import time

def connect_to_service():
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
        
        # Receive response
        response = sock.recv(1024).decode('utf-8')
        print("Response after sending '6':")
        print(response)
        
        # Wait a bit and see if there are more prompts
        time.sleep(1)
        try:
            more_data = sock.recv(1024).decode('utf-8')
            if more_data:
                print("Additional data received:")
                print(more_data)
        except:
            pass
        
        # Try to send some common commands
        commands = ["help", "ls", "dir", "list", "show", "flag", "cat flag", "cat flag.txt", "pwd", "whoami", "?", "menu"]
        
        for cmd in commands:
            print(f"\nTrying command: {cmd}")
            sock.send(f"{cmd}\n".encode('utf-8'))
            time.sleep(1)
            try:
                response = sock.recv(1024).decode('utf-8')
                if response:
                    print(f"Response: {response}")
                else:
                    print("No response")
            except Exception as e:
                print(f"Error receiving response: {e}")
                break
        
        sock.close()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    connect_to_service()