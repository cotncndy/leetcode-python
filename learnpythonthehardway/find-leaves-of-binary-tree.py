# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def helper(root, result):
            if not root:
                return -1

            depth = 1 + max(helper(root.left, result), helper(root.right, result))
            if len(result) < depth + 1:
                result.append([])
            result[depth] += root.val,
            return depth

        res = []
        helper(root, res)
        return res
