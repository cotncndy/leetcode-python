# Time:  O(n)
# Space: O(n)
#
# Given an array of integers and an integer k, return true if
# and only if there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and the difference between i and j is at most k.
#

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        lookup = {}
        for i, n in enumerate(nums):
            if n not in lookup:
                lookup[n] = i
            else:
                if i - lookup[n] <= k:
                    return True
                lookup[n] = i  # don't forget to update the value of n

        return False
