# Time:  O(n)
# Space: O(h)

# Serialization is the process of converting a data structure or
# object into a sequence of bits so that it can be stored in a file
# or memory buffer, or transmitted across a network connection link
# to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization
# algorithm should work. You just need to ensure that a binary tree can
# be serialized to a string and this string can be deserialized to the
# original tree structure.
#
# For example, you may serialize the following tree
#
#     1
#   / \
#   2   3
#      / \
#     4   5
# as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes
# a binary tree. You do not necessarily need to follow this format, so
# please be creative and come up with different approaches yourself.
# Note: Do not use class member/global/static variables to store states.
# Your serialize and deserialize algorithms should be stateless.
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            serial = []
            queue = [self]

            while queue:
                cur = queue[0]

                if cur:
                    serial.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    serial.append("#")

                queue = queue[1:]

            while serial[-1] == "#":
                serial.pop()

            return repr(serial)


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def serializeHelper(node):
            if not node:
                vals.append('#')  # review why I don't need 'global' here, but recover-binary-tree can not
            else:
                vals.append(str(node.val))
                serializeHelper(node.left)
                serializeHelper(node.right)

        vals = []
        serializeHelper(root)

        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def deserializeHelper():
            val = next(vals)
            if val == '#':
                return None
            else:
                node = TreeNode(int(val))
                node.left = deserializeHelper()
                node.right = deserializeHelper()

            return node

        def issplit(source, sep):
            sepsize = len(sep)
            start = 0
            while True:
                idx = source.find(sep, start)
                if idx == -1:
                    yield source[
                          start:]  # review what yield means? https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
                    return
                yield source[start:idx]
                start = idx + sepsize

        vals = iter(issplit(data, ' '))
        return deserializeHelper()


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print root

    st1 = Codec().serialize(root)
    print st1

    node = Codec().deserialize(st1)
    print node
