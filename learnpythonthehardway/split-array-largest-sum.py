# Time:  O(nlogs), s is the sum of nums
# Space: O(1)

# Given an array which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.
#
# Note:
# Given m satisfies the following constraint: 1 <= m <= length(nums) <= 14,000.
#
# Examples:
#
# Input:
# nums = [7,2,5,10,8]
# m = 2
#
# Output:
# 18
#
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

        def can_split(nums, m, s):
            cnt, cur_sum = 1, 0
            for n in nums:
                cur_sum += n
                if cur_sum > s:
                    cur_sum, cnt = n, cnt + 1

            return cnt <= m

        left, right = 0, 0
        for n in nums:
            left = max(left, n)
            right += n

        while left <= right:
            mid = left + (right - left) / 2
            if can_split(nums, m, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
