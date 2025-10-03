#!/usr/bin/env python3
"""
JavaScript Deobfuscator for CTF Challenge
"""

import re
import requests
from bs4 import BeautifulSoup
import execjs
import json

class JSDeobfuscator:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        
    def fetch_page(self):
        """Fetch the main page"""
        response = self.session.get(self.base_url)
        return response.text
    
    def extract_obfuscated_js(self, html):
        """Extract obfuscated JavaScript from HTML"""
        soup = BeautifulSoup(html, 'html.parser')
        scripts = soup.find_all('script')
        
        obfuscated_scripts = []
        for script in scripts:
            if script.string and ('_0x' in script.string or 'eval' in script.string):
                obfuscated_scripts.append(script.string)
        
        return obfuscated_scripts
    
    def analyze_hex_array_obfuscation(self, script):
        """Analyze common hex array obfuscation pattern"""
        print("[*] Analyzing hex array obfuscation...")
        
        # Extract the array function
        array_func_match = re.search(r'function\s+(_0x[a-f0-9]+)\(\){.*?return\s*\[(.*?)\];', script, re.DOTALL)
        if array_func_match:
            func_name = array_func_match.group(1)
            array_content = array_func_match.group(2)
            
            # Extract strings from array
            strings = re.findall(r"'([^']*)'", array_content)
            print(f"[+] Found {len(strings)} strings in array function {func_name}:")
            for i, s in enumerate(strings):
                print(f"    [{i}]: {s}")
            
            return strings
        
        return []
    
    def try_manual_deobfuscation(self, script):
        """Try to manually deobfuscate the script"""
        print("\n[*] Attempting manual deobfuscation...")
        
        # Look for the rotator function pattern
        rotator_match = re.search(r'function\s+(_0x[a-f0-9]+)\(_0x[a-f0-9]+,_0x[a-f0-9]+\){.*?}', script, re.DOTALL)
        if rotator_match:
            print(f"[+] Found rotator function: {rotator_match.group(1)}")
        
        # Extract all function calls that might reveal something
        func_calls = re.findall(r'(_0x[a-f0-9]+)\((0x[a-f0-9]+)\)', script)
        print(f"[+] Found {len(func_calls)} function calls")
        
        # Look for console.log or other revealing patterns
        if 'console' in script:
            console_matches = re.findall(r'console\.[a-zA-Z]+\((.*?)\)', script)
            print(f"[+] Found console statements: {console_matches}")
        
        # Look for window.location or redirects
        if 'location' in script:
            location_matches = re.findall(r'location.*?=.*?[\'"]([^\'"]+)[\'"]', script)
            print(f"[+] Found location assignments: {location_matches}")
        
        # Look for fetch or XMLHttpRequest
        if 'fetch' in script:
            fetch_matches = re.findall(r'fetch\([\'"]([^\'"]+)[\'"]', script)
            print(f"[+] Found fetch calls: {fetch_matches}")
    
    def check_external_scripts(self):
        """Check external JavaScript files"""
        print("\n[*] Checking external scripts...")
        
        # Check art.js
        art_url = self.base_url.rstrip('/') + '/art.js'
        try:
            response = self.session.get(art_url)
            if response.status_code == 200:
                print(f"[+] Downloaded art.js ({len(response.text)} bytes)")
                
                # Look for interesting patterns
                if 'flag' in response.text.lower():
                    print("[!] Found 'flag' keyword in art.js")
                    flag_context = re.findall(r'.{0,50}flag.{0,50}', response.text, re.IGNORECASE)
                    for context in flag_context:
                        print(f"    Context: {context}")
                
                return response.text
        except Exception as e:
            print(f"[-] Error fetching art.js: {e}")
        
        return None
    
    def check_hidden_endpoints(self):
        """Check for hidden API endpoints"""
        print("\n[*] Checking for hidden endpoints...")
        
        endpoints = [
            '/api/flag',
            '/api/secret',
            '/flag',
            '/secret',
            '/hidden',
            '/.hidden',
            '/admin',
            '/debug',
            '/test',
            '/obscure',
            '/getFlag',
            '/flag.php',
            '/flag.json',
            '/api',
            '/api/v1',
            '/api/v1/flag'
        ]
        
        for endpoint in endpoints:
            url = self.base_url.rstrip('/') + endpoint
            try:
                response = self.session.get(url, timeout=3)
                if response.status_code != 404:
                    print(f"[+] Found endpoint {endpoint}: Status {response.status_code}")
                    if response.status_code == 200 and len(response.text) < 500:
                        print(f"    Response: {response.text}")
            except:
                pass
    
    def run(self):
        """Run the deobfuscation analysis"""
        print("="*60)
        print("JavaScript Deobfuscation Analysis")
        print("="*60)
        
        # Fetch the page
        html = self.fetch_page()
        
        # Extract obfuscated scripts
        scripts = self.extract_obfuscated_js(html)
        
        for i, script in enumerate(scripts):
            print(f"\n[*] Analyzing script #{i+1}")
            print(f"[*] Script length: {len(script)} characters")
            
            # Analyze hex array obfuscation
            strings = self.analyze_hex_array_obfuscation(script)
            
            # Try manual deobfuscation
            self.try_manual_deobfuscation(script)
        
        # Check external scripts
        art_js = self.check_external_scripts()
        
        # Check hidden endpoints
        self.check_hidden_endpoints()
        
        # Save the obfuscated script for manual analysis
        if scripts:
            with open('obfuscated.js', 'w') as f:
                f.write(scripts[0])
            print("\n[+] Saved obfuscated script to obfuscated.js for manual analysis")

if __name__ == "__main__":
    url = "http://chals.uscc-cyberbowl-2025.ctf.institute:3004/"
    deobfuscator = JSDeobfuscator(url)
    deobfuscator.run()