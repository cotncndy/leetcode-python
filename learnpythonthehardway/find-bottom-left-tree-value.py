#  Given a binary tree, find the leftmost value in the last row of the tree.
#
# Example 1:
#
# Input:
#
#     2
#    / \
#   1   3
#
# Output:
# 1
#
# Example 2:
#
# Input:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
#
# Output:
# 7
#
# Note: You may assume the tree (i.e., the given root node) is not NULL.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        que, mostLeft = collections.deque(), -1
        que.append(root)
        while que:
            s = len(que)
            for i in xrange(s):
                node = que.popleft()
                if i == 0:
                    mostLeft = node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        return mostLeft

    maxDepth = 1
    res = None
    def findBottomLeftValue2(self, root):  # how to do it recursively
        def helper(root, depth):
            if not root:
                return
            if depth > self.maxDepth:
                self.res = root
                self.maxDepth = depth
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        self.res = root
        helper(root, 1)
        return self.res.val
