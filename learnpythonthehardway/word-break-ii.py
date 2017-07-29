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
            for j in xrange(1, min(i, max_len)):  # word ends at i-1
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
                path.append([s[start:i + 1]])
                self.backtrack(s, wordDict, valid, i + 1, path, res)
                path.pop()  # backtrack


if __name__ == "__main__":
    print Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
