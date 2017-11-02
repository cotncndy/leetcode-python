# Time:  O(n)
# Space: O(n)
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i

        return self.builder(lookup, postorder, inorder, len(postorder), 0, len(inorder))

    def builder(self, lookup, postorder, inorder, post_end, in_start, in_end):
        if in_start == in_end:
            return None

        node = TreeNode(postorder[post_end - 1])
        i = lookup[postorder[post_end - 1]]
        node.left = self.builder(lookup, postorder, inorder, post_end - 1 - (in_end - i - 1), in_start, i)
        node.right = self.builder(lookup, postorder, inorder, post_end - 1, i + 1, in_end)

        return node

    def buildTree2(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder and not postorder:
            return None

        idx = -1
        if len(postorder) == 1:
            return TreeNode(postorder[0])

        for i, k in enumerate(inorder):
            if postorder[-1] == k:
                idx = i
                break
        root = TreeNode(postorder[-1])
        left_inorder, right_inorder = inorder[0:idx], inorder[idx + 1:]
        left_postorder, right_postorder = postorder[0:idx], \
                                          postorder[idx:len(postorder) - 1]
        root.left, root.right = self.buildTree2(left_inorder, left_postorder), \
                                self.buildTree2(right_inorder, right_postorder)
        return root


if __name__ == "__main__":
    inorder = [1, 2, 3, 4]
    postorder = [2, 1, 4, 3]
    result = Solution().buildTree2(inorder, postorder)
    print result.val
    print result.left.val
    print result.right.val
