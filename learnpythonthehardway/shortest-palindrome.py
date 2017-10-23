# Shortest Palindrome
# Difficulty:Hard
#
# Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and
# return the shortest palindrome you can find by performing this transformation.
#
# For example:
#
# Given "aacecaaa", return "aaacecaaa".
#
# Given "abcd", return "dcbabcd".


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = self.longestPalindrome(s)
        return s[l + 1:][::-1] + s[:l + 1] + s[l + 1:]

    def longestPalindrome(self, s):
        dp, l = [[False] * (len(s) + 1) for _ in xrange(len(s) + 1)], 0
        for i in xrange(len(s)):
            dp[i][i] = True
        for j in xrange(1, len(s)):
            for i in xrange(len(s)):
                if i + j >= len(s):
                    continue
                if (j == 1 and s[i] == s[i + j]) or (s[i] == s[i + j] and dp[i + 1][i + j - 1]):
                    dp[i][i + j] = True
                    if i == 0 and j > l:
                        l = j

        return l

    def longestPalindrome2(self, s):
        i, end = 0, len(s) - 1
        j, res = end, ""

        while i < j:
            if s[i] == s[j]:
                i, j = i + 1, j - 1
            else:
                end -= 1
                i, j = 0, end

        return s[end + 1:][::-1] + s


if __name__ == '__main__':
    print Solution().shortestPalindrome("baaaad")
    print Solution().shortestPalindrome("aacecaaa")
