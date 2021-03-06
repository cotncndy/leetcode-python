# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
#
# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.
#
# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
#
#       6
#     /   \
#    3     5
#     \    /
#      2  0
#        \
#         1
# Note:
# The size of the given array will be in the range [1,1000].

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        big, idx = self.findMax(nums)
        root = TreeNode(big)
        if idx > 0:
            root.left = self.constructMaximumBinaryTree(nums[:idx])
        if idx < len(nums) - 1:
            root.right = self.constructMaximumBinaryTree(nums[idx + 1:])

        return root

    def findMax(self, nums):
        biggest, idx = float('-inf'), -1
        for k, v in enumerate(nums):
            if v > biggest:
                biggest, idx = v, k

        # return (biggest, idx)
        return biggest, idx  # knowledge ,(biggest,idx) is a tuple, biggest, idx is a list , both works

    def constructMaximumBinaryTree2(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            pos = nums.index(max(nums))  # knowledge, how to use some builtin function of paython list
            root = TreeNode(nums[pos])
            root.left = self.constructMaximumBinaryTree(nums[:pos])
            root.right = self.constructMaximumBinaryTree(nums[pos + 1:])
            return root

    # how to use stack to do and what is its time complexity
    def constructMaxTree(self, nums):
        st = []
        for n in nums:
            t = TreeNode(n)
            while st and st[-1].val < n:
                t.left = st.pop()

            if st:
                st[-1].right = t

            st.append(t)

        return st[0]


if __name__ == '__main__':
    root = Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    print root.val, root.left.val, root.right.val
