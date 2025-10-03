#!/usr/bin/env python3
import socket
import time
import re

def deep_analysis():
    """Deep analysis of all responses"""
    
    print("=== DEEP ANALYSIS OF JUNKYARD RESPONSES ===")
    
    # First, let's collect all the standard responses and analyze them
    standard_levels = [1, 2, 3, 4, 5, 6]
    level_descriptions = {}
    
    for level in standard_levels:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            # Use the lag behavior: send level, then another level to get description
            sock.send(f"{level}\n".encode('utf-8'))
            sock.recv(4096)  # Skip prompt
            
            sock.send("1\n".encode('utf-8'))  # Trigger to get description
            response = sock.recv(4096)
            
            decoded = response.decode('utf-8', errors='replace')
            level_descriptions[level] = decoded.strip()
            
            print(f"Level {level}: {repr(decoded)}")
            
            sock.close()
            
        except Exception as e:
            print(f"Error getting level {level}: {e}")
    
    # Analyze the descriptions for hidden patterns
    print(f"\n=== ANALYZING DESCRIPTIONS FOR PATTERNS ===")
    
    all_text = ' '.join(level_descriptions.values())
    print(f"All text combined: {all_text}")
    
    # Look for hidden characters or encoding
    for level, desc in level_descriptions.items():
        print(f"\nLevel {level} analysis:")
        print(f"  Text: {desc}")
        print(f"  Length: {len(desc)}")
        print(f"  Bytes: {desc.encode('utf-8')}")
        
        # Check each character
        for i, char in enumerate(desc):
            if ord(char) > 127 or ord(char) < 32:
                if char not in ['\n', '\r', '\t']:
                    print(f"  Special char at pos {i}: {ord(char)} ({repr(char)})")
    
    # Try to find patterns in first letters, last letters, etc.
    descriptions_clean = [desc.replace('\n', '').strip() for desc in level_descriptions.values()]
    
    first_letters = ''.join([desc[0] if desc else '' for desc in descriptions_clean])
    print(f"\nFirst letters: {first_letters}")
    
    # Try different encodings or patterns
    print(f"\n=== TESTING DIFFERENT APPROACHES ===")
    
    # Maybe the flag is revealed by accessing levels in a specific pattern
    # based on the descriptions themselves
    
    # Test accessing levels based on alphabetical order of descriptions
    desc_with_levels = [(desc, level) for level, desc in level_descriptions.items()]
    desc_with_levels.sort()  # Sort by description
    
    alphabetical_order = [level for desc, level in desc_with_levels]
    print(f"Levels in alphabetical order of descriptions: {alphabetical_order}")
    
    # Test this order
    result = test_sequence(alphabetical_order)
    if result:
        return result
    
    # Test reverse alphabetical
    reverse_alpha = list(reversed(alphabetical_order))
    print(f"Reverse alphabetical order: {reverse_alpha}")
    result = test_sequence(reverse_alpha)
    if result:
        return result
    
    # Test based on length of descriptions
    desc_by_length = sorted([(len(desc), level) for level, desc in level_descriptions.items()])
    length_order = [level for length, level in desc_by_length]
    print(f"Levels by description length: {length_order}")
    result = test_sequence(length_order)
    if result:
        return result
    
    # Maybe we need to send all levels at once?
    print(f"\n=== TESTING BULK SENDING ===")
    result = test_bulk_sending()
    if result:
        return result
    
    # Test sending levels as a single string
    print(f"\n=== TESTING COMBINED INPUT ===")
    result = test_combined_input()
    if result:
        return result
    
    return None

def test_sequence(sequence):
    """Test a specific sequence and look for flags"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        
        print(f"Testing sequence: {sequence}")
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        sock.recv(4096)  # Skip banner
        
        for level in sequence:
            sock.send(f"{level}\n".encode('utf-8'))
            response = sock.recv(4096)
            decoded = response.decode('utf-8', errors='replace')
            
            if ('uscc{' in decoded.lower() or 'flag{' in decoded.lower() or 
                'cyberbowl{' in decoded.lower()):
                print(f"*** FLAG FOUND: {decoded} ***")
                return decoded
        
        # Try one more command after the sequence
        sock.send("flag\n".encode('utf-8'))
        response = sock.recv(4096)
        decoded = response.decode('utf-8', errors='replace')
        if decoded.strip() and 'Enter access band' not in decoded:
            print(f"Post-sequence response: {repr(decoded)}")
            if 'uscc{' in decoded.lower():
                return decoded
        
        sock.close()
        
    except Exception as e:
        print(f"Error testing sequence: {e}")
    
    return None

def test_bulk_sending():
    """Test sending all levels at once"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        sock.recv(4096)  # Skip banner
        
        # Send all levels at once
        bulk_input = "123456\n"
        print(f"Sending bulk input: {repr(bulk_input)}")
        sock.send(bulk_input.encode('utf-8'))
        
        response = sock.recv(4096)
        decoded = response.decode('utf-8', errors='replace')
        print(f"Bulk response: {repr(decoded)}")
        
        if 'uscc{' in decoded.lower():
            return decoded
        
        sock.close()
        
    except Exception as e:
        print(f"Bulk sending error: {e}")
    
    return None

def test_combined_input():
    """Test various combined inputs"""
    combined_inputs = [
        "654321",
        "135246", 
        "246135",
        "123456789",
        "987654321",
        "1a2b3c4d5e6f",
        "admin123456",
        "root654321",
        "flag123456",
    ]
    
    for input_str in combined_inputs:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            print(f"Testing combined input: {repr(input_str)}")
            sock.send(f"{input_str}\n".encode('utf-8'))
            
            response = sock.recv(4096)
            decoded = response.decode('utf-8', errors='replace')
            
            if decoded.strip() and 'Enter access band' not in decoded:
                print(f"  Response: {repr(decoded)}")
                if 'uscc{' in decoded.lower():
                    return decoded
            
            sock.close()
            
        except Exception as e:
            pass
    
    return None

if __name__ == "__main__":
    result = deep_analysis()
    
    if result:
        print(f"\n*** FLAG FOUND: {result} ***")
    else:
        print("\nNo flag found with deep analysis approach.")
        print("The flag might require a different technique or be hidden elsewhere.")