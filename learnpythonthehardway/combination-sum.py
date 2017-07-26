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
        self.dfs(sorted(candidates), target, 0, [], res)  # fixed, need to sort them
        # self.combinationSumRecu(sorted(candidates), res, 0, [], target)

        return res

    def dfs(self, candidates, target, start, cur, res):
        if target == 0:
            res.append(list(cur))
            return
        while start < len(candidates) and candidates[start] <= target:  # bugfixed missing "="
            cur.append(candidates[start])
            self.dfs(candidates, target - candidates[start], start, cur, res)
            cur.pop()
            start += 1

    def combinationSumRecu(self, candidates, result, start, intermediate, target):
        if target == 0:
            result.append(list(intermediate))
        while start < len(candidates) and candidates[start] <= target:
            intermediate.append(candidates[start])
            self.combinationSumRecu(candidates, result, start, intermediate, target - candidates[start])
            intermediate.pop()
            start += 1


if __name__ == "__main__":
    candidates, target = [8, 7, 4, 3], 11
    result = Solution().combinationSum(candidates, target)
    print result
