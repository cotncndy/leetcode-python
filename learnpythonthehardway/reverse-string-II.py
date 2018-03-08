# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from
# the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k
# but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k >= len(s):
            return s[::-1]
        left, right = 0, k * 2
        while right < len(s):
            s = s[:right - k] + s[right - k: right][::-1] + s[right:]
            left, right = right, right + right

        s = s[0:left] + s[left: min(k, len(s) - left + 1)][::-1]
        return s

    def reverseStr2(self, s, k):
        res = ''
        i = 0
        while i < len(s):
            res = res + s[i:i + k][::-1]
            res = res + s[i + k:i + (k * 2)]
            i = i + (k * 2)
        return res


if __name__ == '__main__':
    print Solution().reverseStr("abcdefg", 2)
    print Solution().reverseStr(
        "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39)
