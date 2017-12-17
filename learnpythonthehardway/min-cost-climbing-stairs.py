class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.extend([0])

        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in xrange(2, len(dp)):
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])

        return dp[-1]


if __name__ == '__main__':
    print Solution().minCostClimbingStairs([10, 15, 20])
    print Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    print Solution().minCostClimbingStairs([0, 0, 1, 1])
