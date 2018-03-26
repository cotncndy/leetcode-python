# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words,
# one of the first string's permutations is the substring of the second string.
# Example 1:
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
import collections


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m = collections.defaultdict(int)
        for c in s1:
            m[c] += 1

        hasStr1 = self.hash(s1, m)

        idx = 0
        while idx < len(s2) - len(s1):
            if s2[idx] not in m:
                idx += 1
                continue

            s = s2[idx:idx + len(s1)]
            for k, v in enumerate(s):
                if v not in m:
                    idx += k  #
                    break
            else:
                if hasStr1 == self.hash(s, m):
                    return True
            idx += 1

        return False

    def hash(self, s, m):
        return ''.join(map(lambda c: c + str(m[c]), sorted(s)))


if __name__ == '__main__':
    print Solution().checkInclusion("ab", "eidbcabooo")
