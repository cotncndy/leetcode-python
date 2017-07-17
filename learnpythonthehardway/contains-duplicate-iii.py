# Time:  O(n * t)
# Space: O(max(k, t))
#
# Given an array of integers, find out whether there
# are two distinct in windows i and j in the array such
# that the difference between nums[i] and nums[j] is
# at most t and the difference between i and j is at
# most k.
#

# This is not the best solution
# since there is no built-in bst structure in Python.
# The better solution could be found in C++ solution.
import collections


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):  # review bucket sorting + map
        if k < 0 or t < 0:
            return False
        window = collections.OrderedDict()  # knowledge ordered dict in python
        # knowledge orderedDict for python would keep the insert order of the entry
        for n in nums:
            if len(window) > k:
                window.popitem(False)  # knowledge true, LIFO, False: FIFO
            bucket = n if not t else n // t
            for m in (
            window.get(bucket - 1), window.get(bucket), window.get(bucket + 1)):  # knowledge the for loop is so concise
                if m is not None and abs(n - m) <= t:
                    return True

            window[bucket] = n

        return False

    def containsNearbyAlmostDuplicate2(self, nums, k, t):  # review bucket sorting + map
        if k < 0 or t < 0:
            return False
        lookup, w = {}, t + 1
        for i in xrange(len(nums)):
            bucket = nums[i] / w
            for m in (lookup.get(bucket - 1), lookup.get(bucket), lookup.get(bucket + 1)):
                if m is not None and abs(m - nums[i]) <= t:
                    return True

            lookup[bucket] = nums[i]
            if len(lookup) > k:
                del lookup[nums[i - k]]
        return False
