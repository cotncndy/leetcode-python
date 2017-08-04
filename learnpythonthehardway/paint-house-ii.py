# Time:  O(n * k)
# Space: O(k)

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        if k == 0:
            return 0
        min1, min2, cost, idx = 0, 0, 0, -1

        for i in xrange(n):
            m1, m2, id = float('inf'), float('inf'), -1
            for j in xrange(k):
                prev = min2 if j == idx else min1
                cost = costs[i][j] + prev  # if j is the color of the mininum one, use the second min
                if cost < m1:  # cost is less than the current mininum
                    m2, m1, id = m1, cost, j
                elif cost < m2:
                    m2 = cost

            min1, min2, idx = m1, m2, id

        return min1


if __name__ == '__main__':
    print Solution().minCostII([[3, 5, 2, 6, 1], [1, 3, 4, 2, 6], [3, 5, 3, 7, 2]])
