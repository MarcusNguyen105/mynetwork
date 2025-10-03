# CTF Challenge Solution: Advanced Employee Management System

## Challenge Details
- **Service**: `nc chals.uscc-cyberbowl-2025.ctf.institute 3013`
- **Type**: Binary Exploitation (Use-After-Free)
- **Objective**: Access secret files to retrieve the flag

## Vulnerability Analysis

### Binary Information
From the strings and symbol table, the binary contains:
- `win` function - reads `./flag` file
- `view_secrets` function - checks admin PIN
- `add`, `delete`, `print` functions for employee management
- `add_admin` function - creates default administrator

### Key Findings

1. **Administrator Setup**:
   - The program creates a default administrator account
   - Name: "Administrator" (hardcoded)
   - Default PIN: Appears to be checked against `0x1E4` (484 decimal)

2. **Use-After-Free Vulnerability**:
   - Employees are stored in a linked list structure
   - The `delete` function frees memory but may leave dangling pointers
   - Memory addresses are leaked via the "List Employees" option (format: `%p`)

3. **Access Control**:
   - Option 3 "Access Secret HR Files" calls `view_secrets()`
   - This function checks if the admin PIN equals `0x1E4` (484)
   - If successful, it likely calls the `win()` function or reads the flag

## Exploitation Strategy

### Method 1: Use-After-Free Attack

1. **List Employees** (Option 4)
   - This reveals the admin's memory address
   - Format: `Employee Id: 0xXXXXXXXX`

2. **Delete the Administrator** (Option 2)
   - Input the admin's address when prompted
   - This frees the memory but may leave pointers intact
   - Note: The program might prevent deleting the system administrator

3. **Create New Employee** (Option 1)
   - The new employee struct will likely reuse the freed memory
   - Name: Can be any value (try "Administrator" or similar)
   - PIN: **484** (0x1E4 in hex)
   - This overwrites the freed admin struct with our controlled data

4. **Access Secret Files** (Option 3)
   - The PIN check should now pass with our crafted value
   - This should print the flag

### Method 2: Direct PIN Manipulation

If the binary allows:
1. Create multiple employees
2. Use the memory leak to calculate offsets
3. Exploit the use-after-free to overwrite the admin PIN value directly
4. Access the secret files

## Manual Exploitation Steps

```bash
# Connect to the service
nc chals.uscc-cyberbowl-2025.ctf.institute 3013

# Step 1: List employees to see the admin
> 4

# Note the admin's Employee Id (e.g., 0x804c008)

# Step 2: Try to delete admin (may fail with "cannot delete system administrator")
> 2
Employee ID to remove: 0x804c008

# Step 3: Create new employee with PIN 484
> 1
Enter employee name: Administrator
Enter employee 4-digit pin: 484

# Step 4: List employees again to verify
> 4

# Step 5: Access secret files
> 3
```

## Automated Exploit Script

See `exploit.py`, `exploit2.py`, or `exploit3.py` for automated exploitation attempts.

### Key Points for Exploitation:
- The admin PIN must equal **484** (decimal) / **0x1E4** (hex)
- Use-after-free allows overwriting freed memory
- Memory addresses are leaked via the list function
- The vulnerability is in the delete/add cycle

## Alternative Approach: Format String

If the input handling has format string vulnerabilities:
- The `%p` in "Debug: Allocated at %p" suggests possible format string issues
- Could potentially read/write arbitrary memory

## Expected Flag Format

The flag should be in the standard CTF format, likely:
```
USCC{...}
```

## Notes

- The binary uses GLIBC 2.0-2.7, suggesting an older system
- No PIE/ASLR mentioned, addresses may be static
- The `win()` function directly reads the flag file
- Connection issues may indicate the challenge server is down or requires VPN access

## Testing

To test locally (if you have the binary):
```bash
./aems
# Follow the manual exploitation steps above
```

## Connection Troubleshooting

If unable to connect:
1. Verify the challenge is still active
2. Check if VPN connection is required
3. Verify correct host/port: `chals.uscc-cyberbowl-2025.ctf.institute:3013`
4. Try using `nc` directly instead of pwntools
