# list1, represents the first list of size N,
# list2, represents the second list of size M.


def funcSum(list1, list2):
    # Write your code here
    num1 = int("".join(map(str, list1[::-1]))) if list1 else 0
    num2 = int("".join(map(str, list2[::-1]))) if list2 else 0
    total = num1 + num2
    return [int(d) for d in str(total)[::-1]]

def main():
    #Input for list1
    list1 = []
    list1_size = int(input())
    list1 = list(map(int, input().split()))

    #Input for list2
    list2 = []
    list2_size = int(input())
    list2 = list(map(int, input().split()))


    result = funcSum(list1, list2)
    # Fixed: Print space-separated integers instead of the list representation
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()