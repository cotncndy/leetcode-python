# Time:  O(n + c^2)
# Space: O(c)

# The best theory solution (DP, O(n + c^2)) could be seen here:
# https://leetcode.com/discuss/64344/theory-matters-from-backtracking-128ms-to-dp-0m
class Solution(object):
    def canWin(self, s):
        for i in xrange(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                st = list(s)
                st[i], st[i + 1] = '-', '-'
                if not self.canWin(''.join(st)):  # bugfixed
                    return True

        return False

    def canWin2(self, s):
        winset = set()

        return self.helper(s, winset)

    def helper(self, s, winset):  # review top-down dp, memo, so great
        if not s or len(s) < 2:
            return False

        if s in winset:
            return True

        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                sub = s[:i] + '--' + s[i + 2:]

                if not self.helper(sub, winset):
                    winset.add(s)
                    return True
        return False
