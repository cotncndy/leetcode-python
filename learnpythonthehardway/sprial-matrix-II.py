class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in xrange(n)] for _ in xrange(n)]
        left, right, top, bottom, num = 0, n - 1, 0, n - 1, 1
        while True:
            for col in xrange(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1
            if (top > bottom):
                return matrix
            for row in xrange(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1
            if (left > right):
                return matrix
            for col in reversed(xrange(left, right + 1)):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
            if (top > bottom):
                return matrix
            for row in reversed(xrange(top, bottom + 1)):
                matrix[row][left] = num
                num += 1
            left += 1
            if left > right:
                return matrix


if __name__ == "__main__":
    print Solution().generateMatrix(3)
    print Solution().generateMatrix(8)
