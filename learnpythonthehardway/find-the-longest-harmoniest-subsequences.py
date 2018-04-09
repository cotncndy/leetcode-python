# We define a harmonious array is an array where the difference between its maximum value and its minimum value is
# exactly 1.
#
# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its
# possible subsequences.
#
# Example 1:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Note: The length of the input array will not exceed 20,000.
import collections


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = collections.defaultdict(int)
        for n in nums:
            m[n] += 1

        res = 0
        keys = m.keys()
        for k in keys:
            if k - 1 in keys:
                res = max(res, m[k] + m[k - 1])

        return res


if __name__ == '__main__':
    print Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7])
