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
class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if not s1 or not s2 or len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        dp = [[[False for j in xrange(len(s2))] for i in xrange(len(s1))] for n in xrange(len(s1) + 1)]
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

        return dp[n][0][0]
