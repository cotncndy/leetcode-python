# Time:  O(m * n)
# Space: O(m + n)
#
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        sum = list(grid[0])
        for i in xrange(1, len(grid[0])):
            sum[i] += sum[i - 1]  # bugfixed, since sum aleady is grid[0], no need to +grid[0][i]
        print sum

        for i in xrange(1, len(grid)):
            sum[0] += grid[i][0]
            for j in xrange(1, len(grid[0])):
                sum[j] = min(sum[j], sum[j - 1]) + grid[i][j]
            print sum

        return sum[-1]


if __name__ == '__main__':
    print Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
