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
            if not res or (c not in res and (map[res[-1]] == 0 or c > res[-1])):  # bugfixed
                res += c
            elif c not in res:  # bugfixed
                while res and c < res[-1] and map[
                    res[-1]] > 0:  # this should be  a while loop to remove any letter is bigger than cur
                    res = res[:-1]
                res += c
            map[c] -= 1

        return "".join(res)


if __name__ == '__main__':
    print Solution().removeDuplicateLetters('cbabc')
    print Solution().removeDuplicateLetters("cbacdcbc")
    print Solution().removeDuplicateLetters("bbcaac")
