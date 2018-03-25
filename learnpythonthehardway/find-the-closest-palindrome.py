# Given an integer n, find the closest integer (not including itself), which is a palindrome.
#
# The 'closest' is defined as absolute difference minimized between two integers.
#
# Example 1:
# Input: "123"
# Output: "121"
# Note:
# The input n is a positive integer represented by string, whose length will not exceed 18.
# If there is a tie, return the smaller one as answer.


class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        l, s = len(n), set()
        s.add(10 ** l + 1)
        s.add(10 ** (l - 1) - 1)

        prefix = int(n[0:(l + 1) / 2])
        for i in xrange(-1, 2):
            pre = str(prefix + i)
            if l & 1:
                can = pre + pre[:-1]
            else:
                can = pre + pre[::-1]
            s.add(int(can))

        res, minDiff = -1, float('inf')
        for i in s:
            if abs(i - int(n)) < minDiff:
                res = str(i)
                minDiff = abs(i - int(n))
            elif abs(i - int(n)) == minDiff and i < res:
                res = str(i)

        return res


if __name__ == '__main__':
    # print Solution().nearestPalindromic("121")
    print Solution().nearestPalindromic("123")
    print Solution().nearestPalindromic("1234")
