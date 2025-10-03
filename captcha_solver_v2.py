#!/usr/bin/env python3
import socket
import re
import time

def solve_math_expression(expression):
    """Solve simple math expressions from the CAPTCHA"""
    # Convert word numbers to digits - comprehensive mapping
    word_to_num = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
        'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
        'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
        'twenty-one': 21, 'twenty-two': 22, 'twenty-three': 23, 'twenty-four': 24,
        'twenty-five': 25, 'twenty-six': 26, 'twenty-seven': 27, 'twenty-eight': 28,
        'twenty-nine': 29, 'thirty': 30, 'thirty-one': 31, 'thirty-two': 32,
        'thirty-three': 33, 'thirty-four': 34, 'thirty-five': 35, 'thirty-six': 36,
        'thirty-seven': 37, 'thirty-eight': 38, 'thirty-nine': 39, 'forty': 40,
        'forty-one': 41, 'forty-two': 42, 'forty-three': 43, 'forty-four': 44,
        'forty-five': 45, 'forty-six': 46, 'forty-seven': 47, 'forty-eight': 48,
        'forty-nine': 49, 'fifty': 50, 'fifty-one': 51, 'fifty-two': 52,
        'fifty-three': 53, 'fifty-four': 54, 'fifty-five': 55, 'fifty-six': 56,
        'fifty-seven': 57, 'fifty-eight': 58, 'fifty-nine': 59, 'sixty': 60,
        'sixty-one': 61, 'sixty-two': 62, 'sixty-three': 63, 'sixty-four': 64,
        'sixty-five': 65, 'sixty-six': 66, 'sixty-seven': 67, 'sixty-eight': 68,
        'sixty-nine': 69, 'seventy': 70, 'seventy-one': 71, 'seventy-two': 72,
        'seventy-three': 73, 'seventy-four': 74, 'seventy-five': 75, 'seventy-six': 76,
        'seventy-seven': 77, 'seventy-eight': 78, 'seventy-nine': 79, 'eighty': 80,
        'eighty-one': 81, 'eighty-two': 82, 'eighty-three': 83, 'eighty-four': 84,
        'eighty-five': 85, 'eighty-six': 86, 'eighty-seven': 87, 'eighty-eight': 88,
        'eighty-nine': 89, 'ninety': 90, 'ninety-one': 91, 'ninety-two': 92,
        'ninety-three': 93, 'ninety-four': 94, 'ninety-five': 95, 'ninety-six': 96,
        'ninety-seven': 97, 'ninety-eight': 98, 'ninety-nine': 99, 'hundred': 100,
        'one hundred': 100
    }
    
    # Clean and normalize the expression
    expr_lower = expression.lower().strip()
    
    # Remove question mark and emoji
    expr_lower = re.sub(r'[❓?]', '', expr_lower).strip()
    
    # Parse the expression to find numbers and operation
    numbers = []
    operation = None
    
    # Split by common operation words
    if ' times ' in expr_lower:
        parts = expr_lower.split(' times ')
        operation = '*'
    elif ' plus ' in expr_lower:
        parts = expr_lower.split(' plus ')
        operation = '+'
    elif ' minus ' in expr_lower:
        parts = expr_lower.split(' minus ')
        operation = '-'
    elif ' divided by ' in expr_lower:
        parts = expr_lower.split(' divided by ')
        operation = '/'
    else:
        return None
    
    # Extract numbers from each part
    for part in parts:
        part = part.strip()
        
        # Try to find word number first (longest match)
        found_num = None
        for word, num in sorted(word_to_num.items(), key=lambda x: len(x[0]), reverse=True):
            if word in part:
                found_num = num
                break
        
        if found_num is not None:
            numbers.append(found_num)
        else:
            # Try to extract digit
            digit_match = re.search(r'\d+', part)
            if digit_match:
                numbers.append(int(digit_match.group()))
    
    # Perform the calculation
    if len(numbers) >= 2 and operation:
        if operation == '+':
            return str(numbers[0] + numbers[1])
        elif operation == '-':
            return str(numbers[0] - numbers[1])
        elif operation == '*':
            return str(numbers[0] * numbers[1])
        elif operation == '/':
            return str(numbers[0] // numbers[1])
    
    return None

def connect_and_solve():
    """Connect to the CAPTCHA server and solve challenges"""
    host = 'chals.uscc-cyberbowl-2025.ctf.institute'
    port = 3010
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((host, port))
        
        print("Connected to CAPTCHA server!")
        
        buffer = ""
        
        while True:
            try:
                data = sock.recv(4096).decode('utf-8', errors='ignore')
                if not data:
                    break
                
                buffer += data
                print(data, end='', flush=True)
                
                # Look for questions
                lines = buffer.split('\n')
                for line in lines:
                    if '❓' in line and '?' in line:
                        question = line.strip()
                        print(f"\n[SOLVING] {question}")
                        
                        answer = solve_math_expression(question)
                        if answer:
                            print(f"[ANSWER] {answer}")
                            sock.send(f"{answer}\n".encode())
                            time.sleep(0.1)  # Small delay
                        else:
                            print("[ERROR] Could not solve question!")
                
                # Check for flag
                if any(flag in buffer.lower() for flag in ['uscc{', 'flag{', 'ctf{']):
                    print("\n🎉 FLAG FOUND!")
                    # Extract and print the flag
                    flag_match = re.search(r'(uscc\{[^}]+\}|flag\{[^}]+\}|ctf\{[^}]+\})', buffer, re.IGNORECASE)
                    if flag_match:
                        print(f"FLAG: {flag_match.group(1)}")
                    break
                
                # Check if we reached 100%
                if "100.0%" in buffer:
                    print("\n🎉 Reached 100% human likelihood!")
                    time.sleep(2)  # Wait for flag
                
            except socket.timeout:
                continue
            except Exception as e:
                print(f"Error: {e}")
                break
        
        sock.close()
        
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    connect_and_solve()