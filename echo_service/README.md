# Echo Service - CTF Challenge (500 pts)

## Challenge Information
- **Name**: Echo Service
- **Points**: 500
- **Category**: Binary Exploitation
- **Connection**: `nc chals.uscc-cyberbowl-2025.ctf.institute 3014`

## Binary Analysis

The challenge provides a 32-bit ELF executable with the following key components:

### Identified Functions
- `main()` - Entry point
- `vuln()` - Vulnerable function (likely contains buffer overflow)
- `read_flag()` - Function that reads and displays the flag
- Various libc functions: `fgets`, `read`, `memset`, `printf`, `puts`, etc.

### Identified Strings
- `"./flag"` - Flag file path
- `"Missing flag file!"` - Error message
- `"---\nECHO SERVICE\n---"` - Service banner
- `"> "` - Input prompt
- `"Invalid command:"` - Error message

### Vulnerability
Based on the function names and typical CTF patterns, this appears to be a classic **buffer overflow** vulnerability where:
1. The `vuln()` function contains an unsafe input operation
2. User input can overflow a buffer and overwrite the return address
3. By overwriting the return address with the address of `read_flag()`, we can execute that function
4. `read_flag()` will read and display the contents of the flag file

## Exploitation Strategy

1. **Find the offset**: Determine how many bytes are needed to reach the return address
2. **Find read_flag address**: Extract the address of the `read_flag()` function from the binary
3. **Craft payload**: Create payload = padding + read_flag_address
4. **Send exploit**: Send the payload to the service

## Usage

### Test the service
```bash
python3 exploit.py test
```

### Exploit with known offset and address
```bash
python3 exploit.py <offset> <read_flag_addr>
```

For example:
```bash
python3 exploit.py 40 0x080486a7
```

## Finding the Correct Values

To properly exploit this, you need to:

1. **Get the binary**: Download the actual ELF file to analyze it properly
2. **Disassemble**: Use tools like `objdump`, `radare2`, or `ghidra` to find:
   - The exact address of `read_flag()`
   - The buffer size in `vuln()`
3. **Calculate offset**: The offset is typically: buffer_size + saved_ebp_size (4 bytes on 32-bit)

### Example Analysis Commands
```bash
# If you have the binary file:
objdump -d echo_service | grep read_flag
readelf -s echo_service | grep read_flag
```

## Notes

- This is a 32-bit ELF binary (little-endian)
- No PIE (Position Independent Executable) appears to be enabled based on the fixed addresses
- The binary uses standard libc functions without apparent mitigations like stack canaries

## Solution Workflow

1. Connect to the service and observe the behavior
2. Find the buffer overflow offset (typically 40-60 bytes for small buffers)
3. Identify the `read_flag()` function address
4. Send payload: `b'A' * offset + p32(read_flag_addr)`
5. Receive the flag!
