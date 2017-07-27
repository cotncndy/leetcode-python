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


if __name__ == "__main__":
    print Solution().subsets([1, 2, 3])
