# Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:
#
# 0 < i, i + 1 < j, j + 1 < k < n - 1
# Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
# where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.
# Example:
# Input: [1,2,1,2,1,2,1]
# Output: True
# Explanation:
# i = 1, j = 3, k = 5.
# sum(0, i - 1) = sum(0, 0) = 1
# sum(i + 1, j - 1) = sum(2, 2) = 1
# sum(j + 1, k - 1) = sum(4, 4) = 1
# sum(k + 1, n - 1) = sum(6, 6) = 1
# Note:
# 1 <= n <= 2000.
# Elements in the given array will be in range [-1,000,000, 1,000,000].


class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 7:
            return False

        n = len(nums)

        sum = [nums[0]] * n
        for i in xrange(1, n):
            sum[i] = sum[i - 1] + nums[i]

        for j in xrange(3, n - 3):
            sums = set()
            for i in xrange(1, j):
                if sum[i - 1] == sum[j - 1] - sum[i]:
                    sums.add(sum[i - 1])

            for k in xrange(j + 1, n - 1):
                s = sum[k - 1] - sum[j]
                if s == sum[n - 1] - sum[k]:
                    if s in sums:
                        return True

        return False
