# Given a list of words (without duplicates), please write a program that returns all concatenated words in the given
#  list of words.
# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given
# array.
#
# Example:
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
#
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
#  "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Note:
# The number of elements of the given array will not exceed 10,000
# The length sum of elements in the given array will not exceed 600,000.
# All the input string will only include lower case letters.
# The returned elements order does not matter.
import collections


class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key=lambda s: len(s))
        m, res = collections.defaultdict(set), []
        for w in words:
            m[len(w)].add(w)

        for i in reversed(xrange(len(words))):
            cache = collections.defaultdict(list)
            self.dfs(words[i], m, cache, 0)
            if len(cache[0]) > 1:
                res.append(words[i])

        return res

    def dfs(self, word, map, cache, start):
        if cache[start]:
            return cache[start]

        res = []
        for l in map:
            if start + l > len(word):
                break;

            w = word[start: start + l]
            if w in map[l] and w != word:
                res.append(w)
                for s in self.dfs(word, map, cache, start + l):
                    res.append(s)

        cache[start] = res
        return res


if __name__ == '__main__':
    print Solution().findAllConcatenatedWordsInADict(
        ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"])
