# If the given array is not sorted and the memory is unlimited:
#   - Time:  O(m + n)
#   - Space: O(min(m, n))
# elif the given array is already sorted:
#   if m << n or m >> n:
#     - Time:  O(min(m, n) * log(max(m, n)))
#     - Space: O(1)
#   else:
#     - Time:  O(m + n)
#     - Soace: O(1)
# else: (the given array is not sorted and the memory is limited)
#     - Time:  O(max(m, n) * log(max(m, n)))
#     - Space: O(1)

# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
#
# Follow up:
# - What if the given array is already sorted? How would you optimize your algorithm?
# - What if nums1's size is small compared to num2's size? Which algorithm is better?
# - What if elements of nums2 are stored on disk, and the memory is limited such that
#   you cannot load all elements into the memory at once?


# If the given array is not sorted and the memory is unlimited.
# Time:  O(m + n)
# Space: O(min(m, n))
# Hash solution.
import collections


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        lookup = collections.defaultdict(int)
        for i in nums1:
            lookup[i] += 1

        res = []
        for i in nums2:
            if lookup[i] > 0:
                res += nums2[i]
                lookup[i] -= 1  # review don't forget this

        return res
