# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than
# 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        # sliding windows
        count, left, right, map, res, s = len(p), 0, 0, collections.defaultdict(int), [], s + '#'
        for c in p:
            map[c] += 1

        while right < len(s):
            if right - left == len(p):
                if count == 0:
                    res.append(left)

                if s[left] in map:
                    if map[s[left]] >= 0:
                        count += 1
                    map[s[left]] += 1

                left += 1

            if s[right] in map:
                map[s[right]] = map[s[right]] - 1
                if map[s[right]] >= 0:
                    count -= 1

            right += 1

        return res


if __name__ == '__main__':
    print Solution().findAnagrams("aebcbac", "cab")
