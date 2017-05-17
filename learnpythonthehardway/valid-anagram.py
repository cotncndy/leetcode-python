# Time:  O(n)
# Space: O(1)
#
# Given two strings s and t, write a function to
# determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
# You may assume the string contains only lowercase alphabets.
#

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dict = {}

        for c in s:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        for c in t:
            if c in dict:
                dict[c] -= 1
            else:
                dict[c] = -1
            if dict[c] < 0:
                return False

        return True
