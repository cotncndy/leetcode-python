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
        for i in xrange(len(nums)):
            size = len(res)
            for j in xrange(size):
                if i == 0 or nums[i] != nums[i - 1] or j >= prev_size:
                    res.append(list(res[j]))
                    res[-1].append(nums[i])
            prev_size = size

        return res


if __name__ == "__main__":
    print Solution().subsetsWithDup([1, 2, 2])
