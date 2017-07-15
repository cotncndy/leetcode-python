# Time:  O(logn)
# Space: O(1)
#
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:  # review, there need to be <= , think about case ([1],1)
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            if (nums[mid] >= nums[left] and nums[left] <= target < nums[mid]) or \
                    (nums[mid] < nums[left] and not (nums[mid] < target <= nums[right])):
                # case 1: nums[mid] >= nums[left] means mid is at the left part of pivot
                # case 2: nums[mid] < nums[left] means mid is at the right part of pivot
                right = mid - 1
            else:
                left = mid + 1

        return -1
