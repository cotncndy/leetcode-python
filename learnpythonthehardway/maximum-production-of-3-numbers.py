# Given an integer array, find three numbers whose product is maximum and output the maximum product.
#
# Example 1:
# Input: [1,2,3]
# Output: 6
# Example 2:
# Input: [1,2,3,4]
# Output: 24
# Note:
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])

    def maximumProduct2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = max3 = -1000
        min1 = min2 = 1000
        for n in nums:
            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif n > max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n
            if n < min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n
        return max(max1 * max2 * max3, max1 * min1 * min2)
