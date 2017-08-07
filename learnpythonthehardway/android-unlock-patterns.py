# Time:  O(9^2 * 2^9)
# Space: O(9 * 2^9)

# DP solution.
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res, visited = 0, [False] * 10
        jumps = [[0 for _ in xrange(10)] for _ in xrange(10)]
        jumps[1][3] = jumps[3][1] = 2
        jumps[4][6] = jumps[6][4] = 5
        jumps[7][9] = jumps[9][7] = 8
        jumps[1][7] = jumps[7][1] = 4
        jumps[2][8] = jumps[8][2] = 5
        jumps[3][9] = jumps[9][3] = 6
        jumps[1][9] = jumps[9][1] = jumps[3][7] = jumps[7][3] = 5

        res += self.backtrack(1, 1, m, n, jumps, visited, 0) * 4
        res += self.backtrack(2, 1, m, n, jumps, visited, 0) * 4
        res += self.backtrack(5, 1, m, n, jumps, visited, 0)

        return res

    def backtrack(self, start, len, m, n, jumps, visited, res):
        if len >= m:  # any pattern which larger than m satisfied the requirements, could be count as one pattern
            res += 1
        len += 1
        if len > n:  # bugfixed
            return res
        visited[start] = True
        for next in xrange(1, 10):
            jump = jumps[start][next]
            if not visited[next] and (jump == 0 or visited[jump]):
                res = self.backtrack(next, len, m, n, jumps, visited,
                                     res)  # can not miss res = , otherwise you would get 0

        visited[start] = False  # backtrack
        return res


if __name__ == '__main__':
    print Solution().numberOfPatterns(1, 1)
