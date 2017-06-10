# Time:  O(n)
# Space: O(n)
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces . The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# Note: Do not use the eval built-in library function.
#

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        res, operand, operands, sign = 0, "", [], '+'
        for i in xrange(len(s)):
            if s[i].isdigit():
                operand += s[i]
            # don't forget this one 'i==len(s)-1' , otherwise , such as 1+2, when reach 2, you loop is over already
            # also remember that you can not use elif here
            if (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
                temp = 0
                if operand != "":
                    temp = int(operand[::1])
                # don't forget this
                operand = ""
                if sign == '+':
                    operands.append(temp)
                elif sign == '-':
                    operands.append(-temp)
                elif sign == '*':
                    t = operands[-1]
                    operands.pop()
                    operands.append(t * temp)
                elif sign == '/':
                    t = operands[-1]
                    operands.pop()
                    operands.append(int(t * 1.0 / temp))
                sign = s[i]

        while operands:
            res += operands[-1]
            operands.pop()

        return res


if __name__ == '__main__':
# print Solution().calculate("1 + 2 * 3 / 6")
# print Solution().calculate("42")
print Solution().calculate("14 - 3 / 2")
