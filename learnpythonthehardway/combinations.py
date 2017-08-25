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
import itertools


class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        res = []
        self.backtrack(n, k, 0, [], res)
        return res

    def backtrack(self, n, k, start, cur, res):
        if k == 0:
            # res.append(list(cur))
            # cur[:] means a clone of cur. if we append cur directly, then during backtrack, cur could be change,
            # so the res would also change , this is not what we want, so we need copy of cur, kind of like java
            res.append(cur[:])  # knowledge what doesn this mean
            return
        for i in xrange(start, n):
            cur.append(i + 1)
            self.backtrack(n, k - 1, i + 1, cur, res)  # bugfixed
            cur.pop()

    # review beatiful
    def combine2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        elif k == n:
            return [[i for i in range(1, n + 1)]]
        else:
            res = []
            res += self.combine(n - 1, k)
            part = self.combine(n - 1, k - 1)
            for item in part:
                item.append(n)
            res += part
            return res

    def combine3(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return list(itertools.combinations(range(1, n + 1), k))


if __name__ == "__main__":
    result = Solution().combine(4, 2)
    print result
