# Time:  O(n)
# Space: O(1)

class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        if not expression:
            return ""
        for i in expression[::-1]:
            if stack and stack[-1] == '?':
                stack.pop()  # pop the '?'
                first = stack.pop()  # pop the second one
                stack.pop()  # pop the ':'
                second = stack.pop()

                if i == 'T':
                    stack.append(first)
                else:
                    stack.append(second)
            else:
                stack.append(i)

        return str(stack.pop())

    def parseTernary2(self, expression):
        st = []
        for i in reversed(xrange(0, len(expression))):
            if expression[i] == '?':
                first, second = st.pop(), st.pop()
                if expression[i - 1] == 'T':
                    st.append(first)
                else:
                    st.append(second)

            elif expression[i] == ':' or (i < len(expression) - 1 and expression[i + 1] == '?'):
                continue
            else:
                st.append(expression[i])

        return str(st.pop())



if __name__ == '__main__':
    print Solution().parseTernary2("F?1:T?4:5")
    print Solution().parseTernary2("T?T?F:5:3")

    print Solution().parseTernary("F?1:T?4:5")
    print Solution().parseTernary("T?T?F:5:3")
