#!/usr/bin/env python3
import socket
import time
import threading

def connect_interactive(access_level):
    """Connect to junkyard service and allow interactive exploration"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(30)
        
        print(f"Connecting to access level {access_level}...")
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        
        # Receive initial prompt
        response = sock.recv(4096).decode('utf-8')
        print(response)
        
        # Send access level
        sock.send(f"{access_level}\n".encode('utf-8'))
        
        # Receive access level response
        response = sock.recv(4096).decode('utf-8')
        print(response)
        
        # Wait a bit longer to see if there's more output
        time.sleep(2)
        
        # Try to receive more data
        sock.settimeout(5)
        try:
            while True:
                data = sock.recv(4096).decode('utf-8')
                if not data:
                    break
                print(data, end='')
        except socket.timeout:
            pass
        except Exception as e:
            print(f"Connection ended: {e}")
        
        # Try sending some common commands
        commands = ['help', 'ls', 'dir', 'flag', 'cat flag', 'show', 'status', 'info', '']
        
        for cmd in commands:
            try:
                if cmd:
                    print(f"\n>>> Trying command: {cmd}")
                    sock.send(f"{cmd}\n".encode('utf-8'))
                else:
                    print(f"\n>>> Sending empty line")
                    sock.send(f"\n".encode('utf-8'))
                
                sock.settimeout(3)
                response = sock.recv(4096).decode('utf-8')
                if response.strip():
                    print(response)
                else:
                    print("(no response)")
            except socket.timeout:
                print("(timeout)")
            except Exception as e:
                print(f"Error: {e}")
                break
        
        sock.close()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Focus on the highest access level (BOSS)
    connect_interactive(6)