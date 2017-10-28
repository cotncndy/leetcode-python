# Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are
#  represented with '.'s. You may assume the following rules:
#
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (
# 1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.
# Invalid Example:
# ...X
# XXXX
# ...X
# This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
# Follow up:
# Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not len(board) or not len(board[0]):
            return 0
        row, col, res, first = len(board), len(board[0]), 0, True
        for i in xrange(row):
            for j in xrange(col):
                if board[i][j] == 'X':
                    if first:
                        board[i][j] = str(1)
                        first = False
                    elif i - 1 and int(board[i - 1][j]) > 0:
                        board[i - 1][j], board[i][j] = str(0), str(0)
                    elif j - 1 and int(board[i][j - 1]) >= 0:
                        board[i][j] = str(0)
                    elif i - 1 and board[i - 1][j] == '.':
                        board[i][j] = str(1)

        for i in xrange(row):
            for j in xrange(col):
                if int(board[i][j]):
                    res += int(board[i][j])
        return res

    def countBattleships2(self, board):
        res = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == '.' or (i > 0 and board[i - 1][j] == 'X') or (j > 0 and board[i][j - 1] == 'X'):
                    continue
                res += 1
        return res

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        row, col = len(board), len(board[0])
        cnt = 0

        for i in xrange(row):
            for j in xrange(col):
                if board[i][j] == 'X':
                    if (i > 0 and board[i - 1][j] == '.') or (j > 0 and board[i][j - 1] == '.'):
                        cnt += 1

        return cnt

if __name__ == '__main__':
    # print Solution().countBattleships(["X..X", "X..X", "X..X"])
    print Solution().countBattleships2(['XX', '..'])
