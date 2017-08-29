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
    def numDistinct(self, S, T):  # review, I figured out by myself convert 2-d to 1-d dp
        ways = [0 for _ in xrange(len(S) + 1)]
        # prev, cur = 0, 0
        for i in xrange(len(S) + 1):
            ways[i] = 1

        for i in xrange(1, len(T) + 1):
            prev, ways[0] = ways[0], 0
            for j in xrange(1, len(S) + 1):
                cur = ways[j]
                ways[j] = ways[j - 1]
                if T[i - 1] == S[j - 1]:
                    ways[j] += prev
                prev = cur

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

    def numDistinct4(self, S, T):  # todo figure out how this 1-d dp works?
        ways = [0 for _ in xrange(len(T) + 1)]
        ways[0] = 1
        for S_char in S:
            for j, T_char in reversed(list(enumerate(T))):
                if S_char == T_char:
                    ways[j + 1] += ways[j]
        return ways[len(T)]

    def numDistinct5(self, S, T):  # todo figure out how this 1-d dp works?
        ways = [1 for _ in xrange(len(S) + 1)]
        for T_char in T:
            ways[0] = 0
            for j, S_char in reversed(list(enumerate(S))):
                if S_char == T_char:
                    ways[j + 1] += ways[j]
        return ways[len(S)]

if __name__ == '__main__':
    print Solution().numDistinct5("rabbbit", "rabbit")
