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
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
            self.n = self.n * 2 + 1  # notice how to reference the instance variales
            self.count(root.right, depth - 1)
        elif self.get_depth(root.left) == depth - 1:  # bugfixed should be elif instead of if
            self.n *= 2
            self.count(root.left, depth - 1)

    def countNodes2(self, root):
        left_h, right_h = self.left_heigt(root), self.right_height(
            root)  # bugfixed use root instead of root.left an droot.right
        if left_h == right_h:
            return 2 ** left_h - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def left_heigt(self, root):
        if not root:
            return 0
        return 1 + self.left_heigt(root.left)

    def right_height(self, root):
        if not root:
            return 0
        return 1 + self.right_height(root.right)



if __name__ == '__main__':
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(3)
    print Solution().countNodes(root)
