# Time:  O(n * d), n is length of string, d is size of dictionary
# Space: O(d)
#
# Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# For example,
#
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# All words have the same length.
# All words contain only lowercase alphabetic characters.
#

# BFS
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def findLadders(self, start, end, dict):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        dict.add(start)
        dict.add(end)

        res, cur, visited, found, trace = [], [start], set([start]), False, {word: [] for word in
                                                                             dict}  # knowledge, how to initialize a map-like list

        while cur and not found:
            for word in cur:
                visited.add(word)

            next = set()
            for word in cur:
                for i in xrange(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in dict:
                            if candidate == end:
                                found = True
                            next.add(candidate)
                            trace[candidate].append(word)
            cur = next

        if found:
            self.backtrack(trace, end, [], res)

        return res

    def backtrack(self, trace, word, path, res):
        if not trace[word]:
            res.append([word] + path)

        else:
            for prev in trace[word]:
                self.backtrack(trace, prev, [word] + path, res)


if __name__ == "__main__":
    print Solution().findLadders("hit", "cog", set(["hot", "dot", "dog", "lot", "log"]))
