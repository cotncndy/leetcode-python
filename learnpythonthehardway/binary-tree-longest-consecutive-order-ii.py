# Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.
#
# Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both
# considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child
#  order, where not necessarily be parent-child order.
#
# Example 1:
# Input:
#         1
#        / \
#       2   3
# Output: 2
# Explanation: The longest consecutive path is [1, 2] or [2, 1].
# Example 2:
# Input:
#         2
#        / \
#       1   3
# Output: 3
# Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
# Note: All the values of tree nodes are in the range of [-1e7, 1e7].


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):  # review wonderful recursion problem. so good.
        """
        :type root: TreeNode
        :rtype: int
        """
        max_len = [0]

        def helper(root, parent):
            if not root:
                return 0, 0
            left_desc, left_inc = helper(root.left, root)
            right_desc, right_inc = helper(root.right, root)

            max_len[0] = max(max_len[0], left_desc + right_inc + 1)
            max_len[0] = max(max_len[0], right_desc + left_inc + 1)

            inc, desc = 0, 0
            if root.val == parent.val + 1:
                inc = max(left_inc, right_inc) + 1
            if root.val == parent.val - 1:
                desc = max(left_desc, right_desc) + 1

            return desc, inc

        helper(root, root)

        return max_len[0]

    def longestConsecutive2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global l  # knowledge usage of global
        l = 0

        def dfs(node, parent):
            global l
            if not node: return 0, 0
            li, ld = dfs(node.left, node)
            ri, rd = dfs(node.right, node)
            l = max(l, li + 1 + rd, ld + 1 + ri)
            if node.val == parent.val + 1:
                return max(li, ri) + 1, 0
            if node.val == parent.val - 1:
                return 0, max(ld, rd) + 1
            return 0, 0

        dfs(root, root)
        return l

    def longestConsecutive3(self, root):
        self.max_len = 0

        def dfs(node, parent):
            if not node:
                return 0, 0
            li, ld = dfs(node.left, node)
            ri, rd = dfs(node.right, node)

            self.max_len = max(self.max_len, li + 1 + rd, ld + 1 + ri)
            if node.val == parent.val + 1:
                return max(li, ri) + 1, 0
            if node.val == parent.val - 1:
                return 0, max(ld, rd) + 1  # bugfixed

            return 0, 0

        dfs(root, root)

        return self.max_len
