# Time:  O(n!)
# Space: O(n)
#
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# For example,
# If n = 4 and k = 2, a solution is:
#
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        res = []
        self.backtrack(n, k, 0, [], res)
        return res

    def backtrack(self, n, k, start, cur, res):
        if k == 0:
            res.append(list(cur))
            return
        for i in xrange(start, n):
            cur.append(i + 1)
            self.backtrack(n, k - 1, start + 1, cur, res)
            cur.pop()


if __name__ == "__main__":
    result = Solution().combine(4, 2)
    print result
