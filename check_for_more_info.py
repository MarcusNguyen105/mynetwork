#!/usr/bin/env python3
import socket
import time

def check_for_additional_info():
    host = "chals.uscc-cyberbowl-2025.ctf.institute"
    port = 3015
    
    print("Checking for additional information from the service...")
    print("=" * 60)
    
    # Try to see if there's more information after getting BOSS access
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        # Receive banner
        banner = sock.recv(1024).decode('utf-8')
        print(f"Banner: {banner.strip()}")
        
        # Send level 6
        sock.send(b"6\n")
        
        # Wait and see if there's more data
        time.sleep(1)
        
        # Try to receive more data
        try:
            sock.settimeout(5)
            data = sock.recv(1024).decode('utf-8')
            print(f"Response: {repr(data)}")
            
            # Wait a bit more
            time.sleep(2)
            try:
                more_data = sock.recv(1024).decode('utf-8')
                if more_data:
                    print(f"Additional data: {repr(more_data)}")
            except:
                pass
                
        except socket.timeout:
            print("No additional data received")
        except Exception as e:
            print(f"Error: {e}")
        
        sock.close()
        
    except Exception as e:
        print(f"Connection error: {e}")

def try_multiple_connections():
    """Try connecting multiple times to see if there are different responses"""
    host = "chals.uscc-cyberbowl-2025.ctf.institute"
    port = 3015
    
    print("\nTrying multiple connections to see if responses vary...")
    print("=" * 60)
    
    for i in range(5):
        print(f"\nConnection {i+1}:")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            
            # Receive banner
            banner = sock.recv(1024).decode('utf-8')
            print(f"Banner: {banner.strip()}")
            
            # Send level 6
            sock.send(b"6\n")
            
            # Receive response
            response = sock.recv(1024).decode('utf-8')
            print(f"Response: {repr(response)}")
            
            sock.close()
            
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(1)

def check_network_info():
    """Check if there's any network-level information"""
    print("\nChecking network information...")
    print("=" * 60)
    
    host = "chals.uscc-cyberbowl-2025.ctf.institute"
    port = 3015
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        # Get socket info
        local_addr = sock.getsockname()
        remote_addr = sock.getpeername()
        
        print(f"Local address: {local_addr}")
        print(f"Remote address: {remote_addr}")
        
        sock.close()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_for_additional_info()
    try_multiple_connections()
    check_network_info()