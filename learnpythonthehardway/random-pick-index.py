# Time:  O(n)
# Space: O(1)

# Given an array of integers with possible duplicates,
# randomly output the index of a given target number.
# You can assume that the given target number must exist in the array.
#
# Note:
# The array size can be very large.
# Solution that uses too much extra space will not pass the judge.
#
# Example:
#
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
#
# // pick(3) should return either index 2, 3, or 4 randomly.
# Each index should have equal probability of returning.
# solution.pick(3);
#
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);

from random import randint


class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.__num = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res, n = -1, 0
        for i in xrange(len(self.__num)):
            if self.__num[i] != target:
                continue

            res = i if n == 0 or randint(1, n + 1) == 0 else res
            n += 1

        return res
