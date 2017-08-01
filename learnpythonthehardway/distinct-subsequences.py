# Time:  O(n^2)
# Space: O(n)
#
# Given a string S and a string T, count the number of distinct subsequences of T in S.
#
# A subsequence of a string is a new string which is formed from the original string
# by deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Here is an example:
# S = "rabbbit", T = "rabbit"
#
# Return 3.
#

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        ways = [0 for _ in xrange(len(S) + 1)]
        ways[0], prev = 1, 0
        for i in xrange(1, len(T) + 1):
            for j in xrange(1, len(S) + 1):
                ways[j] += ways[j - 1]
                if T[i - 1] == S[j - 1]:
                    ways[j] += prev
                prev = ways[j - 1]

        return ways[-1]
