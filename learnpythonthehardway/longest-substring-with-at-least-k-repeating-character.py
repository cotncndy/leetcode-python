# Time:  O(26 * n) = O(n)
# Space: O(26) = O(1)

# Find the length of the longest substring T of a given string
# (consists of lowercase letters only) such that every character in T
# appears no less than k times.
#
# Example 1:
#
# Input:
# s = "aaabb", k = 3
#
# Output:
# 3
#
# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:
#
# Input:
# s = "ababbc", k = 2
#
# Output:
# 5
#
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

import collections


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i, max_dis = 0, 0
        while i + k < len(s):
            lookup, mask, start = collections.defaultdict(int), 0, i
            for j in xrange(i, len(s)):
                lookup[s[j]] += 1
                mask |= (1 << lookup[s[j]])  # left shift, set the corresponding bit to be 1
                if lookup[s[j]] >= k:
                    mask &= (~(1 << lookup[s[j]]))  # get the complement of corresponding bit, which would be reset to 0

                if mask == 0:
                    max_dis = max(max_dis, j - i + 1)
                    start = j

            i = start + 1
        return max_dis
