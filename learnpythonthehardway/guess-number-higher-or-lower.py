# Time:  O(logn)
# Space: O(1)

# Given an array nums containing n + 1 integers where each integer is
# between 1 and n (inclusive), prove that at least one duplicate number
# must exist. Assume that there is only one duplicate number, find the duplicate one.
#
# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    pass


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(n) == 0:
            return n
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) < 0:  # very twisted, guess(mid) < 0 means my picked num < mid here
                right = mid - 1
            else:
                left = mid + 1
