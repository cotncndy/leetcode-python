#  You are given coins of different denominations and a total amount of money. Write a function to compute the number
#  of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
#
# Note: You can assume that
#
#     0 <= amount <= 5000
#     1 <= coin <= 5000
#     the number of coins is less than 500
#     the answer is guaranteed to fit into signed 32-bit integer
#
# Example 1:
#
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
# Example 2:
#
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#
# Example 3:
#
# Input: amount = 10, coins = [10]
# Output: 1


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        m = len(coins)
        # bag = [[0] * (m + 1) for _ in xrange(amount + 1)]
        bag = [[0] * (amount + 1) for _ in xrange(m + 1)]
        bag[0][0] = 1

        # for i in xrange(1, amount + 1):
        #     bag[i][0] = 1
        #     for k in xrange(1, m + 1):
        #         bag[i][k] = bag[i][k - 1]
        #         if i >= coins[k - 1]:
        #             bag[i][k] += bag[i - coins[k - 1]][k]
        # return bag[amount][m]

        for k in xrange(1, m + 1):  # loop coins firstly
            bag[k][0] = 1
            for i in xrange(1, amount + 1):
                bag[k][i] = bag[k - 1][i]
                if i >= coins[k - 1]:
                    bag[k][i] += bag[k][i - coins[k - 1]]

        return bag[m][amount]




if __name__ == '__main__':
    print Solution().change(5, [1, 2, 5])
