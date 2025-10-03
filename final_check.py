#!/usr/bin/env python3
import socket
import time

def get_boss_access():
    """Get BOSS access and see if there's a flag"""
    host = "chals.uscc-cyberbowl-2025.ctf.institute"
    port = 3015
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        # Receive banner
        banner = sock.recv(1024).decode('utf-8')
        print("Banner received:")
        print(banner)
        
        # Send level 6 (BOSS)
        sock.send(b"6\n")
        
        # Receive response
        response = sock.recv(1024).decode('utf-8')
        print("Response received:")
        print(repr(response))
        
        # Wait a bit and try to get more data
        time.sleep(1)
        try:
            more_data = sock.recv(1024).decode('utf-8')
            if more_data:
                print("Additional data:")
                print(repr(more_data))
        except:
            pass
        
        sock.close()
        
        # Check if the response contains any flag-like patterns
        full_response = banner + response
        flag_patterns = ["uscc{", "USCC{", "flag{", "FLAG{", "ctf{", "CTF{"]
        
        print("\nChecking for flag patterns:")
        for pattern in flag_patterns:
            if pattern in full_response:
                print(f"Found '{pattern}' in response!")
        
        # Check if the response contains the word "flag" anywhere
        if "flag" in full_response.lower():
            print("Found 'flag' in response!")
        
        return full_response
        
    except Exception as e:
        print(f"Error: {e}")
        return None

def check_common_flag_formats():
    """Check if the flag might be in a common format"""
    print("\nChecking common flag formats:")
    print("=" * 40)
    
    # Common flag formats
    possible_flags = [
        "6",
        "BOSS",
        "BOSS — Secure compound & vaults",
        "uscc{6}",
        "uscc{BOSS}",
        "uscc{BOSS — Secure compound & vaults}",
        "flag{6}",
        "flag{BOSS}",
        "flag{BOSS — Secure compound & vaults}",
        "ctf{6}",
        "ctf{BOSS}",
        "ctf{BOSS — Secure compound & vaults}",
    ]
    
    print("Possible flags based on the challenge:")
    for flag in possible_flags:
        print(f"  {flag}")

if __name__ == "__main__":
    response = get_boss_access()
    check_common_flag_formats()
    
    print("\n" + "="*60)
    print("CONCLUSION:")
    print("="*60)
    print("The challenge asks for 'the highest level of access'")
    print("Level 6 is BOSS — Secure compound & vaults")
    print("This appears to be the highest level available.")
    print("\nPossible flags:")
    print("- 6 (the access level number)")
    print("- BOSS (the job title)")
    print("- BOSS — Secure compound & vaults (the full description)")
    print("- uscc{6}, uscc{BOSS}, etc. (common CTF flag formats)")