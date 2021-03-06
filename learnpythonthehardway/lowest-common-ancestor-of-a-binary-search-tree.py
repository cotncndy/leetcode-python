# Time:  O(n)
# Space: O(1)
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA)
# of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes v and w as the lowest node in T that has both v
# and w as descendants (where we allow a node to be a descendant of itself).”
#
#         _______6______
#       /              \
#     ___2__          ___8__
#   /      \        /      \
#   0      _4       7       9
#          /  \
#          3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
# Another example is LCA of nodes 2 and 4 is 2, since a node can be a
# descendant of itself according to the LCA definition.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):  # review too NB , really need to remember this method
        s, b = sorted([p.val, q.val])  # bugfixed

        while not s <= root.val <= b:
            root = root.left if s <= root.val else root.right  # review so cool

        return root

    def lowestCommonAncestor2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        s, b = sorted([p.val, q.val])

        while not s <= root.val <= b:
            root = root.left if b <= root.val else root.right  # review so cool, replace s <= root.val with b <=
            # root.val, performance the same 122ms, 65%

        return root

    def lowestCommon(self, root, p, q):
        if root.val > q.val and root.val > p.val:
            return self.lowestCommon(root.left, p, q)
        if root.val < q.val and root.val < p.val:
            return self.lowestCommon(root.right, p, q)
        else:
            return root
