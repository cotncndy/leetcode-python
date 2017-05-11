# Time:  O(n)
# Space: O(n)
#
# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000,
#  and there exists one unique longest palindromic substring.
#

# Manacher's Algorithm
# http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(i,j):
            while i > -1 and j < len(s):
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
            return s[i+1:j]
        res, str = 0, None
        for k in xrange(len(s)):
            sr = expand(k,k)
            if(res < len(sr)):
                res = len(sr)
                str = sr
            if k > 0:
                sr = expand(k-1,k)
                if(res < len(sr)):
                    res = len(sr)
                    str = sr

        return str

if __name__ == "__main__":
    s = "babad"
    print Solution().longestPalindrome(s)
