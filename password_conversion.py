'''currPassword, represents the current password.
newPassword, represents the new password.
'''

def funcUpdation(currPassword, newPassword):
    # Write your code here
    
    # This problem is about finding minimum insertions and deletions
    # We can solve this using the Longest Common Subsequence (LCS) approach
    # Minimum operations = (len(curr) - LCS) + (len(new) - LCS)
    
    m, n = len(currPassword), len(newPassword)
    
    # Create DP table for LCS
    # dp[i][j] represents length of LCS of currPassword[0:i] and newPassword[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if currPassword[i-1] == newPassword[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Length of LCS
    lcs_length = dp[m][n]
    
    # Minimum operations = deletions + insertions
    # Deletions = characters in currPassword not in LCS
    # Insertions = characters in newPassword not in LCS
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