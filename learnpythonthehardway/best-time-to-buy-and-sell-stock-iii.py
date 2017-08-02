# Time:  O(n)
# Space: O(1)
#
# Say you have an array for which the ith element
# is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).
#

# Time:  O(n)
# Space: O(1)
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        # global[i][j] = max(global[i-1][j] , local[i][j])
        # local[i][j] = max(global[i-1][j-1] + max(diff,0), local[i-1][j] + diff)
        if not prices:
            return 0
        days = len(prices)
        global_max, local_max = [[0, 0, 0] * days], [[0, 0, 0] * days]
        for i in xrange(1, days):
            diff = prices[i] - prices[i - 1]
            for j in xrange(1, 3):
                local_max[i][j] = max(global_max[i - 1][j - 1] + max(diff, 0), local_max[i - 1][j] + diff)
                global_max[i][j] = max(global_max[i - 1][j], local_max[i][j])

        return global_max[-1][2]
