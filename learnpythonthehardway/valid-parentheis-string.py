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
        if not s and not len(st):  # bugfixed when s is empty but st is not empty, is is false
            return True
        for i in xrange(len(s)):
            c = s[i]
            if c in ['(', '*']:
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
                    r = self.helper(s[i:], temp)
                    if r:
                        return True
            # else:  # if it is '*', we could push  or not push or pop
            #     if st and st[-1] == '(':
            #         temp = []
            #         temp.extend(st)
            #         temp.pop()  # we pop
            #         r = self.helper(s[i + 1:], temp)
            #         if r:
            #             return True

        while len(st) > 1 and st[-1] == '*' and st[-2] == '(':
            st.pop()
            st.pop()
        return False if len(st) else True

    def checkValidString2(self, s):
        left, star = [], []
        for n, c in enumerate(s):
            if c == '(':
                left.append(n)
            elif c == '*':
                star.append(n)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()

        while left and star:
            if left[-1] > star[-1]:
                return False
            left.pop()
            star.pop()

        return len(left) == 0








if __name__ == '__main__':
    print Solution().checkValidString("()")  # True
    print Solution().checkValidString("(()")  # False
    print Solution().checkValidString("(())")  # True
    print Solution().checkValidString("(*)")  # True

    print Solution().checkValidString("(*()")  # TRUE

    print Solution().checkValidString("(*))")  # True

    print Solution().checkValidString("*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)")  # True
    print Solution().checkValidString("(((((()*)(*)*))())())(()())())))((**)))))(()())()")  # False

    # print Solution().checkValidString("(*())") # True
    # print Solution().checkValidString("(())") # True
    # print Solution().checkValidString("((*))")
    # print Solution().checkValidString("((**")
    # print Solution().checkValidString("((**(")
    # print Solution().checkValidString("((**))")
