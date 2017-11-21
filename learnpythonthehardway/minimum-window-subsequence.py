class Solution(object):
    def minWindow(self, S, T):
        """
        :param S: str
        :param T: str
        :return: str
        """
        m, n = len(T), len(S)
        dp = [[-1] * n for _ in xrange(m)]
        for j in xrange(n):
            if S[j] == T[0]:
                dp[0][j] = j
        for i in xrange(1, m):
            k = -1
            for j in xrange(n):
                if k != -1 and S[j] == T[i]:
                    dp[i][j] = k
                if dp[i - 1][j] != -1:
                    k = dp[i - 1][j]

        start, length = -1, float('inf')
        for j in xrange(n):
            if dp[m - 1][j] > 0 and length > j - dp[m - 1][j] + 1:
                start, length = dp[m - 1][j], j - dp[m - 1][j] + 1

        return "" if start == -1 else S[start:start + length]


if __name__ == '__main__':
    print Solution().minWindow('abcdebdde', 'bde')
