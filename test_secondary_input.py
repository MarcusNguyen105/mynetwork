#!/usr/bin/env python3
from pwn import *

context.log_level = 'debug'

host = "chals.uscc-cyberbowl-2025.ctf.institute"
port = 3015

print("Testing if there's secondary input after band selection...")

for band in [6]:  # Test with BOSS level
    print(f"\n{'='*70}")
    print(f"Testing band {band}")
    print(f"{'='*70}")
    
    try:
        conn = remote(host, port, timeout=15)
        
        # Get initial prompt
        data = conn.recvuntil(b":", timeout=5)
        print(f"Initial prompt: {data}")
        
        # Send band selection  
        conn.sendline(str(band).encode())
        
        # Wait and see if there's more output or prompts
        sleep(1)
        
        # Try to receive what comes next
        try:
            data = conn.recv(timeout=3)
            print(f"\nFirst response: {repr(data)}")
            
            # Check if it's waiting for more input
            if data and not data.endswith(b'\n'):
                print("Might be waiting for more input!")
                
                # Try sending exploit payload
                payload = cyclic(300)
                print(f"\nSending payload of length {len(payload)}")
                conn.sendline(payload)
                
                # Get response
                try:
                    resp = conn.recvall(timeout=3)
                    print(f"\nResponse to payload: {repr(resp)}")
                    
                    output = resp.decode('utf-8', errors='ignore')
                    if 'USCC{' in output or 'RAIDER' in output:
                        print("\n" + "!"*70)
                        print("FOUND SOMETHING!")
                        print(output)
                        print("!"*70)
                except:
                    pass
                    
        except Exception as e:
            print(f"Receive error: {e}")
        
        conn.close()
        
    except Exception as e:
        print(f"Connection error: {e}")
