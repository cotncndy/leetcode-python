# Time:  O(n^2)
# Space: O(h)

# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf,
# but it must go downwards (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#   / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def helper(root, prev, sum):
            if not root:
                return 0
            curr = prev + root.val

            return int(curr == sum) + helper(root.left, curr, sum) + helper(root.right, curr, sum)

        if not root:  # bugfixed dont' forget this check, otherwise, the code below would throw NPE
            return 0
        # bugfixed, forgot to put a 0
        return helper(root, 0, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSum2(self, root, sums):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        prefix_map = defaultdict(int)
        # **important**
        # this will make sure that
        # path from the root will be counted
        prefix_map[0] = 1
        return self.helper(root, 0, prefix_map, sums)

    def helper(self, root, cursum, prefix_map, target):
        if not root:
            return 0
        # get current sum
        cursum = cursum + root.val
        # check if a segment has the target sum,
        # if yes, get the count (otherwise res will be 0)
        res = prefix_map[cursum - target]
        # increase the count of cursum if it exists, otherwise
        # store cursum (from root to current node) and count
        # bc of defaultdict, if cursum does not exist in map
        # originally, it will be 0 by default
        prefix_map[cursum] = prefix_map[cursum] + 1
        # recursively get the result from left, right subtrees
        res += self.helper(root.left, cursum, prefix_map, target) + self.helper(root.right, cursum, prefix_map, target)
        # **important**
        # when backtracking, decrease cursum count
        prefix_map[cursum] = prefix_map[cursum] - 1
        return res
