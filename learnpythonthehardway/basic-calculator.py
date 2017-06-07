# Time:  O(n)
# Space: O(n)
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ),
# the plus + or minus sign -, non-negative integers and empty spaces .
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
#

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        pre, stack, temp, total = 1, [], 0, 0
        stack.append(pre)

        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append(pre)
            elif s[i] == ')':
                stack.pop()
            elif s[i] == '+' or s[i] == '-':
                total += pre * temp
                pre = -1 * stack[-1] if s[i] == '-' else stack[-1]
                temp = 0
            elif s[i].isdigit():
                temp = temp * 10 + int(s[i])

        return total + pre * temp


if __name__ == '__main__':
    print Solution().calculate("1-(2-3)")
