#!/usr/bin/env python3
import socket
import time

def try_different_inputs():
    host = "chals.uscc-cyberbowl-2025.ctf.institute"
    port = 3015
    
    # Try different inputs that might reveal more information
    test_inputs = [
        "6",           # Normal level 6
        "06",          # Zero-padded
        "6.0",         # Decimal
        "six",         # Word
        "BOSS",        # Job title
        "admin",       # Common admin input
        "root",        # Common root input
        "flag",        # Direct flag request
        "help",        # Help command
        "?",           # Help symbol
        "ls",          # List command
        "cat flag",    # Common flag command
        "id",          # ID command
        "whoami",      # Who am I command
        "pwd",         # Print working directory
        "exit",        # Exit command
        "quit",        # Quit command
        "",            # Empty input
        "\n",          # Just newline
        "6\nhelp",     # Multiple commands
        "6\nls",       # Multiple commands
        "6\ncat flag", # Multiple commands
    ]
    
    for test_input in test_inputs:
        print(f"\n{'='*50}")
        print(f"Testing input: '{test_input}'")
        print('='*50)
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            
            # Receive banner
            banner = sock.recv(1024).decode('utf-8')
            print(f"Banner: {banner.strip()}")
            
            # Send test input
            if isinstance(test_input, str):
                sock.send(test_input.encode('utf-8'))
            else:
                sock.send(test_input)
            
            # Receive all available data
            full_response = ""
            timeout_count = 0
            while timeout_count < 3:  # Try up to 3 times
                try:
                    sock.settimeout(2)
                    data = sock.recv(1024).decode('utf-8')
                    if not data:
                        break
                    full_response += data
                    timeout_count = 0  # Reset timeout counter
                except socket.timeout:
                    timeout_count += 1
                    if timeout_count >= 3:
                        break
                except:
                    break
            
            sock.close()
            
            if full_response.strip():
                print(f"Response: {full_response.strip()}")
            else:
                print("No response received")
                
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(0.5)  # Small delay between requests

if __name__ == "__main__":
    try_different_inputs()