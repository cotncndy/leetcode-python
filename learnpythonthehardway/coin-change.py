# Time:  O(n * k), n is the number of coins, k is the amount of money
# Space: O(k)
#
# You are given coins of different denominations and
# a total amount of money amount. Write a function to
# compute the fewest number of coins that you need to
# make up that amount. If that amount of money cannot
# be made up by any combination of the coins, return -1.
#
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
# Example 2:
# coins = [2], amount = 3
# return -1.
#
# Note:
# You may assume that you have an infinite number of each kind of coin.

# DP solution. (1680ms)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)  # initially make the value to be 'amount+1'
        dp[0] = 0  # bugfixed
        for i in xrange(amount + 1):
            for j in coins:
                if j <= i:  # coin value shold be <= the amount you want, you can not use 2-cents coin to get number 1
                    dp[i] = min(dp[i], dp[i - j] + 1)

        return dp[amount] if dp[
                                 amount] <= amount else -1  # if dp[amount] = amount+1, then  we can not get amount by given coins
