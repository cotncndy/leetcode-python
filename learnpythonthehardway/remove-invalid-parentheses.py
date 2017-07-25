# Time:  O(C(n, c)), try out all possible substrings with the minimum c deletion.
# Space: O(c), the depth is at most c, and it costs n at each depth
#
# Remove the minimum number of invalid parentheses in order to
# make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the
# parentheses ( and ).
#
# Examples:
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]
#

# DFS solution.
class Solution(object):
    # review BFS
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def is_valid(s):
            cnt = 0
            for i in s:
                if i == '(':
                    cnt += 1
                elif i == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        que, visited, found, res = [s], set(), False, []
        visited.add(s)

        while que:
            t = que.pop(0)
            if is_valid(t):
                res += t,
                found = True  # notice don't forget
            if found:
                continue  # notice, if found already, no need to go further, since min remove required

            for i in xrange(len(t)):
                if t[i] == '(' or t[i] == ')':
                    k = t[i + 1::] if i == 0 else t[:i:] + t[i + 1::]
                    if k not in visited:
                        visited.add(k)
                        que.append(k)

        return res


if __name__ == '__main__':
    print Solution().removeInvalidParentheses('()())()')
