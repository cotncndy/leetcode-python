# Time:  O(h)
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res = root.val
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val
            elif target == root.val:
                break;
            root = root.left if target < root.val else root.right

        return res
