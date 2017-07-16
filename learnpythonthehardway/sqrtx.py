# Time:  O(logn)
# Space: O(1)

# Implement int sqrt(int x).
#
# Compute and return the square root of x.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        # bugfixed left should = 1 instead of 0
        left, right = 1, x // 2  # knowledge '//' floor division, 9.0//2 = 4.0
        while left <= right:
            mid = left + (right - left) // 2
            if mid > x / mid:  # notice, can not use mid * mid > x, overflow
                right = mid - 1
            else:
                left = mid + 1
        return left - 1


if __name__ == '__main__':
    print Solution().mySqrt(2)
