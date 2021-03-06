#  Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is
# defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So
#  what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency
# in any order.
#
# Examples 1
# Input:
#
#   5
#  /  \
# 2   -3
#
# return [2, -3, 4], since all the values happen only once, return all of them in any order.
#
# Examples 2
# Input:
#
#   5
#  /  \
# 2   -5
#
# return [2], since 2 happens twice, however -5 only occur once.
#
# Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.


# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        count = collections.defaultdict(int)
        self.helper(root, count)

        tmax = 0
        for k, v in count.iteritems():
            tmax = max(tmax, v)
        for k, v in count.iteritems():  # knowledge hwo to loop dict with key, value pair
            if v == tmax:
                res.append(k)

        return res

    def helper(self, root, count):
        if not root.left and not root.right:
            count[root.val] += 1
            return root.val
        left, right = 0, 0
        if root.left:
            left = self.helper(root.left, count)
        if root.right:
            right = self.helper(root.right, count)
        sum = root.val + left + right

        count[sum] += 1
        return sum  # bugfixed don't forgot

    def findFrequentTreeSum2(self, root):
        res = []
        count, biggest = collections.defaultdict(int), 0
        self.helper2(root, count, res)

        return res

    def helper2(self, root, count, res):
        if not root:
            return 0
        left = self.helper2(root.left, count, res)
        right = self.helper2(root.right, count, res)
        sum = root.val + left + right
        count[sum] += 1
        if count[sum] >= self.cnt:
            if count[sum] > self.cnt:
                del res[:]
            self.cnt = count[sum]
            res.append(sum)

        return sum

    cnt = 0  # knowledge , how to define class level variable



if __name__ == '__main__':
    R, l, r = TreeNode(5), TreeNode(2), TreeNode(-3)
    R.left, R.right = l, r

    # R, l, l_l = TreeNode(5), TreeNode(14), TreeNode(1)
    # R.left, l.left = l, l_l

    print Solution().findFrequentTreeSum2(R)
