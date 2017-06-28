# Time:  O(n)
# Space: O(h)
#
# Invert a binary tree.
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#

# Time:  O(n)
# Space: O(w), w is the max number of the nodes of the levels.
# BFS solution.

# Definition for a  binary tree node
from collections import deque


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

        else:
            return None


class Queue:  # review how to get a deque
    def __init__(self):
        self.data = deque()

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.popleft()

    def peek(self):
        return self.data[0]

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0






class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None or (root.left is None and root.right is None):
            return root
        cur = root  # review written by me
        self.invertTree(root.left)
        self.invertTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp

        return cur

    def invertTree2(self, root):
        if root is not None:
            nodes = Queue()
            nodes.push(root)

            while not nodes.empty():
                node = nodes.pop()
                node.left, node.right = node.right, node.left
                if node.left is not None:
                    nodes.push(node.left)
                if node.right is not None:
                    nodes.push(node.right)

        return root

    def invertTree3(self, root):
        if root is not None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root



if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print root
    Solution().invertTree2(root)
    print root
