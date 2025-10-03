#!/usr/bin/env python3
import socket
import re
import time

def solve_math_expression(expression):
    """Solve simple math expressions from the CAPTCHA"""
    # Convert word numbers to digits
    word_to_num = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
        'ten': '10', 'eleven': '11', 'twelve': '12', 'thirteen': '13',
        'fourteen': '14', 'fifteen': '15', 'sixteen': '16', 'seventeen': '17',
        'eighteen': '18', 'nineteen': '19', 'twenty': '20', 'twenty-one': '21',
        'twenty-two': '22', 'twenty-three': '23', 'twenty-four': '24', 'twenty-five': '25',
        'twenty-six': '26', 'twenty-seven': '27', 'twenty-eight': '28', 'twenty-nine': '29',
        'thirty': '30', 'thirty-one': '31', 'thirty-two': '32', 'thirty-three': '33',
        'thirty-four': '34', 'thirty-five': '35', 'thirty-six': '36', 'thirty-seven': '37',
        'thirty-eight': '38', 'thirty-nine': '39', 'forty': '40', 'forty-one': '41',
        'forty-two': '42', 'forty-three': '43', 'forty-four': '44', 'forty-five': '45',
        'forty-six': '46', 'forty-seven': '47', 'forty-eight': '48', 'forty-nine': '49',
        'fifty': '50', 'fifty-one': '51', 'fifty-two': '52', 'fifty-three': '53',
        'fifty-four': '54', 'fifty-five': '55', 'fifty-six': '56', 'fifty-seven': '57',
        'fifty-eight': '58', 'fifty-nine': '59', 'sixty': '60', 'sixty-one': '61',
        'sixty-two': '62', 'sixty-three': '63', 'sixty-four': '64', 'sixty-five': '65',
        'sixty-six': '66', 'sixty-seven': '67', 'sixty-eight': '68', 'sixty-nine': '69',
        'seventy': '70', 'seventy-one': '71', 'seventy-two': '72', 'seventy-three': '73',
        'seventy-four': '74', 'seventy-five': '75', 'seventy-six': '76', 'seventy-seven': '77',
        'seventy-eight': '78', 'seventy-nine': '79', 'eighty': '80', 'eighty-one': '81',
        'eighty-two': '82', 'eighty-three': '83', 'eighty-four': '84', 'eighty-five': '85',
        'eighty-six': '86', 'eighty-seven': '87', 'eighty-eight': '88', 'eighty-nine': '89',
        'ninety': '90', 'ninety-one': '91', 'ninety-two': '92', 'ninety-three': '93',
        'ninety-four': '94', 'ninety-five': '95', 'ninety-six': '96', 'ninety-seven': '97',
        'ninety-eight': '98', 'ninety-nine': '99', 'hundred': '100', 'one hundred': '100'
    }
    
    # Convert to lowercase for matching
    expr_lower = expression.lower()
    
    # Replace word numbers with digits (longest first to avoid partial matches)
    for word, num in sorted(word_to_num.items(), key=lambda x: len(x[0]), reverse=True):
        expr_lower = expr_lower.replace(word, num)
    
    # Handle basic math operations
    if 'times' in expr_lower or '*' in expr_lower:
        # Extract numbers and multiply
        numbers = re.findall(r'\d+', expr_lower)
        if len(numbers) >= 2:
            return str(int(numbers[0]) * int(numbers[1]))
    
    elif 'plus' in expr_lower or '+' in expr_lower:
        # Extract numbers and add
        numbers = re.findall(r'\d+', expr_lower)
        if len(numbers) >= 2:
            return str(int(numbers[0]) + int(numbers[1]))
    
    elif 'minus' in expr_lower or '-' in expr_lower:
        # Extract numbers and subtract
        numbers = re.findall(r'\d+', expr_lower)
        if len(numbers) >= 2:
            return str(int(numbers[0]) - int(numbers[1]))
    
    elif 'divided by' in expr_lower or '/' in expr_lower:
        # Extract numbers and divide
        numbers = re.findall(r'\d+', expr_lower)
        if len(numbers) >= 2:
            return str(int(numbers[0]) // int(numbers[1]))
    
    # If we can't parse it, try to evaluate it directly
    try:
        # Extract just numbers and basic operators
        clean_expr = re.sub(r'[^\d+\-*/\s]', '', expr_lower)
        if clean_expr.strip():
            return str(eval(clean_expr))
    except:
        pass
    
    return None

def connect_and_solve():
    """Connect to the CAPTCHA server and solve challenges"""
    host = 'chals.uscc-cyberbowl-2025.ctf.institute'
    port = 3010
    
    try:
        # Create socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(30)
        sock.connect((host, port))
        
        print("Connected to CAPTCHA server!")
        
        # Receive initial data
        data = ""
        while True:
            try:
                chunk = sock.recv(1024).decode('utf-8', errors='ignore')
                if not chunk:
                    break
                data += chunk
                print(chunk, end='')
                
                # Look for questions in the received data
                if '?' in data and 'Your answer' in data:
                    # Extract the question - look for lines with ❓ emoji or math operations
                    lines = data.split('\n')
                    question_line = None
                    
                    for line in lines:
                        # Look for lines that start with ❓ or contain math operations
                        if ('❓' in line and '?' in line) or (
                            '?' in line and any(word in line.lower() for word in ['times', 'plus', 'minus', 'divided by']) and
                            any(num in line.lower() for num in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'])
                        ):
                            question_line = line.strip()
                            break
                    
                    if question_line:
                        print(f"\nFound question: {question_line}")
                        
                        # Solve the math problem
                        answer = solve_math_expression(question_line)
                        
                        if answer:
                            print(f"Calculated answer: {answer}")
                            
                            # Send the answer
                            sock.send(f"{answer}\n".encode())
                            
                            # Reset data buffer for next question
                            data = ""
                        else:
                            print("Could not solve the question!")
                            break
                
                # Check if we got the flag
                if 'uscc{' in data.lower() or 'flag{' in data.lower() or 'ctf{' in data.lower():
                    print("\n🎉 Found flag in response!")
                    break
                    
            except socket.timeout:
                print("Timeout waiting for more data")
                break
            except Exception as e:
                print(f"Error receiving data: {e}")
                break
        
        sock.close()
        
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    connect_and_solve()