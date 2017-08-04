# Time:  O(n)
# Space: O(1)

# DP solution with rolling window.
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        same, diff = 0, k
        for i in xrange(2, n + 1):
            t = diff
            diff = (same + diff) * (k - 1)
            same = t

        return same + diff
