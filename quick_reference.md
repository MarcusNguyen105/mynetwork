# Quick Reference - Enumeration Checklist

## Priority Order (Based on Ease of Access)

### 1. Web Servers (Easiest - No Auth Required)
- [ ] 10.12.0.42:80 (nginx)
- [ ] 10.12.0.111:80 (HTTPAPI)
- [ ] 10.12.0.111:8080 (IIS)
- [ ] 10.12.0.194:80 (Apache)

**Quick Commands:**
```bash
for ip in 10.12.0.42 10.12.0.111 10.12.0.194; do
  echo "=== $ip ==="
  curl -s http://$ip/ | head -20
  curl -s http://$ip/robots.txt
  curl -s http://$ip/flag.txt
done
curl -s http://10.12.0.111:8080/
```

### 2. FTP Service
- [ ] 10.12.0.42:21 (ProFTPD 1.3.5)

**Quick Commands:**
```bash
ftp 10.12.0.42
# Try: anonymous/anonymous
# Check for mod_copy vulnerability
```

### 3. SMB Shares
- [ ] 10.12.0.111:139 (NetBIOS)
- [ ] 10.12.0.136:139 (if available)

**Quick Commands:**
```bash
smbclient -L //10.12.0.111/ -N
enum4linux -a 10.12.0.111
```

### 4. WinRM
- [ ] 10.12.0.111:5985

**Quick Commands:**
```bash
crackmapexec winrm 10.12.0.111 -u '' -p ''
```

### 5. RDP
- [ ] 10.12.0.136:3389

**Quick Commands:**
```bash
nc 10.12.0.136 3389
nmap --script rdp-enum-encryption -p 3389 10.12.0.136
```

### 6. SSH (Requires Credentials)
- [ ] 10.12.0.42:22
- [ ] 10.12.0.194:22

**Quick Commands:**
```bash
nc 10.12.0.42 22
nc 10.12.0.194 22
```

---

## Flag Locations to Check (After Access)

### Linux Systems:
```bash
find / -name "*flag*" 2>/dev/null
find / -name "flag.txt" 2>/dev/null
cat /root/flag.txt
cat /home/*/flag.txt
cat /var/www/html/flag.txt
```

### Windows Systems:
```cmd
dir C:\flag.txt /s
dir C:\Users\*\flag.txt /s
type C:\flag.txt
type C:\Users\*\flag.txt
```

---

## Known Vulnerabilities to Check

### ProFTPD 1.3.5 (10.12.0.42)
- CVE-2015-3306: mod_copy directory traversal
- Check: `searchsploit ProFTPD 1.3.5`

### Apache 2.4.29 (10.12.0.194)
- CVE-2019-0211: mod_rewrite privilege escalation
- Check: `searchsploit Apache 2.4.29`

### OpenSSH 7.6 (10.12.0.194)
- CVE-2018-15473: Username enumeration
- Check: `searchsploit OpenSSH 7.6`

---

## Current Status

✅ **Flag Found**: CSEC-3961-QOTD (10.12.0.136 - Port 17)

**Remaining Flags**: 11 (3 per system × 4 systems - 1 found)
