# Time:  O(n^2)
# Space: O(n)
#
# Given a string S and a string T, count the number of distinct subsequences of T in S.
#
# A subsequence of a string is a new string which is formed from the original string
# by deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Here is an example:
# S = "rabbbit", T = "rabbit"
#
# Return 3.
#

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        ways = [0 for _ in xrange(len(S) + 1)]
        ways[0], prev = 1, 0
        for i in xrange(1, len(T) + 1):
            for j in xrange(1, len(S) + 1):
                ways[j] += ways[j - 1]
                if T[i - 1] == S[j - 1]:
                    ways[j] += prev
                prev = ways[j - 1]

        return ways[-1]

    def numDistinct2(self, S, T):
        dp = [[0 for i in xrange(len(S) + 1)] for j in xrange(len(T) + 1)]

        for i in xrange(len(S) + 1):
            dp[0][i] = 1
        for i in xrange(1, len(T) + 1):  # bugfixed, should start from 1
            dp[i][0] = 0

        for i in xrange(1, len(T) + 1):
            for j in xrange(1, len(S) + 1):
                dp[i][j] = dp[i][j - 1]
                if S[j - 1] == T[i - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[-1][-1]

    def numDistinct3(self, S, T):
        dp = [[0 for i in xrange(len(T) + 1)] for j in xrange(len(S) + 1)]

        for i in xrange(len(S) + 1):
            dp[i][0] = 1
        for i in xrange(1, len(T) + 1):  # bugfixed, should start from 1
            dp[0][i] = 0

        for i in xrange(1, len(S) + 1):
            for j in xrange(1, len(T) + 1):
                dp[i][j] = dp[i - 1][j]  # bugfixed should be [i][j] = [i-1][j] instad of [i][j] == [i][j-1]
                if S[i - 1] == T[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[-1][-1]
