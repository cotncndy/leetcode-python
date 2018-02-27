#  Given a list of non-negative numbers and a target integer k, write a function to check if the array has a
# continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also
# an integer.
#
# Example 1:
#
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
#
# Example 2:
#
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
#
# Note:
#
#     The length of the array won't exceed 10,000.
#     You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
import collections


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False

        sum = [0] * len(nums)

        for key, val in enumerate(nums):
            sum[key] = sum[key - 1] + val
            if key > 0 and self.isMulitple(sum[key], k):
                return True
            if key > 1:
                for i in xrange(key - 1):
                    if self.isMulitple(sum[key] - sum[i], k):
                        return True

        return False

    def isMulitple(self, n, k):
        if n == 0 and k == 0:
            return True
        if n != 0 and k == 0:
            return False
        return n % k == 0


if __name__ == '__main__':
    # print Solution().checkSubarraySum([23, 2, 4, 6, 7], 8)
    # print Solution().checkSubarraySum([23, 2, 4, 6, 7], 6)
    # print Solution().checkSubarraySum([23, 2, 6, 4, 7], 6)
    print Solution().checkSubarraySum([23, 2, 6, 4, 7], 0)
    # print Solution().checkSubarraySum([1,2,-2,-1], 0)
    # print Solution().checkSubarraySum([2,-2], 1)
