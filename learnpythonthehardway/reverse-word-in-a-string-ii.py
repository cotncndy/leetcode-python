# Time: O(n)
# Space:O(1)
#
# Given an input string, reverse the string word by word.
# A word is defined as a sequence of non-space characters.
#
# The input string does not contain leading or trailing spaces
# and the words are always separated by a single space.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
# Could you do it in-place without allocating extra space?
#

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """

        def reverse(s, begin, end):
            while begin < end:
                s[begin], s[end] = s[end], s[begin]
                begin, end = begin + 1, end - 1
            return s

        s = reverse(s, 0, len(s) - 1)

        i, j = 0, 0
        while j <= len(s):
            if j == len(s) or s[j] == ' ':
                reverse(s, i, j - 1)
                i = j + 1
            j += 1

        return s


if __name__ == "__main__":
    s = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    print Solution().reverseWords(s)
