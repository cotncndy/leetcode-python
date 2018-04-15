# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees
# are overlapped while the others are not.
#
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up
#  as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
#
# Example 1:
# Input:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# Output:
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7
# Note: The merging process must start from the root nodes of both trees.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        def preorder(r1, r2):
            if r1 and r2:
                r = TreeNode(r1.val + r2.val)
                r.left = preorder(r1.left, r2.left)
                r.right = preorder(r1.right, r2.right)
            elif r1:
                r = TreeNode(r1.val)
                r.left = preorder(r1.left, None)
                r.right = preorder(r1.right, None)
            elif r2:
                r = TreeNode(r2.val)
                r.left = preorder(None, r2.left)
                r.right = preorder(None, r2.right)
            else:
                return None

            return r

        return preorder(t1, t2)


