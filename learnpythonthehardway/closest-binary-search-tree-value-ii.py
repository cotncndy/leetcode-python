# Time:  O(h + k)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        res = []
        self.inorder(root, target, k, res)

        return res

    def inorder(self, root, target, k, res):
        if not root:
            return
        self.inorder(root, target, k, res)
        if len(res) < k:
            res.append(root.val)
        else:
            if abs(target - res[0]) > abs(target - root.val):
                res.pop(0)
                res.append(root.val)
            else:
                return
        self.inorder(root, target, k, res)

    def closestKvalues2(self, root, target, k):
        stack, res = [], []
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        if len(res) < k:
            res.append(root.val)
        else:
            if abs(root.val - target) < abs(res[0] - target):
                res.pop(0)
                res.append(root.val)
        root = root.right

        return res
