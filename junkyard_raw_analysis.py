#!/usr/bin/env python3
import socket

def hex_dump(data):
    """Simple hex dump function"""
    result = []
    for i in range(0, len(data), 16):
        chunk = data[i:i+16]
        hex_part = ' '.join(f'{b:02x}' for b in chunk)
        ascii_part = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in chunk)
        result.append(f'{i:08x}: {hex_part:<48} |{ascii_part}|')
    return '\n'.join(result)

def comprehensive_analysis():
    """Comprehensive analysis of the service"""
    try:
        print("=== COMPREHENSIVE JUNKYARD ANALYSIS ===")
        
        # Test if there might be a level 0 or level 7+
        for test_level in [0, 7, 8, 9, 10, -1, 99, 255]:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
                
                # Skip banner
                sock.recv(4096)
                
                # Send test level
                sock.send(f"{test_level}\n".encode('utf-8'))
                
                # Get response
                response = sock.recv(4096)
                
                if response and b"Enter access band" not in response:
                    print(f"\n*** DIFFERENT RESPONSE FOR LEVEL {test_level} ***")
                    print(f"Raw: {repr(response)}")
                    print(f"Decoded: {response.decode('utf-8', errors='replace')}")
                    print(f"Hex dump:\n{hex_dump(response)}")
                
                sock.close()
                
            except Exception as e:
                print(f"Error testing level {test_level}: {e}")
        
        # Test if the flag might be in a specific sequence or combination
        print("\n=== TESTING SEQUENTIAL ACCESS ===")
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            
            # Skip banner
            sock.recv(4096)
            
            # Try accessing levels in sequence
            for level in [1, 2, 3, 4, 5, 6]:
                print(f"Accessing level {level}...")
                sock.send(f"{level}\n".encode('utf-8'))
                response = sock.recv(4096)
                print(f"Response: {response.decode('utf-8', errors='replace').strip()}")
                
                # Check if there's more data after each level
                try:
                    sock.settimeout(1)
                    extra = sock.recv(4096)
                    if extra:
                        print(f"Extra data: {repr(extra)}")
                except socket.timeout:
                    pass
            
            sock.close()
            
        except Exception as e:
            print(f"Sequential access error: {e}")
        
        # Test if there's a backdoor or special command
        print("\n=== TESTING BACKDOOR COMMANDS ===")
        
        backdoor_commands = [
            "backdoor",
            "debug",
            "test",
            "secret",
            "hidden",
            "bypass",
            "override",
            "master",
            "superuser",
            "god",
            "developer",
            "console",
            "shell",
            "/flag",
            "\\flag",
            "flag{",
            "uscc{",
            chr(0) + "flag",  # null byte prefix
            "flag" + chr(0),  # null byte suffix
        ]
        
        for cmd in backdoor_commands:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
                
                # Skip banner
                sock.recv(4096)
                
                # Send backdoor command
                sock.send(f"{cmd}\n".encode('utf-8'))
                
                # Get response
                response = sock.recv(4096)
                
                if response and b"Enter access band" not in response:
                    print(f"\n*** BACKDOOR RESPONSE FOR '{cmd}' ***")
                    print(f"Raw: {repr(response)}")
                    print(f"Decoded: {response.decode('utf-8', errors='replace')}")
                
                sock.close()
                
            except Exception as e:
                print(f"Error testing backdoor '{cmd}': {e}")
    
    except Exception as e:
        print(f"Analysis error: {e}")

if __name__ == "__main__":
    comprehensive_analysis()