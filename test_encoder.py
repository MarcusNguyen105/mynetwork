def funcEncode(inputStr):
	"""Encodes a string based on the given rules."""
	outputStr=""
	for char in inputStr:
		if char.isalpha():
			outputStr += char
		elif char == '3':
			outputStr = outputStr[::-1]
		elif char.isdigit():
			outputStr += outputStr

	return outputStr

# Test cases
test_cases = [
	"abc",
	"a1b",
	"a3b",
	"ab3c",
	"a12",
	"123",
	"a1b2c",
	"a3b3c",
	"1a2b3c",
	"a1b3c2d"
]

print("Current implementation results:")
for test in test_cases:
	result = funcEncode(test)
	print(f"'{test}' -> '{result}'")