# Given a binary tree where every node has a unique value, and a target key k, find the value of the closest leaf
# node to target k in the tree.
#
# Here, closest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree.
#  Also, a node is called a leaf if it has no children.
#
# In the following examples, the input tree is represented in flattened form row by row. The actual root tree given
# will be a TreeNode object.
#
# Example 1:
#
# Input:
# root = [1, 3, 2], k = 1
# Diagram of binary tree:
#           1
#          / \
#         3   2
#
# Output: 2 (or 3)
#
# Explanation: Either 2 or 3 is the closest leaf node to the target of 1.
# Example 2:
#
# Input:
# root = [1], k = 1
# Output: 1
#
# Explanation: The closest leaf node is the root node itself.
# Example 3:
#
# Input:
# root = [1,2,3,4,null,null,null,5,null,6], k = 2
# Diagram of binary tree:
#              1
#             / \
#            2   3
#           /
#          4
#         /
#        5
#       /
#      6
#
# Output: 3
# Explanation: The leaf node with value 3 (and not the leaf node with value 6) is closest to the node with value 2.
# Note:
# root represents a binary tree with at least 1 node and at most 1000 nodes.
# Every node has a unique node.val in range [1, 1000].
# There exists some node in the given binary tree for which node.val == k.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.target = None
        self.res = None
        self.step = float('inf')

    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root.val == k:
            return 0
        self.traverse(root, k)

        return self.res.val

    def traverse(self, root, k):
        left, right, root1, root2 = float('inf'), float('inf'), None, None
        if root.left:
            left, root1 = self.traverse(root.left, k)
            left += 1
        if root.right:
            right, root2 = self.traverse(root.right, k)
            right += 1

        if not root.left and not root.right:
            return 0, root
        if root.val == k:
            self.target = root
            self.step = min(left, right)
            self.res = root1 if left < right else root2
        elif self.target and root.left == self.target:
            self.step = min(self.step, left - 1, right + 1)
            if self.step == left - 1:
                self.res = root1
            elif self.step == right + 1:
                self.res = root2
        elif self.target and root.right == self.target:
            self.step = min(self.step, right - 1, left + 1)
            if self.step == right - 1:
                self.res = root2
            elif self.step == left + 1:
                self.res = root1

        can = root1 if left < right else root2
        return min(left, right), can


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.left.left.left.left = TreeNode(6)
    print Solution().findClosestLeaf(root, 2)
