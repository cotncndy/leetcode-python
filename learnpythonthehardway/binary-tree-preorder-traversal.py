# Time:  O(n)
# Space: O(1)
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        st, res = [], []
        while st or root:
            if root:
                res.append(root.val)
                if root.right:
                    st.append(root.right)
                root = root.left
            else:
                root = st.pop()
        return res

    def preorderTraversal2(self, root):
        st, res = [], []
        if root is None:
            return res

        st.append(root)
        while st:
            node = st.pop()
            res.append(node.val)
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)

        return res

    # morris traversal
    def preorderTraversal3(self, root):
        cur, res = root, []

        while cur:
            if cur.left is None:
                res.append(cur.val)
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right
                if node.right is None:
                    res.append(cur.val)
                    node.right = cur
                    cur = cur.left
                else:
                    node.right = None
                    cur = cur.right
        return res
