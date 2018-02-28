# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
# Example 1:
#
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
#
# Example 2:
#
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#
# Note: The length of the given binary array will not exceed 50,000.

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res, st1, st0 = 0, [], []

        for k, v in enumerate(nums):
            if v == 1:
                st1.append(v)
            else:
                st0.append(v)
            res = min(len(st0), len(st1))

        return res * 2


if __name__ == '__main__':
    print Solution().findMaxLength([0, 1])
    print Solution().findMaxLength([0, 1, 0])
    print Solution().findMaxLength([0, 0, 0, 1, 1, 0, 1, 1, 0, 0])
    print Solution().findMaxLength([0, 0, 0, 1, 1, 0, 1, 1, 0, 1])
