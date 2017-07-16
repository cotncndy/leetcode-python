# Time:  O(logn)
# Space: O(1)

# A peak element is an element that is greater than its neighbors.
#
# Given an input array where num[i] != num[i+1],
# find a peak element and return its index.
#
# The array may contain multiple peaks, in that case
# return the index to any one of the peaks is fine.
#
# You may imagine that num[-1] = num[n] = -infinite.
#
# For example, in array [1, 2, 3, 1], 3 is a peak element
# and your function should return the index number 2.
#
# Note:
# Your solution should be in logarithmic complexity.


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] > nums[mid + 1]:  # bugfixed should compare mid and mid + 1 careless
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1

        return left
