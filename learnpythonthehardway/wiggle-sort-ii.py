# Time:  O(nlogn)
# Space: O(n)

# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
#
# Example:
# (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
# (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].
#
# Note:
# You may assume all input has valid answer.
#
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?

# Sorting and reoder solution. (92ms)
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums) - 1) / 2
        # review this is cool, for ex, [1,1,1,4,5,6], mid = 2
        # nums[mid::-1] means starting from mid, counting backwords, so it is [1,1,1]
        # nums[:mid:-1] means start from end, to the mid, counting backwards, so it is [6,5,4]
        # nums[::2] means start from 0 to end, step is 2, so we got :
        # [1,6,1,5,4,1]
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
        print nums


if __name__ == '__main__':
    Solution().wiggleSort([1, 5, 1, 1, 6, 4])
