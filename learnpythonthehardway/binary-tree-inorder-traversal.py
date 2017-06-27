# Time:  O(n)
# Space: O(1)
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#   1
#    \
#     2
#    /
#   3
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Morris Traversal Solution
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
