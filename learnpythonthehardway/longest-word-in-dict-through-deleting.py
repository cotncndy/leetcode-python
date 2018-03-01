#  Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting
# some characters of the given string. If there are more than one possible results, return the longest word with the
# smallest lexicographical order. If there is no possible result, return the empty string.
#
# Example 1:
#
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output:
# "apple"
#
# Example 2:
#
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output:
# "a"
#
# Note:
#
#     All the strings in the input will only contain lower-case letters.
#     The size of the dictionary won't exceed 1,000.
#     The length of all the strings in the input won't exceed 1,000.
import collections


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        slist = sorted(set(d), key=len, reverse=True)
        mp, res = collections.defaultdict(int), ""
        for c in s:
            mp[c] += 1
        for l in slist:
            if self.lcs(l, s, mp) == len(l):
                res = l
                break

        return res

    def lcs(self, s, t, mp):
        m, n = len(s), len(t)
        dp = [[0] * (m + 1) for _ in xrange(n + 1)]

        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                elif s[j - 1] not in mp:
                    return 0
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


if __name__ == '__main__':
    print Solution().findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"])
    print Solution().findLongestWord("abpcplea", ["a", "b", "c"])
