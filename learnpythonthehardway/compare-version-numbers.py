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
        while i < l1 or j < l2:
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

    def compareVersion2(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = version1.split("."), version2.split(".")
        i, j = 0, 0
        while i < len(v1) and j < len(v2):
            if int(v1[i]) != int(v2[j]):
                return 1 if int(v1[i]) > int(v2[j]) else -1

            i, j = i + 1, j + 1

        while i < len(v1):
            if int(v1[i]) != '0':
                return 1
        while j < len(v2):
            if int(v2[j]) != '0':
                return -1

        return 0

    def compareVersion3(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1, v2 = version1.split("."), version2.split(".")
        if len(v1) < len(v2):
            v1 += ['0' for _ in xrange(len(v2) - len(v1))]
        if len(v2) < len(v1):
            v2 += ['0' for _ in xrange(len(v1) - len(v2))]

        i = 0
        while i < len(v1):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i] < int(v2[i])):
                return -1
            else:
                i += 1

        return 0
