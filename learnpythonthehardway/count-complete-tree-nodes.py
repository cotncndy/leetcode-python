# Time:  O(h * logn) = O((logn)^2)
# Space: O(1)

# Given a complete binary tree, count the number of nodes.
#
# In a complete binary tree every level, except possibly the last,
# is completely filled, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2h nodes inclusive at
# the last level h.
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
    n = 1

    def countNodes(self, root):
        if not root:
            return 0
        depth = self.get_depth(root)
        self.count(root, depth)

        return self.n

    def get_depth(self, root):
        depth = 0
        while root:
            depth, root = depth + 1, root.left
        return depth

    def count(self, root, depth):
        if depth == 1:
            return

        if self.get_depth(root.right) == depth - 1:
            self.n = self.n * 2 + 1
            self.count(root.right, depth - 1)
        if self.get_depth(root.left) == depth - 1:
            n *=
            self.count(root.left, depth - 1)
