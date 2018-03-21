# Given several boxes with different colors represented by different positive numbers.
# You may experience several rounds to remove boxes until there is no box left. Each time you can choose some
# continuous boxes with the same color (composed of k boxes, k >= 1), remove them and get k*k points.
# Find the maximum points you can get.
#
# Example 1:
# Input:
#
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# Output:
# 23
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
# ----> [1, 3, 3, 3, 1] (1*1=1 points)
# ----> [1, 1] (3*3=9 points)
# ----> [] (2*2=4 points)
# Note: The number of boxes n would not exceed 100.


class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        n = len(boxes)
        dp = [[0] * n for _ in xrange(n)]

        for i in xrange(n):
            dp[i][i] = 1

        for k in xrange(1, n - 1):
            for left in xrange(0, n - k):
                right = left + k
                i = left
                while i <= right:
                    temp = 0
                    bL, bR = self.findContinous(boxes, i, left, right)
                    temp = (bR - bL + 1) ** 2
                    if bL > left:
                        temp += dp[left][bL - 1]
                    if bR < right:
                        temp += dp[bR + 1][right]
                    dp[left][right] = max(dp[left][right], temp)
                    i = bR + 1

        return dp[0][n - 1]

    def findContinous(self, boxes, idx, left, right):
        i, j = idx, idx
        while i >= left and boxes[i] == boxes[idx]:
            i -= 1
        while j <= right and boxes[j] == boxes[idx]:
            j += 1

        return (i + 1, j - 1)


if __name__ == '__main__':
    print Solution().removeBoxes([1, 3, 2, 2, 2, 4, 3, 1])
