#!/usr/bin/env python3
# Try to extract useful information from the provided binary hex dump

binary_text = """ELF               …4   <      4   	 (      4   4€4€               T  TT                    € €ô  ô               Ÿ ŸD  H             ŸŸè   è            h  hhD   D         Påtdl  l‹l‹L   L         Qåtd                          Råtd    Ÿ Ÿ            /lib/ld-linux.so.2           GNU                        GNU ‡ÅÞB¶ÎRsyÖ°Ï¬Çü                       ­KãÀ                G              i              N              4              ®                             T              x              Š              A              p                            [              9              b              %                 ¬‰      libc.so.6 _IO_stdin_used exit fopen __isoc99_scanf puts putchar stdin printf fgets strlen memset stdout stderr setvbuf __libc_start_main write GLIBC_2.7 GLIBC_2.1 GLIBC_2.0 __gmon_start__"""

# Look for addresses and function names
import re

# Extract strings that look like they contain addresses or important info
lines = binary_text.split('\n')
for line in lines:
    if 'win' in line.lower() or 'vuln' in line.lower():
        print(f"Found: {line}")

# Try to find hex patterns that might be addresses
# In the full binary data, look for patterns

full_data = open('/workspace/jat_binary.hex', 'r').read()

# Look for "win" function reference
if 'win' in full_data:
    idx = full_data.index('win')
    print(f"\n'win' found at index {idx}")
    print(f"Context: ...{full_data[max(0,idx-50):idx+50]}...")

# Look for function addresses in symbol table area
print("\nLooking for symbol references...")
for match in re.finditer(r'(win|vuln|main)', full_data, re.IGNORECASE):
    start = max(0, match.start() - 30)
    end = min(len(full_data), match.end() + 30)
    print(f"\nMatch '{match.group()}' at {match.start()}:")
    print(f"  Context: {repr(full_data[start:end])}")
