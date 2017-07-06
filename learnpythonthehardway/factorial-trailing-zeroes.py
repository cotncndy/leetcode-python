# Time:  O(logn) = O(1)
# Space: O(1)
#
# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.
#

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        res = 0
        while n:
            res += n / 5
            n /= 5

        return res
