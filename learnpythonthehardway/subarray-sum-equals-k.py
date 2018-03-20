# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum
# equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
import collections


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        subSum, dic, res = 0, collections.defaultdict(int), 0
        for key, val in enumerate(nums):
            subSum += val
            dic[subSum] += 1
            if subSum == k:
                res += 1
            if k and subSum - k in dic:
                res += dic[subSum - k]
            elif k == 0 and subSum - k in dic and dic[subSum - k] > 1:
                res += dic[subSum] - 1

        return res


if __name__ == '__main__':
    print Solution().subarraySum([1, 1, 1], 2)
    print Solution().subarraySum([1, 1, 1], 5)
    print Solution().subarraySum([-1, 1, 0], 0)
    print Solution().subarraySum([-1, 0, 1], 0)
