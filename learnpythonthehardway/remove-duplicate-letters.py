# Time:  O(n)
# Space: O(k), k is size of the alphabet

# Given a string which contains only lowercase letters,
# remove duplicate letters so that every letter appear
# once and only once. You must make sure your result is
# the smallest in lexicographical order among all
# possible results.
#
# Example:
# Given "bcabc"
# Return "abc"
#
# Given "cbacdcbc"
# Return "acdb"

import collections


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        map = collections.defaultdict(int)
        for c in s:
            map[c] += 1

        res = []
        for c in s:
            if len(res) == 0 or map[res[-1]] == 0 or c > res[-1]:
                res += c
            elif c < res[-1] and map[res[-1]] > 0:
                res[-1] = c
            map[c] -= 1

        return "".join(res)


if __name__ == '__main__':
    print Solution().removeDuplicateLetters('cbacdcbc')
