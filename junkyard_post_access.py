#!/usr/bin/env python3
import socket
import time

def test_post_access_commands(access_level):
    """Test commands after establishing access level"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(15)
        
        print(f"=== TESTING POST-ACCESS COMMANDS FOR LEVEL {access_level} ===")
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        
        # Get initial prompt
        initial = sock.recv(4096)
        print(f"Initial: {initial.decode('utf-8', errors='replace')}")
        
        # Send access level
        sock.send(f"{access_level}\n".encode('utf-8'))
        
        # Get access response
        access_response = sock.recv(4096)
        print(f"Access response: {access_response.decode('utf-8', errors='replace')}")
        
        # Now try various commands
        commands = [
            "",           # Empty line
            "help",       # Help command
            "ls",         # List
            "dir",        # Directory
            "flag",       # Flag command
            "cat flag",   # Cat flag
            "show flag",  # Show flag
            "get flag",   # Get flag
            "flag.txt",   # Flag file
            "status",     # Status
            "info",       # Info
            "menu",       # Menu
            "options",    # Options
            "commands",   # Commands
            "list",       # List
            "inventory",  # Inventory
            "access",     # Access
            "vault",      # Vault (for BOSS level)
            "secure",     # Secure
            "compound",   # Compound
            "exit",       # Exit
            "quit",       # Quit
            "back",       # Back
            "1",          # Try going to level 1
            "2",          # Try going to level 2
            "admin",      # Admin
            "root",       # Root
            "sudo",       # Sudo
            "whoami",     # Who am I
            "pwd",        # Present working directory
            "cd",         # Change directory
            "find flag",  # Find flag
            "search flag", # Search flag
            "locate flag", # Locate flag
        ]
        
        for cmd in commands:
            try:
                print(f"\n>>> Sending: {repr(cmd)}")
                sock.send(f"{cmd}\n".encode('utf-8'))
                
                # Wait for response
                sock.settimeout(3)
                response = sock.recv(4096)
                
                if response:
                    decoded = response.decode('utf-8', errors='replace')
                    print(f"Response: {repr(decoded)}")
                    
                    # Check if this looks like a flag
                    if 'flag' in decoded.lower() or 'uscc' in decoded.lower() or '{' in decoded:
                        print(f"*** POTENTIAL FLAG FOUND: {decoded} ***")
                else:
                    print("No response")
                    
            except socket.timeout:
                print("Timeout")
            except Exception as e:
                print(f"Error: {e}")
                break
        
        sock.close()
        
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    # Test the highest access level first
    test_post_access_commands(6)
    
    print("\n" + "=" * 80)
    print("TESTING LEVEL 5 AS WELL")
    print("=" * 80)
    
    # Also test level 5 in case level 6 doesn't have the flag
    test_post_access_commands(5)