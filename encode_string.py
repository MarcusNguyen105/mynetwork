"""
inputStr, represents the given string (S).
"""
def funcEncode(inputStr):
	# Write your code here
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

def main():
	#input for inputStr
	inputStr = str(input())
	
	
	result = funcEncode(inputStr)
	print(result)	

if __name__ == "__main__":
	main()
