# Time:  O(n)
# Space: O(n)
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}"
# are all valid but "(]" and "([)]" are not.
#

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}

        for p in s:
            if p in lookup:
                stack.append(p)
            elif len(stack) == 0 or lookup[stack.pop()] != p:
                return False

        return len(stack) == 0
