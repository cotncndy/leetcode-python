# Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal,
# vertical, diagonal or anti-diagonal.
#
# Example:
# Input:
# [[0,1,1,0],
#  [0,1,1,0],
#  [0,0,0,1]]
# Output: 3
# Hint: The number of elements in the given matrix will not exceed 10,000.

class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not len(M) or not len(M[0]):
            return 0
        row, col, res = len(M), len(M[0]), 0
        dp = [[[0] * 4 for _ in xrange(col)] for _ in xrange(row)]  # notice, how to initialize a 3-dim list
        for i in xrange(row):
            for j in xrange(col):
                if M[i][j] == 0:
                    continue
                for k in xrange(4):
                    dp[i][j][k] = 1
                if j:
                    dp[i][j][0] += dp[i][j - 1][0]  # horizontally
                if i:
                    dp[i][j][1] += dp[i - 1][j][1]  # vertically
                if i and j:
                    dp[i][j][2] += dp[i - 1][j - 1][2]  # diag
                if i and j < col - 1:
                    dp[i][j][3] += dp[i - 1][j + 1][3]  # anti-diag
                res = max(res, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])

        return res


if __name__ == '__main__':
    print Solution().longestLine([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]])
