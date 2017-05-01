def lcs(x,y):
    m = len(x)
    n = len(y)

    #declare the array for dp
    dp = [[None] * (n+1) for i in xrange(m+1)]

    for i in xrange(m+1):
        for j in xrange(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print "Length of LCS is ", lcs(X, Y)
