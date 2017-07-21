# Time:  O(n)
# Space: O(|V|+|E|) = O(26 + 26^2) = O(1)

# BFS solution.
import collections


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        result, queue, in_degree, out_degree = [], collections.deque(), {}, {}
        dict = set()

        for w in words:
            for c in w:
                dict.add(c)

        for i in xrange(1, len(words)):
            if len(words[i - 1]) > len(words[i]) and \
                            words[i - 1][:len(words[i])] == words[i]:
                return ""  # for ex, abced abc, this case is wrong, abced should not be preceding abc
            self.findEdges(words[i - 1], words[i], in_degree, out_degree)

        for c in dict:
            if c not in in_degree:
                queue.append(c)

        while queue:
            p = queue.popleft()
            result.append(p)

            if p in out_degree:
                for c in out_degree[p]:
                    in_degree[c].discard(p)
                    if c not in in_degree:
                        queue.append(c)
                del out_degree[p]

        if out_degree:
            return ""

        return "".join(result)

    def findEdges(self, word1, word2, in_degree, out_degree):
        min_len = min(len(word1), len(word2))
        for i in xrange(min_len):
            if word1[i] != word2[i]:  # word1[i] -> word2[i],
                if word2[i] not in in_degree:
                    in_degree[word2[i]] = set()
                if word1[i] not in out_degree:
                    out_degree[word1[i]] = set()
                in_degree[word2[i]] = word1[i]
                out_degree[word1[i]] = word2[i]
                break  # break immediately, no need to compare any more


if __name__ == '__main__':
    print Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
