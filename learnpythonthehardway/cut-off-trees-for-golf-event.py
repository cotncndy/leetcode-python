# You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map,
# in this map:
#
# 0 represents the obstacle can't be reached.
# 1 represents the ground can be walked through.
# The place with number bigger than 1 represents a tree can be walked through, and this positive number represents
# the tree's height.
# You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with
# lowest height first. And after cutting, the original place has the tree will become a grass (value 1).
#
# You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the
# trees. If you can't cut off all the trees, output -1 in that situation.
#
# You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.
#
# Example 1:
# Input:
# [
#  [1,2,3],
#  [0,0,4],
#  [7,6,5]
# ]
# Output: 6
# Example 2:
# Input:
# [
#  [1,2,3],
#  [0,0,0],
#  [7,6,5]
# ]
# Output: -1
# Example 3:
# Input:
# [
#  [2,3,4],
#  [0,0,5],
#  [8,7,6]
# ]
# Output: 6
# Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
# Hint: size of the given matrix will not exceed 50x50.
class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        que, m, n = [], len(forest), len(forest[0])
        steps = [[float('inf')] * n for _ in xrange(m)]
        steps[0][0] = 0

        que.append((0, 0))
        while que:
            x, y = que.pop(0)
            t, step, cX, cY = float('inf'), steps[x][y], -1, -1
            for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nX, nY = x + dir[0], y + dir[1]
                if nX < 0 or nX >= m or nY < 0 or nY >= n or forest[nX][nY] == 0 or 1 < forest[nX][nY] < forest[x][y] or \
                        steps[nX][nY] < 1 + steps[x][y]:
                        continue
                if t > forest[nX][nY]:
                    t , cX, cY = forest[nX][nY], nX, nY

            if cX == -1:
                return step
            forest[cX][cY], steps[cX][cY] = 1, step + 1
            que.append((cX,cY))

        return -1

if __name__ == '__main__':
    print Solution().cutOffTree([[1,2,3],[0,0,4],[7,6,5]])
    print Solution().cutOffTree([[1,2,3],[0,0,0],[7,6,5]])

