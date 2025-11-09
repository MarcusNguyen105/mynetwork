# Network Enumeration Summary

## Overview
This directory contains comprehensive enumeration documentation and scripts for the 10.12.0.0/24 network penetration testing exercise.

## Files Created

1. **enumeration_results.md** - Detailed findings for each system with ports, services, and flags
2. **enumeration_guide.md** - Step-by-step enumeration guide with commands for each system
3. **enumeration_scripts.sh** - Executable script with quick reference commands
4. **quick_reference.md** - Quick checklist and priority order for enumeration

## Current Status

### Systems Discovered: 4
- 10.12.0.42 (Linux/Ubuntu)
- 10.12.0.111 (Windows)
- 10.12.0.136 (Windows) ⭐
- 10.12.0.194 (Linux/Ubuntu)

### Flags Found: 1/12
- ✅ **CSEC-3961-QOTD** (10.12.0.136 - Port 17 - QOTD service)

### Flags Remaining: 11
- 3 flags per system × 4 systems = 12 total
- 1 found, 11 remaining

## Next Steps

### Immediate Actions:
1. **Web Server Enumeration** (All systems)
   - Check for flag files, hidden directories, web applications
   - Use gobuster/dirb for directory brute forcing

2. **FTP Enumeration** (10.12.0.42)
   - Check for anonymous access
   - Investigate ProFTPD 1.3.5 vulnerabilities (CVE-2015-3306)

3. **SMB Enumeration** (10.12.0.111)
   - Check for anonymous share access
   - Enumerate users and shares

4. **Third-Party Service Detection** (10.12.0.136)
   - Full port scan (TCP and UDP)
   - Look for vulnerable third-party services as hinted

5. **Apache Enumeration** (10.12.0.194)
   - Check for CVE-2019-0211 (mod_rewrite)
   - Directory brute forcing

## Key Vulnerabilities to Investigate

- **ProFTPD 1.3.5** (10.12.0.42): CVE-2015-3306 (mod_copy)
- **Apache 2.4.29** (10.12.0.194): CVE-2019-0211 (mod_rewrite)
- **OpenSSH 7.6** (10.12.0.194): CVE-2018-15473 (username enumeration)

## Usage

From your Kali environment, run:
```bash
# Review the enumeration guide
cat enumeration_guide.md

# Use the quick reference
cat quick_reference.md

# Execute enumeration commands (copy from scripts)
./enumeration_scripts.sh
```

## Important Notes

- Each system has 3 flags: enumeration, low-level user, root/admin
- Systems are independent - can be attacked in any order
- Same exploit can only be used once across all systems
- Be careful not to lock yourself out of systems
- If stuck for >1 hour, reach out for hints

## Flag Format
Flags appear to be in format: `CSEC-XXXX-XXXX`
Example: `CSEC-3961-QOTD`
