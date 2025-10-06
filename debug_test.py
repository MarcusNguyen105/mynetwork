def funcEncode(inputStr):
	"""Encodes a string based on the given rules."""
	outputStr=""
	for char in inputStr:
		print(f"Processing '{char}', outputStr before: '{outputStr}'")
		if char.isalpha():
			outputStr += char
			print(f"  After alpha: '{outputStr}'")
		elif char.isdigit():
			outputStr += outputStr
			print(f"  After digit dup: '{outputStr}'")
		elif char == '3':
			if outputStr:
				old_output = outputStr
				outputStr = outputStr[::-1]
				print(f"  After reversal: '{old_output}' -> '{outputStr}'")
		print(f"outputStr after: '{outputStr}'")
		print("---")

	return outputStr

# Test specific case
result = funcEncode("1a2b3c")
print(f"Final result: '{result}'")