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
        global_max, local_max = [[0 for _ in xrange(3)] for _ in xrange(days)], \
                                [[0 for _ in xrange(3)] for _ in xrange(days)]
        for i in xrange(1, days):
            diff = prices[i] - prices[i - 1]
            for j in xrange(1, 3):
                local_max[i][j] = max(global_max[i - 1][j - 1] + max(diff, 0), local_max[i - 1][j] + diff)
                global_max[i][j] = max(global_max[i - 1][j], local_max[i][j])

        return global_max[-1][2]

    def maxProfit2(self, prices):  # review
        if not prices:
            return 0
        global_max, local_max = [0] * 3, [0] * 3
        days = len(prices)
        for i in xrange(1, days):
            diff = prices[i] - prices[i - 1]
            for j in reversed(xrange(1, 3)):  # notice the j is reversed
                local_max[j] = max(global_max[j - 1] + max(diff, 0), local_max[j] + diff)
                global_max[j] = max(global_max[j], local_max[j])

        return global_max[-1]


    def maxProfit3(self,prices):
        l = len(prices)
        left, right = [0] * l, [0]  * l
        localMin, leftMax = float('inf'), 0

        for i in xrange(l):
            localMin = min(localMin, prices[i])
            leftMax = max(leftMax, prices[i] - localMin)
            left[i] = leftMax

        localMax, rightMax = float('-inf'), 0
        for i in reversed(xrange(l)):
            localMax = max(localMax, prices[i])
            rightMax = max(rightMax, localMax - prices[i])
            right[i] = rightMax

        maxProfit = 0
        for i in xrange(l):
            maxProfit = max(maxProfit, left[i] + right[i])

        return maxProfit





if __name__ == '__main__':
    print Solution().maxProfit3([1, 6, 3, 7,4,9,2,10,12,4])
