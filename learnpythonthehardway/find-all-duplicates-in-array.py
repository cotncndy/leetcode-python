#
# Given an array of integers, 1 <= a[i] <=n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in xrange(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                res.append(abs(nums[i]))
            nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        return res


if __name__ == '__main__':
    print Solution().findDuplicates([4, 5, 2, 7, 5, 2, 3, 1])
