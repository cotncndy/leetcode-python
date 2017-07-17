# Time:  O(max(h, k))
# Space: O(h)

# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Follow up:
# What if the BST is modified (insert/delete operations) often and
# you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    count = 0

    def kthSmallest(self, root, k):  # review how to use recursion
        self.count = k
        return self.helper(root)

    def helper(self, root):
        if not root:
            return -1
        val = self.helper(root.left)
        if self.count == 0:
            return val
        self.count -= 1
        if self.count == 0:
            return root.val
        return self.helper(root.right)

    def kthSmallest2(self, root, k):
        s, cur, rank = [], root, 0

        while s or cur:
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                rank += 1
                if rank == k:
                    return cur.val
                cur = cur.right
        return float('-inf')
