# Time:  O(n)
# Space: O(1)
#
# Note: This is an extension of House Robber.
#
# After robbing those houses on that street, the thief has found himself a new place
# for his thievery so that he will not get too much attention. This time, all houses
# at this place are arranged in a circle. That means the first house is the neighbor
# of the last one. Meanwhile, the security system for these houses remain the same as
# for those in the previous street.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
#
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_range(nums, left, right):
            last, now = 0, 0
            for i in xrange(left, right):
                last, now = now, max(last + nums[i], now)

            return now

        return max(rob_range(nums, 0, len(nums) - 1), rob_range(nums, 1, len(nums)))  # bugfixed


if __name__ == '__main__':
    print Solution().rob([1, 3, 7, 2])
