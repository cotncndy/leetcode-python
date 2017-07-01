# Time:  O(n)
# Space: O(1)
#
# Given a string, find the length of the longest substring T
# that contains at most 2 distinct characters.
#
# For example, Given s = "eceba",
#
# T is "ece" which its length is 3.
#

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstringTwoDistinct(self, s):
        res, start, distince_count, visited = 0, 0, 0, [0 for _ in xrange(256)]
        for i, c in enumerate(s):
            if visited[ord(c)] == 0:
                distince_count += 1
            visited[ord(c)] += 1

            while distince_count > 2:
                visited[ord(s[start])] -= 1
                if visited[ord(s[start])] == 0:
                    distince_count -= 1
                start += 1
            res = max(res, i - start + 1)

        return res


if __name__ == "__main__":
    print Solution().lengthOfLongestSubstringTwoDistinct("eceba")
