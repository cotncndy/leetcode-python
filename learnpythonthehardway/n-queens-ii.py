# Time:  O(n!)
# Space: O(n)
#
# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.
#

# quick solution for checking if it is diagonally legal
class Solution:
    # @return an integer
    def totalNQueens(self, n):
        return self.backtrack(n, [], 0)

    def backtrack(self, n, solution, row):
        if row == n:
            return 1
        result = 0
        for i in xrange(n):
            if i not in solution and reduce(lambda acc, j: abs(row - j) == abs(i - solution[j]) and acc, \
                                            xrange(len(solution)), True):
                result += self.backtrack(n, solution + [i], row + 1)
        return result


if __name__ == "__main__":
    print Solution().totalNQueens(8)
