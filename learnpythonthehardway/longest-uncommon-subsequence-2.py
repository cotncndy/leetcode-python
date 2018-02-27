#  Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon
# subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any
# subsequence of the other strings.
#
# A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the
# order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a
# subsequence of any string.
#
# The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If
# the longest uncommon subsequence doesn't exist, return -1.
#
# Example 1:
#
# Input: "aba", "cdc", "eae"
# Output: 3
#
# Note:
#
#     All the given strings' lengths will not exceed 10.
#     The length of the given list will be in the range of [2, 50].
import collections


class Solution(object):

    def uncommon(self, parent, child):
        lp, lc = len(parent), len(child)
        pp = pc = 0
        while pp < lp and pc < lc:
            if parent[pp] == child[pc]:
                pc += 1
            pp += 1

        return pc != lc

    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        cnt = collections.Counter(strs)
        slist = sorted(set(strs), key=len, reverse=True)
        for i, c in enumerate(slist):
            if cnt[c] > 1: continue
            if all(self.uncommon(p, c) for p in slist[:i]):  # knowledge the usage of all
                return len(c)
        return -1


if __name__ == '__main__':
    print Solution().findLUSlength(["abcd", "bcd", "acd"])
