# Time:  O(n * h)
# Space: O(h)
#
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#   1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res = []
        if root:
            self.dfs(root, '', res)
        return res

    def dfs(self, root, out, res):
        out += str(root.val)

        if not root.left and not root.right:
            res.append(out)
            return
        if root.left:
            self.dfs(root.left, out + "->", res)
        if root.right:
            self.dfs(root.right, out + "->", res)
