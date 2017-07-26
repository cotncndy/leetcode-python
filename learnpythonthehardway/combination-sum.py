# Time:  O(k * n^k)
# Space: O(k)
#
# Given a set of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 2,3,6,7 and target 7,
# A solution set is:
# [7]
# [2, 2, 3]
#

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        res = []
        self.dfs(candidates, target, 0, [], res)

        return res

    def dfs(self, candidates, target, start, cur, res):
        if target == 0:
            res.append(list(cur))
        while start < len(candidates) and candidates[start] < target:
            cur.append(candidates[start])
            self.dfs(candidates, target - candidates[start], start, cur, res)
            cur.pop()
            start += 1


if __name__ == "__main__":
    candidates, target = [2, 3, 6, 7], 7
    result = Solution().combinationSum(candidates, target)
    print result
