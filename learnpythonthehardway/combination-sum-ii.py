# Time:  O(k * C(n, k))
# Space: O(k)
#
# Given a collection of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 10,1,2,7,6,1,5 and target 8,
# A solution set is:
# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6]
#

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        res = []
        self.dfs(sorted(candidates), target, 0, [], res)

        return res

    def dfs(self, candidates, target, start, cur, res):
        if target == 0:
            res.append(list(cur))

        prev = 0
        while start < len(candidates) and candidates[start] <= target:
            if candidates[start] != prev:
                cur.append(candidates[start])
                self.dfs(candidates, target - candidates[start], start + 1, cur, res)
                cur.pop()
                prev = candidates[start]

            start += 1


if __name__ == "__main__":
    candidates, target = [10, 1, 2, 7, 6, 1, 5], 8
    result = Solution().combinationSum2(candidates, target)
    print result
