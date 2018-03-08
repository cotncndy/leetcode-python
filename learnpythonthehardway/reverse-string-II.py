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
        right = k
        while right <= len(s):
            s = s[:right - k] + s[right - k: right][::-1] + s[right:]
            right += k * 2
        return s


if __name__ == '__main__':
    print Solution().reverseStr("abcdefg", 2)
