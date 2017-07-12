# Time:  O(n)
# Space: O(1)
#
# Given an array nums containing n + 1 integers where each integer
# is between 1 and n (inclusive), prove that at least one duplicate
# element must exist. Assume that there is only one duplicate number,
# find the duplicate one.
#
# Note:
# - You must not modify the array (assume the array is read only).
# - You must use only constant extra space.
# - Your runtime complexity should be less than O(n^2).
#

# Two pointers method, same as Linked List Cycle II.
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Treat each (key, value) pair of the array as the (pointer, next) node of the linked list,
        # thus the duplicated number will be the begin of the cycle in the linked list.
        # Besides, there is always a cycle in the linked list which
        # starts from the first element of the array.
        slow, fast = 0, 0

        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
