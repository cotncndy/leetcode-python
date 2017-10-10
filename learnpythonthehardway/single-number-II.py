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
                j >>= i  # bugfixed
                s += (j & bit_mask)
                # deal with the negative situation
            if i == 31 and s % 3:
                res -= 1 << 31  # knowledge in python , by default, number could be infinity, so it won't use
                # '0' or '1' to differentiate positive or negative number, so we need to manually handle it.
            res |= (s % 3) << i  # bugfixed
        return res

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x1 = x2 = 0
        for n in nums:
            x2 ^= (x1 & n)
            x1 ^= n
            mask = ~(x1 & x2)
            x1 &= mask
            x2 &= mask
        return x1


if __name__ == '__main__':
    # print Solution().singleNumber([1])
    print Solution().singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2])
