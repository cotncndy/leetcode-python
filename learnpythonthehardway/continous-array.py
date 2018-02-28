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

        res, st1, st0 = 1, [], []

        for k, v in enumerate(nums):
            if not st1:
                st1.append(k)
            elif (v == 1 and nums[st1[-1]] == 0) or (v == 0 and nums[st1[-1]] == 1):
                st0.append(st1.pop())
                st0.append(k)
            else:
                st1.append(k)

        st0.sort()

        temp = 1
        for i in xrange(1, len(st0)):
            if st0[i] == st0[i - 1] + 1:
                temp += 1
                res = max(res, temp)
            else:
                temp = 1

        return res


if __name__ == '__main__':
    # print Solution().findMaxLength([0, 1])
    # print Solution().findMaxLength([0, 1, 0])
    # print Solution().findMaxLength([0, 0, 0, 1, 1, 0, 1, 1, 0, 0])
    # print Solution().findMaxLength([0, 0, 0, 1, 1, 0, 1, 1, 0, 1])
    # print Solution().findMaxLength([0, 1, 1, 0, 1, 1, 1, 0])
    print Solution().findMaxLength([0, 0, 1, 0, 0, 0, 1, 1])
