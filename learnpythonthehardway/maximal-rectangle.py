# Time:  O(n^2)
# Space: O(n)

# Given a 2D binary matrix filled with 0's and 1's,
# find the largest rectangle containing all ones and return its area.

# Ascending stack solution.
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
