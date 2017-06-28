# Time:  O(min(n, h)), per operation
# Space: O(min(n, h))
#
# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or ..
# A . means it can represent any one letter.
#
# For example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_full = False
        self.leaves = {}  # review how to create a map


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        cur = self.root
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_full = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.searchHelper(word, 0, self.root)

    def searchHelper(self, word, start, cur):
        if start == len(word):
            return cur.is_full
        if word[start] in cur.leaves:
            return self.searchHelper(word, start + 1, cur.leaves[word[start]])
        elif word[start] == '.':
            for c in cur.leaves:
                if self.searchHelper(word, start + 1, cur.leaves[c]):
                    return True

        return False


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

if __name__ == '__main__':
    wordDict = WordDictionary()
    wordDict.addWord("word")
    wordDict.addWord("wor1d")
    wordDict.addWord("wor2d")
    print wordDict.search("pattern")
    print wordDict.search("wor1d")
    print wordDict.search("wor.d")
