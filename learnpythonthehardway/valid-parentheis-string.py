# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this
# string is valid. We define the validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
# Example 1:
# Input: "()"
# Output: True
# Example 2:
# Input: "(*)"
# Output: True
# Example 3:
# Input: "(*))"
# Output: True


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        return self.helper(s, st)

    def helper(self, s, st):
        if not s:
            return True
        for i in xrange(len(s)):
            c = s[i]
            if c == '(':
                st.append(c)
            elif c == ')':
                if not st:
                    return False
                if st[-1] == '(':
                    st.pop()
                elif st[-1] == '*':  # if it is '*' we could pop or not
                    temp = []
                    temp.extend(st)
                    temp.pop()
                    r = self.helper(s[i + 1:], temp)
                    if r:
                        return True
            else:  # if it is '*', we could push  or not push or pop
                temp = []
                temp.extend(st)
                r = self.helper(s[i + 1:], temp)
                if r:
                    return True
                if st and st[-1] == '(':
                    temp = []
                    temp.extend(st)
                    temp.pop()  # we pop
                    r = self.helper(s[i + 1:], temp)
                    if r:
                        return True


        return False if len(st) else True


if __name__ == '__main__':
    # print Solution().checkValidString("()")
    # print Solution().checkValidString("(()")
    # print Solution().checkValidString("(())")
    # print Solution().checkValidString("(*)")
    #
    # print Solution().checkValidString("(*()")

    print Solution().checkValidString("(*())")
    print Solution().checkValidString("(())")
    print Solution().checkValidString("((*))")
    print Solution().checkValidString("((**")
    print Solution().checkValidString("((**(")
    print Solution().checkValidString("((**))")
