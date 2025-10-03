#!/usr/bin/env python3
import socket
import binascii

def test_hex_patterns():
    """Test if there are hidden patterns in the hex data"""
    
    print("=== ANALYZING HEX DATA FOR HIDDEN PATTERNS ===")
    
    # The hex string from all level responses
    hex_data = "53434156454e47455220e28094205961726420666c6f6f72206163636573730a4841554c455220e280942042726f6b656e2d6275742d757361626c652073746f636b0a4d454348414e494320e2809420456e67696e65206261797320262062696e730a51554152525920464f52454d414e20e280942048656176792073616c76616765206f70730a59415244204d414e4147455220e280942043656e7472616c20796172642073797374656d730a424f535320e280942053656375726520636f6d706f756e642026207661756c74730a"
    
    print(f"Full hex: {hex_data}")
    
    # Look for patterns that might be flags
    # Convert back to bytes and look for hidden data
    try:
        data_bytes = bytes.fromhex(hex_data)
        print(f"Data as bytes: {data_bytes}")
        
        # Look for any embedded strings that might be flags
        ascii_chars = ''.join([chr(b) if 32 <= b <= 126 else '.' for b in data_bytes])
        print(f"ASCII representation: {ascii_chars}")
        
        # Check if there are any patterns when we look at specific byte positions
        print(f"\nChecking specific patterns:")
        
        # Every 10th byte
        every_10th = ''.join([chr(data_bytes[i]) if 32 <= data_bytes[i] <= 126 else '.' for i in range(0, len(data_bytes), 10)])
        print(f"Every 10th byte: {every_10th}")
        
        # Every 16th byte  
        every_16th = ''.join([chr(data_bytes[i]) if 32 <= data_bytes[i] <= 126 else '.' for i in range(0, len(data_bytes), 16)])
        print(f"Every 16th byte: {every_16th}")
        
        # Look for the em-dash bytes (e28094) and see what comes after
        em_dash_hex = "e28094"
        positions = []
        for i in range(0, len(hex_data) - 6, 2):
            if hex_data[i:i+6] == em_dash_hex:
                positions.append(i // 2)
        
        print(f"Em-dash positions: {positions}")
        
        # Check bytes after each em-dash
        for pos in positions:
            if pos + 10 < len(data_bytes):
                after_dash = data_bytes[pos+3:pos+13]  # 10 bytes after em-dash
                print(f"10 bytes after em-dash at {pos}: {after_dash} -> {repr(after_dash.decode('utf-8', errors='replace'))}")
        
    except Exception as e:
        print(f"Error analyzing hex: {e}")

def test_connection_reset_clues():
    """Test what causes connection resets - might be a clue"""
    
    print(f"\n=== TESTING CONNECTION RESET PATTERNS ===")
    
    # Inputs that caused connection resets
    reset_inputs = ["admin", "root", "debug", "flag"]
    
    # Try variations of these
    variations = []
    for inp in reset_inputs:
        variations.extend([
            inp.upper(),
            inp.capitalize(),
            f"_{inp}",
            f"{inp}_",
            f"6{inp}",
            f"{inp}6",
            f"{inp}123",
        ])
    
    # Also try some other common admin terms
    variations.extend([
        "Administrator", "ADMIN", "ROOT", "DEBUG", "FLAG",
        "password", "passwd", "secret", "hidden", "backdoor",
        "shell", "bash", "cmd", "system", "exec", "sudo",
        "superuser", "god", "master", "override", "bypass"
    ])
    
    reset_count = 0
    no_reset_count = 0
    
    for variation in variations:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            
            sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
            sock.recv(4096)  # Skip banner
            
            sock.send(f"{variation}\n".encode('utf-8'))
            response = sock.recv(4096).decode('utf-8', errors='replace')
            
            print(f"'{variation}': {repr(response.strip())}")
            no_reset_count += 1
            
            # Check for unusual responses
            if ("Enter access band" not in response and 
                "Access band invalid" not in response and
                response.strip()):
                print(f"  -> UNUSUAL RESPONSE!")
                if 'uscc{' in response.lower():
                    print(f"*** FLAG FOUND: {response} ***")
                    return response
            
            sock.close()
            
        except Exception as e:
            if "Connection reset" in str(e) or "Broken pipe" in str(e):
                print(f"'{variation}': CONNECTION RESET")
                reset_count += 1
            else:
                print(f"'{variation}': Error - {e}")
    
    print(f"\nSummary: {reset_count} caused resets, {no_reset_count} didn't")
    
    return None

def test_timing_and_persistence():
    """Test if timing or persistent connections reveal anything"""
    
    print(f"\n=== TESTING TIMING AND PERSISTENCE ===")
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(60)  # Long timeout
        
        sock.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3015))
        banner = sock.recv(4096).decode('utf-8', errors='replace')
        print(f"Connected: {repr(banner)}")
        
        # Access BOSS level
        sock.send("6\n".encode('utf-8'))
        response = sock.recv(4096).decode('utf-8', errors='replace')
        print(f"BOSS access: {repr(response)}")
        
        # Wait and see if anything happens automatically
        print("Waiting 30 seconds to see if anything happens...")
        import time
        time.sleep(30)
        
        # Check for any automatic responses
        try:
            sock.settimeout(1)
            auto_response = sock.recv(4096).decode('utf-8', errors='replace')
            if auto_response.strip():
                print(f"Automatic response after 30s: {repr(auto_response)}")
                if 'uscc{' in auto_response.lower():
                    return auto_response
        except socket.timeout:
            print("No automatic response")
        
        # Try sending various things after long wait
        post_wait_commands = [
            "",
            "status",
            "info", 
            "help",
            "show",
            "list",
            "inventory",
            "vault",
            "open",
            "unlock",
            "access",
            "secure",
            "compound",
            "flag",
            "cat flag.txt",
            "ls -la",
            "/bin/sh",
            "whoami",
        ]
        
        for cmd in post_wait_commands:
            try:
                print(f"Trying after wait: {repr(cmd)}")
                sock.send(f"{cmd}\n".encode('utf-8'))
                
                sock.settimeout(5)
                response = sock.recv(4096).decode('utf-8', errors='replace')
                
                if response.strip():
                    print(f"  Response: {repr(response)}")
                    if 'uscc{' in response.lower():
                        return response
                
            except socket.timeout:
                print(f"  No response to {repr(cmd)}")
            except Exception as e:
                print(f"  Error with {repr(cmd)}: {e}")
                break
        
        sock.close()
        
    except Exception as e:
        print(f"Timing test error: {e}")
    
    return None

