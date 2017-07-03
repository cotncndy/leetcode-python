# Time:  O(9^2)
# Space: O(9)

# Determine if a Sudoku is valid,
# according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled,
# where empty cells are filled with the character '.'.
#
# A partially filled sudoku which is valid.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable.
# Only the filled cells need to be validated.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            if not self.validList(board[i][j] for j in xrange(9)) or \
                    not self.validList(board[j][i] for j in xrange(9)):
                return False
        for i in xrange(3):
            for j in xrange(3):
                if not self.validList(board[m][n] for n in xrange(3 * j, 3 * j + 3) \
                                      for m in xrange(3 * i, 3 * i + 3)):  # how to do double for loop to get list
                    return False

        return True

    def validList(self, xs):
        xs = filter(lambda x: x != '.', xs)  # review how to define lamda function
        return len(set(xs)) == len(xs)  # review how to filte a list


if __name__ == "__main__":
    board = [[1, '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', 2, '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', 3, '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 4, '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', 5, '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', 6, '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', 7, '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', 8, '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', 9]]
    print Solution().isValidSudoku(board)