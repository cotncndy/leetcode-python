# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, find the maximum path sum.
#
# The path may start and end at any node in the tree.
#
# For example:
# Given the below binary tree,
#
#        1
#       / \
#      2   3
# Return 6.
#
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    maxSum = float("-inf")  # define a class level variable

    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maxPathFinder(root)

        return self.maxSum

    def maxPathFinder(self, root):
        if not root:
            return 0
        left = max(0, self.maxPathFinder(root.left))
        right = max(0, self.maxPathFinder(root.right))
        self.maxSum = max(self.maxSum, left + root.val + right)
        return root.val + max(left, right)
