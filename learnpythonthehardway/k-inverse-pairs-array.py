# Given two integers n and k, find how many different arrays consist of numbers from 1 to n such that there are
# exactly k inverse pairs.
#
# We define an inverse pair as following: For ith and jth element in the array, if i < j and a[i] > a[j] then it's an
#  inverse pair; Otherwise, it's not.
#
# Since the answer may be very large, the answer should be modulo 109 + 7.
#
# Example 1:
# Input: n = 3, k = 0
# Output: 1
# Explanation:
# Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.
# Example 2:
# Input: n = 3, k = 1
# Output: 2
# Explanation:
# The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
# Note:
# The integer n is in the range [1, 1000] and k is in the range [0, 1000].

class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # a(n,k) = a(n-1,k) + a(n-1,k-1) + .. + a(n-1,k-n + 1) , if k >= n-1 or 0 , ie max(k-n+1,0)

        dp = [[0] * (k + 1) for _ in xrange(n + 1)]
        dp[0][0] = 1

        for i in xrange(n + 1):
            for j in xrange(k + 1):
                if i - 1 >= 0:
                    for l in xrange(max(j - i + 1, 0), j + 1):
                        dp[i][j] = (dp[i][j] + dp[i - 1][l]) % 1000000007

        return dp[n][k]

    def kInversePairs2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # a(n,k) = a(n-1,k) + a(n-1,k-1) + .. + a(n-1,k-n + 1) , if k >= n-1 or 0 , ie max(k-n+1,0)
        # replace k with k+1 , we got
        # a(n,k+1) = a(n-1,k+1) + a(n-1,k) + .. + a(n-1,k+1-(n - 1))
        # a(n,k+1) - a(n,k) = a(n-1,k+1)  - a(n-1,k-n+1)
        # replace k+1  with k back, we got
        # a(n,k) - a(n,k-1) = a(n-1,k) - a(n-1, k+1-n) => a(n,k) = a(n,k-1) + a(n-1,k) - a(n-1,k-n)

        dp = [[0] * (k + 1) for _ in xrange(n + 1)]
        dp[0][0] = 1

        for i in xrange(1, n + 1):
            dp[i][0] = 1
            for j in xrange(1, k + 1):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000007
                if j - i >= 0:
                    dp[i][j] = (dp[i][j] - dp[i - 1][j - i]) % 1000000007

        return dp[n][k]

    # copied from the best solution
    def kInversePairs3(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        if n * (n - 1) / 2 < k:
            return 0
        if k == 0:
            return 1

        mod = 10 ** 9 + 7

        dp = [0 for _ in range(k + 1)]
        dp_next = [0 for _ in range(k + 1)]
        dp[0] = 1
        dp[1] = 1
        for nn in range(2, n):
            s = 0
            for kk in range(0, k + 1):
                s += dp[kk]
                if kk - nn - 1 >= 0:
                    s -= dp[kk - nn - 1]
                s %= mod
                dp_next[kk] = s
            temp = dp
            dp = dp_next
            dp_next = temp

        return dp[k]


if __name__ == '__main__':
    print Solution().kInversePairs(3, 0)
    print Solution().kInversePairs(3, 1)
    print Solution().kInversePairs2(1000, 1000)
    print Solution().kInversePairs(1000, 1000)
