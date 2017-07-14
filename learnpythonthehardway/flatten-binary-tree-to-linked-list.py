# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, flatten it to a linked list in-place.
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    prev = None
    def flatten(self, root):
        if root != None:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.prev
            root.left = None
            self.prev = root
            return root

    def flattern2(self, root):
        if not root:
            return
        if root.left:
            self.flattern2(root.left)
        if root.right:
            self.flattern2(root.right)
        temp = root.right
        root.right = root.left
        root.left = None  # bugfixed root.left need to point to null
        while root.right:
            root = root.right
        root.right = temp
        return root



if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    result = Solution().flatten(root)
    print result.val
    print result.right.val
    print result.right.right.val
    print result.right.right.right.val
    print result.right.right.right.right.val
    print result.right.right.right.right.right.val

