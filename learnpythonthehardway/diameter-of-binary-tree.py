# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is
# the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    res = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.traverse(root)
        return self.res - 1

    def traverse(self, root):
        if not root:
            return (0, 0)  # first is path include root, second is the max of left , or right path
        p1, p2 = self.traverse(root.left)
        p3, p4 = self.traverse(root.right)
        self.res = max(p1, p3, p2 + p4 + 1, self.res)  # bugfixed, forgot self.res
        return (p2 + p4 + 1, max(p2, p4) + 1)


if __name__ == '__main__':
    root, node = TreeNode(4), TreeNode(2)
    node.left, node.right = TreeNode(1), TreeNode(3)
    root.left = node

    print Solution().diameterOfBinaryTree(root)
