def funcUpdation(currPassword, newPassword):
    # Write your code here
    def lcs_length(s1, s2):
        m, n = len(s1), len(s2)
        # Create a DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

    # Calculate LCS length
    lcs_len = lcs_length(currPassword, newPassword)

    # Minimum operations = deletions + insertions
    deletions = len(currPassword) - lcs_len
    insertions = len(newPassword) - lcs_len

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