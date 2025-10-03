# CTF Challenge: Advanced Employee Management System

## Challenge Overview
**Target**: `nc chals.uscc-cyberbowl-2025.ctf.institute 3013`

This is a binary exploitation challenge where you need to access secret HR files by bypassing PIN authentication.

## Problem Statement
- The system has a default Administrator account with PIN **1234**
- To access secret files (Option 3), the admin PIN must be **484** (0x1E4)  
- The admin cannot be deleted (protected)
- **Goal**: Change the admin PIN from 1234 to 484 and access the flag

## Files in This Repository

| File | Description |
|------|-------------|
| `SOLUTION.md` | Detailed vulnerability analysis and exploitation strategy |
| `FINDINGS.md` | Complete list of tested attacks and results |
| `aems` | Binary file (may be corrupted from paste) |
| `exploit*.py` | Various exploitation attempts |
| `socket_exploit.py` | Working connection script (✓ connects successfully) |

## What We Discovered

### ✓ Confirmed Facts
1. **Use-After-Free vulnerability exists** - can delete and recreate employees
2. **Memory addresses are leaked** via the List Employees function
3. **Employee struct is 32 bytes**:
   - `struct employee *next` (4 bytes)
   - `char name[24]` (24 bytes)
   - `int pin` (4 bytes)
4. **Admin is protected** - cannot be deleted directly
5. **PIN check**: `view_secrets()` verifies `admin->pin == 0x1E4`

### ✗ Failed Exploitation Attempts
- Delete admin and recreate with PIN 484
- Use-after-free to overwrite admin memory
- Create duplicate "Administrator" with correct PIN
- Buffer overflow in name field (limited to 18 chars)
- Format string attack (not vulnerable)
- Delete PIN address directly (0xADMIN+28)
- Integer overflow in PIN field
- Heap spraying/grooming

## Working Exploit Scripts

### Connect and Interact
```bash
python3 socket_exploit.py
```

This script successfully connects and allows interaction with the service.

### Test Specific Attacks
```bash
python3 simple_exploit.py      # Basic UAF attempt
python3 duplicate_admin.py     # Duplicate admin test
python3 creative_exploit.py    # Advanced techniques
```

## Next Steps to Solve

### Option 1: Get the Actual Binary
The binary provided in the challenge prompt is likely corrupted. To properly solve:
1. Download the actual ELF binary from the CTF platform
2. Analyze with `Ghidra`, `IDA Pro`, or `radare2`
3. Reverse engineer the `view_secrets()` and `win()` functions
4. Identify the exact vulnerability

### Option 2: Advanced Heap Exploitation
The vulnerability likely involves:
- Precise heap grooming
- Exploiting malloc/free metadata
- Corrupting the linked list structure
- Writing to admin PIN via heap overlap

### Option 3: Find Hidden Functionality
- Test for hidden menu options
- Try special input sequences
- Look for undocumented features

## Manual Testing

You can manually connect and explore:
```bash
# If netcat is available:
nc chals.uscc-cyberbowl-2025.ctf.institute 3013

# Commands to try:
# 4 - List employees (shows addresses)
# 1 - Create employee
# 2 - Delete employee (enter hex address)
# 3 - Access secrets (need admin PIN = 484)
```

## Key Insight

The error message **"Your administrator seems to have the wrong PIN number configured! Please ask them to change it!"** is a strong hint that we need to:
1. Find a way to WRITE to the admin's PIN field
2. Change the value at `admin_address + 28` from 1234 to 484

The use-after-free vulnerability is present, but the exact technique to exploit it and modify the admin PIN remains to be discovered.

## Tools Used

- Python 3 with `pwntools` library
- Socket programming
- Binary string analysis

## Status

🟡 **Partial Solution** - Can connect and interact with the service, vulnerability identified but not yet exploited successfully.

## For CTF Participants

If you're working on this challenge:
1. Start with `socket_exploit.py` to understand the service
2. Read `SOLUTION.md` for detailed vulnerability analysis
3. Review `FINDINGS.md` to see what's already been tested
4. Focus on heap exploitation techniques and precise memory manipulation

The flag is likely in format: `USCC{...}`

Good luck! 🚩
