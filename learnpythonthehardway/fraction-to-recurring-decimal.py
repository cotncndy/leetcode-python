# Time:  O(logn), where logn is the length of result strings
# Space: O(1)

# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = ""
        sign = (numerator < 0) ^ (denominator < 0)
        if sign:
            res = "-"
        numerator, denominator = abs(numerator), abs(denominator)
        res += str(numerator / denominator)
        numerator %= denominator
        if numerator > 0:
            res += '.'

        lookup = {}
        while numerator and numerator not in lookup:
            lookup[numerator] = len(res)
            numerator *= 10
            res += str(numerator / denominator)
            numerator %= denominator

        if numerator in lookup:
            res = res[:lookup[numerator]] + "(" + res[lookup[numerator]:] + ")"

        return res


if __name__ == '__main__':
    print Solution().fractionToDecimal(2, 300)
