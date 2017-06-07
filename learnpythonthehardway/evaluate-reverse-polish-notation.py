# Time:  O(n)
# Space: O(n)
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
#
import operator


class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        numerials, operators = [], {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
        for token in tokens:
            if token not in operators:
                numerials.append(int(token))
            else:
                y, x = numerials.pop(), numerials.pop()
                numerials.append(operators[token](x * 1.0, y))

        return numerials.pop()


if __name__ == "__main__":
    print Solution().evalRPN(["2", "1", "+", "3", "*"])
    print Solution().evalRPN(["4", "13", "5", "/", "+"])
    print Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
