# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
# stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the
#  same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be
# serialized to a string and this string can be deserialized to the original tree structure.
#
# The encoded string should be as compact as possible.
#
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms
# should be stateless.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Codec:
    # preorder + inorder traversal can uiquely define one tree
    # but for BST, preorder can uniquely define the tree
    # for BST, inorder can be obtained by just sorting preorder or postorder
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        tree = ""
        if not root:
            return tree

        def preorder(root, val):
            if root:
                val.append(str(root.val))
                preorder(root.left, val)
                preorder(root.right, val)

        v = []
        preorder(root, v)
        return ' '.join(v)  # use space as splitter

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(int(val) for val in data.split())

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()  # m-l-r
                node = TreeNode(val)
                node.left = build(minVal,
                                  val)  # since every middle node will pop out, the left tree will gone before
                # operate the right one
                node.right = build(val, maxVal)
                return node

        return build(float('-infinity'), float('infinity'))

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))
