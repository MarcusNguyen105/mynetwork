'''currPassword, represents the current password.
newPassword, represents the new password.
'''

def funcUpdation(currPassword, newPassword):
    # Write your code here
    m, n = len(currPassword), len(newPassword)
    
    # Create a 2D table to store LCS lengths
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if currPassword[i-1] == newPassword[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # LCS length
    lcs_length = dp[m][n]
    
    # Minimum operations = deletions + insertions
    # deletions = len(currPassword) - lcs_length
    # insertions = len(newPassword) - lcs_length
    deletions = m - lcs_length
    insertions = n - lcs_length
    
    return deletions + insertions

def main():
    #Input for currPassword
    currPassword = str(input())

    #Input for newPassword
    newPassword = str(input())


    result = funcUpdation(currPassword, newPassword)
    print(result)

if __name__ == "__main__":
    main()