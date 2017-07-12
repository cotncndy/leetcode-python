# Time:  O(n)
# Space: O(1)
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Morris Traversal Solution
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def isValidBST(self, root):
        if root is None:
            return True
        prev, st = None, []
        while root != None or len(st) > 0:
            if root:
                st.append(root)
                root = root.left
            else:
                curr = st.pop()
                if prev:
                    if prev.val >= curr.val:  # bugfixed don't forget >=
                        return False
                prev = curr  # bugfixed, no need else,otherwise there is no udpate for 'if' block
                root = curr.right
        return True
