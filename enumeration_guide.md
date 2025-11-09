# Comprehensive Enumeration Guide

## System 1: 10.12.0.42 (Linux/Ubuntu)

### Ports Open:
- 21/tcp - FTP (ProFTPD 1.3.5)
- 22/tcp - SSH (OpenSSH 8.2p1)
- 80/tcp - HTTP (nginx 1.18.0)

### Enumeration Steps:

#### 1. FTP Enumeration (Port 21)
```bash
# Check for anonymous login
ftp 10.12.0.42
# Try: anonymous/anonymous or anonymous/

# Check ProFTPD version and known vulnerabilities
searchsploit ProFTPD 1.3.5

# Try mod_copy vulnerability (CVE-2015-3306) if applicable
# Check for directory traversal
```

#### 2. Web Server Enumeration (Port 80)
```bash
# Basic enumeration
curl -v http://10.12.0.42/
curl -v http://10.12.0.42/robots.txt
curl -v http://10.12.0.42/sitemap.xml

# Directory brute forcing
gobuster dir -u http://10.12.0.42/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
dirb http://10.12.0.42/

# Check for common files
curl http://10.12.0.42/flag.txt
curl http://10.12.0.42/flag
curl http://10.12.0.42/.flag.txt
curl http://10.12.0.42/index.html
curl http://10.12.0.42/index.php

# Nikto scan
nikto -h http://10.12.0.42/

# Check HTTP headers
curl -I http://10.12.0.42/
```

#### 3. SSH Enumeration (Port 22)
```bash
# Banner grabbing
nc 10.12.0.42 22

# Check for weak credentials (if you have wordlists)
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://10.12.0.42

# Check SSH version for known vulnerabilities
ssh -v 10.12.0.42
```

---

## System 2: 10.12.0.111 (Windows)

### Ports Open:
- 80/tcp - HTTP (Microsoft HTTPAPI httpd 2.0)
- 135/tcp - MSRPC
- 139/tcp - NetBIOS-SSN
- 5985/tcp - WinRM (HTTP)
- 8080/tcp - HTTP (IIS 10.0)

### Enumeration Steps:

#### 1. Web Server Enumeration (Ports 80 & 8080)
```bash
# Port 80
curl -v http://10.12.0.111/
curl -v http://10.12.0.111/robots.txt
gobuster dir -u http://10.12.0.111/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
nikto -h http://10.12.0.111/

# Port 8080 (IIS)
curl -v http://10.12.0.111:8080/
curl -v http://10.12.0.111:8080/robots.txt
gobuster dir -u http://10.12.0.111:8080/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
nikto -h http://10.12.0.111:8080/

# Check for common files
curl http://10.12.0.111/flag.txt
curl http://10.12.0.111:8080/flag.txt
```

#### 2. SMB Enumeration (Port 139)
```bash
# List shares
smbclient -L //10.12.0.111/ -N

# Try anonymous access
smbclient //10.12.0.111/IPC$ -N
smbclient //10.12.0.111/C$ -N

# Enum4linux
enum4linux -a 10.12.0.111

# Nmap SMB scripts
nmap --script smb-enum-shares,smb-enum-users,smb-os-discovery -p 139 10.12.0.111
```

#### 3. WinRM Enumeration (Port 5985)
```bash
# Check WinRM
crackmapexec winrm 10.12.0.111 -u '' -p ''
crackmapexec winrm 10.12.0.111 -u 'guest' -p 'guest'

# Try Evil-WinRM if credentials found
# evil-winrm -i 10.12.0.111 -u username -p password
```

#### 4. MSRPC Enumeration (Port 135)
```bash
# RPC enumeration
rpcclient -U "" -N 10.12.0.111
# Then try: srvinfo, enumdomusers, enumdomgroups
```

---

## System 3: 10.12.0.136 (Windows) - FLAG 1 FOUND

### Ports Open:
- 7/tcp - echo
- 9/tcp - discard
- 13/tcp - daytime
- **17/tcp - qotd** ⭐ **FLAG: CSEC-3961-QOTD**
- 19/tcp - chargen
- 135/tcp - MSRPC
- 3389/tcp - RDP

