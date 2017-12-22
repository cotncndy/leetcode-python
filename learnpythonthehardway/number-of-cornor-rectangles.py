# Given a grid where each entry is only 0 or 1, find the number of corner rectangles.
#
# A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. Note that only the corners
# need to have the value 1. Also, all four 1s used must be distinct.
#
# Example 1:
# Input: grid =
# [[1, 0, 0, 1, 0],
#  [0, 0, 1, 0, 1],
#  [0, 0, 0, 1, 0],
#  [1, 0, 1, 0, 1]]
# Output: 1
# Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
# Example 2:
# Input: grid =
# [[1, 1, 1],
#  [1, 1, 1],
#  [1, 1, 1]]
# Output: 9
# Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
# Example 3:
# Input: grid =
# [[1, 1, 1, 1]]
# Output: 0
# Explanation: Rectangles must have four distinct corners.
# Note:
# The number of rows and columns of grid will each be in the range [1, 200].
# Each grid[i][j] will be either 0 or 1.
# The number of 1s in the grid will be at most 6000.


class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) < 2 or len(grid[0]) < 2:
            return 0
        cnt = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                for l in xrange(1, len(grid)):
                    if i + l == len(grid):
                        break
                    for m in xrange(1, len(grid[i])):
                        if j + m == len(grid[i]):
                            break;
                        if grid[i][j + m] == 0 or grid[i + l][j] == 0 or grid[i + l][j + m] == 0:
                            continue
                        cnt += 1

        return cnt


if __name__ == '__main__':
    print Solution().countCornerRectangles([[0, 1, 0], [1, 0, 1], [1, 0, 1], [0, 1, 0]])
