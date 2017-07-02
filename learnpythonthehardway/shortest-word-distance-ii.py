# Time:  init: O(n), lookup: O(a + b), a, b is occurences of word1, word2
# Space: O(n)

from collections import defaultdict


class WordDistance:
    # initialize your data structure here.
    # @param {string[]} words
    def __init__(self, words):
        self.word_indexes = defaultdict(list)

        for i in xrange(len(words)):
            self.word_indexes[words[i]].append(i)

    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    # Adds a word into the data structure.
    def shortest(self, word1, word2):
        min_len, i, j = float('inf'), 0, 0
        ids1, ids2 = self.word_indexes[word1], self.word_indexes[word2]

        while i < len(ids1) and j < len(ids2):
            min_len = min(min_len, abs(ids2[j] - ids1[i]))
            if ids1[i] < ids2[j]:
                i += 1
            else:
                j += 1

        return min_len
