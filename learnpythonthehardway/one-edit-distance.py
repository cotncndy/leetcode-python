# Time:  O(m + n)
# Space: O(1)
#
# Given two strings S and T, determine if they are both one edit distance apart.
#

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        if abs(m - n) == 1:
            return True
        elif abs(m - n) > 1:
            return False
        else:
            i = 0
            for k in xrange(len(s)):
                if s[k] != t[k]:
                    i += 1
            return i == 1


if __name__ == "__main__":
    print Solution().isOneEditDistance("teacher", "acher")
