# Time:  O(n * d), n is length of string, d is size of dictionary
# Space: O(d)
#
# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start
# to end, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# For example,
#
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
#

# BFS
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    # simple BFS won't work, you will get TLE , has 2 use 2-end BFS
    def ladderLength(self, start, end, word_list):
        distance, cur, visited = 0, [start], set([start])  # knowledge how to use set

        while cur:
            _next = []
            for word in cur:
                if word == end:
                    return distance + 1
                for i in xrange(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in word_list:
                            _next.append(candidate)
                            visited.add(candidate)
                            word_list.remove(candidate)
            cur, distance = _next, distance + 1

        return 0

    # review two-ended bfs
    def ladderLength2(self, beginWord, endWord, wordList):
        if endWord not in wordList:  # bugfixed
            return 0
        distance, start, end, visited = 1, [beginWord], [endWord], set([beginWord, endWord])

        while start and end:
            if len(start) > len(end):
                start, end = end, start  # bugfixed should exchange

            _next = []
            for word in start:
                for i in xrange(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate in end:
                            return distance + 1
                        if candidate not in visited and candidate in wordList:
                            visited.add(candidate)
                            _next.append(candidate)

            start, distance = _next, distance + 1

        return 0


if __name__ == "__main__":
    print Solution().ladderLength2("hit", "cog", set(["hot", "dot", "dog", "lot", "log"]))
    print Solution().ladderLength("hit", "cog", set(["hot", "dot", "dog", "lot", "log", "cog"]))
