# Time:  O(n)
# Space: O(h)

# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#   / \
#   9  20
#     /  \
#   15   7
#
# There are two left leaves in the binary tree,
# with values 9 and 15 respectively. Return 24.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root, is_left):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val if is_left else 0
            return helper(root.left, True) + helper(root.right, False)

        return helper(root, False)  # bugfixed, forget to pass in parameter
