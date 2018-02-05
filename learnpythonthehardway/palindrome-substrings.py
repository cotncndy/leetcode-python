# Given a string, your task is to count how many palindromic substrings in this string.
#
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of
#  same characters.
#
# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, res = len(s), 0
        dp = [[False] * (l) for _ in xrange(l)]

        for k in xrange(0, l):
            for i in xrange(0, l):
                if i + k == l:
                    break
                if k == 0 or (k == 1 and s[i] == s[i + k]) or \
                        (k > 1 and dp[i + 1][i + k - 1] and s[i] == s[i + k]):
                    dp[i][i + k], res = True, res + 1

        return res


if __name__ == '__main__':
    # print Solution().countSubstrings("abc")
    print Solution().countSubstrings("aaa")
