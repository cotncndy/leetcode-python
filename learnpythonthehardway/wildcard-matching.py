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


if __name__ == '__main__':
    print Solution().isMatch('aa', '*')
