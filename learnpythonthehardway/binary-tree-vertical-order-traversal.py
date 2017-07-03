# Time:  O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
# BFS + hash solution.
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # review compared with java, python code a lot more concise and more like nature lanaguage
        cols = defaultdict(list)
        queue = [(root,0)]  # review how to initialize a queue
        for node, i in queue:
            if node :
                cols[i].append(node.val)
                queue += (node.left,i-1), (node.right,i+1) # review how to add multiple items in queue directly

        return [cols[i] for i in xrange(min(cols.keys()), max(cols.keys())+1)] \
                if cols else []
