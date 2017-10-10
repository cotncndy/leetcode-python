# Given an array of integers, every element appears three times except for one, which appears exactly once. Find that
#  single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, bit_mask = 0, 1
        for i in xrange(32):
            s = 0
            for j in nums:
                s += (j & bit_mask)
            res += (s % 3) << i  # bugfixed
            bit_mask <<= 1
        return res


if __name__ == '__main__':
    # print Solution().singleNumber([1])
    print Solution().singleNumber([0, 0, 0, 5])
