# -*- coding: utf-8 -*-
# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k
# coins.
#
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt, start, sum = 0, 1, 0
        while sum < n:
            if sum + start > n:
                break;
            sum, start, cnt = sum + start, start + 1, cnt + 1

        return cnt


if __name__ == '__main__':
    print Solution().arrangeCoins(8)
    print Solution().arrangeCoins(5)
    print Solution().arrangeCoins(10)
