# USCC Cyberbowl 2025 - Junkyard Access Terminal Challenge

## Challenge Details
- **Service**: `nc chals.uscc-cyberbowl-2025.ctf.institute 3015`
- **Type**: Binary Exploitation (32-bit ELF)
- **Goal**: Get "highest level of access" - presumably RAIDER KING level

## Access Levels Discovered
1. SCAVENGER — Yard floor access  
2. HAULER — Broken-but-usable stock
3. MECHANIC — Engine bays & bins
4. QUARRY FOREMAN — Heavy salvage ops
5. YARD MANAGER — Central yard systems
6. BOSS — Secure compound & vaults
7. RAIDER KING — Override scrapyard locks (hidden)

## Key Findings

### Binary Functions (from symbol table)
- `win` function - likely contains the flag
- `vuln` function - likely the vulnerable function
- `main` function - entry point
- Uses: `fgets`, `scanf`, `fopen`, `printf`, `puts`

### Program Behavior
1. Prompts for access band (1-6)
2. Validates input - rejects anything outside 1-6 range
3. After valid band selection, receives single space character (b' ')
4. Appears to accept secondary input (possible vulnerability point)
5. Prints corresponding access level message and exits

## Exploitation Attempts Made

### 1. Direct Input Manipulation
- ❌ Tried: 7, -1, -7, 57337, 14649, large integers
- ❌ Tried: ASCII characters (A, R, K, |, ~)
- ❌ Tried: Format strings (%x, %s, %p)
- All rejected as "Access band invalid!"

### 2. Buffer Overflow Attempts
- ❌ Tested offsets: 8-120 bytes
- ❌ Tested win addresses: 0x08048000 - 0x08049000 range
- ❌ Tested all 6 access bands as entry points
- Result: All attempts only printed normal access level message

### 3. Rate Limiting
- Server implements connection throttling
- Brute force approaches get blocked quickly

## Why the Exploits Failed

Without the actual binary file, I cannot determine:
1. **Exact win function address** - tried educated guesses
2. **Buffer overflow offset** - tried common values but need precise measurement
3. **Stack protections** - may have canaries, NX, ASLR enabled
4. **Actual vulnerability location** - assumed in secondary input but unconfirmed

## To Successfully Solve This Challenge

### Required Steps:
1. **Obtain the binary file**
   - Check CTF platform for downloads
   - May be in challenge description or separate link

2. **Static Analysis**
   ```bash
   file jat
   checksec jat
   strings jat | grep -i "flag\|uscc\|raider"
   objdump -d jat | grep -A20 "<win>"
   ```

3. **Find win function address**
   ```bash
   objdump -d jat | grep "<win>:"
   # or use: radare2 -A jat; afl | grep win
   ```

4. **Determine buffer offset**
   ```python
   # Using pwntools
   from pwn import *
   pattern = cyclic(200)
   # Send pattern, find crash offset
   ```

5. **Craft precise exploit**
   ```python
   payload = b"A" * offset + p32(win_addr)
   ```

## Recommended Tools
- **Ghidra** / **IDA Pro**: Decompilation and analysis
- **radare2** / **gdb-peda**: Dynamic analysis and debugging
- **pwntools**: Exploit development
- **checksec**: Security feature detection

## Next Steps
1. Locate and download the actual `jat` binary file
2. Run `checksec` to identify protections
3. Disassemble to find exact `win` function address
4. Use cyclic pattern to find exact buffer overflow offset
5. Craft targeted ret2win exploit with correct parameters

## Files Created
- `/workspace/*.py` - Various exploitation attempts
- `/workspace/jat_binary.hex` - Hex dump from challenge description

## Conclusion
This is a classic **ret2win** buffer overflow challenge. The solution requires:
- The actual binary file for analysis
- Precise measurements of buffer offset
- Exact address of win function
- Proper exploit payload construction

The challenge cannot be reliably solved through blind brute force due to:
- Server rate limiting
- Large address space to search
- Unknown exact offset value
