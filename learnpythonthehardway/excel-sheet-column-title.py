# Time:  O(logn)
# Space: O(1)

# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res, dvd = "", n
        while dvd:
            res += chr((dvd - 1) % 26 + ord('A'))
            dvd = (dvd - 1) / 26

        return res[::-1]
