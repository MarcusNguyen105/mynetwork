def funcSum(list1, list2):
    # Write your code here
    result = []
    carry = 0
    i, j = 0, 0

    while i < len(list1) or j < len(list2) or carry:
        digit1 = list1[i] if i < len(list1) else 0
        digit2 = list2[j] if j < len(list2) else 0

        total = digit1 + digit2 + carry
        digit = total % 10
        carry = total // 10

        result.append(digit)
        i += 1
        j += 1

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