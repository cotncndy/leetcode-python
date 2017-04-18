# Time:  O(1)
# Space: O(1)
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647,
# return the bitwise AND of all numbers in this range, inclusive.
#
# For example, given the range [5, 7], you should return 4.
#

class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return m << i

    def rangeBitwiseAnd2(self, m,n):
        while m < n:
            n &= (n-1)

        return n

if __name__ == '__main__':
    print Solution().rangeBitwiseAnd(5, 7)
    print Solution().rangeBitwiseAnd2(5, 7)
