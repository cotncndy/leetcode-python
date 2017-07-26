# Time:  O(n * n!)
# Space: O(n)
#
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].
#

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, used = [], [False] * len(nums)
        nums.sort()
        self.backtrack(nums, [], used, res)
        return res

    def backtrack(self, nums, cur, used, res):
        if len(cur) == len(nums):
            res.append(list(cur))
            return
        for i in xrange(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            cur.append(nums[i])
            self.backtrack(nums, cur, used, res)
            cur.pop()
            used[i] = False


if __name__ == "__main__":
    print Solution().permuteUnique([1, 1, 2])
    print Solution().permuteUnique([1, -1, 1, 2, -1, 2, 2, -1])
