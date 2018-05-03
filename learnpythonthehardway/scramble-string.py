# Time:  O(n^4)
# Space: O(n^3)
#
# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
#
# Below is one possible representation of s1 = "great":
#
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.
#
# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
#
#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".
#
# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
#
#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".
#
# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
#

# DP solution
# Time:  O(n^4)
# Space: O(n^3)
import collections


class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):  # review, 3-d dp , wonderful
        if not s1 or not s2 or len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        # dp = [[[False for j in xrange(len(s2))] for i in xrange(len(s1))] for n in xrange(len(s1) + 1)]
        dp = [[[False] * len(s2)] * len(s1)] * (len(s1) + 1)
        for i in xrange(len(s1)):
            for j in xrange(len(s2)):
                if s1[i] == s2[j]:
                    dp[1][i][j] = True

        for n in xrange(2, len(s1) + 1):
            for i in xrange(len(s1) - n + 1):
                for j in xrange(len(s2) - n + 1):
                    for k in xrange(1, n):
                        if dp[k][i][j] and dp[n - k][i + k][j + k] or \
                                        dp[k][i][j + n - k] and dp[n - k][i + k][j]:
                            dp[n][i][j] = True

        return dp[len(s1)][0][0]

    def isScramble2(self, s1, s2, r=0):
        if not s1 or s1 == s2: return True
        dic = collections.Counter([])
        different = 0
        for i, c1, c2 in zip(range(len(s1)), s1, s2):
            if c1 != c2:
                dic[c1] += 1
                dic[c2] -= 1
                different += 2 - (dic[c1] <= 0) * 2 - (dic[c2] >= 0) * 2
            if not different and i < len(s1) - 1:
                if self.isScramble(s1[:i + 1], s2[:i + 1]) and self.isScramble(s1[i + 1:], s2[i + 1:]): return True
        if not r and not different and self.isScramble(s1, s2[::-1], 1): return True
        return False

    def isScramble3(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False

        memo = {}
        return self.search(s1, s2, memo)

    def search(self, s1, s2, memo):  # review top-down dp, so cool
        if memo.get(s1 + '#' + s2) != None:
            return memo[s1 + '#' + s2]

        n = len(s1)
        if n == 1:
            return s1 == s2
        elif not sorted(s1) == sorted(s2):
            return False
        for i in range(1, n):
            if self.search(s1[:i], s2[:i], memo) and self.search(s1[i:], s2[i:], memo) or \
                            self.search(s1[:i], s2[n - i:], memo) and self.search(s1[i:], s2[:n - i], memo):
                memo[s1 + '#' + s2] = True
                return True
        memo[s1 + '#' + s2] = False
        return False

    def isScramble4(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        def find(w1, w2):
            if w1 == w2:
                return True
            m = {}
            for w in w1:
                if w not in m:
                    m[w] = 1
                else:
                    m[w] += 1
            for w in w2:
                if w not in m or m[w] == 0:
                    return False
                m[w] -= 1
            l = len(w1)
            for i in xrange(1, l):
                if find(w1[:i], w2[:i]) and find(w1[i:], w2[i:]):
                    return True
                elif find(w1[:i], w2[l - i:]) and find(w1[i:], w2[:l - i]):
                    return True
            return False

        return find(s1, s2)
