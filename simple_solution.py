#!/usr/bin/env python3
"""
Simple solution - just concatenate the hex values
"""

# Based on our analysis, we found these hex-decoded values:
hex_values = ['f1ed6', 'b2', '9a743', '3a2d4', '4c830', 'aa400', 'a4534']

# The instruction says to concatenate the hashes together
concatenated = ''.join(hex_values)

print("Hex values found:", hex_values)
print("Concatenated:", concatenated)
print(f"\nFlag: CCSU{{{concatenated}}}")

# Alternative ordering based on how they appear in the code
alt1 = "f1ed6b29a7433a2d44c830aa400a4534"
print(f"\nAlternative flag 1: CCSU{{{alt1}}}")

# Try without some values
alt2 = "f1ed69a7434c830aa400"
print(f"\nAlternative flag 2: CCSU{{{alt2}}}")

# The base64 decoded values as hex strings
b64_hex = "c95ee47c70c3eb7722c69"
print(f"\nWith base64 values: CCSU{{{b64_hex + concatenated}}}")