# Time:  O(n * glogg), g is the max size of groups.
# Space: O(n)
#
# Given an array of strings, return all groups of strings that are anagrams.
#
# Note: All inputs will be in lower-case.
#
import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words, result = collections.defaultdict(list), []
        for s in strs:
            sorted_str = "".join(sorted(s))
            words[sorted_str].append(s)

        for anagram in words.values():
            result.append(anagram)
        return result


if __name__ == "__main__":
    result = Solution().groupAnagrams(["cat", "dog", "act", "mac"])
    print result
