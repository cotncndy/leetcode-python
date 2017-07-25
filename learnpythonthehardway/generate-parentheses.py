# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(n)
#
# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"
#

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        res = []
        self.generateHelper('', n, n, res)
        return res

    def generateHelper(self, cur, left, right, res):
        if left == 0 and right == 0:
            res += cur,

        if left > 0:
            self.generateHelper(cur + '(', left - 1, right, res)
        if right > left:
            self.generateHelper(cur + ')', left, right - 1, res)


if __name__ == "__main__":
    print Solution().generateParenthesis(3)
