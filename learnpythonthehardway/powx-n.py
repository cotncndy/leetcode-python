# Time:  O(logn) = O(1)
# Space: O(1)

# Implement pow(x, n).

# Iterative solution.
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res, abs_n = 1, abs(n)
        while abs_n:
            if abs_n & 1:
                res *= x
            abs_n >>= 1
            x *= x

        return 1 / res if n < 0 else res
