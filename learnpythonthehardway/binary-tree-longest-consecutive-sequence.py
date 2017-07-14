# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_len = 0

        def helper(root):
            if not root:
                return 0
            left, right = helper(root.left), helper(root.right)

            curr = 1
            if root.left and root.left.val == root.val + 1:
                curr = max(curr, left + 1)
            if root.right and root.right.val == root.val + 1:
                curr = max(curr, right + 1)

            self.max_len = max(self.max_len, curr)
            return curr

        helper(root)
        return self.max_len
