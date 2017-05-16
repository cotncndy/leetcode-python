# Time:  O(n)
# Space: O(1)

# Compare two version numbers version1 and version1.
# If version1 > version2 return 1, if version1 < version2
# return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and
# contain only digits and the . character.
# The . character does not represent a decimal point and
# is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to
# version three", it is the fifth second-level revision of
# the second first-level revision.
#
# Here is an example of version numbers ordering:
#
# 0.1 < 1.1 < 1.2 < 13.37
#
import itertools


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1, l2 = len(version1), len(version2)
        i, j = 0, 0
        while i < l1 and j < l2:
            v1, v2 = 0, 0
            while i < l1 and version1[i] != '.':
                v1 = v1 * 10 + int(version1[i])
                i += 1
            while j < l2 and version2[j] != '.':
                v2 = v2 * 10 + int(version2[j])
                j += 1
            if v1 != v2:
                return 1 if v1 > v2 else -1
            i += 1
            j += 1

        return 0
