# Time:  O(n)
# Space: O(1)
#
# Follow up for problem "Populating Next Right Pointers in Each Node".
#
# What if the given tree could be any binary tree? Would your previous solution still work?
#
# Note:
#
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        head = root
        while head:
            prev, curr, next_head = None, head, None
            while curr:
                if curr.left:
                    if not next_head:
                        next_head = curr.left
                    if prev:
                        prev.next = curr.left
                    prev = curr.left
                elif curr.right:
                    if not next_head:
                        next_head = curr.right
                    if prev:
                        prev.next = curr.right
                    prev = curr.right

                curr = curr.next
            head = next_head


if __name__ == "__main__":
    root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(3)
    root.left.left, root.left.right, root.right.right = TreeNode(4), TreeNode(5), TreeNode(7)
    Solution().connect(root)
    print root
    print root.left
    print root.left.left
