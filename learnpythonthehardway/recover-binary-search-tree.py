# Time:  O(n)
# Space: O(1)
#
# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
#

# Definition for a  binary tree node
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

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        global pre, first, second
        pre , first, second = None, None, None

        def inorder(root):
            global pre, first, second
            if not root:
                return
            inorder(root.left)
            if not pre:
                pre = root
            if pre.val > root.val:
                if not first:
                    first = pre
                second = root
            pre = root
            inorder(root.right)

        inorder(root)
        if first and second:
            first.val, second.val = second.val,first.val

    # morris traversal
    def recoverTree2(self, root):
        # TODO implement the morris traversal
        pass
        # FIXME implement the morris traversal with 2 pointers







if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(15)
    root.right = TreeNode(12)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(9)
    root.right.left = TreeNode(11)
    root.right.right = TreeNode(8)
    print root
    Solution().recoverTree(root)
    print root
