# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with
# a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
#
# Example 1:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def traverse(root, list):
            if not root:
                return ""
            traverse(root.left, list)
            traverse(root.right, list)
            list += str(root.val)

            return list

        def traverse2(root, list):
            if not root:
                return ""
            traverse2(root.right, list)
            traverse2(root.left, list)
            list += str(root.val)

            return list


        ls1, ls2 = [], []
        ls1 = traverse(s, ls1)
        ls2 = traverse(t, ls2)

        st1 = "".join(map(str, ls1))
        st2 = "".join(map(str, ls2))

        rs1, rs2 = [], []
        rs1 = traverse(s, rs1)
        rs2 = traverse(t, rs2)

        rst1 = "".join(map(str, rs1))
        rst2 = "".join(map(str, rs2))
        if st2 in st1 and rst2 in rst1:
            return True
        return False

    def isSubtree2(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        if self.isSame(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val == root2.val and self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right)

    def isSubtree3(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def serialize(root, li):
            if not root:
                li.append(',#')
                return
            else:
                li.append(',')
                li.append(str(root.val))
            serialize(root.left, li)
            serialize(root.right, li)

        l1, l2 = list(), list()
        serialize(s, l1)
        serialize(t, l2)

        st1, st2 = "".join(l1), "".join(l2)
        if st2 in st1:
            return True

        return False





if __name__ == '__main__':
    root, lN, rN = TreeNode(3), TreeNode(4), TreeNode(5)
    root.left, root.right = lN, rN
    llN, lrN = TreeNode(1), TreeNode(2)
    lN.left, lN.right = llN, lrN

    root2, lN1, rN1 = TreeNode(4), TreeNode(1), TreeNode(2)
    root2.left, root2.right = lN1, rN1

    print Solution().isSubtree(root, root2)
