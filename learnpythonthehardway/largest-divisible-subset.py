# Time:  O(n^2)
# Space: O(n)

# Given a set of distinct positive integers,
# find the largest subset such that every pair (Si, Sj) of
# elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
#
# nums: [1,2,3]
#
# Result: [1,2] (of course, [1,3] will also be ok)
# Example 2:
#
# nums: [1,2,4,8]
#
# Result: [1,2,4,8]

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()

        dp = [1] * len(nums)
        prev = [-1] * len(nums)

        res, maxIdx = [], 0
        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < 1 + dp[j]:
                        dp[i] = 1 + dp[j]
                        prev[i] = j

                if dp[maxIdx] < dp[i]:
                    maxIdx = i

        while maxIdx != -1:
            res.append(nums[maxIdx])
            maxIdx = prev[maxIdx]

        return res[::-1]

    def largestDivisibleSubset2(self, nums):  # todo , try to understand
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {-1: set()}
        for i in sorted(nums):
            dict[i] = max((dict[d] for d in dict if i % d == 0), key=len) | {i}

        return list(max(dict.values(), key=len))
