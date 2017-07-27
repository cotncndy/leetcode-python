# Time:  O(n * 2^n)
# Space: O(1)

# Given a collection of integers that might contain duplicates, S, return all possible subsets.
#
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,2], a solution is:
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, prev_size = [[]], 0
        nums.sort()  # bugfixed
        for i in xrange(len(nums)):
            size = len(res)
            for j in xrange(size):
                if i == 0 or nums[i] != nums[i - 1] or j >= prev_size:
                    res.append(list(res[j]))
                    res[-1].append(nums[i])
            prev_size = size

        return res

    def subsetsWithDup2(self, nums):
        res, count, i = [], 1 << len(nums), 0
        nums.sort()  # bugfixed
        while i < count:
            cur = []
            for j in xrange(len(nums)):
                if i & (1 << j):
                    cur += nums[j],

            if cur not in res:  # notice, this would be slow
                res.append(cur)
            i += 1
        return res

    def subsetsWithDup3(self, nums):
        res = []
        self.dfs(sorted(nums), '', res)

        return res

    def dfs(self, nums, cur, res):
        if not nums:
            if cur not in res:
                res.append(cur)

        self.dfs(nums[1:], cur, res)
        self.dfs(nums[1:], cur + [nums[0]], res)


if __name__ == "__main__":
    print Solution().subsetsWithDup3([4, 4, 1, 4, 4])
