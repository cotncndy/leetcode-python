# There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to
# adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move
# N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large,
# return it after mod 109 + 7.
#
# Example 1:
# Input:m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:
#
# Example 2:
# Input:m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation:
#
# Note:
# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].


class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[[0] * n for _ in xrange(m)] for _ in xrange(N + 1)]

        for k in xrange(1, N + 1):
            for x in xrange(0, m):
                for y in xrange(0, n):
                    v1 = 1 if x == 0 else dp[k - 1][x - 1][y]
                    v2 = 1 if x == m - 1 else dp[k - 1][x + 1][y]
                    v3 = 1 if y == 0 else dp[k - 1][x][y - 1]
                    v4 = 1 if y == n - 1 else dp[k - 1][x][y + 1]

                    dp[k][x][y] = (v1 + v2 + v3 + v4) % 1000000007

        return dp[N][i][j]

    def findPaths2(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """

        res, dp = 0, [[0] * n for _ in xrange(m)]
        dp[i][j] = 1

        for k in xrange(0, N):
            t = [[0] * n for _ in xrange(m)]
            for i in xrange(0, m):
                for j in xrange(0, n):
                    for l, k in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                        x, y = i + l, j + k
                        if x < 0 or x >= m or y < 0 or y >= n:
                            res = (res + dp[i][j]) % 1000000007
                        else:
                            t[x][y] = (t[x][y] + dp[i][j]) % 1000000007

            dp = t

        return res


if __name__ == '__main__':
    print Solution().findPaths2(2, 2, 2, 0, 0)
