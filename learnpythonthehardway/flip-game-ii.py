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
                if self.canWin(''.join(st)):
                    return True

        return False
