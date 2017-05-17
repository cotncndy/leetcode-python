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
        for i in xrange(min(m, n)):
            if (s[i] != t[i]):
                if m > n:
                    return s[i + 1::] == t[i::]
                elif n > m:
                    return s[i::] == t[i + 1::]
                else:
                    return s[i + 1::] == t[i + 1::]

        return abs(m - n) == 1




if __name__ == "__main__":
    print Solution().isOneEditDistance("teacher", "acher")
    print Solution().isOneEditDistance("teacher", "tacher")
    print Solution().isOneEditDistance("teacher", "tEacher")
    print Solution().isOneEditDistance("teacher", "teacher")
    print Solution().isOneEditDistance("teacher", "teache")
