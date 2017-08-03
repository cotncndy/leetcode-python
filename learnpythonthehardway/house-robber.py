# Time:  O(n)
# Space: O(1)
#
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
#
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if len(num) == 0:
            return 0
        if len(num) == 1:
            return num[0]

        num_cur, num_prev_1 = max(num[1], num[0]), num[0]
        for i in xrange(2, len(num)):
            num_prev_1, num_prev_2 = num_cur, num_prev_1
            num_cur = max(num_prev_1, num_prev_2 + num[i])

        return num_cur

    def rob2(self, num):
        last, now = 0, 0
        for i in num:
            last, now = now, max(last + i, now)

        return now


if __name__ == '__main__':
    print Solution().rob2([1, 3, 7, 2])
