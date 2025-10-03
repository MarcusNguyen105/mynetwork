#!/usr/bin/env python3
import socket
import time

def test_sequential_access():
    """Test accessing all levels in sequence on one connection"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(15)
        
        print("=== SEQUENTIAL ACCESS TEST ===")
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        
        # Get initial banner
        banner = sock.recv(4096)
        print(f"Banner: {banner.decode('utf-8', errors='replace')}")
        
        all_responses = []
        
        # Access each level in sequence
        for level in range(1, 7):
            print(f"\n--- Accessing Level {level} ---")
            
            # Send level
            sock.send(f"{level}\n".encode('utf-8'))
            
            # Get immediate response
            response = sock.recv(4096)
            decoded = response.decode('utf-8', errors='replace')
            print(f"Level {level} response: {repr(decoded)}")
            all_responses.append(decoded)
            
            # Wait a bit and check for additional data
            time.sleep(1)
            try:
                sock.settimeout(2)
                extra = sock.recv(4096)
                if extra:
                    extra_decoded = extra.decode('utf-8', errors='replace')
                    print(f"Extra data: {repr(extra_decoded)}")
                    all_responses.append(extra_decoded)
            except socket.timeout:
                pass
        
        # Try sending an empty line to see if anything happens
        print(f"\n--- Sending empty line ---")
        sock.send(b"\n")
        try:
            sock.settimeout(3)
            final_response = sock.recv(4096)
            if final_response:
                final_decoded = final_response.decode('utf-8', errors='replace')
                print(f"Final response: {repr(final_decoded)}")
                all_responses.append(final_decoded)
        except socket.timeout:
            print("No final response")
        
        sock.close()
        
        # Analyze all responses together
        print(f"\n=== ANALYSIS OF ALL RESPONSES ===")
        combined = ''.join(all_responses)
        print(f"Combined responses: {repr(combined)}")
        
        # Look for flag patterns
        import re
        flag_patterns = [
            r'uscc\{[^}]*\}',
            r'flag\{[^}]*\}', 
            r'\{[^}]*\}',
            r'[A-Za-z0-9_]{20,}',  # Long strings that might be encoded
        ]
        
        for pattern in flag_patterns:
            matches = re.findall(pattern, combined, re.IGNORECASE)
            if matches:
                print(f"*** POTENTIAL FLAG PATTERN {pattern}: {matches} ***")
        
        # Check if first letters spell something
        level_names = ["SCAVENGER", "HAULER", "MECHANIC", "QUARRY FOREMAN", "YARD MANAGER", "BOSS"]
        first_letters = ''.join([name[0] for name in level_names])
        print(f"First letters of levels: {first_letters}")
        
        # Check if there are any hidden characters
        for i, char in enumerate(combined):
            if ord(char) > 127 or (ord(char) < 32 and char not in '\n\r\t'):
                print(f"Non-ASCII/control char at pos {i}: {ord(char)} ({repr(char)})")
        
    except Exception as e:
        print(f"Error: {e}")

def test_reverse_access():
    """Test accessing levels in reverse order"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(15)
        
        print("\n=== REVERSE ACCESS TEST ===")
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        
        # Skip banner
        sock.recv(4096)
        
        # Access levels in reverse order (6 to 1)
        for level in range(6, 0, -1):
            print(f"Accessing level {level}...")
            sock.send(f"{level}\n".encode('utf-8'))
            response = sock.recv(4096)
            decoded = response.decode('utf-8', errors='replace')
            print(f"Response: {repr(decoded)}")
            
            if 'flag' in decoded.lower() or 'uscc' in decoded.lower():
                print(f"*** POTENTIAL FLAG IN REVERSE ACCESS: {decoded} ***")
        
        sock.close()
        
    except Exception as e:
        print(f"Reverse access error: {e}")

if __name__ == "__main__":
    test_sequential_access()
    test_reverse_access()