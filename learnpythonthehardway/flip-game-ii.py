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

    def plan_a(s):
        sub = set()
        for game in s.split('-'):
            if not game: continue
            n = len(game)
            if n in sub:
                sub.remove(n)
            else:
                sub.add(n)
        if not sub: return False
        N = max(sub) + 1
        nims = [0] * N

        def mex(sub):
            i = 0
            while i in sub: i += 1
            return i

        for i in range(2, N):
            s = set()
            for j in range(i // 2):
                s.add(nims[j] ^ nims[i - j - 2])
            nims[i] = mex(s)

        r = 0
        for n in sub: r ^= nims[n]
        return bool(r)

    class Solution2(object):
        def canWin(self, s):
            """
            :type s: str
            :rtype: bool
            """
            return plan_a(s)

    def canWin3(self, s):
        """
        :type s: str
        :rtype: bool
        """
        f = [0, 0]
        n = len(s)
        for i in range(2, n + 1):
            dic = set()
            for j in range(i - 1):
                dic.add(f[i - j - 2] ^ f[j])
            g = sorted(list(dic))
            for j in range(len(g)):
                if g[j] != j:
                    f.append(j)
                    break
            if len(f) != i + 1:
                f.append(len(g))
        print f
        g = s.split('-')
        res = 0
        for i in g:
            res ^= f[len(i)]
        return res != 0
