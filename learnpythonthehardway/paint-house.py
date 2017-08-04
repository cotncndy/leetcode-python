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
        min_costs = [costs[0]]
        for i in xrange(1, n):
            min_costs.append([0, 0, 0])  # bugfixed
            for j in xrange(0, 3):
                min_costs[i][j] = min(min_costs[i - 1][(j + 1) % 3], min_costs[i - 1][(j + 2) % 3]) + costs[i][j]

        return min(min_costs[-1])

    # space O(1), the above one ,space is O(n)
    def minCost2(self, costs):
        if not costs:
            return 0
        n = len(costs)
        if not n:
            return 0
        min_costs = [costs[0], [0, 0, 0]]
        for i in xrange(1, n):
            for j in xrange(0, 3):
                min_costs[i % 2][j] = costs[i][j] + min(min_costs[(i - 1) % 2][(j + 1) % 3],
                                                        min_costs[(i - 1) % 2][(j + 2) % 3])

        return min(min_costs[n - 1])



if __name__ == '__main__':
    print Solution().minCost([[7, 6, 2], [1, 4, 5], [3, 8, 4]])
