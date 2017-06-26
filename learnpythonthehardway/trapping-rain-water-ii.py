# Time:  O(m * n * log(m + n)) ~ O(m * n * log(m * n))
# Space: O(m * n)

# Given an m x n matrix of positive integers representing the height of each unit cell in
# a 2D elevation map, compute the volume of water it is able to trap after raining.
#
# Note:
# Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.
#
# Example:
#
# Given the following 3x6 height map:
# [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]
#
# Return 4.

from heapq import heappush, heappop


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m = len(heightMap)
        if not m:
            return 0
        n = len(heightMap[0])
        if not n:
            return 0

        min_heap = []
        is_vistied = [[False for i in xrange(n)] for j in xrange(m)]

        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heappush(min_heap, [heightMap[i][j], i, j])
                    is_vistied[i][j] = True
        trap = 0
        while min_heap:
            h, x, y = heappop(min_heap)
            for (dx, dy) in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and not is_vistied[new_x][new_y]:
                    trap += max(0, h - heightMap[new_x][new_y])
                    heappush(min_heap, [heightMap[new_x][new_y], new_x, new_y])
                    is_vistied[new_x][new_y] = True

        return trap
