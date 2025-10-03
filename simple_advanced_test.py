#!/usr/bin/env python3
import socket
import time

def test_special_inputs():
    host = "chals.uscc-cyberbowl-2025.ctf.institute"
    port = 3015
    
    # Try different inputs that might reveal more information
    test_cases = [
        ("7", "Overflow test"),
        ("0", "Underflow test"),
        ("-1", "Negative test"),
        ("999", "Large number"),
        ("6\n", "With newline"),
        ("6\r\n", "With CRLF"),
        ("6 ", "With trailing space"),
        (" 6", "With leading space"),
        ("6; ls", "Command injection"),
        ("6 | cat", "Pipe test"),
        ("6 && ls", "And operator"),
        ("6 || ls", "Or operator"),
    ]
    
    for test_input, description in test_cases:
        print(f"\n{'='*50}")
        print(f"Testing: {description}")
        print(f"Input: {repr(test_input)}")
        print('='*50)
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            
            # Receive banner
            banner = sock.recv(1024).decode('utf-8')
            print(f"Banner: {banner.strip()}")
            
            # Send test input
            sock.send(test_input.encode('utf-8'))
            
            # Try to receive response
            try:
                sock.settimeout(3)
                data = sock.recv(1024).decode('utf-8')
                print(f"Response: {repr(data)}")
                
                # Check for additional data
                time.sleep(0.5)
                try:
                    more_data = sock.recv(1024).decode('utf-8')
                    if more_data:
                        print(f"Additional: {repr(more_data)}")
                except:
                    pass
                    
            except socket.timeout:
                print("No response (timeout)")
            except Exception as e:
                print(f"Error: {e}")
            
            sock.close()
            
        except Exception as e:
            print(f"Connection error: {e}")
        
        time.sleep(0.5)

if __name__ == "__main__":
    test_special_inputs()