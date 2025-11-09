# CTF Network Enumeration and Exploitation Guide

## Overview
This directory contains documentation and scripts for enumerating and exploiting the CTF targets in the 10.12.0.0/24 network.

## Current Status

### Flags Found: 1/12 (3 per system × 4 systems)
- ✅ **CSEC-3961-QOTD** - 10.12.0.136:17 (Flag 1 - Enumeration)

### Systems Identified: 4
1. **10.12.0.42** - Linux (Ubuntu) - ProFTPD 1.3.5, SSH, nginx
2. **10.12.0.111** - Windows - IIS, SMB, WinRM
3. **10.12.0.136** - Windows - RDP, MSRPC, QOTD (flag found)
4. **10.12.0.194** - Linux (Ubuntu) - SSH, Apache

## Files in This Directory

### Documentation
- `enumeration_plan.md` - Detailed enumeration plan for each system
- `findings_summary.md` - Summary of findings and vulnerabilities
- `flags_found.txt` - Running list of found flags
- `README_CTF.md` - This file

### Scripts
- `enumeration_scripts.py` - Python scripts for service enumeration
- `proftpd_exploit.py` - ProFTPD mod_copy exploit script

## Quick Start

### 1. Verify Network Access
```bash
# Test connectivity
ping -c 1 10.12.0.42
ping -c 1 10.12.0.111
ping -c 1 10.12.0.136
ping -c 1 10.12.0.194
```

### 2. Get the QOTD Flag (Already Found)
```bash
# Connect to QOTD service
python3 -c "import socket; s=socket.socket(); s.connect(('10.12.0.136',17)); print(s.recv(1024).decode()); s.close()"
# Or use telnet/nc
telnet 10.12.0.136 17
```

### 3. Exploit ProFTPD on 10.12.0.42
```bash
python3 proftpd_exploit.py 10.12.0.42
```

### 4. Enumerate Web Services
```bash
# Use gobuster or dirb
gobuster dir -u http://10.12.0.42 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
gobuster dir -u http://10.12.0.111:8080 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
gobuster dir -u http://10.12.0.194 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

### 5. Enumerate SMB
```bash
smbclient -L //10.12.0.111
enum4linux -a 10.12.0.111
```

## Key Vulnerabilities

### High Priority
1. **ProFTPD 1.3.5** (10.12.0.42) - CVE-2015-3306 mod_copy RCE
2. **Web Services** - Directory traversal, file uploads, default credentials
3. **SMB** (10.12.0.111) - Anonymous access, share enumeration

### Medium Priority
1. **SSH** - Weak credentials on 10.12.0.42 and 10.12.0.194
2. **RDP** (10.12.0.136) - Weak credentials
3. **WinRM** (10.12.0.111) - Weak credentials

## Flag Locations to Check

### Linux Systems
- `/flag.txt`
- `/root/flag.txt`
- `/home/*/flag.txt`
- `/var/www/html/flag.txt`
- `/tmp/flag.txt`

### Windows Systems
- `C:\flag.txt`
- `C:\Users\*\flag.txt`
- `C:\Users\*\Desktop\flag.txt`
- `C:\inetpub\wwwroot\flag.txt`

## Notes
- Each system has 3 flags (enumeration, user, root)
- Systems are independent - can work on them in parallel
- Be careful not to lock yourself out
- Document all methods used (bonus points for alternate methods)

## Next Steps
1. ✅ Document found flag
2. ⏳ Exploit ProFTPD on 10.12.0.42
3. ⏳ Enumerate web directories
4. ⏳ Enumerate SMB shares
5. ⏳ Check other services for flags
