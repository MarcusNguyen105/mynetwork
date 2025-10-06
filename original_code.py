def funcEncode(inputStr):
	# Write your code here
	"""Encodes a string based on the given rules."""
	outputStr="" 
	for char in inputStr:
		if char.isalpha():
			outputStr += char
		elif char.isdigit():
			outputStr += outputStr
		elif char == '3':
			outputStr = outputStr[::-1]

	return outputStr