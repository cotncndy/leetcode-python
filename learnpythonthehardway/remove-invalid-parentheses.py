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

    def removeInvalidParentheses2(self, s):
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

        def find_min_remove(s):
            left_remove, right_remove = 0, 0
            for i in s:
                if i == '(':
                    left_remove += 1
                elif i == ')':
                    if not left_remove:
                        right_remove += 1
                    else:
                        left_remove -= 1

        que, visited, found, res = [s], set(), False, []
        visited.add(s)
        (left_remove, right_remove) = find_min_remove(s)

        while que:
            t = que.pop(0)
            if is_valid(t):
                res += t,
                found = True  # notice don't forget
            if found:
                continue  # notice, if found already, no need to go further, since min remove required

            for i in xrange(len(t)):
                if left_remove > 0:
                    if
                if t[i] == '(' or t[i] == ')':
                    k = t[i + 1::] if i == 0 else t[:i:] + t[i + 1::]
                    if k not in visited:
                        visited.add(k)
                        que.append(k)

        return res

    # 43ms
    def removeInvalidParentheses3(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.remove_helper(s, ans, 0, 0, ['(', ')'])

        return ans

    def remove_helper(self, s, ans, last_i, last_j, par):
        counter = 0
        for i in xrange(last_i, len(s)):
            if s[i] == par[0]:
                counter += 1
            if s[i] == par[1]:
                counter -= 1
            if counter >= 0:
                continue
            for j in xrange(last_j, i + 1):
                if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                    self.remove_helper(s[0:j] + s[j + 1:len(s)], ans, i, j, par)
            return

        reversed_s = s[::-1]

        if par[0] == '(':
            self.remove_helper(reversed_s, ans, 0, 0, [')', '('])
        else:
            ans.append(reversed_s)


if __name__ == '__main__':
    print Solution().removeInvalidParentheses('()())()')
