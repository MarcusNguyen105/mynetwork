#!/usr/bin/env python3
"""
CTF Challenge Solver: Security Through Obscurity
URL: http://chals.uscc-cyberbowl-2025.ctf.institute:3004/
"""

import requests
from bs4 import BeautifulSoup
import re
import base64
import json
from urllib.parse import urljoin, urlparse
import sys

class CTFSolver:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
    def initial_recon(self):
        """Perform initial reconnaissance on the website"""
        print(f"[*] Starting reconnaissance on {self.base_url}")
        
        try:
            response = self.session.get(self.base_url)
            print(f"[+] Status Code: {response.status_code}")
            print(f"[+] Response Headers:")
            for header, value in response.headers.items():
                print(f"    {header}: {value}")
            
            return response
        except Exception as e:
            print(f"[-] Error accessing URL: {e}")
            return None
    
    def analyze_html(self, response):
        """Analyze HTML content for hidden elements"""
        print("\n[*] Analyzing HTML content...")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check for HTML comments
        comments = soup.find_all(string=lambda text: isinstance(text, str) and text.strip().startswith('<!--'))
        if comments:
            print("[+] Found HTML comments:")
            for comment in comments:
                print(f"    {comment.strip()}")
        
        # Check for hidden inputs
        hidden_inputs = soup.find_all('input', {'type': 'hidden'})
        if hidden_inputs:
            print("[+] Found hidden inputs:")
            for inp in hidden_inputs:
                print(f"    Name: {inp.get('name', 'N/A')}, Value: {inp.get('value', 'N/A')}")
        
        # Check for data attributes
        elements_with_data = soup.find_all(attrs={"data-flag": True})
        if elements_with_data:
            print("[+] Found elements with data-flag attributes:")
            for elem in elements_with_data:
                print(f"    {elem.get('data-flag')}")
        
        # Check for any elements with suspicious attributes
        for elem in soup.find_all():
            for attr in elem.attrs:
                if any(keyword in attr.lower() for keyword in ['flag', 'secret', 'hidden', 'obscure', 'ctf']):
                    print(f"[+] Found suspicious attribute '{attr}' in {elem.name}: {elem.get(attr)}")
        
        return soup
    
    def analyze_javascript(self, soup, response):
        """Analyze JavaScript for obfuscated content"""
        print("\n[*] Analyzing JavaScript...")
        
        # Find all script tags
        scripts = soup.find_all('script')
        js_content = []
        
        for i, script in enumerate(scripts):
            if script.string:
                js_content.append(script.string)
                print(f"[+] Found inline script #{i+1}")
                
                # Look for common obfuscation patterns
                if 'eval(' in script.string:
                    print("    [!] Found eval() - possible obfuscation")
                if 'atob(' in script.string:
                    print("    [!] Found atob() - possible base64 encoding")
                if 'String.fromCharCode' in script.string:
                    print("    [!] Found String.fromCharCode - possible character encoding")
                
                # Try to extract base64 encoded strings
                b64_pattern = r'[A-Za-z0-9+/]{20,}={0,2}'
                b64_matches = re.findall(b64_pattern, script.string)
                for match in b64_matches:
                    try:
                        decoded = base64.b64decode(match).decode('utf-8', errors='ignore')
                        if decoded.isprintable():
                            print(f"    [!] Possible base64 string decoded: {decoded}")
                    except:
                        pass
            
            # Check for external scripts
            if script.get('src'):
                print(f"[+] Found external script: {script.get('src')}")
                try:
                    js_url = urljoin(self.base_url, script.get('src'))
                    js_response = self.session.get(js_url)
                    if js_response.status_code == 200:
                        js_content.append(js_response.text)
                        print(f"    [+] Downloaded external script")
                except:
                    pass
        
        return js_content
    
    def check_cookies(self, response):
        """Check for interesting cookies"""
        print("\n[*] Checking cookies...")
        
        if response.cookies:
            for cookie in response.cookies:
                print(f"[+] Cookie: {cookie.name} = {cookie.value}")
                
                # Try to decode cookie values
                try:
                    decoded = base64.b64decode(cookie.value).decode('utf-8', errors='ignore')
                    if decoded.isprintable():
                        print(f"    Decoded: {decoded}")
                except:
                    pass
    
    def check_common_paths(self):
        """Check for common hidden paths"""
        print("\n[*] Checking common hidden paths...")
        
        common_paths = [
            'robots.txt',
            '.git/HEAD',
            '.htaccess',
            'flag.txt',
            'flag',
            'secret',
            'hidden',
            'admin',
            'backup',
            '.env',
            'config.php',
            'source',
            'src',
            '.DS_Store',
            'README.md',
            'TODO.txt'
        ]
        
        for path in common_paths:
            url = urljoin(self.base_url, path)
            try:
                response = self.session.get(url, timeout=5)
                if response.status_code == 200:
                    print(f"[+] Found {path}: Status {response.status_code}")
                    if len(response.text) < 1000:  # Only print if content is reasonably sized
                        print(f"    Content: {response.text[:200]}...")
            except:
                pass
    
    def check_response_headers(self, response):
        """Check for interesting response headers"""
        print("\n[*] Checking response headers for clues...")
        
        interesting_headers = ['X-Flag', 'X-Secret', 'X-CTF', 'X-Hidden', 'Flag', 'Secret']
        
        for header in interesting_headers:
            if header in response.headers:
                print(f"[+] Found interesting header: {header} = {response.headers[header]}")
    
    def run(self):
        """Run the complete analysis"""
        print("="*60)
        print("CTF Challenge: Security Through Obscurity")
        print("="*60)
        
        # Initial reconnaissance
        response = self.initial_recon()
        if not response:
            return
        
        # Analyze HTML
        soup = self.analyze_html(response)
        
        # Analyze JavaScript
        js_content = self.analyze_javascript(soup, response)
        
        # Check cookies
        self.check_cookies(response)
        
        # Check response headers
        self.check_response_headers(response)
        
        # Check common paths
        self.check_common_paths()
        
        # Print raw HTML for manual inspection
        print("\n[*] Raw HTML content (first 1000 chars):")
        print(response.text[:1000])
        print("\n[*] Analysis complete!")

if __name__ == "__main__":
    url = "http://chals.uscc-cyberbowl-2025.ctf.institute:3004/"
    solver = CTFSolver(url)
    solver.run()