#!/usr/bin/env python3
from pwn import *

# Context settings
context.log_level = 'info'

host = "chals.uscc-cyberbowl-2025.ctf.institute"
port = 3015

def try_access(value):
    print(f"\n{'='*60}")
    print(f"Trying access band: {value}")
    print(f"{'='*60}")
    
    try:
        # Connect to the server
        conn = remote(host, port, timeout=10)
        
        # Receive the initial prompt
        prompt = conn.recvuntil(b":", timeout=5)
        print(prompt.decode('utf-8', errors='ignore'))
        
        # Send our input
        conn.sendline(str(value).encode())
        
        # Wait a bit and try to receive more
        sleep(1)
        
        # Receive the response
        try:
            response = conn.recvall(timeout=5)
            print(response.decode('utf-8', errors='ignore'))
            return response
        except:
            try:
                response = conn.recv(timeout=2)
                print(response.decode('utf-8', errors='ignore'))
                return response
            except:
                print("No response received")
                return None
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        try:
            conn.close()
        except:
            pass

# Try valid inputs to see full output for each level
for val in [1, 2, 3, 4, 5, 6]:
    try_access(val)
