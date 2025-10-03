# Echo Service - Quick Start Guide

## TL;DR - Get the Flag Fast! 🚩

This is a buffer overflow CTF challenge. Here's how to solve it quickly:

### Option 1: Automated Brute Force (Easiest)
```bash
cd /workspace/echo_service
python3 bruteforce.py
```

This will automatically try common offset and address combinations until it finds the flag.

⚠️ **Warning**: This will make many connections to the server. Use responsibly!

### Option 2: Manual Exploitation (If you know the values)
```bash
cd /workspace/echo_service
python3 exploit.py <offset> <read_flag_address>

# Example:
python3 exploit.py 40 0x080486a7
```

### Option 3: Test and Explore
```bash
cd /workspace/echo_service
python3 exploit.py test
```

This connects to the service and sends a test pattern to help you understand the behavior.

## What's Included

| File | Purpose |
|------|---------|
| `exploit.py` | Main exploitation script with multiple modes |
| `bruteforce.py` | Automated brute force to find correct parameters |
| `analyze_dump.py` | Analyzes the binary dump for useful info |
| `README.md` | Detailed challenge documentation |
| `SOLUTION.md` | Complete solution guide with explanations |
| `QUICKSTART.md` | This file - quick reference |

## Understanding the Challenge

**Vulnerability**: Buffer overflow in the `vuln()` function  
**Goal**: Overwrite return address to jump to `read_flag()`  
**Difficulty**: The main challenge is finding the correct offset and address

### What You Need to Find

1. **Buffer Offset**: How many bytes until you overwrite the return address? (typically 32-72)
2. **read_flag Address**: Where is the `read_flag()` function located? (typically 0x08048500-0x08048800)

## Quick Commands Reference

```bash
# Run automated brute force
python3 bruteforce.py

# Test the connection
python3 exploit.py test

# Exploit with known values
python3 exploit.py 40 0x080486a7

# Brute force just the offset (if you know the address)
python3 bruteforce.py offset 0x080486a7

# Brute force just the address (if you know the offset)
python3 bruteforce.py address 40

# Test a specific configuration
python3 bruteforce.py test 40 0x080486a7

# View the binary analysis
python3 analyze_dump.py
```

## Troubleshooting

### "Connection timed out"
- The CTF server might be offline or experiencing issues
- Try again in a few minutes
- Check if the CTF is still running

### "Connection refused"
- The service might be down
- Verify the hostname and port are correct
- Check your network connection

### Script doesn't find the flag
- The address range might be wrong - adjust in `bruteforce.py`
- The offset might be outside the common range - adjust the range
- There might be additional protections (ASLR, stack canaries, etc.)

## If Nothing Works

1. **Get the actual binary**:
   ```bash
   wget http://chals.uscc-cyberbowl-2025.ctf.institute/echo_service
   # or check the CTF platform for a download link
   ```

2. **Analyze it properly**:
   ```bash
   file echo_service
   objdump -d echo_service | grep read_flag
   ```

3. **Use proper tools**:
   - Ghidra / IDA Pro for static analysis
   - GDB with pwndbg/gef for dynamic analysis
   - Radare2 for quick disassembly

## Expected Output (Success)

When you successfully exploit the service, you should see:
```
[+] Response:
uscc{your_flag_here_xxxxxxxxxxxxx}
```

Or possibly:
```
Missing flag file! Please contact support if you see this error on the remote target!
```
(This means you successfully redirected execution to `read_flag()`, but the flag file doesn't exist in your local test environment)

## Pro Tips

- Start with `python3 bruteforce.py` and let it run
- The most common offsets in CTF challenges: 40, 44, 48, 52
- The `read_flag` function is usually right after or near `main`
- Look for responses that differ from the normal echo behavior
- Each attempt takes ~1 second due to rate limiting

## Next Steps After Getting the Flag

1. Submit the flag to the CTF platform
2. Review the solution to understand the vulnerability
3. Practice similar challenges on platforms like:
   - picoCTF
   - pwnable.kr
   - exploit.education
   - HackTheBox

Good luck! 🎯
