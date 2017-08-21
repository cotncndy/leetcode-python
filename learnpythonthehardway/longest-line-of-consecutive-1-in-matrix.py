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

    def longestLine2(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M) == 0 or len(M[0]) == 0:
            return 0

        tmp = 0
        res = 0
        t1, t2 = {}, {}
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    tmp += 1
                    if tmp > res:
                        res = tmp
                else:
                    tmp = 0
                t1[i + j] = []
                t2[i - j] = []
            tmp = 0

        for i in range(len(M[0])):
            for j in range(len(M)):
                if M[j][i] == 1:
                    tmp += 1
                    if tmp > res:
                        res = tmp
                else:
                    tmp = 0
                t1[i + j].append(M[j][i])
                t2[j - i].append(M[j][i])
            tmp = 0

        for i in t1.values() + t2.values():
            tmp = 0
            for j in i:
                if j == 1:
                    tmp += 1
                    if tmp > res:
                        res = tmp
                else:
                    tmp = 0

        return res

    def longestLine3(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        h, w = len(M), len(M) and len(M[0]) or 0
        ans = 0

        # horizontal & diagonal
        diag = [[0] * w for r in range(h)]
        for x in range(h):
            cnt = 0
            for y in range(w):
                cnt = M[x][y] * (cnt + 1)  # horizontal
                diag[x][y] = M[x][y]
                if x > 0 and y > 0 and M[x][y] and diag[x - 1][y - 1]:
                    diag[x][y] = diag[x - 1][y - 1] + 1
                ans = max(ans, cnt, diag[x][y])

        # vertical & anti-diagonal
        adiag = [[0] * w for r in range(h)]
        for x in range(w):
            cnt = 0
            for y in range(h):
                cnt = M[y][x] * (cnt + 1)
                adiag[y][x] = M[y][x]
                if y < h - 1 and x > 0 and M[y][x] and adiag[y + 1][x - 1]:
                    adiag[y][x] += adiag[y + 1][x - 1]
                ans = max(ans, cnt, adiag[y][x])

        return ans

    def longestLine4(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        res = 0
        m = len(M)
        n = len(M[0])

        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    if j == 0 or M[i][j - 1] == 0:
                        count = 0
                        index = j
                        while index < n and M[i][index] == 1:
                            count += 1
                            index += 1
                        res = max(res, count)
                    if i == 0 or M[i - 1][j] == 0:
                        count = 0
                        index = i
                        while index < m and M[index][j] == 1:
                            count += 1
                            index += 1
                        res = max(res, count)
                    if i == 0 or j == 0 or M[i - 1][j - 1] == 0:
                        count = 0
                        indexi = i
                        indexj = j
                        while indexi < m and indexj < n and M[indexi][indexj] == 1:
                            count += 1
                            indexi += 1
                            indexj += 1
                        res = max(res, count)
                    if i == 0 or j == n - 1 or M[i - 1][j + 1] == 0:
                        count = 0
                        indexi = i
                        indexj = j
                        while indexi < m and indexj >= 0 and M[indexi][indexj] == 1:
                            count += 1
                            indexi += 1
                            indexj -= 1
                        res = max(res, count)
        return res

    def longestLine5(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        if n == 0:
            return 0
        m = len(M[0])

        helper_map = [{'h': 0, 'v': 0, 'd': 0, 'rd': 0} for _ in range(m + 1)]
        prev_d = 0
        max_length = 0
        for i in range(n):
            prev_d = 0
            for j in range(m):
                if M[i][j] != 0:
                    helper_map[j]['h'] = helper_map[j - 1]['h'] + 1
                    helper_map[j]['v'] = helper_map[j]['v'] + 1

                    tmp = helper_map[j]['d']
                    helper_map[j]['d'] = prev_d + 1
                    prev_d = tmp

                    helper_map[j]['rd'] = helper_map[j + 1]['rd'] + 1
                    max_length = max(max_length, helper_map[j]['h'], helper_map[j]['v'], helper_map[j]['d'],
                                     helper_map[j]['rd'])
                else:
                    prev_d = helper_map[j]['d']
                    helper_map[j] = {'h': 0, 'v': 0, 'd': 0, "rd": 0}

        return max_length

    def longestLine6(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        ret, m, n = 0, len(M), len(M[0])
        cols, diags, adiags = [0] * n, [0] * (m + n - 1), [0] * (m + n - 1)
        for i in xrange(m):
            row = 0
            for j in xrange(n):
                if M[i][j] == 1:
                    row += 1
                    cols[j] += 1
                    diags[i + j] += 1
                    adiags[j - i] += 1
                    ret = max(ret, row, cols[j], diags[i + j], adiags[j - i])
                else:
                    row = cols[j] = diags[i + j] = adiags[j - i] = 0
        return ret


if __name__ == '__main__':
    print Solution().longestLine([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]])