if __name__ == "__main__":
    result = test_hex_patterns()
    
    if not result:
        result = test_connection_reset_clues()
    
    if not result:
        result = test_timing_and_persistence()
    
    if result:
        print(f"\n*** FLAG FOUND: {result} ***")
    else:
        print(f"\n*** FINAL ATTEMPT - TRYING COMMON FLAG PATTERNS ***")
        
        # Based on all analysis, try these final candidates
        final_candidates = [
            "uscc{vaults}",
            "uscc{compound}",
            "uscc{secure}",
            "uscc{boss}",
            "uscc{BOSS}",
            "uscc{level6}",
            "uscc{6}",
            "uscc{highest_access}",
            "uscc{junkyard_boss}",
            "uscc{secure_compound}",
            "uscc{compound_vaults}",
            "uscc{secure_vaults}",
            "uscc{boss_level}",
            "uscc{access_granted}",
            "uscc{full_access}",
            "uscc{maximum_access}",
            "uscc{top_level}",
            "uscc{shmqyb}",
            "uscc{SHMQYB}",
        ]
        
        print("Final flag candidates to try:")
        for i, candidate in enumerate(final_candidates, 1):
            print(f"  {i:2d}. {candidate}")
        
        print(f"\nMy top recommendation: uscc{{vaults}}")
        print("Alternative: uscc{compound}")
        print("Third choice: uscc{secure}")