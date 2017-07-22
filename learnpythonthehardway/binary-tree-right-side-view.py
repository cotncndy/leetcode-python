# Time:  O(n)
# Space: O(h)
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers
    # review dfs , really smart traversal
    def rightSideView(self, root):
        res = []
        self.dfs_traversal(root, 1, res)
        return res

    def dfs_traversal(self, root, depth, res):
        if not root:
            return res
        if len(res) < depth:
            res.append(root.val)
        self.dfs_traversal(root.right, depth + 1, res)  # review firstly from right, then left
        self.dfs_traversal(root.left, depth + 1, res)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    result = Solution().rightSideView(root)
    print result
