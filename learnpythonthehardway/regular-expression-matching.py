# Time:  O(m * n)
# Space: O(n)
#
# Implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "a*") -> true
# isMatch("aa", ".*") -> true
# isMatch("ab", ".*") -> true
# isMatch("aab", "c*a*b") -> true
#

# dp with rolling window
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        res = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]
        res[0][0] = True

        for i in xrange(2, len(p) + 1):
            if p[i - 1] == '*':
                res[0][i] = res[0][i - 2]

        for i in xrange(1, len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if p[j - 1] != '*':
                    res[i][j] = res[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                else:
                    res[i][j] = res[i][j - 2] or (
                    res[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))  # bugfixed and should be 'or'

        return res[len(s)][len(p)]


if __name__ == '__main__':
    print Solution().isMatch("aa", 'a*')
