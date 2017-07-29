# Time:  O(m * n * l)
# Space: O(l)
#
# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells
# are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# For example,
# Given words = ["oath","pea","eat","rain"] and board =
#
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#

class TrieNode(object):
    def __init__(self):
        self.is_string = False
        self.leaves = {}

    # insert a word into trie
    def insert(self, word):
        cur = self
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]

        cur.is_string = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        row, col = len(board), len(board[0])
        # visited = [[False for _ in xrange(col)] for _ in xrange(row)]
        visited = [[False] * col for _ in xrange(row)]
        res, trie = {}, TrieNode()
        for w in words:
            trie.insert(w)

        for i in xrange(row):
            for j in xrange(col):
                self.backtrack(board, trie, i, j, visited, [], res)

        return res.keys()

    def backtrack(self, board, trie, i, j, visited, cur_word, res):
        if not trie or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
            return

        if board[i][j] not in trie.leaves:  # critical , use trie to speed up search
            return

        cur_word.append(board[i][j])
        next_node = trie.leaves[board[i][j]]
        if next_node.is_string:
            res["".join(cur_word)] = True

        visited[i][j] = True
        self.backtrack(board, next_node, i + 1, j, visited, cur_word,
                       res)  # bugfix forget to replace trie with next_node
        self.backtrack(board, next_node, i - 1, j, visited, cur_word, res)
        self.backtrack(board, next_node, i, j - 1, visited, cur_word, res)
        self.backtrack(board, next_node, i, j + 1, visited, cur_word, res)
        visited[i][j] = False  # backtrack
        cur_word.pop()  # backtrack


if __name__ == '__main__':
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]

    print Solution().findWords(board, words)
