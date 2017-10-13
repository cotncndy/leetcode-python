# Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k
# that has the maximum average value. And you need to output the maximum average value.
#
# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation:
# when length is 5, maximum average value is 10.8,
# when length is 6, maximum average value is 9.16667.
# Thus return 12.75.
# Note:
# 1 <= k <= n <= 10,000.
# Elements of the given array will be in range [-10,000, 10,000].
# The answer with the calculation error less than 10-5 will be accepted.


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        def check(nums, k, x):
            a = [0] * len(nums)
            for i, n in enumerate(nums):
                a[i] = n - x

            now, last = 0, 0
            for i in xrange(0, k):
                now += a[i]

            if now > 0:
                return True
            for i in xrange(k, len(nums)):
                now, last = now + a[i], last + a[i - k]
                if (last < 0):
                    now -= last
                    last = 0
                if now > 0:
                    return True

            return False

        l, r = -2 << 31, 2 << 31
        while (r - l > 0.000005):
            mid = (l + r) / 2.0
            t = check(nums, k, mid)
            if t:
                l = mid
            else:
                r = mid

        return (l + r) / 2.0  # return r is also ok.



if __name__ == '__main__':
    print Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4)
