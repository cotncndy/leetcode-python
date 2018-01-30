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

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals, res = collections.deque(), ""
        if not root:
            return res
        vals.append(root)

        while vals:
            t = vals.popleft()
            if t:
                res += str(t.val)
                vals.append(t.left)
                vals.append(t.right)
            else:
                res += '#'

        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        vals = collections.deque(val for val in data)
        root = TreeNode(int(vals.popleft()))
        cur, que = root, collections.deque()
        que.append(cur)

        while vals:
            t = vals.popleft()
            cur = que.popleft()
            if t != '#':
                node = TreeNode(int(t))
                cur.left = node
                que.append(node)
            t = vals.popleft()
            if t != '#':
                node = TreeNode(int(t))
                cur.right = node
                que.append(node)

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    root = TreeNode(2)
    root.right = TreeNode(3)
    codec = Codec()
    print codec.deserialize(codec.serialize(root))
