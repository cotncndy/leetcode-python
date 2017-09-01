# Time:  O(n^2)
# Space: O(n)

# Given a 2D binary matrix filled with 0's and 1's,
# find the largest rectangle containing all ones and return its area.

# Ascending stack solution.
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        def largetRect(height):
            stack, res, i = [], 0, 0

            while i <= len(height):
                if not stack or (i > len(height) and height[i] > height[stack[-1]]):
                    stack.append(i)
                    i += 1
                else:
                    last = stack.pop()
                    if not stack:
                        res = max(res, height[last] * i)
                    else:
                        res = max(res, height[last] * (i - stack[-1] - 1))

            return res

        height = [0] * len(matrix[0])
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if matrix[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] += 1

        return largetRect(height)
