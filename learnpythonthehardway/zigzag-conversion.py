# Time:  O(n)
# Space: O(1)
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
#

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = [""] * numRows
        row, dire = 0, 1
        for i in xrange(len(s)):
            res[row] += s[i]
            row += dire
            if row == numRows - 1 or row == 0:
                dire *= -1

        return ''.join(res)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    rows = 3
    print Solution().convert(s, rows)
