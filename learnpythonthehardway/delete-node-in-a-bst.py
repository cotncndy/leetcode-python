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
        if not root or (root.left == None and root.right == None):
            return root

        def findSuccessor(node):
            if not node.right:
                return None
            cur = node.right
            while cur.left:
                prev, cur = cur, cur.left
            prev.next = None

            return cur

        if root.val == key:
            succ = findSuccessor(root)
            succ.left, succ.right = root.left, root.right
            return succ
        cur, p = root, root
        while cur and cur.val != key:
            p = cur
            if cur.val < key:
                cur = cur.right
            else:
                cur = cur.left

        succ = findSuccessor(cur)

        if p.left == cur:
            p.left = succ
        else:
            p.right = succ

        if succ:
            succ.left, succ.right = cur.left, cur.right

        return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    print Solution().deleteNode(root, 4)
