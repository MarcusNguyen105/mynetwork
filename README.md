# Junkyard Access Terminal - CTF Challenge Analysis

## Challenge Summary
**USCC Cyberbowl 2025** - Binary Exploitation Challenge  
**Goal**: Get the highest level of access (RAIDER KING level)  
**Service**: `nc chals.uscc-cyberbowl-2025.ctf.institute 3015`

## Current Status: ⚠️ Incomplete - Binary File Required

I've conducted extensive analysis and exploitation attempts on this challenge, but **cannot complete it without the actual binary file**. The hex dump provided appears to be corrupted or improperly formatted for direct analysis.

## What I've Discovered

### Program Behavior
1. Prompts for access band selection (1-6)
2. Validates input strictly - only accepts 1-6
3. Has 7 access levels total:
   - Levels 1-6: Standard access (SCAVENGER through BOSS)
   - **Level 7: RAIDER KING** (hidden - the target)
4. Contains a `win()` function that likely reads and displays the flag
5. Contains a `vuln()` function that is likely exploitable

### Exploitation Attempts Made
- ✅ Confirmed secondary input exists after band selection
- ❌ Tried 1000+ buffer overflow combinations (unknown correct address/offset)
- ❌ Tried format string vulnerabilities
- ❌ Tried integer overflows
- ❌ Tried direct input manipulation
- ❌ Server rate-limiting prevents brute force

## Files Created

### 📄 `SOLUTION_SUMMARY.md`
Detailed report of all attempts and findings

### 📄 `solve_template.py`  
**Ready-to-use exploit script** - Just needs two values:
- `WIN_ADDR`: Address of the win() function
- `OFFSET`: Buffer overflow offset

### 📁 Analysis Scripts
- `connect.py` - Basic connection test
- `test_inputs.py` - Input testing
- `find_offset.py` - Offset finder (attempted)
- `comprehensive_exploit.py` - Brute force attempts

## How to Complete This Challenge

### Step 1: Get the Binary
You need to download the actual `jat` binary file from the CTF platform. Check:
- Challenge description page
- Downloads section
- CTF dashboard
- Ask CTF organizers

### Step 2: Analyze the Binary
```bash
# Check file type and protections
file jat
checksec jat  # or: checksec --file=jat

# Find the win function address
objdump -d jat | grep "<win>:"
# Example output: 08048596 <win>:
# Use this address in solve_template.py

# Alternative: use radare2
r2 -A jat
afl | grep win
```

### Step 3: Find Buffer Overflow Offset
```bash
# Run the template script in offset-finding mode
python3 solve_template.py --find-offset

# Or manually with gdb:
gdb jat
run
# Enter band: 6
# Enter payload: (cyclic pattern)
# Note crash address, calculate offset
```

### Step 4: Update and Run Exploit
```python
# Edit solve_template.py:
WIN_ADDR = 0x08048596  # From objdump
OFFSET = 32            # From cyclic pattern

# Run exploit:
python3 solve_template.py
```

## Expected Solution Type
Based on analysis, this is a **ret2win** buffer overflow challenge:
1. Select access band (likely band 6)
2. Overflow buffer in secondary input
3. Overwrite return address with win() function address
4. win() function executes and prints flag

## Tools Needed
- **objdump** / **readelf**: Analyze ELF file
- **gdb** / **gdb-peda**: Debug and find offsets
- **pwntools**: Python exploitation framework (already installed)
- **Optional**: Ghidra, radare2, IDA for deeper analysis

## Quick Start (Once You Have the Binary)

```bash
# 1. Analyze
objdump -d jat | grep "<win>:" | head -1
# Output: 08048596 <win>:

# 2. Find offset (try 32 first, common for 32-bit)
# Test with solve_template.py --find-offset

# 3. Update solve_template.py
nano solve_template.py
# Set WIN_ADDR = 0x08048596
# Set OFFSET = 32

# 4. Run exploit
python3 solve_template.py
```

## Architecture
- **32-bit ELF** binary
- Uses standard C library functions
- No PIE (likely) - addresses should be static

## Contact
If you can provide the actual binary file, I can:
1. Analyze it with proper tools
2. Find exact win() address
3. Determine correct offset
4. Create working exploit
5. Retrieve the flag

## Notes
- Server has rate limiting - avoid brute force
- Challenge is solvable with proper binary analysis
- Template script is ready and tested (with placeholder values)
- All tools and framework are installed and working

---

**Next Action Required**: Obtain the actual `jat` binary file from the CTF platform.
