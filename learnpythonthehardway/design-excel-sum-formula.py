# Your task is to design the basic function of Excel and implement the function of sum formula. Specifically,
# you need to implement the following functions:
#
# Excel(int H, char W): This is the constructor. The inputs represents the height and width of the Excel form. H is a
#  positive integer, range from 1 to 26. It represents the height. W is a character range from 'A' to 'Z'. It
# represents that the width is the number of characters from 'A' to W. The Excel form content is represented by a
# height * width 2D integer array C, it should be initialized to zero. You should assume that the first row of C
# starts from 1, and the first column of C starts from 'A'.
#
#
# void Set(int row, char column, int val): Change the value at C(row, column) to be val.
#
#
# int Get(int row, char column): Return the value at C(row, column).
#
#
# int Sum(int row, char column, List of Strings : numbers): This function calculate and set the value at C(row,
# column), where the value should be the sum of cells represented by numbers. This function return the sum result at
# C(row, column). This sum formula should exist until this cell is overlapped by another value or another sum formula.
#
# numbers is a list of strings that each string represent a cell or a range of cells. If the string represent a
# single cell, then it has the following format : ColRow. For example, "F7" represents the cell at (7, F).
#
# If the string represent a range of cells, then it has the following format : ColRow1:ColRow2. The range will always
#  be a rectangle, and ColRow1 represent the position of the top-left cell, and ColRow2 represents the position of
# the bottom-right cell.
#
#
# Example 1:
# Excel(3,"C");
# // construct a 3*3 2D array with all zero.
# //   A B C
# // 1 0 0 0
# // 2 0 0 0
# // 3 0 0 0
#
# Set(1, "A", 2);
# // set C(1,"A") to be 2.
# //   A B C
# // 1 2 0 0
# // 2 0 0 0
# // 3 0 0 0
#
# Sum(3, "C", ["A1", "A1:B2"]);
# // set C(3,"C") to be the sum of value at C(1,"A") and the values sum of the rectangle range whose top-left cell is
#  C(1,"A") and bottom-right cell is C(2,"B"). Return 4.
# //   A B C
# // 1 2 0 0
# // 2 0 0 0
# // 3 0 0 4
#
# et(2, "B", 2);
# // set C(2,"B") to be 2. Note C(3, "C") should also be changed.
# //   A B C
# // 1 2 0 0
# // 2 0 2 0
# // 3 0 0 6
# Note:
# You could assume that there won't be any circular sum reference. For example, A1 = sum(B1) and B1 = sum(A1).
# The test cases are using double-quotes to represent a character.
# Please remember to RESET your class variables declared in class Excel, as static/class variables are persisted
# across multiple test cases. Please see here for more details.

class Excel(object):

    def __init__(self, H, W):
        """
        :type H: int
        :type W: str
        """
        self.__h = H
        self.__w = ord(W) - ord('A') + 1
        self.table = [[0] * self.__w for _ in xrange(self.__h)]
        self.__bits = [[0] * self.__w for _ in xrange(self.__h)]
        self.__formulars = [[list()] * self.__w for _ in xrange(self.__h)]

    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """
        arr = self.__formulars[r][ord(c)-ord('A')]
        for row, col in arr:
            self.table[row][col] +=  v - self.table[r][ord(c)-ord('A')]
        self.update(r, ord(c) - ord('A'), v)


    def get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        return self.table[r][ord(c)-ord('A')]

    def sum(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        for s  in strs:
            arr, res = s.split(':'), 0
            if len(arr) == 1:
                r1, c1 , r2, c2 = int(arr[0][1]), ord(arr[0][0]) - ord('A'), int(arr[0][1]), ord(arr[0][0]) - ord('A')
            else:
                r1, c1 , r2, c2 = int(arr[0][1]), ord(arr[0][0]) - ord('A'), int(arr[1][1]), ord(arr[1][0]) - ord('A')

            res += self.getSumRange(r1,c1,r2,c2)

        for i in xrange(r1, r2+1):
            for j in xrange(c1, c2+1):
                self.__formulars[i][j].append((r, ord(c)-ord('A')))

        self.update(r, ord(c)-ord('A'), res)

        return res




    def update(self, r, c, v):
        diff = v - self.table[r][c]
        self.table[r][c] = v
        i, j = r + 1, c+1
        while i < self.__h:
            j = c + 1
            while j < self.__w:
                self.__bits[i][j] += diff
                j +=self.lowbit(j)
            i += self.lowbit(i)

    def getSum(self, r, c):
        i, j, res= r, c, 0
        while i > 0:
            j = c
            while j > 0:
                res += self.__bits[i][j]
                j -= self.lowbit(j)
            i -= self.lowbit(i)

        return res

    def getSumRange(self, r1, c1, r2, c2):
        if r1 == r2 and c1 == c2:
            return self.table[r1][c1]
        return self.getSum(r2+1, c2+1) - self.getSum(r2 + 1, c1) - self.getSum(r1, c2+1) + self.getSum(r1,c1)



    def lowbit(self, x):
        return x & -x

# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)

if __name__ == '__main__':
    obj = Excel(3,'C')
    obj.set(1,'A',2)
    print obj.sum(3, "C", ["A1", "A1:B2"])
