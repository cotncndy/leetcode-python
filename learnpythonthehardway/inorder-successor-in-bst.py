# Time:  O(h)
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        res = None
        while root:
            if root.val > p.val:
                res = root
                root = root.left
            else:
                root = root.right

        return res
