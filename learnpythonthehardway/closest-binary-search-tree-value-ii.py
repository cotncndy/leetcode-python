# Time:  O(h + k)
# Space: O(h)
# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
#
#
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
#
# Hint:
#
# 1. Consider implement these two helper functions:
# 　　i. getPredecessor(N), which returns the next smaller node to N.
# 　　ii. getSuccessor(N), which returns the next larger node to N.
# 2. Try to assume that each node has a parent pointer, it makes the problem much easier.
# 3. Without parent pointer we just need to keep track of the path from the root to the current node using a stack.
# 4. You would need two stacks to track the path in finding predecessor and successor node separately.
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        res = []
        self.inorder(root, target, k, res)

        return res

    def inorder(self, root, target, k, res):
        if not root:
            return
        self.inorder(root.left, target, k, res)
        if len(res) < k:
            res.append(root.val)
        else:
            if abs(target - res[0]) > abs(target - root.val):
                res.pop(0)
                res.append(root.val)
            else:
                return
        self.inorder(root.right, target, k, res)

    def closestKvalues2(self, root, target, k):
        stack, res = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if len(res) < k:
                    res.append(root.val)
                else:
                    if abs(root.val - target) < abs(res[0] - target):
                        res.pop(0)
                        res.append(root.val)
                    else:
                        break
                root = root.right

        return res


if __name__ == '__main__':
    root, node = TreeNode(1), TreeNode(2)
    root.right = node

    print Solution().closestKvalues2(root, 3.428671, 1)
