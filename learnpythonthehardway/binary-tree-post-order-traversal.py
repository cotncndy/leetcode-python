# Given a binary tree, return the postorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        st, prev, res = [root], root, []
        while st:
            top = st[-1]
            if (top.left is None and top.right is None) or top.left == prev or top.right == prev:
                res.append(top)
                prev = top
                st.pop()  # bugfixed
            elif top.right is not None:
                res.append(top.right)
            elif top.left is not None:
                res.append(top.left)

        return res
