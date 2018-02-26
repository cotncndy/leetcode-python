# You need to find the largest value in each row of a binary tree.
#
# Example:
#
# Input:
#
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
#
# Output: [1, 3, 9]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        que, res = [], []
        que.append(root)
        while que:
            l, lMax = len(que), float('-inf')
            for i in xrange(l):
                n = que.pop(0)
                lMax = max(lMax, n.val)
                if n.left:
                    que.append(n.left)
                if n.right:
                    que.append(n.right)
            res.append(lMax)

        return res
