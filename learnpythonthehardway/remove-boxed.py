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

    def removeBoxes2(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        # dp[100][100][100]
        dp = [[[0] * 100 for _ in xrange(100)] for _ in xrange(100)]
        return self.dfs(boxes, 0, len(boxes) - 1, 0, dp)

    def dfs(self, boxes, l, r, k, dp):
        if l > r:
            return 0
        # dp(l,r,k) mean there are consecutive k ele which == boxes[l] on l's left side
        if dp[l][r][k]:
            return dp[l][r][k]
        dp[l][r][k] = (k + 1) ** 2 + self.dfs(boxes, l + 1, r, 0, dp)
        for i in xrange(l + 1, r + 1):
            if boxes[i] == boxes[l]:
                dp[l][r][k] = max(dp[l][r][k],
                                  self.dfs(boxes, l + 1, i - 1, 0, dp) + self.dfs(boxes, i + 1, r, k + 1, dp))

        return dp[l][r][k]





if __name__ == '__main__':
    print Solution().removeBoxes2([1, 3, 2, 2, 2, 3, 4, 3, 1])
