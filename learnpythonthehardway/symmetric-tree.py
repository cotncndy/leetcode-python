# Time:  O(n)
# Space: O(h), h is height of binary tree
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Iterative solution
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        stack = []

        stack.append(root.left)
        stack.append(root.right)

        while stack:
            p, q = stack.pop(), stack.pop()
            if p is None and q is None:
                continue
            if p is None or q is None or p.val != q.val:
                return False
            stack.append(p.left)
            stack.append(q.right)

            stack.append(p.right)
            stack.append(q.left)

        return True


if __name__ == "__main__":
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(3)
    # root.left.left, root.right.right = TreeNode(3), TreeNode(3)
    # root.left.right, root.right.left = TreeNode(4), TreeNode(4)
    print Solution().isSymmetric(root)
