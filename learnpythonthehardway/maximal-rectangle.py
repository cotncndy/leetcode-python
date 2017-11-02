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
                if not stack or (i < len(height) and height[i] > height[stack[-1]]):  # bugfixed
                    stack.append(i)
                    i += 1
                else:
                    last = stack.pop()
                    if not stack:
                        res = max(res, height[last] * i)
                    else:
                        res = max(res, height[last] * (i - stack[-1] - 1))

            return res

        if not matrix or not len(matrix[0]):
            return 0
        height, area = [0] * len(matrix[0]), 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if matrix[i][j] == '0':  # bugfixed
                    height[j] = 0
                else:
                    height[j] += 1

            area = max(area, largetRect(height))  # bugfixed

        return area

    def maximalRectangle2(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp, res = [0] * col, float('-inf')

        for i in xrange(row):
            for j in xrange(col):
                if matrix[i][j] == '1':
                    if i == 0:
                        dp[j] = 1
                    else:
                        dp[j] += 1
                else:
                    dp[j] = 0

            res = max(res, self.findMaxRec(dp))

        return res

    def findMaxRec(self, dp):
        stack, maxArea = [], 0
        a, i = [], 0
        a.extend(dp)
        a.extend([0])
        while i < len(a):
            if not stack or dp[stack[-1]] <= a[i]:
                stack.append(i)
                i += 1
            else:
                maxArea = max(maxArea, (i - stack[-1]) * a[stack[-1]])
                stack.pop()

        return maxArea


if __name__ == '__main__':
    print Solution().maximalRectangle2(["10100", "10111", "11111", "10010"])
    # print Solution().maximalRectangle2(["1"])
    # print Solution().findMaxRec([3,1,2,2,2,0])
