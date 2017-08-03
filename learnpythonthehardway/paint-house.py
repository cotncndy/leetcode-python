# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        n = len(costs)
        if not n:
            return 0
        min_costs = [costs[0], [0, 0, 0] * (n - 1)]
        for i in xrange(1, n):
            for j in xrange(0, 3):
                min_costs[i][j] = min(min_costs[i - 1][(j + 1) % 3], min_costs[i - 1][(j + 2) % 3]) + costs[i][j]

        return min(min_costs[-1][0], min_costs[-1][1], min_costs[-1][2])
