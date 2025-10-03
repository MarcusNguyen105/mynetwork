#!/usr/bin/env python3
import socket
import binascii

def hex_analysis():
    """Analyze the raw bytes from the service"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        
        print("=== HEX ANALYSIS OF JUNKYARD SERVICE ===")
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        
        # Get all initial data
        all_data = b""
        while True:
            try:
                sock.settimeout(2)
                chunk = sock.recv(1024)
                if not chunk:
                    break
                all_data += chunk
            except socket.timeout:
                break
        
        print("Initial banner hex dump:")
        print(binascii.hexdump(all_data))
        print(f"Raw bytes: {repr(all_data)}")
        print(f"Decoded: {all_data.decode('utf-8', errors='replace')}")
        
        # Test each access level and look for hidden data
        for level in range(1, 7):
            print(f"\n=== LEVEL {level} HEX ANALYSIS ===")
            
            # Send access level
            sock.send(f"{level}\n".encode('utf-8'))
            
            # Get response
            response = sock.recv(4096)
            
            print(f"Level {level} hex dump:")
            print(binascii.hexdump(response))
            print(f"Raw bytes: {repr(response)}")
            print(f"Decoded: {response.decode('utf-8', errors='replace')}")
            
            # Check for any non-printable characters or hidden data
            for i, byte in enumerate(response):
                if byte < 32 or byte > 126:  # Non-printable ASCII
                    if byte not in [10, 13]:  # Exclude newline and carriage return
                        print(f"Non-printable byte at position {i}: {byte} (0x{byte:02x})")
            
            # Reconnect for next level
            if level < 6:
                sock.close()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(10)
                sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
                sock.recv(4096)  # Skip banner
        
        sock.close()
        
    except Exception as e:
        print(f"Error: {e}")

def check_for_steganography():
    """Check if flag might be hidden in the text itself"""
    access_levels = [
        "SCAVENGER — Yard floor access",
        "HAULER — Broken-but-usable stock",
        "MECHANIC — Engine bays & bins", 
        "QUARRY FOREMAN — Heavy salvage ops",
        "YARD MANAGER — Central yard systems",
        "BOSS — Secure compound & vaults"
    ]
    
    print("\n=== CHECKING FOR HIDDEN PATTERNS ===")
    
    # Check first letters
    first_letters = ''.join([level.split()[0][0] for level in access_levels])
    print(f"First letters of each level: {first_letters}")
    
    # Check if there are any patterns in the descriptions
    all_text = ' '.join(access_levels)
    print(f"All text combined: {all_text}")
    
    # Look for potential flag patterns
    import re
    flag_patterns = [
        r'uscc\{.*?\}',
        r'flag\{.*?\}',
        r'\{.*?\}',
        r'[A-Z]{4,}',
    ]
    
    for pattern in flag_patterns:
        matches = re.findall(pattern, all_text, re.IGNORECASE)
        if matches:
            print(f"Pattern {pattern} matches: {matches}")

if __name__ == "__main__":
    hex_analysis()
    check_for_steganography()