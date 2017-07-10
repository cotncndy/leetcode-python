# Time:  O(n) ~ O(n^2), O(n) on average.
# Space: O(n)

# Given a non-empty array of integers,
# return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
# Note:
# You may assume k is always valid,
# 1 <= k <= number of unique elements.
# Your algorithm's time complexity must be better
# than O(n log n), where n is the array's size.

import collections


class Solution(object):
    # todo, bucket sort and heap method
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # review th usage of most_common, it would return (key, count)
        return [key for key, _ in collections.Counter(nums).most_common(k)]


if __name__ == '__main__':
    print Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
