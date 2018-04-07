# -*- coding: utf-8 -*-
# Given a string representing an expression of fraction addition and subtraction, you need to return the calculation
# result in string format. The final result should be irreducible fraction. If your final result is an integer,
# say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be
# converted to 2/1.
#
# Example 1:
# Input:"-1/2+1/2"
# Output: "0/1"
# Example 2:
# Input:"-1/2+1/2+1/3"
# Output: "1/3"
# Example 3:
# Input:"1/3-1/2"
# Output: "-1/6"
# Example 4:
# Input:"5/3+1/3"
# Output: "2/1"
# Note:
# The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
# Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is
# positive, then '+' will be omitted.
# The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will
# always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction
#  format defined above.
# The number of given fractions will be in the range [1,10].
# The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.


import re


class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        expression += '+'
        answer, start = '0/1', 0
        for i in xrange(1, len(expression)):
            if expression[i] in ['+', '-']:
                num = expression[start:i]
                answer = self.add(answer, num)
                start = i

        return answer if answer[0] != '+' else answer[1:]  # bugfixed

    def add(self, a, b):  # -1/3 + 2 /5
        if a == '0/1':
            return b
        (an, ad), (bn, bd) = map(int, a.split('/')), map(int, b.split('/'))  # (-1,3), (2,5)
        an = an * bd + ad * bn
        ad = ad * bd
        l = abs(self.gcd(an, ad))
        an /= l
        ad /= l

        return str(an) + '/' + str(ad)

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def fractionAddition2(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if (expression == ""): return "0/1"

        fracs = map(int, re.findall('[+-]?\d+', expression))

        sumN = fracs[0]
        sumD = fracs[1]

        for i in xrange(2, len(fracs), 2):
            gcd = self.gcd(sumD, fracs[i + 1])
            lcm = (sumD * fracs[i + 1]) / gcd
            sumN = (lcm / sumD) * sumN + (lcm / fracs[i + 1]) * fracs[i]
            sumD = lcm

            d = self.gcd(sumN, sumD)
            sumN = sumN / d
            sumD = sumD / d

        if (sumN % sumD == 0):
            sumN = sumN / sumD
            sumD = 1

        if (sumN == 0):
            frac = "0/1"
        elif (sumN < 0 and sumD > 0):
            frac = "-" + str(sumN * -1) + "/" + str(sumD)
        elif (sumN > 0 and sumD < 0):
            frac = "-" + str(sumN) + "/" + str(sumD * -1)
        else:
            frac = str(sumN) + "/" + str(sumD)

        return frac


if __name__ == '__main__':
    a = "1/2+1/2+1/3-3/7"
    b = re.split('-|\+', a)  # knowledge how to use regex to split string
    fracs = map(int, re.findall('[+-]?\d+', a))  # knowledge how regex parse the expression
    c, d = map(int, "-3/5".split('/'))
    print b, c, d, fracs

    print Solution().fractionAddition("-1/2+1/2+1/3")
