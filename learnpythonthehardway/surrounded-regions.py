# Time:  O(m * n)
# Space: O(m + n)
#
# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
#

import collections


class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board:
            return
        q = collections.deque([])
        for i in xrange(len(board)):
            q.append((i, 0))
            q.append((i, len(board[i]) - 1))  # bugfixed

        for j in xrange(len(board[0])):
            q.append((0, j))
            q.append((len(board) - 1, j))

        while q:
            i, j = q.popleft()
            if board[i][j] in ['O', 'V']:
                board[i][j] = 'V'
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1),
                             (i, j - 1)]:  # bugfixed, for loop should be inside if block
                    if 0 <= x < len(board) and 0 <= y < len(board[i]) and board[x][y] == 'O':  # bugfixed, careless
                        board[x][y] = 'V'
                        q.append((x, y))

        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def solve2(self, board):
        if not board:
            return
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[i]) - 1:
                    if board[i][j] == 'O':
                        self.dfs(board, i, j)

        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def dfs(self, board, i, j):
        board[i][j] = 'V'
        for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
            if 0 < x < len(board) and 0 < y < len(board[x]) and \
                            board[x][y] == 'O':
                self.dfs(board, x, y)


if __name__ == "__main__":
    board = [['X', 'O', 'X', 'X'],
             ['O', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'O'],
             ['O', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'O'],
             ['O', 'X', 'O', 'X']]
    # board = ["XOXX","OXOX","XOXO","OXOX","XOXO","OXOX"]
    Solution().solve2(board)
    print board
