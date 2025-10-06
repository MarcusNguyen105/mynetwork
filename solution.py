# list1, represents the first list of size N,
# list2, represents the second list of size M.


def funcSum(list1, list2):
    # Write your code here
    # Convert list1 to number (digits are in reverse order)
    num1 = 0
    for i in range(len(list1) - 1, -1, -1):
        num1 = num1 * 10 + list1[i]
    
    # Convert list2 to number (digits are in reverse order)
    num2 = 0
    for i in range(len(list2) - 1, -1, -1):
        num2 = num2 * 10 + list2[i]
    
    # Add the two numbers
    result_num = num1 + num2
    
    # Convert the sum back to a list in reverse order
    if result_num == 0:
        return [0]
    
    result = []
    while result_num > 0:
        result.append(result_num % 10)
        result_num //= 10
    
    return result

      
def main():
    #Input for list1
    list1 = []
    list1_size = int(input())
    list1 = list(map(int,input().split()))

    #Input for list2
    list2 = []
    list2_size = int(input())
    list2 = list(map(int,input().split()))


    result = funcSum(list1, list2)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
