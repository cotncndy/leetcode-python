# Time:  O(n * s), s is the sum of nums
# Space: O(s)

# Given a non-empty array containing only positive integers,
# find if the array can be partitioned into two subsets
# such that the sum of elements in both subsets is equal.
#
# Note:
# Both the array size and each of the array element will not exceed 100.
#
# Example 1:
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.
import collections
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)  # knowledge there is a sum function in python
        counter = collections.Counter(nums)
        if s % 2:
            return False

        dp = [False] * (s / 2 + 1)
        dp[0] = True

        for num in nums:
            for i in xrange(1, len(dp)):
                if num <= i:  # bugfixed
                    dp[i] = dp[i] or dp[i - num] if i != 2 * num else (dp[i - num] and counter[num] > 1)  # bugfixed

        return dp[-1]


if __name__ == '__main__':
    print Solution().canPartition([1, 2, 5])
