#  Given two strings representing two complex numbers.
#
# You need to return a string representing their multiplication. Note i2 = -1 according to the definition.
#
# Example 1:
#
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
#
# Example 2:
#
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
#
# Note:
#
#     The input strings will not have extra blank.
#     The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of
#  [-100, 100]. And the output should be also in this form.


class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aL, bL = a.split('+'), b.split('+')
        fir, thi, sec, four = int(aL[0]), int(bL[0]), int(aL[1][:-1]), int(bL[1][:-1])

        s1 = fir * thi - sec * four
        s2 = fir * four + sec * thi

        # print fir, sec, thi, four
        return str(s1) + '+' + str(s2) + 'i'

    def complexNumberMultiply2(self, a, b):
        a = map(int, a[:-1].split('+', 1))
        b = map(int, b[:-1].split('+', 1))
        return '%s+%si' % (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

if __name__ == '__main__':
    print Solution().complexNumberMultiply("1+2i", "3+-2i")
    print Solution().complexNumberMultiply("1+-1i", "1+-1i")
    print Solution().complexNumberMultiply("1+1i", "1+1i")
