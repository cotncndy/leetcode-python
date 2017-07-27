# Time:  O(n * 2^n)
# Space: O(1)

# Given a set of distinct integers, S, return all possible subsets.
#
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    # review, good way
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        for i in xrange(len(nums)):
            size = len(res)
            for j in xrange(size):
                res.append(list(res[j]))
                res[-1].append(nums[i])
        return res

    def subsets2(self, nums):
        res, i, count = [], 0, 1 << len(nums)
        nums.sort()

        while i < count:
            cur = []
            for j in xrange(len(nums)):
                if i & (1 << j):
                    cur += nums[j],
            res.append(cur)  # notice, why here I can use 'cur' or list(cur), both works!
            i += 1

        return res




if __name__ == "__main__":
    print Solution().subsets2([1, 2, 3])
