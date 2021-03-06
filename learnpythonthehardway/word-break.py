# Time:  O(n * l^2)
# Space: O(n)

# Given a string s and a dictionary of words dict,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)
        can_break = [False] * (n + 1)
        can_break[0] = True
        max_len = 0
        for word in wordDict:
            max_len = max(max_len, len(word))

        for i in xrange(1, n + 1):
            for j in xrange(1, min(i, max_len) + 1):  # bugfixed
                if can_break[i - j] and s[i - j:i] in wordDict:  # bugfixed
                    can_break[i] = True
                    break

        return can_break[-1]
