# Time:  O(n)
# Space: O(1)
#
# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors
# only include 2, 3, 5. For example,
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the
# first 10 ugly numbers.
#
# Note that 1 is typically treated as an ugly number.
#
# Hint:
#
# The naive approach is to call isUgly for every number
# until you reach the nth one. Most numbers are not ugly.
# Try to focus your effort on generating only the ugly ones.
#

import heapq


class Solution:
    ugly = sorted(2 ** a * 3 ** b * 5 ** c for a in xrange(32) for b in xrange(20) for c in xrange(14))

    # @param {integer} n
    # @return {integer}
    def nthUglyNumber(self, n):
        return self.ugly[n - 1]

    def nthUglyNumber2(self, n):
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while len(ugly) < n:
            l, m, t = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            k = min(l, m, t)
            if k == l:
                i2 += 1
            if k == m:
                i3 += 1
            if k == t:
                i5 += 1
            ugly.append(k)

        return ugly[-1]

    def nthUglyNumber3(self, n):
        p, q, r = [2], [3], [5]
        ugly = 1
        for u in heapq.merge(p, q, r):
            if n == 1:
                return ugly
            if u > ugly:
                ugly = u
                n -= 1
                p.append(2 * u)
                q.append(3 * u)
                r.append(5 * u)
        return ugly


if __name__ == '__main__':
    print Solution().nthUglyNumber3(7)
