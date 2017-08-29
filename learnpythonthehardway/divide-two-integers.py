# Time:  O(logn) = O(1)
# Space: O(1)
#
# Divide two integers without using multiplication, division and mod operator.


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = (dividend < 0) is (divisor < 0)  # review so concise
        res, dividend, divisor = 0, abs(dividend), abs(divisor)

        while dividend >= divisor:
            t, m = divisor, 1
            while dividend >= (t << 1):
                t <<= 1
                m <<= 1
            dividend -= t
            res += m
        if not sign:
            res = -res

        return min(max(-2147483648, res), 2147483647)


if __name__ == '__main__':
    print Solution().divide(3, 0)
