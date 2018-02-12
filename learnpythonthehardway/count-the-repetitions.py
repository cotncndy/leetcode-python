# -*- coding: utf-8 -*-
# Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".
#
# On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2
#  such that it becomes s1. For example, “abc” can be obtained from “abdbec” based on our definition, but it can not
# be obtained from “acbbe”.
#
# You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 ≤ n1 ≤ 106 and
# 1 ≤ n2 ≤ 106. Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such
# that [S2,M] can be obtained from S1.
#
# Example:
#
# Input:
# s1="acb", n1=4
# s2="ab", n2=2
#
# Return:
# 2


class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        t1, t2 = s1 * n1, s2 * n2
        n = int(len(t1) / len(t2))
        left, right = 0, n

        while left <= right:
            mid = (right - left) / 2 + left
            t3 = t2 * mid
            if self.lcs(t1, t3) == len(t3):
                left = mid + 1
            else:
                right = mid - 1

        return right

    def lcs(self, s1, s2):
        l1, l2 = len(s1), len(s2)
        dp = [[0] * (l2 + 1) for _ in xrange(l1 + 1)]
        for i in xrange(1, l1 + 1):
            for j in xrange(1, l2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[l1][l2]


if __name__ == '__main__':
    print Solution().getMaxRepetitions("acb", 4, "ab", 2)
