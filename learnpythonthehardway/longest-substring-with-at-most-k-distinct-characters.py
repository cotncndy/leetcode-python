# Time:  O(n)
# Space: O(1)

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_len, distint_count, start, visited = 0, 0, 0, [0 for _ in xrange(256)]
        for i, char in enumerate(s):
            if visited[ord(char)] == 0:
                distint_count += 1
            visited[ord(char)] += 1

            while distint_count > k:
                visited[ord(s[start])] -= 1
                if visited[ord(s[start])] == 0:
                    distint_count -= 1
                start += 1

            max_len = max(max_len, i - start + 1)
        return max_len
