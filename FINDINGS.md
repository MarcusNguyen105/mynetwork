# CTF Challenge Analysis: Complete Findings

## Challenge
- **Target**: `nc chals.uscc-cyberbowl-2025.ctf.institute 3013`
- **Binary**: Advanced Employee Management System v1.0

## What We Know

### Program Behavior
1. Default administrator account created with:
   - Name: "Administrator"
   - PIN: 1234 (changes each run? Or fixed?)
   - Address: varies (ASLR-like, e.g., 0x9a0b008)

2. Employee structure (32 bytes):
   - Offset 0: `struct employee *next` (4 bytes)
   - Offset 4: `char name[24]` (24 bytes) 
   - Offset 28: `int pin` (4 bytes)

3. Memory allocation pattern:
   - Admin at: base_addr
   - Employee 1 at: base_addr + 0x20 (32 bytes)
   - Employee 2 at: base_addr + 0x40
   - etc.

### Vulnerabilities Tested

#### ✗ Cannot Delete System Administrator
- Attempting to delete admin shows: "You are not allowed to delete the system administrator!"
- Admin remains protected in the linked list

#### ✓ Use-After-Free Exists
- Can create employee at address X
- Delete employee (frees memory at X)
- Create new employee (reuses address X)
- However, doesn't affect admin's memory

#### ✗ No Format String Vulnerability
- Sending `%x`, `%n`, etc. in name field stores as literal string
- Not interpreted as format specifiers

#### ✗ No Buffer Overflow in Name
- Input limited to 18 characters via `%18s` scanf
- Cannot overflow to adjacent memory

#### ✗ Cannot Create Duplicate Admin
- Creating second "Administrator" with PIN 484 doesn't help
- view_secrets() checks the FIRST/original Administrator

### Access Control
- Option 3 "Access Secret HR Files" checks: `if (admin->pin == 0x1E4)` where 0x1E4 = 484
- Admin PIN is 1234, needs to be 484
- Error message: "Your administrator seems to have the wrong PIN number configured!"

## Attempted Exploits (All Failed)

1. ✗ Delete admin and recreate with PIN 484
2. ✗ Use-after-free to overwrite admin memory  
3. ✗ Create duplicate "Administrator" with correct PIN
4. ✗ Buffer overflow in name field
5. ✗ Format string attack
6. ✗ Manipulate linked list pointers

## Missing Piece

The vulnerability must be one of:

### Theory 1: Integer Overflow/Underflow
- Maybe PIN input can accept values outside 0-9999 range
- Try negative numbers: -3050 might wrap to 484?
- Try large numbers that truncate to 484

### Theory 2: Write-What-Where via scanf
- The `%x` scanf for employee ID might allow writing to arbitrary address
- Could we delete address `0xADMIN_ADDR + 28` (PIN location)?

### Theory 3: Hidden Input/Option
- Maybe there's a secret option 6, 7, etc.
- Or special input that changes behavior

### Theory 4: Race Condition
- Multiple rapid requests might corrupt state

### Theory 5: PIN Arithmetic
- Maybe the check is `(pin1 + pin2 + ...) == 484`
- Or `(pin1 * pin2) mod something == 484`

### Theory 6: Heap Grooming
- Create specific pattern of employees
- Delete in specific order
- Cause heap metadata corruption
- Overwrite admin PIN through heap chunks

## Recommended Next Steps

1. **Test Integer Manipulation**:
   ```
   Try PIN values: -3050, 65536+484, 0xFFFF, etc.
   ```

2. **Test Arbitrary Address Delete**:
   ```
   Calculate admin_pin_address = admin_addr + 28
   Try to delete that specific address
   ```

3. **Heap Grooming Pattern**:
   ```
   Create employees: A, B, C
   Delete: B
   Create: D (with crafted data)
   Delete: A  
   Create: E (overwrites admin somehow?)
   ```

4. **Source Code Analysis**:
   - Need to reverse engineer the actual binary
   - Use tools like Ghidra, IDA Pro, radare2

## Tools Needed

- Proper ELF binary file (current paste is corrupted)
- Disassembler (Ghidra/IDA)
- Debugger (gdb with pwndbg)
- Local instance to test without rate limits

## Current Blocker

Without the actual compiled binary or source code, we're limited to black-box testing.
The remote service appears to have no obvious vulnerability from our extensive testing.

**The admin PIN stubbornly remains 1234 despite all our attempts to change it to 484.**
