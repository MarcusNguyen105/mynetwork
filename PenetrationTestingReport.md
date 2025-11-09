# Penetration Testing Report - 10.12.0.0/24 Network

**Date:** 2025-11-08  
**Scope:** 10.12.0.42, 10.12.0.111, 10.12.0.136, 10.12.0.194  
**Status:** Active reconnaissance and enumeration phase

---

## Executive Summary

- **Total Live Hosts:** 4
- **Flags Found:** 1/12 (8.33%)
- **Operating Systems:** 2 Linux, 2 Windows

---

## Discovered Systems

### 10.12.0.42 - Linux (Ubuntu)
**OS:** Ubuntu Linux  
**Open Ports:**
- **21/tcp** - ProFTPD 1.3.5
- **22/tcp** - OpenSSH 8.2p1 Ubuntu 4ubuntu0.1
- **80/tcp** - nginx 1.18.0 (Ubuntu)

**Vulnerability Assessment:**
- ProFTPD 1.3.5 has known vulnerabilities (CVE-2015-3306, CVE-2019-12815)
- Check for anonymous FTP access
- Web server should be enumerated for hidden directories and files

**Recommended Actions:**
1. Test anonymous FTP login: `ftp 10.12.0.42`
2. Enumerate web directories: `gobuster dir -u http://10.12.0.42 -w /usr/share/wordlists/dirb/common.txt`
3. Check for ProFTPD exploits: `searchsploit proftpd 1.3.5`
4. Banner grab and manual service interaction

---

### 10.12.0.111 - Windows Server
**OS:** Microsoft Windows  
**Open Ports:**
- **80/tcp** - Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
- **135/tcp** - Microsoft Windows RPC
- **139/tcp** - NetBIOS-SSN
- **5985/tcp** - WinRM (Microsoft HTTPAPI httpd 2.0)
- **8080/tcp** - Microsoft IIS 10.0

**Vulnerability Assessment:**
- Two web servers (ports 80 and 8080) - potential for web-based exploits
- SMB service on 139 - check for null sessions, shares, and SMB vulnerabilities
- WinRM on 5985 - potential for password spraying and remote command execution

**Recommended Actions:**
1. Enumerate SMB shares: `smbclient -L //10.12.0.111 -N`
2. Check for null session: `enum4linux -a 10.12.0.111`
3. Enumerate both web servers:
   - `gobuster dir -u http://10.12.0.111 -w /usr/share/wordlists/dirb/common.txt`
   - `gobuster dir -u http://10.12.0.111:8080 -w /usr/share/wordlists/dirb/common.txt`
4. Check for web application vulnerabilities
5. Attempt WinRM authentication if credentials are found

---

### 10.12.0.136 - Windows Server ⭐
**OS:** Microsoft Windows  
**Open Ports:**
- **7/tcp** - echo
- **9/tcp** - discard
- **13/tcp** - daytime
- **17/tcp** - QOTD (Quote of the Day)
- **19/tcp** - chargen
- **135/tcp** - Microsoft Windows RPC
- **3389/tcp** - Microsoft Terminal Services (RDP)

**🚩 FLAG FOUND #1:**
```
FLAG: CSEC-3961-QOTD
Source: Port 17/tcp (QOTD service)
Hint: "This looks like a new, fully patched system. Maybe there is a vulnerable, 3rd party service installed instead."
```

**Vulnerability Assessment:**
- Legacy network services (echo, discard, daytime, qotd, chargen) are unusual on modern systems
- These services are rarely used and could indicate misconfigurations
- RDP on 3389 - potential for brute force or known RDP vulnerabilities
- Hint suggests looking for vulnerable 3rd-party applications

**Recommended Actions:**
1. ✅ Document QOTD flag (COMPLETED)
2. Interact with each legacy service to look for additional flags or information
3. Check for RDP vulnerabilities: `nmap -p 3389 --script rdp-vuln-ms12-020 10.12.0.136`
4. Look for 3rd-party services (hint provided by flag)
5. Attempt to enumerate Windows version and installed applications via RPC

---

### 10.12.0.194 - Linux (Ubuntu)
**OS:** Ubuntu Linux  
**Open Ports:**
- **22/tcp** - OpenSSH 7.6p1 Ubuntu 4ubuntu0.7
- **80/tcp** - Apache httpd 2.4.29 ((Ubuntu))

**Vulnerability Assessment:**
- Apache 2.4.29 is older - check for known vulnerabilities
- Minimal attack surface (only SSH and HTTP)
- Web application likely hosts content that needs enumeration

**Recommended Actions:**
1. Enumerate web directories: `gobuster dir -u http://10.12.0.194 -w /usr/share/wordlists/dirb/common.txt`
2. Check for Apache vulnerabilities specific to 2.4.29
3. Look for web application vulnerabilities (SQLi, LFI, RFI, etc.)
4. Check for `.git` exposure or sensitive files (robots.txt, backup files)

