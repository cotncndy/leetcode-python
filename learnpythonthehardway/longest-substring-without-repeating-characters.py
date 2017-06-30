# Time:  O(n)
# Space: O(1)
#
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.
#

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        longest, left, table = 0, 0, [0 for _ in xrange(256)]
        for i, ch in enumerate(s):
            if table[ord(ch)] == 0 or table[ord(ch)] < left:
                longest = max(longest, i - left + 1)
            else:
                left = table[ord(ch)]

            table[ord(ch)] = i

        return longest
