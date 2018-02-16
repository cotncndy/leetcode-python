# Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G),
# and white(W). You also have several balls in your hand.
#
# Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and
# rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep
#  doing this until no more balls can be removed.
#
# Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls,
#  output -1.
#
# Examples:
#
# Input: "WRRBBW", "RB"
# Output: -1
# Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW
#
# Input: "WWRRBBWW", "WRBRW"
# Output: 2
# Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty
#
# Input:"G", "GGGGG"
# Output: 2
# Explanation: G -> G[G] -> GG[G] -> empty
#
# Input: "RBYYBBRRB", "YRBGB"
# Output: 3
# Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty
#
# Note:
# You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same
# color.
# The number of balls on the table won't exceed 20, and the string represents these balls is called "board" in the
# input.
# The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.
# Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.
import collections


class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        
    def dfs(self, board, hand):
        if not board:
            return (True, len(hand))

        i, map = 0, collections.defaultdict(set)
        while i < len(board):
            k = 0
            while i + k < len(board) and board[i] == board[i + k]:
                k += 1
            map[k].add(i)
            i += k

        for k in map:  # remove all 3's 4's, etc
            if k > 2:
                for v in map[k]:
                    board = board[0:v] + board[v + k:]

        for k in map:
            if k == 2:
                for v in map[k]:
                    if board[v] in hand:
                        temp_board, temp_hand = board[0:v] + board[v + k:], hand.replace(board[v], "", 1)
                        return self.dfs(temp_board, temp_hand)

        for k in map:
            if k == 1:
                for v in map[k]:
                    if board[v] in hand:
                        temp_board, temp_hand = board[0:v] + board[v] + board[v:], hand.replace(board[v], "", 1)
                        return self.dfs(temp_board, temp_hand)

        return (False, hand)
