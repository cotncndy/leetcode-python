# Given a positive integer n, return the number of all possible attendance records with length n, which will be
# regarded as rewardable. The answer may be very large, return it after mod 109 + 7.
#
# A student attendance record is a string that only contains the following three characters:
#
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L'
# (late).
#
# Example 1:
# Input: n = 2
# Output: 8
# Explanation:
# There are 8 records with length 2 will be regarded as rewardable:
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" won't be regarded as rewardable owing to more than one absent times.
# Note: The value of n won't exceed 100,000.

class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        A, P, L = [0] * (n + 2), [0] * (n + 2), [0] * (n + 2)
        P[0], A[0], L[0], L[1], A[1], A[2] = 1, 1, 1, 3, 2, 4
        M = 1000000007

        # A[i] = A[i-1] + A[i-2] + A[i-3]
        # P[i] = P[i-1] + A[i-1] + L[i-1]
        # L[i] = p[i-1] + A[i-1] + p[i-2] + A[i-2]

        for i in xrange(1, n):
            P[i] = ((P[i - 1] + A[i - 1]) % M + L[i - 1]) % M
            if i > 1:
                L[i] = ((P[i - 1] + A[i - 1]) % M + (P[i - 2] + A[i - 2]) % M) % M
            if i > 2:
                A[i] = ((A[i - 1] + A[i - 2]) % M + A[i - 3]) % M

        return ((A[n - 1] + P[n - 1]) % M + L[n - 1]) % M

    def checkRecord2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 3
        if n == 0:
            return 0
        dp = [1] * (n + 1)
        dp[1], dp[2] = 2, 4  # dp[1] = {l,p}, dp[2]= {ll,pp, pl, lp}
        M = 10 ** 9 + 7

        for i in xrange(3, n + 1):
            # end with p, pl, pll.
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % M
        res = dp[n]

        for i in xrange(n):
            res += dp[i] * dp[n - 1 - i] % M
            res %= M
        return res

if __name__ == '__main__':
    print Solution().checkRecord2(1)
    print Solution().checkRecord2(2)
    print Solution().checkRecord(3)
    print Solution().checkRecord(4)
    print Solution().checkRecord(21230)
