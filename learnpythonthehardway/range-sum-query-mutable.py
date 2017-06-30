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


# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)
# review Segment Tree solutoin.

class NumArray2(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        # Build segment tree.
        self.__nums = nums

        def builderHelper(nums, start, end):
            if start > end:
                return None
            # the root's start and end is given by builder
            root = self._SegmentTreeNode(start, end, 0)

            # If start equals to end, there will be no children for this node.
            if start == end:
                root.sum = nums[start]
                return root

            # Left child: start=nums.left, end=(nums.left + nums.right) / 2.
            root.left = builderHelper(nums, start, (start + end) / 2)

            # Right child: start=(nums.left + nums.right) / 2 + 1, end=nums.right.
            root.right = builderHelper(nums, (start + end) / 2 + 1, end)

            # Update sum.
            root.sum = (root.left.sum if root.left else 0) + \
                       (root.right.sum if root.right else 0)

            return root

        self.__root = builderHelper(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """

        def updateHelper(root, i, val):
            # Out of range.
            if not root or root.start > i or root.end < i:
                return

            # Change the node's value with [i] to the new given value.
            if root.start == i and root.end == i:
                root.sum = val
                return

            updateHelper(root.left, i, val)
            updateHelper(root.right, i, val)

            # Update sum.
            root.sum = (root.left.sum if root.left else 0) + \
                       (root.right.sum if root.right else 0)

        if self.__nums[i] != val:
            self.__nums[i] = val
        updateHelper(self.__root, i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        def sumRangeHelper(root, start, end):
            # out of range
            if not root or root.start > end or root.end < start:
                return 0
            if root.start >= start and root.end <= end:
                return root.sum
            return sumRangeHelper(root.left, start, end) + \
                   sumRangeHelper(root.right, start, end)

        return sumRangeHelper(self.__root, i, j)

    # review the usage of inner class in python https://stackoverflow.com/questions/719705/what-is-the-purpose-of-pythons-inner-classes
    class _SegmentTreeNode:
        def __init__(self, i, j, s):
            self.start, self.end, self.sum = i, j, s




if __name__ == '__main__':
    abc = NumArray2([1, 3, 5])
    print abc.sumRange(0, 0)
