# Time:  O(n)
# Space: O(n)

# Given an unsorted array, find the maximum difference between
#
# the successive elements in its sorted form.
#
# Try to solve it in linear time/space.
#
# Return 0 if the array contains less than 2 elements.
#
# You may assume all elements in the array are non-negative integers
#
#  and fit in the 32-bit signed integer range.

# bucket sort
# Time:  O(n)
# Space: O(n)
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        max_val, min_val = max(nums), min(nums)
        gap = (max_val - min_val) / len(nums) + 1
        bucket_size = (max_val - min_val) / gap + 1
        bucket = [{'min': float('inf'), 'max': float('-inf')} for _ in xrange(bucket_size)]

        for n in nums:
            i = (n - min_val) / gap
            bucket[i]['min'] = min(bucket[i]['min'], n)
            bucket[i]['max'] = max(bucket[i]['max'], n)

        max_gap, pre_bucket_max = 0, min_val
        for i in xrange(bucket_size):
            # skip the empty bucket
            if bucket[i]['min'] == float('inf') and bucket[i]['max'] == float('-inf'):
                continue
            max_gap = max(max_gap, bucket[i]['min'] - pre_bucket_max)
            pre_bucket_max = bucket[i]['max']

        return max_gap


if __name__ == "__main__":
    print Solution().maximumGap([1, 100])
