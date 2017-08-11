# Time:  O(m + n)
# Space: O(1)
#
# Implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
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
# isMatch("aa", "*") -> true
# isMatch("aa", "a*") -> true
# isMatch("ab", "?*") -> true
# isMatch("aab", "c*a*b") -> false
#

# iteration
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        scur, pcur, sstar, pstar = 0, 0, -1, -1
        while scur < len(s):
            if pcur < len(p) and (s[scur] == p[pcur] or p[pcur] == '?'):  # bugfixed
                scur, pcur = scur + 1, pcur + 1
            elif pcur < len(p) and p[pcur] == '*':
                pstar, pcur, sstar = pcur, pcur + 1, scur
            elif pstar > -1:
                pcur, sstar = pstar, sstar + 1  # bugfixed
                scur = sstar
            else:
                return False

        while pcur < len(p) and p[pcur] == '*':
            pcur += 1

        return pcur == len(p)

    # time : O(m * n)
    # space : O(m * n)
    def isMatch2(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in xrange(len(s) + 1)]
        dp[0][0] = True
        for i in xrange(1, len(p) + 1):  # bugfixed
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]

        for i in xrange(1, len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if p[j - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')
                else:
                    # when p[j-1] == '*', if '*' means empty string, dp[i][j] = dp[i][j-1]
                    # else '*' could represent any char, so dp[i-1][j], ie, if dp[i-1][j] is true, then no matter
                    # for what char in s[i-1], '*' could match it
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[len(s)][len(p)]

    # time : O(m * n)
    # space : O(m * n)
    def isMatch3(self, s, p):
        k = 2
        dp = [[False] * (len(p) + 1) for _ in xrange(k)]
        dp[0][0] = True
        for i in xrange(1, len(p) + 1):  # bugfixed
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]

        for i in xrange(1, len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if p[j - 1] != '*':
                    dp[i % k][j] = dp[(i - 1) % k][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')
                else:
                    # when p[j-1] == '*', if '*' means empty string, dp[i][j] = dp[i][j-1]
                    # else '*' could represent any char, so dp[i-1][j], ie, if dp[i-1][j] is true, then no matter
                    # for what char in s[i-1], '*' could match it
                    dp[i % k][j] = dp[i % k][j - 1] or dp[(i - 1) % k][j]

        return dp[len(s)][len(p)]




if __name__ == '__main__':
    print Solution().isMatch2('', '')
