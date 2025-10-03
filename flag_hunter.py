#!/usr/bin/env python3
import socket
import re
import time

def solve_math_expression(expression):
    """Solve simple math expressions from the CAPTCHA"""
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
    
    expr_lower = expression.lower().strip()
    expr_lower = re.sub(r'[❓?]', '', expr_lower).strip()
    
    numbers = []
    operation = None
    
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
    
    for part in parts:
        part = part.strip()
        found_num = None
        for word, num in sorted(word_to_num.items(), key=lambda x: len(x[0]), reverse=True):
            if word in part:
                found_num = num
                break
        
        if found_num is not None:
            numbers.append(found_num)
        else:
            digit_match = re.search(r'\d+', part)
            if digit_match:
                numbers.append(int(digit_match.group()))
    
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

def hunt_for_flag():
    """Connect and hunt for the flag"""
    host = 'chals.uscc-cyberbowl-2025.ctf.institute'
    port = 3010
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((host, port))
        
        print("🎯 Hunting for the flag...")
        
        buffer = ""
        last_percentage = 0
        
        while True:
            try:
                data = sock.recv(2048).decode('utf-8', errors='ignore')
                if not data:
                    break
                
                buffer += data
                
                # Check current percentage
                percentage_match = re.search(r'(\d+\.\d+)%', buffer)
                if percentage_match:
                    current_percentage = float(percentage_match.group(1))
                    if current_percentage > last_percentage:
                        print(f"Progress: {current_percentage}%")
                        last_percentage = current_percentage
                
                # Look for questions and solve them quickly
                lines = buffer.split('\n')
                for line in lines:
                    if '❓' in line and '?' in line:
                        answer = solve_math_expression(line)
                        if answer:
                            try:
                                sock.send(f"{answer}\n".encode())
                            except:
                                pass
                
                # Check for flags with multiple patterns
                flag_patterns = [
                    r'uscc\{[^}]+\}',
                    r'flag\{[^}]+\}', 
                    r'ctf\{[^}]+\}',
                    r'USCC\{[^}]+\}',
                    r'FLAG\{[^}]+\}',
                    r'CTF\{[^}]+\}'
                ]
                
                for pattern in flag_patterns:
                    matches = re.findall(pattern, buffer, re.IGNORECASE)
                    if matches:
                        for flag in matches:
                            print(f"\n🎉 FOUND FLAG: {flag}")
                            return flag
                
                # Look for 100% and wait for flag
                if "100.0%" in buffer:
                    print("\n🎉 Reached 100%! Waiting for flag...")
                    time.sleep(5)  # Wait longer for flag
                    continue
                
                # Look for success messages
                success_indicators = [
                    "congratulations",
                    "well done", 
                    "success",
                    "you did it",
                    "human verified"
                ]
                
                buffer_lower = buffer.lower()
                for indicator in success_indicators:
                    if indicator in buffer_lower:
                        print(f"\n✅ Success indicator found: {indicator}")
                        time.sleep(3)
                        continue
                
            except socket.timeout:
                continue
            except Exception as e:
                print(f"Error: {e}")
                break
        
        sock.close()
        return None
        
    except Exception as e:
        print(f"Connection error: {e}")
        return None

if __name__ == "__main__":
    for attempt in range(3):
        print(f"\n🚀 Attempt {attempt + 1}/3")
        flag = hunt_for_flag()
        if flag:
            print(f"\n🎯 FINAL FLAG: {flag}")
            break
        else:
            print("No flag found, trying again...")
            time.sleep(2)
    else:
        print("Failed to find flag after 3 attempts")