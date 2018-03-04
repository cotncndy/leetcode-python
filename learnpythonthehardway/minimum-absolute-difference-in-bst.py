# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two
#  nodes.
#
# Example:
#
# Input:
#
#    1
#     \
#      3
#     /
#    2
#
# Output:
# 1
#
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
#
# Note: There are at least two nodes in this BST.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    res = 0

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inorder(root)

        return self.res

    def inorder(self, root):
        if root and not root.left and not root.right:
            return root

        min1, min2, min3, min4 = float('inf'), float('inf'), float('inf'), float('inf')
        if root.left:
            left = self.inorder(root.left)
            min1 = root.val - left.val
            min2 = root.val - root.left.val

        if root.right:
            right = self.inorder(root.right)
            min3 = right.val - root.val
            min4 = root.right.val - root.val
        self.res = min(self.res, min1, min2, min3, min4)

        return root


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    print Solution().getMinimumDifference(root)
