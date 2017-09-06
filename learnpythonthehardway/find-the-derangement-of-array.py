# In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears
# in its original position.
#
# There's originally an array consisting of n integers from 1 to n in ascending order, you need to find the number of
#  derangement it can generate.
#
# Also, since the answer may be very large, you should return the output mod 109 + 7.
#
# Example 1:
# Input: 3
# Output: 2
# Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].
# Note:
# n is in the range of [1, 106].

import math


class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        dp, combine = [0] * (n + 1), [1] * (n + 1)
        dp[0], dp[1] = 1, 0

        for i in xrange(2, n + 1):
            res, combine[i] = 0, combine[i - 1] * i  # % (10**9+7)
            for j in xrange(1, i + 1):
                # res += (self.combination(i, j) * dp[i - j])%(10**9+7)
                res += (combine[i] // combine[j] // combine[i - j]) * dp[i - j]  # %(10**9+7)
            dp[i] = combine[i] - res

        return dp[n] % (10 ** 9 + 7)

    def findDerangement2(self, n):
        if n < 2: return 0
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 0, 1
        for i in xrange(3, n + 1):
            dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % (10 ** 9 + 7)

        return dp[n]


    def combination(self, n, r):
        f = self.factorial
        return (f(n) // f(r) // f(n - r))  # %(10**9+7)

    def factorial(self, n):
        f = math.factorial
        return f(n)  #% (10 ** 9 + 7)


if __name__ == '__main__':
    print Solution().findDerangement(13)
    print Solution().findDerangement(14)
    print Solution().findDerangement(15)
    print Solution().findDerangement(16)
    print Solution().findDerangement(667)
