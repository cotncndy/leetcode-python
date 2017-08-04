# Time:  O(n)
# Space: O(1)

# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as
# many transactions as you like (ie, buy one and sell one share of the
# stock multiple times) with the following restrictions:
#
# You may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day.
# (ie, cooldown 1 day)
# Example:
#
# prices = [1, 2, 3, 0, 2]
# maxProfit = 3
# transactions = [buy, sell, cooldown, buy, sell]
#

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy[i] = max(sell[i-2]-prices[i], buy[i-1])
        # sell[i] = max(buy[i-1] + prices[i], sell[i-1])
        buy, pre_buy, sell, pre_sell = float('-inf'), 0, 0, 0  # bugfixed,at beginning, buy should be float('-inf')
        for p in prices:
            pre_buy = buy  # bugfixed, can not combine this 2 line , we need to use the new value of pre_buy and pre_sell
            buy = max(pre_sell - p, pre_buy)
            pre_sell = sell
            sell = max(pre_buy + p, pre_sell)

        return sell


if __name__ == '__main__':
    print Solution().maxProfit([1, 2, 3, 0, 2])
