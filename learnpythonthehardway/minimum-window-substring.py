# Time:  O(n)
# Space: O(k), k is the number of different characters

# Given a string S and a string T, find the minimum window in S which
# will contain all the characters in T in complexity O(n).
#
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
#
# Note:
# If there is no such window in S that covers all characters in T,
# return the emtpy string "".
#
# If there are multiple such windows, you are guaranteed that
# there will always be only one unique minimum window in S.
import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = ""
        if len(t) > len(s):
            return res
        m, min_len, left, right, count = collections.defaultdict(int), float('inf'), 0, 0, 0
        # review float('inf') define the max, float('-inf') defines the min
        for c in t:
            m[c] += 1

        while right < len(s):
            if s[right] in m:
                m[s[right]] -= 1
                if m[s[right]] >= 0:
                    count += 1
            while count == len(t):
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res = s[left:right + 1]
                if s[left] in m:
                    m[s[left]] += 1
                    if m[s[left]] > 0:
                        count -= 1
                left += 1
            right += 1
        return res


if __name__ == "__main__":
    print Solution().minWindow("ADOBECODEBANC", "ABC")
