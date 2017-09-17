# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or not k:
            return 0
        days = len(prices)
        if k >= (days >> 1):
            return self.quickSolve(prices);
        global_max, local_max = [[0 for _ in xrange(k)] for _ in xrange(days)], \
                                [[0 for _ in xrange(k)] for _ in xrange(days)]
        for i in xrange(1, days):
            diff = prices[i] - prices[i - 1]
            for j in xrange(1, k):
                local_max[i][j] = max(global_max[i - 1][j - 1], local_max[i - 1][j]) + diff
                global_max[i][j] = max(global_max[i - 1][j], local_max[i][j])

        return global_max[-1][k - 1]

    def quickSolve(self, prices):
        res = 0
        for i in xrange(1, len(prices)):
            res += max(0, prices[i] - prices[i - 1])
        return res
