# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        res.append(root.val)
        self.searchLeft(root.left, True, res)
        self.searchRight(root.right, True, res)
        return res

    def searchLeft(self, root, is_edge, res):
        if not root:
            return
        if (is_edge or (not root.left and not root.right)):
            res.append(root.val)
        self.searchLeft(root.left, is_edge, res)
        self.searchLeft(root.right, True if is_edge and not root.left else False, res)

    def searchRight(self, root, is_edge, res):
        if not root:
            return
        self.searchRight(root.right, is_edge, res)
        self.searchRight(root.left, True if is_edge and not root.right else False, res)
        if (is_edge or (not root.left and not root.right)):
            res.append(root.val)


class Solution2(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def findEdge(root, left, right, flag):
            if not root:
                return
            if (flag <= 1 or (not root.left and not root.right)):
                left.append(root.val)
            elif flag == 2:
                right.insert(0, root.val)

            findEdge(root.left, left, right, 1 if (flag <= 1) else (2 if (flag == 2 and not root.right) else 3))
            findEdge(root.right, left, right, 2 if (flag % 2 == 0) else (1 if (flag == 1 and not root.left) else 3))

        left, right = [], []
        findEdge(root, left, right, 0)
        left.extend(right)

        return left