---

## Detailed Action Plan

### Phase 1: Web Server Enumeration (Priority: HIGH)
All systems except 10.12.0.136 have web servers. These should be thoroughly investigated:

**For 10.12.0.42 (nginx):**
```bash
# Directory enumeration
gobuster dir -u http://10.12.0.42 -w /usr/share/wordlists/dirb/common.txt -x php,html,txt
nikto -h 10.12.0.42

# Manual inspection
curl -v http://10.12.0.42
curl http://10.12.0.42/robots.txt
```

**For 10.12.0.111 (IIS on ports 80 & 8080):**
```bash
# Directory enumeration on both ports
gobuster dir -u http://10.12.0.111 -w /usr/share/wordlists/dirb/common.txt -x asp,aspx,txt
gobuster dir -u http://10.12.0.111:8080 -w /usr/share/wordlists/dirb/common.txt -x asp,aspx,txt

# Check for common IIS vulnerabilities
nikto -h 10.12.0.111:8080
```

**For 10.12.0.194 (Apache):**
```bash
# Directory enumeration
gobuster dir -u http://10.12.0.194 -w /usr/share/wordlists/dirb/common.txt -x php,html,txt
nikto -h 10.12.0.194

# Check for common files
curl http://10.12.0.194/robots.txt
curl http://10.12.0.194/.git/config
```

### Phase 2: FTP Service Investigation (10.12.0.42)
```bash
# Test anonymous access
ftp 10.12.0.42
# Username: anonymous
# Password: anonymous (or your email)

# Search for exploits
searchsploit proftpd 1.3.5
msfconsole
> search proftpd 1.3.5
```

### Phase 3: SMB Enumeration (10.12.0.111)
```bash
# List shares
smbclient -L //10.12.0.111 -N

# Enumerate with enum4linux
enum4linux -a 10.12.0.111

# Try accessing shares
smbclient //10.12.0.111/C$ -N
smbclient //10.12.0.111/ADMIN$ -N
```

### Phase 4: Legacy Services Investigation (10.12.0.136)
```bash
# Interact with each service manually
nc 10.12.0.136 7      # Echo service
nc 10.12.0.136 9      # Discard service
nc 10.12.0.136 13     # Daytime service
nc 10.12.0.136 17     # QOTD service (flag already found here)
nc 10.12.0.136 19     # Chargen service

# Check for additional RPC information
rpcclient -U "" -N 10.12.0.136
```

### Phase 5: Vulnerability Research and Exploitation
After enumeration, research specific vulnerabilities:

1. **ProFTPD 1.3.5** - Known mod_copy vulnerability (CVE-2015-3306)
2. **IIS 10.0** - Check for specific web app vulns
3. **Apache 2.4.29** - Check for specific CVEs
4. **Windows Legacy Services** - Research 3rd party apps (per hint)

---

## Flags Progress Tracker

| System | Flag 1 (Enumeration) | Flag 2 (User Access) | Flag 3 (Root/Admin) |
|--------|---------------------|---------------------|---------------------|
| 10.12.0.42 | ❌ | ❌ | ❌ |
| 10.12.0.111 | ❌ | ❌ | ❌ |
| 10.12.0.136 | ✅ CSEC-3961-QOTD | ❌ | ❌ |
| 10.12.0.194 | ❌ | ❌ | ❌ |

**Total: 1/12 flags captured**

---

## Next Immediate Steps

1. **Start with web servers** - Most likely to yield quick results
   - Run gobuster on all three web servers
   - Manually browse and inspect source code
   - Look for hidden directories and files

2. **FTP enumeration** - Test anonymous access on 10.12.0.42
   - Try to list files
   - Look for flag.txt or similar
   - Test ProFTPD 1.3.5 exploits if needed

3. **SMB investigation** - Enumerate shares on 10.12.0.111
   - Look for accessible shares
   - Search for credentials or flags

4. **Continue legacy service enumeration on 10.12.0.136**
   - Interact with all services manually
   - Look for hints about the "3rd party service"

---

## Tools Needed

Ensure these tools are available on your Kali box:
- nmap (✓ already used)
- gobuster or dirb
- nikto
- smbclient / enum4linux
- ftp client
- netcat (nc)
- searchsploit / msfconsole
- hydra (for potential password attacks)
- burp suite (for web app testing)

---

## Notes

- Remember: Each exploit can only be used once across all flags
- Document all attempts and findings
- Be careful with system modifications
- Reach out for hints if stuck for >1 hour on a specific flag
- Multiple methods may exist for each flag (bonus points opportunity)
