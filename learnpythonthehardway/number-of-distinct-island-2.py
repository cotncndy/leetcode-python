# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
# 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Count the number of distinct islands. An island is considered to be the same as another if they have the same
# shape, or have the same shape after rotation (90, 180, or 270 degrees only) or reflection (left/right direction or
# up/down direction).
#
# Example 1:
# 11000
# 10000
# 00001
# 00011
# Given the above grid map, return 1.
#
# Notice that:
# 11
# 1
# and
#  1
# 11
# are considered same island shapes. Because if we make a 180 degrees clockwise rotation on the first island,
# then two islands will have the same shapes.
# Example 2:
# 11100
# 10001
# 01001
# 01110
# Given the above grid map, return 2.
#
# Here are the two distinct islands:
# 111
# 1
# and
# 1
# 1
#
# Notice that:
# 111
# 1
# and
# 1
# 111
# are considered same island shapes. Because if we flip the first array in the up/down direction, then they have the
# same shapes.
# Note: The length of each dimension in the given grid does not exceed 50.


class Solution(object):
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n, pSet = len(grid), len(grid[0]), set()
        visited = [[False] * n for _ in xrange(m)]

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    li = []
                    self.dfs2(grid, i, j, li, visited)
                    li = self.transform(li)
                    pSet.add(''.join(str(e) for e in li))

        return len(pSet)

    def dfs2(self, grid, x, y, li, visited):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[x][y] == 0:
            return
        li.append((x, y))
        visited[x][y] = True
        self.dfs2(grid, x - 1, y, li, visited)
        self.dfs2(grid, x, y + 1, li, visited)
        self.dfs2(grid, x + 1, y, li, visited)
        self.dfs2(grid, x, y - 1, li, visited)

    def transform(self, li):
        tr = [[] for _ in xrange(8)]
        for p, q in li:
            tr[0].append((p, q))
            tr[1].append((-p, q))
            tr[2].append((p, -q))
            tr[3].append((-p, -q))
            tr[4].append((q, p))
            tr[5].append((-q, p))
            tr[6].append((q, -p))
            tr[7].append((-q, -p))

        for t in tr:
            t.sort()

        for t in tr:
            for u, k in enumerate(t):
                if u != 0:
                    t[u] = (k[0] - t[0][0], k[1] - t[0][1])
            t[0] = (0, 0)  # bugfixed ,the first item 's distance to itself should be (0,0)

        tr.sort()
        return tr[0]  # bugfixed should return the first list instead of the first ele of the first list


if __name__ == '__main__':
    print Solution().numDistinctIslands2([[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]])
    print Solution().numDistinctIslands2([[1, 1, 1, 1], [1, 0, 1, 0], [0, 0, 0, 0], [0, 1, 1, 1], [1, 1, 0, 1]])
    print Solution().numDistinctIslands2([[1, 1, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 1, 0]])
