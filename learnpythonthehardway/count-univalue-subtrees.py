# Time:  O(n)
# Space: O(h)
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    count = 0

    def countUnivalSubtrees(self, root):
        self.isUni(root, root.val)
        return self.count

    def isUni(self, root, val):
        if not root:
            return True  # leaf is uni-tree

        if not self.isUni(root.left, root.val) or not self.isUni(root.right, root.val):
            return False

        self.count += 1
        return root.val == val
