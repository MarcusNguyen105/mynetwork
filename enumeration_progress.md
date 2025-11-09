# Enumeration Progress Log

## 10.12.0.111 (Windows) - Enumeration Attempts

### SMB Enumeration (Port 139)
**Attempted**: `nmap --script smb-enum-shares,smb-enum-users,smb-os-discovery -p 139 10.12.0.111`
**Result**: Scripts ran but didn't return share/user information
**Next Steps**:
- Try port 445 (SMB over TCP/IP)
- Use `enum4linux -a 10.12.0.111`
- Try `smbclient -L //10.12.0.111/ -N` (anonymous)
- Check if SMBv1 is disabled (may need different approach)

### WinRM Enumeration (Port 5985)
**Attempted**: `crackmapexec winrm 10.12.0.111 -u '' -p ''`
**Result**: Requires authentication, empty credentials failed
**Next Steps**:
- Try common usernames (guest, administrator, admin)
- Check web servers for credential leaks or information disclosure
- Look for other ways to get credentials

### Recommended Next Actions:

1. **Check Port 445** (SMB over TCP/IP):
   ```bash
   nmap -p 445 -sV 10.12.0.111
   nmap --script smb-enum-shares,smb-enum-users -p 445 10.12.0.111
   smbclient -L //10.12.0.111/ -N
   ```

2. **Use enum4linux**:
   ```bash
   enum4linux -a 10.12.0.111
   enum4linux -v 10.12.0.111
   ```

3. **Thoroughly Check Web Servers** (Most Important):
   ```bash
   # Port 80
   curl -v http://10.12.0.111/
   curl -v http://10.12.0.111/robots.txt
   curl -v http://10.12.0.111/flag.txt
   gobuster dir -u http://10.12.0.111/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
   
   # Port 8080 (IIS)
   curl -v http://10.12.0.111:8080/
   curl -v http://10.12.0.111:8080/robots.txt
   curl -v http://10.12.0.111:8080/flag.txt
   gobuster dir -u http://10.12.0.111:8080/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
   ```

4. **Check MSRPC** (Port 135):
   ```bash
   rpcclient -U "" -N 10.12.0.111
   # Then try: srvinfo, enumdomusers, enumdomgroups
   ```

5. **Try CrackMapExec with SMB**:
   ```bash
   crackmapexec smb 10.12.0.111 -u 'guest' -p ''
   crackmapexec smb 10.12.0.111 -u '' -p ''
   ```

---

## Priority: Web Server Enumeration

**Web servers are often the easiest entry point** - they don't require authentication and may reveal:
- Flag files
- Directory listings
- Web applications with vulnerabilities
- Information disclosure
- Credentials in source code or comments

**Focus on**: Ports 80 and 8080 on 10.12.0.111, and port 80 on other systems.
