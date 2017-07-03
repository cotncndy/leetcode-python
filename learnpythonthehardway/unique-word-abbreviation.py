# Time:  ctor:   O(n), n is number of words in the dictionary.
#        lookup: O(1)
# Space: O(k), k is number of unique words.

from collections import defaultdict


class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.__lookup = defaultdict(set)
        for word in dictionary:
            abbr = self.abbreviation(word)
            self.__lookup[abbr].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self.abbreviation(word)
        return self.__lookup[abbr] <= {word}  # review how to compare 2 set directly

    def abbreviation(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]
