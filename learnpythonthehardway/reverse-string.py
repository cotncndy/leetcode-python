# Time:  O(n)
# Space: O(n)

# Write a function that takes a string as input and
# returns the string reversed.
#
# Example:
# Given s = "hello", return "olleh".

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        sstr = list(s)  # review why use list intead, string is immutable in python!
        i, j = 0, len(sstr) - 1
        while i < j:
            sstr[i], sstr[j] = sstr[j], sstr[i]
            i, j = i + 1, j - 1

        return "".join(sstr)

    def reversString2(self, s):
        return s[::-1]
