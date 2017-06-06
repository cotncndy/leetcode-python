# Time:  O(n)
# Space: O(1)
#
# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
#
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
#

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, start, indices = 0, -1, []

        for i in xrange(len(s)):
            if s[i] == '(':
                indices.append(i)
            elif not indices:
                start = i
            else:
                indices.pop()
                if not indices:
                    longest = max(longest, i - start)
                else:
                    longest = max(longest, i - indices[-1])

        return longest


if __name__ == "__main__":
    print Solution().longestValidParentheses("()")
    print Solution().longestValidParentheses(")())())")
    print Solution().longestValidParentheses("))(()())")
