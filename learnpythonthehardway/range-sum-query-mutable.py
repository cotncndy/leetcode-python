# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)

# Given an integer array nums, find the sum of
# the elements between indices i and j (i <= j), inclusive.
#
# The update(i, val) function modifies nums by
# updating the element at index i to val.
# Example:
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:
# The array is only modifiable by the update function.
# You may assume the number of calls to update
# and sumRange function is distributed evenly.

# review Binary Indexed Tree (BIT) solution.
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if not nums:
            return
        self.__num = [0] * (len(nums) + 1)
        self.__bit = [0] * (len(nums) + 1)  # review how to initialize 1-dimension array
        for i in xrange(len(nums)):
            self.update(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - self.__num[i]
        self.__num[i] = val
        i += 1
        while i < len(self.__num):
            self.__bit[i] += diff
            i += (i & -i)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getSum(j + 1) - self.getSum(i)

    def getSum(self, i):
        res = 0
        while i:
            res += self.__bit[i]
            i -= (i & -i)
        return res


if __name__ == '__main__':
    abc = NumArray([1, 3, 5])
    print abc.sumRange(0, 2)
