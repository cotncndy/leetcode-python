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
        for c in s:
            if c.isdigit():
                operand += c
            elif c != ' ':
                temp = int(operand[::-1])
                # don't forgee this
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
                    operands.append(t / temp)
                sign = c

        while operands:
            res += operands[-1]
            operands.pop()

        return res


if __name__ == '__main__':
    print Solution().calculate("1 + 2 * 3")