### Flag Found:
✅ **Flag 1: CSEC-3961-QOTD** (from QOTD service on port 17)

### Hint:
"This looks like a new, fully patched system. Maybe there is a vulnerable, 3rd party service installed instead."

### Enumeration Steps:

#### 1. Investigate Unusual Ports
```bash
# Check QOTD service (already found flag)
nc 10.12.0.136 17
telnet 10.12.0.136 17

# Check other unusual ports
nc 10.12.0.136 7    # echo
nc 10.12.0.136 9    # discard
nc 10.12.0.136 13   # daytime
nc 10.12.0.136 19   # chargen
```

#### 2. RDP Enumeration (Port 3389)
```bash
# Banner grabbing
nc 10.12.0.136 3389
nmap -sV -p 3389 10.12.0.136

# Check for BlueKeep or other RDP vulnerabilities
nmap --script rdp-enum-encryption,rdp-vuln-ms12-020 -p 3389 10.12.0.136

# Try to connect (if credentials found)
# xfreerdp /u:username /p:password /v:10.12.0.136
```

#### 3. Third-Party Service Detection
```bash
# Full port scan for any other services
nmap -p- -sV 10.12.0.136

# UDP scan (may reveal other services)
nmap -sU --top-ports 1000 10.12.0.136

# Check for common third-party services
nmap --script vuln -p- 10.12.0.136
```

#### 4. SMB Enumeration (if available)
```bash
nmap --script smb-enum-shares,smb-enum-users -p 139,445 10.12.0.136
smbclient -L //10.12.0.136/ -N
```

---

## System 4: 10.12.0.194 (Linux/Ubuntu)

### Ports Open:
- 22/tcp - SSH (OpenSSH 7.6p1)
- 80/tcp - HTTP (Apache 2.4.29)

### Enumeration Steps:

#### 1. Web Server Enumeration (Port 80)
```bash
# Basic checks
curl -v http://10.12.0.194/
curl -v http://10.12.0.194/robots.txt
curl -v http://10.12.0.194/.htaccess

# Directory brute forcing
gobuster dir -u http://10.12.0.194/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt
dirb http://10.12.0.194/

# Check for common files
curl http://10.12.0.194/flag.txt
curl http://10.12.0.194/flag
curl http://10.12.0.194/index.php
curl http://10.12.0.194/index.html

# Nikto scan
nikto -h http://10.12.0.194/

# Check Apache version for vulnerabilities
# Apache 2.4.29 may have CVE-2019-0211 (mod_rewrite) or other issues
searchsploit Apache 2.4.29
```

#### 2. SSH Enumeration (Port 22)
```bash
# Banner grabbing
nc 10.12.0.194 22
ssh -v 10.12.0.194

# Check OpenSSH 7.6p1 for vulnerabilities
searchsploit OpenSSH 7.6

# Try weak credentials
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://10.12.0.194
```

---

## General Enumeration Tips:

1. **Always check for flag files**:
   ```bash
   find / -name "flag.txt" 2>/dev/null
   find / -name "*flag*" 2>/dev/null
   ```

2. **Check common locations**:
   - `/root/flag.txt`
   - `/home/*/flag.txt`
   - `/var/www/html/flag.txt`
   - `C:\flag.txt`
   - `C:\Users\*\flag.txt`

3. **After gaining initial access**:
   - Check current user: `whoami` / `id`
   - Check sudo permissions: `sudo -l`
   - Check for SUID binaries: `find / -perm -4000 2>/dev/null`
   - Check for world-writable files: `find / -perm -2 -type f 2>/dev/null`
   - Check running processes: `ps aux`
   - Check network connections: `netstat -antp` / `ss -antp`

4. **Windows-specific checks**:
   - Check user privileges: `whoami /priv`
   - Check for unquoted service paths
   - Check scheduled tasks: `schtasks /query /fo LIST /v`
   - Check for AlwaysInstallElevated registry keys
