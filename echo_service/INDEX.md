# Echo Service CTF Challenge - Complete Toolkit

## 📋 Challenge Overview

**Challenge Name**: Echo Service  
**Points**: 500  
**Category**: Binary Exploitation / Pwn  
**Connection**: `nc chals.uscc-cyberbowl-2025.ctf.institute 3014`

**Vulnerability Type**: Buffer Overflow  
**Objective**: Exploit a buffer overflow to execute the `read_flag()` function

---

## 🚀 Quick Start

**Want to solve this quickly?** → Read [`QUICKSTART.md`](QUICKSTART.md)

**New to binary exploitation?** → Read [`SOLUTION.md`](SOLUTION.md)

**Want full details?** → Read [`README.md`](README.md)

---

## 📁 Files in This Toolkit

### Exploitation Scripts

| File | Description | Usage |
|------|-------------|-------|
| **`exploit.py`** | Main exploitation script | `python3 exploit.py <offset> <addr>` |
| **`bruteforce.py`** | Automated parameter finder | `python3 bruteforce.py` |
| **`analyze_dump.py`** | Binary dump analyzer | `python3 analyze_dump.py` |

### Documentation

| File | Description | For |
|------|-------------|-----|
| **`QUICKSTART.md`** | Fast reference guide | Users who want to solve quickly |
| **`SOLUTION.md`** | Detailed solution walkthrough | Learning the exploitation process |
| **`README.md`** | Challenge analysis | Understanding the vulnerability |
| **`INDEX.md`** | This file - overview | Navigation and reference |

---

## 🎯 Recommended Approach

### For Beginners
1. Read [`SOLUTION.md`](SOLUTION.md) to understand the vulnerability
2. Run `python3 analyze_dump.py` to see what we know
3. Run `python3 exploit.py test` to interact with the service
4. Run `python3 bruteforce.py` to find the correct parameters
5. Submit the flag!

### For Experienced Players
1. Run `python3 bruteforce.py` immediately
2. Or if you prefer manual: `python3 exploit.py 40 0x080486a7` (adjust values)
3. Submit the flag!

### For Learning
1. Read all documentation in order: README → SOLUTION → QUICKSTART
2. Try to find the offset manually using `exploit.py test`
3. Understand why the exploit works
4. Write your own version from scratch

---

## 🔧 Common Commands

```bash
# Automated solution (easiest)
python3 bruteforce.py

# Manual exploitation
python3 exploit.py 40 0x080486a7

# Test the service
python3 exploit.py test

# Analyze what we know
python3 analyze_dump.py

# Brute force offset only
python3 bruteforce.py offset 0x080486a7

# Brute force address only
python3 bruteforce.py address 40

# Test specific parameters
python3 bruteforce.py test 40 0x080486a7
```

---

## 📚 Key Concepts

### What is Buffer Overflow?
A buffer overflow occurs when data written to a buffer exceeds its allocated size, potentially overwriting adjacent memory. In this challenge, we overflow a buffer to overwrite the return address on the stack.

### The Exploitation Flow
```
1. User input → Buffer (fixed size)
2. Input > Buffer size → Overflow
3. Overflow → Overwrite return address
4. Return address → read_flag() function
5. read_flag() → Prints the flag!
```

### What We Need to Find
- **Offset**: How many bytes to fill before the return address (typically 32-72)
- **Target Address**: Memory address of `read_flag()` function (typically 0x08048xxx)

---

## 🔍 Binary Analysis Summary

From the provided binary dump, we identified:

**Functions:**
- `main()` - Entry point
- `vuln()` - Contains the vulnerability
- `read_flag()` - Reads and displays the flag ⭐

**Strings:**
- `"./flag"` - Flag file location
- `"ECHO SERVICE"` - Service banner
- `"> "` - Input prompt

**Key Libc Functions:**
- `fgets()` / `read()` - Input functions (potentially vulnerable)
- `fopen()` / `puts()` - For reading/displaying the flag

---

## 🛠️ Tools Used

- **Python 3** - Scripting language for exploitation
- **socket** module - Network communication
- **struct** module - Binary data packing (for addresses)

### If You Have the Binary File

You can use these tools for deeper analysis:
```bash
# Get binary info
file echo_service
readelf -h echo_service

# Find function addresses
objdump -d echo_service | grep read_flag
readelf -s echo_service | grep read_flag

# Disassemble in Intel syntax
objdump -M intel -d echo_service

# Interactive debugging
gdb echo_service
```

---

## ⚠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| Connection timeout | Server might be down; try again later |
| No flag received | Wrong offset or address; try brute force |
| Script errors | Ensure Python 3 is installed |
| Need actual binary | Check CTF platform for download link |

---

## 📖 Learning Resources

After solving this challenge, learn more about binary exploitation:

- [Binary Exploitation Intro](https://www.exploit-db.com/docs/english/28475-linux-stack-based-buffer-overflows.pdf)
- [x86 Assembly Guide](https://www.cs.virginia.edu/~evans/cs216/guides/x86.html)
- [Pwntools Documentation](https://docs.pwntools.com/)

Practice platforms:
- [picoCTF](https://picoctf.org/)
- [pwnable.kr](http://pwnable.kr/)
- [exploit.education](https://exploit.education/)
- [HackTheBox](https://www.hackthebox.eu/)

---

## 📞 Need Help?

1. **Read the docs**: Start with QUICKSTART.md
2. **Run the scripts**: They're designed to be beginner-friendly
3. **Check output**: Scripts provide detailed feedback
4. **Understand, don't just run**: Read SOLUTION.md to learn

---

## ✅ Success Indicators

You've successfully exploited the service when you see:
- `uscc{...}` - The actual flag!
- `flag{...}` - Alternative flag format
- `Missing flag file!` - You reached `read_flag()` but running locally

---

## 🎓 What You'll Learn

By completing this challenge, you'll understand:
- How buffer overflows work
- Stack memory layout (stack frames, return addresses)
- Return-oriented exploitation basics
- Binary analysis fundamentals
- Network-based exploitation

---

## 🏁 Final Notes

- This is a **classic buffer overflow** challenge - perfect for learning
- The automated brute force should work if the service is online
- Don't just get the flag - understand **why** the exploit works
- Practice makes perfect - try similar challenges after this one

**Good luck, and happy hacking! 🚩**

---

*Created for USCC CyberBowl 2025 CTF*
