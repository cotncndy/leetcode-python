# Let's play the minesweeper game (Wikipedia, online game)!
#
# You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an
# unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right,
# and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square,
# and finally 'X' represents a revealed mine.
#
# Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'),
# return the board after revealing this position according to the following rules:
#
#     If a mine ('M') is revealed, then the game is over - change it to 'X'.
#     If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of
# its adjacent unrevealed squares should be revealed recursively.
#     If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8')
# representing the number of adjacent mines.
#     Return the board when no more squares will be revealed.
#
# Example 1:
#
# Input:
#
# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]
#
# Click : [3,0]
#
# Output:
#
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Explanation:
#
# Example 2:
#
# Input:
#
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Click : [1,2]
#
# Output:
#
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'X', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Explanation:
#
# Note:
#
#     The range of the input matrix's height and width is [1,50].
#     The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at
#  least one clickable square.
#     The input board won't be a stage when game is over (some mines have been revealed).
#     For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal
# all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board:
            return board
        m, n = len(board), len(board[0])
        if not m or not n:
            return board


        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:  # search its all 8 neighbor , check how many mines there
            cnt = 0
            for i in xrange(-1, 2):
                for j in xrange(-1, 2):
                    x, y = click[0] + i, click[1] + j
                    if 0 <= x < m and 0 <= y < n:
                        if board[x][y] == 'M':
                            cnt += 1
            if cnt > 0:
                board[click[0]][click[1]] = str(cnt)
            else:
                board[click[0]][click[1]] = 'B'  # if it is 'B', we need recursively find all its neighbor
                for i in xrange(-1, 2):
                    for j in xrange(-1, 2):
                        x, y = click[0] + i, click[1] + j
                        if 0 <= x < m and 0 <= y < n:
                            if board[x][y] == 'E':  # only find those has not been marked yet
                                self.updateBoard(board, [x, y])
        return board

    def updateBoard2(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board:
            return board
        m, n = len(board), len(board[0])
        if not m or not n:
            return board

        empty = []

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:  # search its all 8 neighbor , check how many mines there
            cnt = 0
            for i in xrange(-1, 2):
                for j in xrange(-1, 2):
                    x, y = click[0] + i, click[1] + j
                    if 0 <= x < m and 0 <= y < n:
                        if board[x][y] == 'M':
                            cnt += 1
                        if board[x][y] == 'E':
                            empty.append([x, y])

            if cnt > 0:
                board[click[0]][click[1]] = str(cnt)
            else:
                board[click[0]][click[1]] = 'B'  # if it is 'B', we need recursively find all its neighbor
                for x, y in empty:
                    self.updateBoard(board, [x, y])
        return board

    def updateBoard3(self, board, click):
        if not board:
            return board
        m, n = len(board), len(board[0])
        if not m or not n:
            return board

        que = []
        que.append(click)

        while que:
            row, col = que.pop(0)
            if board[row][col] == 'M':
                board[row][col] = 'X'

            else:  # search its all 8 neighbor , check how many mines there
                cnt, neighbor = 0, []
                for i in xrange(-1, 2):
                    for j in xrange(-1, 2):
                        x, y = row + i, col + j
                        if 0 <= x < m and 0 <= y < n:
                            if board[x][y] == 'M':
                                cnt += 1
                            if cnt == 0 and board[x][y] == 'E':  # bugfixed
                                neighbor.append([x, y])

                if cnt > 0:
                    board[row][col] = str(cnt)
                else:
                    board[row][col] = 'B'  # if it is 'B', we need recursively find all its neighbor
                    for x, y in neighbor:  # bugfixed
                        board[x][y] = 'B'
                        que.append([x, y])
        return board
