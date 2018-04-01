# Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same,
# where in each step you can delete one character in either string.
#
# Example 1:
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# Note:
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l, m = len(word1), len(word2)
        dp = [[0] * (l + 1) for _ in xrange(m + 1)]

        for i in xrange(1, m + 1):
            for j in xrange(1, l + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return l + m - dp[m][l] * 2


if __name__ == '__main__':
    print Solution().minDistance("sea", "eat")
