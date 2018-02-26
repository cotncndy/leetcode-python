#  Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length
# of s is 1000.
#
# Example 1:
# Input:
#
# "bbbab"
#
# Output:
#
# 4
#
# One possible longest palindromic subsequence is "bbbb".
#
# Example 2:
# Input:
#
# "cbbd"
#
# Output:
#
# 2
#
# One possible longest palindromic subsequence is "bb".

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        dp = [[0] * l for _ in xrange(l)]

        for k in xrange(0, l):
            for i in xrange(0, l):
                if i + k == l:
                    break
                if k == 0:
                    dp[i][i + k] = 1
                else:
                    if s[i] == s[i + k]:
                        dp[i][i + k] = dp[i + 1][i + k - 1] + 2
                    else:
                        dp[i][i + k] = max(dp[i][i + k - 1], dp[i + 1][i + k])

        return dp[0][-1]

    def longestPalindromeSubseq2(self, s):
        l = len(s)
        dp = [[0] * l for _ in xrange(l)]
        for i in xrange(l - 1, -1, -1):
            dp[i][i] = 1
            for j in xrange(i + 1, l):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        return dp[0][-1]

if __name__ == '__main__':
    print Solution().longestPalindromeSubseq2("bbbab")
    print Solution().longestPalindromeSubseq2("cbbd")
    print Solution().longestPalindromeSubseq("cbbd")
