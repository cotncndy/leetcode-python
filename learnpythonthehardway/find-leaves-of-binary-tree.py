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

    def findLeaves2(self, root):
        def remove(root, leaves):
            if not root:
                return None
            if not root.left and not root.right:
                leaves += root.val,
                return None
            root.left, root.right = remove(root.left, leaves), remove(root.right, leaves)
            return root

        res = []
        while root:
            leaves = []
            remove(root, leaves)
            res.append(leaves)

        return res
