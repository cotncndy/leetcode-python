# Given an array of integers A and let n to be its length.
#
# Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F
#  on A as follow:
#
# F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
#
# Calculate the maximum value of F(0), F(1), ..., F(n-1).
#
# Note:
# n is guaranteed to be less than 105.
#
# Example:
#
# A = [4, 3, 2, 6]
#
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
#
# So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.

class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        def rightRote(A, k):
            l = len(A)
            c = A[::]
            c[0:k], c[k:] = c[l - k:], c[0:l - k]
            return c

        res = float('-inf')  # bugfixed
        for k in xrange(len(A)):
            fk, c = 0, rightRote(A, k)
            for i in xrange(len(c)):
                fk += i * c[i]
            res = max(res, fk)

        res = 0 if res == float('-inf') else res
        return res

    def maxRotateFunction2(self, A):
        dp = [0] * len(A)
        sumA = sum(A)
        for i in xrange(1, len(A)):
            dp[0] += i * A[i]
        for k in xrange(1, len(A)):
            dp[k] = dp[k - 1] - len(A) * A[len(A) - k] + sumA

        return max(dp)

if __name__ == '__main__':
    print Solution().maxRotateFunction2([4, 3, 2, 6])
    print Solution().maxRotateFunction2([-2147483648, -2147483648])
    print Solution().maxRotateFunction2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print Solution().maxRotateFunction2([])
