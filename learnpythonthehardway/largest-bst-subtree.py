# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        max_size = [1]

        # max_size = 0

        def helper(root):
            if root.left is None and root.right is None:
                return 1, root.val, root.val  # knowledge python method could return multiple value, that's cool!

            left_size, left_min, left_max = 0, root.val, root.val
            if root.left:
                left_size, left_min, left_max = helper(root.left)
            right_size, right_min, right_max = 0, root.val, root.val
            if root.right:
                right_size, right_min, right_max = helper(root.right)

            size = 0
            if (not root.left or left_size > 0) and \
                    (not root.right or right_size > 0) and \
                                    left_max < root.val < right_min:
                size = 1 + left_size + right_size
                max_size[0] = max(max_size[0], size)
                # max_size = max(max_size,size) # knowledge max_size would be view as unresolved reference, you have to
                # define it as an array to fix this issue

            return size, left_min, right_max  # bugfixed this return should not be included in the if block

        helper(root)

        return max_size[0]


if __name__ == '__main__':
    root = TreeNode(4)
    root.left, root.right = TreeNode(2), TreeNode(7)
    root.left.left, root.left.right = TreeNode(2), TreeNode(3)
    root.right.left = TreeNode(5)
    root.left.left.left = TreeNode(2)
    root.left.left.left.left = TreeNode(1)

    print Solution().largestBSTSubtree(root)
