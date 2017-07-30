# Time:  O(n^2 * n!)
# Space: O(n^2)

class TrieNode():
    def __init__(self):
        self.indices = []
        self.child = [None] * 26

    def insert(self, words, i):
        cur = self
        for w in words[i]:
            if not cur.child[ord(w) - ord('a')]:
                cur.child[ord(w) - ord('a')] = TrieNode()
            cur = cur.child[ord(w) - ord('a')]
            cur.indices.append(i)


class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        res, trie, cur = [], TrieNode(), []
        for i in xrange(len(words)):
            trie.insert(words, i)

        for w in words:
            cur.append(w)
            self.backtrack(words, trie, cur, res)
            cur.pop()
        return res

    def backtrack(self, words, trie, cur, res):
        if len(cur) == len(words[0]):  # bugfixed
            res.append(list(cur))
            return
        node = trie
        for s in cur:
            node = node.child[ord(s[len(cur)]) - ord('a')]  # check by trie
            if not node:
                return

        for i in node.indices:
            cur.append(words[i])
            self.backtrack(words, trie, cur, res)
            cur.pop()


if __name__ == '__main__':
    print Solution().wordSquares(["area", "lead", "wall", "lady", "ball"])
