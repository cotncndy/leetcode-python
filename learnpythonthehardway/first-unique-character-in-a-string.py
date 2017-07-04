# Time:  O(n)
# Space: O(n)

# Given a string, find the first non-repeating character in it and
# return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.
import collections
import string

from collections import defaultdict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # review the usage of find(), that's really cool, like natural language.
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c) == 1] or [-1])

    def firstUniqChar2(self, s):
        lookup = defaultdict(int)
        candidates = set()

        for i, char in enumerate(s):
            if char in lookup:
                candidates.discard(i)
            else:
                lookup[char] = i
                candidates.add(i)

        return min(candidates) if candidates else  -1


if __name__ == '__main__':
    print  Solution().firstUniqChar2("loveleetcode")
