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
    res = float('inf')

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inorder(root, [])

        return self.res

    def inorder(self, root, arr):

        if not root:
            return

        self.inorder(root.left, arr)
        if not arr:
            arr.append(root.val)
        else:
            self.res = min(self.res, root.val - arr.pop())
            arr.append(root.val)
        self.inorder(root.right, arr)



if __name__ == '__main__':
    root = TreeNode(236)
    root.left, root.right = TreeNode(104), TreeNode(701)
    root.left.right = TreeNode(227)
    root.right.right = TreeNode(911)
    print Solution().getMinimumDifference(root)
