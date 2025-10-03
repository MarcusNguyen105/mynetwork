# CTF Challenge Analysis

## Challenge Details
- Host: `chals.uscc-cyberbowl-2025.ctf.institute`
- Port: `3015`
- Type: ELF 32-bit binary exploitation

## Binary Analysis
From the binary data provided, I can identify:

1. **Functions:**
   - `win` - Likely the target function to trigger
   - `vuln` - Likely contains the vulnerability
   - Standard libc functions: `printf`, `scanf`, `fgets`, etc.

2. **Access Levels:**
   - 1: SCAVENGER — Yard floor access
   - 2: HAULER — Broken-but-usable stock
   - 3: MECHANIC — Engine bays & bins
   - 4: QUARRY FOREMAN — Heavy salvage ops
   - 5: YARD MANAGER — Central yard systems
   - 6: BOSS — Secure compound & vaults
   - 7: RAIDER KING — Override scrapyard locks (hidden/secret level)

3. **Program Behavior:**
   - Prompts for access band (1-6)
   - Rejects level 7 with "Access band invalid!"
   - Buffer overflow attempts cause connection reset
   - Format string attacks cause connection reset

## Attempted Exploits

### 1. Direct Input Manipulation
- Sending `7` directly → "Access band invalid!"
- Various encodings (hex, octal, etc.) → No success

### 2. Buffer Overflow
- Buffer sizes: 10, 20, 50, 100, 200, 500, 1000 bytes
- Result: Connection reset (program crash)

### 3. Format String Attack
- Payloads: `%x`, `%p`, `%s`, `%n`
- Result: Connection reset (program crash)

## Next Steps
To successfully exploit this binary, I would need to:

1. Download the actual binary file from the service
2. Analyze it with tools like:
   - `objdump` - disassemble the binary
   - `gdb` - debug and find exact offsets
   - `checksec` - identify security mitigations
   - `radare2` or `ghidra` - reverse engineer the binary

3. Find the exact vulnerability:
   - Buffer overflow offset
   - Return address location
   - Win function address

4. Craft a precise exploit payload to:
   - Overflow the buffer
   - Overwrite the return address
   - Jump to the `win` function

Without the actual binary file or more information about the vulnerability, I cannot create a working exploit.
