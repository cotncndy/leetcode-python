# Time:  O(n * l^2 + n * r), l is the max length of the words,
#                            r is the number of the results.
# Space: O(n^2)
#
# Given a string s and a dictionary of words dict,
# add spaces in s to construct a sentence where each word is a valid dictionary word.
#
# Return all such possible sentences.
#
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
#
# A solution is ["cats and dog", "cat sand dog"].
#
from collections import Counter, defaultdict


class Solution(object):
    def wordBreak(self, s, wordDict):  # review DP + Backtrack
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        n = len(s)
        can_break, valid = [False for _ in xrange(n + 1)], [[False] * n for _ in xrange(n)]
        can_break[0] = True
        max_len = 0
        for w in wordDict:  # find the max len in the dict
            max_len = max(max_len, len(w))

        for i in xrange(1, n + 1):
            for j in xrange(1, min(i, max_len) + 1):  # word ends at i-1 bugfixed
                if can_break[i - j] and s[i - j:i] in wordDict:  # if [0:i-j] breakable and [i-j:i] is also in dict
                    can_break[i] = True
                    valid[i - j][i - 1] = True

        res = []
        if can_break[-1]:  # if breakable
            self.backtrack(s, wordDict, valid, 0, [], res)
        return res

    def backtrack(self, s, wordDict, valid, start, path, res):
        if start == len(s):
            res.append(" ".join(path))
            return
        for i in xrange(start, len(s)):
            if valid[start][i]:
                path.append(s[start:i + 1])
                self.backtrack(s, wordDict, valid, i + 1, path, res)
                path.pop()  # backtrack

    def dfs(self, s, words, start, cache):  # review wonderful, top-down dp memo
        if start in cache:
            return cache[start]

        result = []
        for end in range(start, len(s)):
            word = s[start: end + 1]
            if word not in words:
                continue
            if end == len(s) - 1:
                result.append(word)
            else:
                for sub_s in self.dfs(s, words, end + 1, cache):
                    result.append(word + ' ' + sub_s)

        cache[start] = result
        return result

    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s:
            return []

        words = set(wordDict)
        return self.dfs(s, words, 0, {})

    def wordBreak3(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordset = set(wordDict)
        cs1 = Counter(s)  # usage of counter
        dcheck = {}
        long_string = "".join(wordDict)
        cs2 = Counter(long_string)
        for key in cs1:
            if key not in cs2:
                return []

        d = defaultdict(list)
        res = []

        def dp(end_index):  # review top-down dp , memo, so cool
            if end_index in d:
                return d[end_index]
            if s[:end_index] in wordset:
                d[end_index].append([s[:end_index]])
            for i in xrange(1, end_index):
                if s[i:end_index] in wordset:
                    temp = dp(i)
                    for v in temp:
                        d[end_index].append(v + [s[i:end_index]])

            return d[end_index]

        res = dp(len(s))
        ans = [" ".join(sentence) for sentence in res]
        return ans


if __name__ == "__main__":
    print Solution().wordBreak3("catsanddog", ["cat", "cats", "and", "sand", "dog"])
