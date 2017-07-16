# Time:  O(logm + logn)
# Space: O(1)
#
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.
#

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:  # bugfixed check row and col
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1  # bugfixed it should be m*n-1
        while left <= right:
            mid = (left + right) / 2
            if matrix[mid / n][mid % n] == target:
                return True
            elif matrix[mid / n][mid % n] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False


if __name__ == '__main__':
    print Solution().searchMatrix([[1]], 2)
