# Time:  O(n)
# Space: O(logn)
#
# Given an array where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return self.helper(num, 0, len(num) - 1)

    def helper(self, num, left, right):
        if left > right:
            return None
        mid = (left + right) / 2
        curr = TreeNode(num[mid])
        curr.left = self.helper(left, mid - 1)
        curr.right = self.helper(mid + 1, right)

        return curr
