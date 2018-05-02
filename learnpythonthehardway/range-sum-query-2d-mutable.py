# Time:  ctor:   O(m * n)
#        update: O(logm * logn)
#        query:  O(logm * logn)
# Space: O(m * n)

# Binary Indexed Tree (BIT) solution.
class NumMatrix(object):
    def __init__(self, matrix):
        if len(matrix) == 0:
            return
        if len(matrix[0]) == 0:
            return
        self.__row, self.__col = len(matrix) + 1, len(matrix[0]) + 1
        self.__bits = [[0] * self.__col for _ in xrange(self.__row)]  # review how to initialize a 2 dimension array
        self.__mat = [[0] * self.__col for _ in xrange(self.__row)]

        for i in xrange(self.__row - 1):
            for j in xrange(self.__col - 1):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        i, j = row + 1, col + 1
        diff = val - self.__mat[i][j]
        self.__mat[i][j] = val
        while i < self.__row:
            j = col + 1
            while j < self.__col:
                self.__bits[i][j] += diff
                j += self.low_bit(j)
            i += self.low_bit(i)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.get_sum(row2 + 1, col2 + 1) - self.get_sum(row2 + 1, col1) - self.get_sum(row1, col2 + 1) + \
               self.get_sum(row1, col1)

    def get_sum(self, row, col):
        i, j, res = row, col, 0
        while i > 0:
            j = col
            while j > 0:
                res += self.__bits[i][j]
                j -= self.low_bit(j)
            i -= self.low_bit(i)

        return res

    def low_bit(self, x):
        return x & -x


if __name__ == '__main__':
    m = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print m.sumRegion(2, 1, 4, 3)

    m = NumMatrix([[1, 2]])
    print m.sumRegion(0, 1, 0, 1)
