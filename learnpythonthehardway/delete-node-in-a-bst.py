# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node
#  reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).
#
# Example:
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Given key to delete is 3. So we find the node with value 3 and delete it.
#
# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
#
#     5
#    / \
#   4   6
#  /     \
# 2       7
#
# Another valid answer is [5,2,6,null,4,null,7].
#
#     5
#    / \
#   2   6
#    \   \
#     4   7


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root

        def findSuccessor(node):
            if not node.right:
                return None
            cur, prev = node.right, node.right
            while cur.left:
                prev, cur = cur, cur.left
            prev.left = None
            if prev == cur:  # bugfixed node.right is successor
                node.right = cur.right  # bugfixed cur.right might not be null

            return cur

        if root.val == key:
            succ = findSuccessor(root)
            if not succ:
                return root.left
            succ.left, succ.right = root.left, root.right
            return succ
        cur, p = root, root
        while cur and cur.val != key:
            p = cur
            if cur.val < key:
                cur = cur.right
            else:
                cur = cur.left
        if not cur:  # bugfixed no such key in tree
            return root
        succ = findSuccessor(cur)

        if p.left == cur:
            p.left = succ if succ else cur.left
        else:
            p.right = succ if succ else cur.right

        if succ:
            succ.left, succ.right = cur.left, cur.right
        return root


if __name__ == '__main__':
    root = TreeNode(18)
    node1, node2 = TreeNode(10), TreeNode(20)
    root.left, root.right = node1, node2
    node3, node4 = TreeNode(8), TreeNode(16)
    node1.left, node1.right = node3, node4
    node5 = TreeNode(14)
    node4.left = node5
    node6, node7 = TreeNode(12), TreeNode(13)
    node5.left, node5.right = node6, node7
    # root.left = TreeNode(2)
    # n_root = Solution().deleteNode(root, 9)
    root = TreeNode(3)
    n_root = Solution().deleteNode(root, 2)
    print n_root
