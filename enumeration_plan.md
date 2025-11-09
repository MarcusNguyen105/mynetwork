# Network Enumeration and Exploitation Plan

## Summary
- **4 live systems** found in 10.12.0.0/24 network
- **1 flag already found**: CSEC-3961-QOTD (10.12.0.136:17)

---

## System 1: 10.12.0.42 (Linux - Ubuntu)
**Services:**
- Port 21: FTP - ProFTPD 1.3.5
- Port 22: SSH - OpenSSH 8.2p1
- Port 80: HTTP - nginx 1.18.0

**Vulnerabilities to check:**
1. **ProFTPD 1.3.5** - Known vulnerabilities:
   - CVE-2011-4130 (mod_copy module command execution)
   - CVE-2015-3306 (mod_copy module command execution)
   - Check for anonymous FTP access
   - Check for default/weak credentials

2. **OpenSSH 8.2p1** - Check for:
   - Weak/default credentials
   - Known vulnerabilities (relatively recent, check for CVE-2020-15778)

3. **nginx 1.18.0** - Check for:
   - Directory traversal
   - Default pages
   - Hidden directories/files
   - Web application vulnerabilities

**Enumeration steps:**
1. FTP enumeration:
   - Try anonymous login
   - Check for writable directories
   - List all files and directories
   - Check for flag files
   
2. Web enumeration:
   - Directory brute force (gobuster/dirb)
   - Check robots.txt, sitemap.xml
   - Check for common files (flag.txt, flag, flags, etc.)
   - Check source code for comments

3. SSH enumeration:
   - Try common username/password combinations
   - Check for SSH key authentication

---

## System 2: 10.12.0.111 (Windows)
**Services:**
- Port 80: HTTP - Microsoft HTTPAPI httpd 2.0
- Port 135: MSRPC - Microsoft Windows RPC
- Port 139: NetBIOS-SSN
- Port 5985: HTTP - Microsoft HTTPAPI httpd 2.0 (WinRM)
- Port 8080: HTTP - Microsoft IIS httpd 10.0

**Vulnerabilities to check:**
1. **IIS 10.0** (port 8080):
   - Check for default pages
   - Directory traversal
   - Web application vulnerabilities
   - Check for PUT method enabled
   
2. **WinRM** (port 5985):
   - Check for weak credentials
   - Check for known vulnerabilities
   
3. **SMB** (port 139):
   - Enumeration with enum4linux/smbclient
   - Check for anonymous access
   - Check for shares
   - Check for known vulnerabilities (EternalBlue, etc.)

**Enumeration steps:**
1. Web enumeration (ports 80, 8080):
   - Directory brute force
   - Check for web applications
   - Check for file upload vulnerabilities
   
2. SMB enumeration:
   - `smbclient -L //10.12.0.111`
   - `enum4linux -a 10.12.0.111`
   - Check for anonymous access
   
3. WinRM enumeration:
   - Try common credentials
   - Check for PowerShell remoting

---

## System 3: 10.12.0.136 (Windows)
**Services:**
- Port 7: echo
- Port 9: discard
- Port 13: daytime
- Port 17: qotd (Quote of the Day) - **FLAG FOUND: CSEC-3961-QOTD**
- Port 19: chargen
- Port 135: MSRPC
- Port 3389: RDP (Terminal Services)

**Vulnerabilities to check:**
1. **RDP** (port 3389):
   - Check for weak credentials
   - Check for BlueKeep (CVE-2019-0708) if older Windows
   - Try common username/password combinations
   
2. **MSRPC** (port 135):
   - Enumeration with rpcclient
   - Check for null sessions
   
3. **Other ports** (7, 9, 13, 19):
   - These are informational services
   - May contain hints or flags

**Enumeration steps:**
1. Already found flag on port 17
2. Check other informational ports for additional hints
3. RDP enumeration:
   - Try common credentials
   - Check for known vulnerabilities
4. MSRPC enumeration:
   - `rpcclient -U "" -N 10.12.0.136`
   - Check for null session access

---

## System 4: 10.12.0.194 (Linux - Ubuntu)
**Services:**
- Port 22: SSH - OpenSSH 7.6p1
- Port 80: HTTP - Apache httpd 2.4.29

**Vulnerabilities to check:**
1. **OpenSSH 7.6p1** - Check for:
   - Weak/default credentials
   - Known vulnerabilities (CVE-2018-15473, etc.)
   
2. **Apache 2.4.29** - Check for:
   - Directory traversal
   - Default pages
   - Hidden directories/files
   - Web application vulnerabilities
   - Check for .htaccess files

**Enumeration steps:**
1. Web enumeration:
   - Directory brute force
   - Check robots.txt
   - Check for common files
   - Check source code
   
2. SSH enumeration:
   - Try common username/password combinations
   - Check for SSH key authentication

---

## Tools Needed
- nmap (for scanning)
- gobuster/dirb (for web directory brute forcing)
- smbclient/enum4linux (for SMB enumeration)
- hydra/medusa (for brute forcing)
- metasploit (for exploitation)
- Python scripts (for custom exploits)
- ProFTPD exploit scripts (for mod_copy vulnerability)

---

## Flag Locations (Expected)
Based on the instructions:
- **Flag 1**: Found through scanning/enumeration (already found one: CSEC-3961-QOTD)
- **Flag 2**: Requires low-level user access
- **Flag 3**: Requires root/administrator access

Most flags are in "flag.txt" or similarly named files.
