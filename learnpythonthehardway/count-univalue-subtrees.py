# Time:  O(n)
# Space: O(h)
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            return "{} : {},{}".format(self.val, self.left.val if self.left else 'None', \
                                       self.right.val if self.right else 'None')

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    count = 0

    def countUnivalSubtrees(self, root):
        self.isUni(root, -1)  # bugfixed
        return self.count

    def isUni(self, root, val):
        if not root:
            return True  # leaf is uni-tree

        if (not self.isUni(root.left, root.val)) | (
        not self.isUni(root.right, root.val)):  # bugfixed, notice can not use or
            # instead need to use '|'
            return False

        self.count += 1
        return root.val == val


if __name__ == '__main__':
    r = TreeNode(5)
    r1, r2 = TreeNode(1), TreeNode(5)
    r.left, r.right = r1, r2
    r1.left, r1.right = TreeNode(5), TreeNode(5)
    r2.left, r2.right = TreeNode(5), TreeNode(5)

    print Solution().countUnivalSubtrees(r)
