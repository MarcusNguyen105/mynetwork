# Network Enumeration Results - 10.12.0.0/24

## Summary
- **Total Systems Found**: 4 live hosts
- **Flags Found**: 1 (CSEC-3961-QOTD on 10.12.0.136)

---

## 10.12.0.42 (Linux/Ubuntu)
**OS**: Linux/Ubuntu  
**MAC**: 00:50:56:A1:D6:13 (VMware)

### Open Ports:
- **21/tcp** - FTP - ProFTPD 1.3.5
- **22/tcp** - SSH - OpenSSH 8.2p1 Ubuntu 4ubuntu0.1
- **80/tcp** - HTTP - nginx 1.18.0 (Ubuntu)

### Flags Found:
- [ ] Flag 1 (Enumeration)
- [ ] Flag 2 (Low-level user)
- [ ] Flag 3 (Root/Admin)

### Notes:
- **ProFTPD 1.3.5** - Check for:
  - CVE-2015-3306 (mod_copy - directory traversal)
  - CVE-2011-4130 (mod_tls vulnerability)
  - Anonymous FTP access
- **nginx 1.18.0** - Generally secure, check for misconfigurations
- **OpenSSH 8.2p1** - Recent version, check for weak credentials
- Check web server for hidden directories, flag files, or web applications

---

## 10.12.0.111 (Windows)
**OS**: Windows  
**MAC**: 00:50:56:A1:90:77 (VMware)

### Open Ports:
- **80/tcp** - HTTP - Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
- **135/tcp** - MSRPC - Microsoft Windows RPC
- **139/tcp** - NetBIOS-SSN - Microsoft Windows netbios-ssn
- **5985/tcp** - HTTP - Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP) - **WinRM**
- **8080/tcp** - HTTP - Microsoft IIS httpd 10.0

### Flags Found:
- [ ] Flag 1 (Enumeration)
- [ ] Flag 2 (Low-level user)
- [ ] Flag 3 (Root/Admin)

### Notes:
- **Two web servers** (port 80 and 8080) - Check both for different content
- **WinRM (5985)** - ✅ Tested: Requires authentication, empty credentials failed
- **SMB (139)** - ✅ Tested: Nmap scripts didn't enumerate shares/users (may need port 445 or different tools)
- **MSRPC (135)** - May reveal user accounts and system info
- **Next**: Try enum4linux, smbclient, check port 445, and thoroughly examine web servers

---

## 10.12.0.136 (Windows)
**OS**: Windows  
**MAC**: 00:50:56:A1:15:F1 (VMware)

### Open Ports:
- **7/tcp** - echo
- **9/tcp** - discard
- **13/tcp** - daytime - Microsoft Windows USA daytime
- **17/tcp** - qotd (Quote of the Day)
- **19/tcp** - chargen
- **135/tcp** - MSRPC - Microsoft Windows RPC
- **3389/tcp** - RDP - Microsoft Terminal Services

### Flags Found:
- [x] Flag 1 (Enumeration) - **CSEC-3961-QOTD** (found on port 17)
- [ ] Flag 2 (Low-level user)
- [ ] Flag 3 (Root/Admin)

### Notes:
- **FLAG FOUND**: CSEC-3961-QOTD on port 17 (QOTD service)
- **Hint**: "This looks like a new, fully patched system. Maybe there is a vulnerable, 3rd party service installed instead."
- **RDP (3389)** - Check for weak credentials, BlueKeep (CVE-2019-0708), or other RDP vulnerabilities
- **Unusual ports** (7, 9, 13, 17, 19) - May indicate custom or third-party services
- **Action**: Perform full port scan (TCP and UDP) to find hidden third-party services
- Check for services on non-standard ports that may be vulnerable

---

## 10.12.0.194 (Linux/Ubuntu)
**OS**: Linux/Ubuntu  
**MAC**: 00:50:56:A1:3C:99 (VMware)

### Open Ports:
- **22/tcp** - SSH - OpenSSH 7.6p1 Ubuntu 4ubuntu0.7
- **80/tcp** - HTTP - Apache httpd 2.4.29 (Ubuntu)

### Flags Found:
- [ ] Flag 1 (Enumeration)
- [ ] Flag 2 (Low-level user)
- [ ] Flag 3 (Root/Admin)

### Notes:
- **Apache 2.4.29** - Check for:
  - CVE-2019-0211 (mod_rewrite vulnerability - local privilege escalation)
  - Directory traversal, exposed files
  - Web application vulnerabilities
- **OpenSSH 7.6p1** - Check for:
  - CVE-2018-15473 (username enumeration)
  - Weak credentials
  - SSH key exposure
- Check web server for hidden directories, flag files, or web applications

---

## Next Steps:
1. Investigate web servers on all systems
2. Check ProFTPD 1.3.5 for vulnerabilities on 10.12.0.42
3. Enumerate SMB shares on Windows systems
4. Check for vulnerable third-party services on 10.12.0.136
5. Examine Apache configuration and content on 10.12.0.194
