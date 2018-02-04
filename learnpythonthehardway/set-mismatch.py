# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in
# the set got duplicated to another number in the set, which results in repetition of one number and loss of another
# number.
#
# Given an array nums representing the data status of this set after the error. Your task is to firstly find the
# number occurs twice and then find the number that is missing. Return them in the form of an array.
#
# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Note:
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        or_1, or_2, s, t1, t2 = 0, 0, set(), -1, -1
        for n in xrange(1, len(nums) + 1):
            or_1, or_2 = or_1 ^ nums[n - 1], or_2 ^ n
            if nums[n - 1] in s:
                t1 = nums[n - 1]
            s.add(nums[n - 1])

        t2 = t1 ^ (or_1 ^ or_2)
        return [t1, t2]


if __name__ == '__main__':
    print Solution().findErrorNums([1, 2, 2, 4])
    print Solution().findErrorNums([1, 2, 3, 3, 4, 6])
