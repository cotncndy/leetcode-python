# Time:  O(n * n!)
# Space: O(n)

import collections


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt = collections.Counter(s)
        mid = ''.join(k for k, v in cnt.iteritems() if v % 2)  # knowledge python syntaxx
        if len(mid) > 1:
            return []
        chars = ''.join(k * (v / 2) for k, v in cnt.iteritems())

        res = []
        self.permute(chars, 0, mid, res)
        return res

    def permute(self, chars, start, mid, res):
        if start == len(chars):
            w = chars + mid + chars[::-1]
            if w not in res:  # bugfixed would decrease the performance
                res.append(chars + mid + chars[::-1])

        for i in xrange(start, len(chars)):
            if i != start and chars[i] == chars[start]:
                continue
            st = list(chars)
            st[i], st[start] = st[start], st[i]
            self.permute(''.join(st), start + 1, mid, res)

    def generatePalindromes2(self, s):
        cnt = collections.Counter(s)
        mid = ''.join(k for k, v in cnt.iteritems() if v % 2)
        if len(mid) > 1:
            return []
        chars = ''.join(k * (v / 2) for k, v in cnt.iteritems())

        used, res = [False] * len(chars), []
        self.permute2(chars, mid, used, [], res)

        return res

    def permute2(self, chars, mid, used, cur, res):
        if len(cur) == len(chars):
            half_palindrome = ''.join(cur)
            res.append(half_palindrome + mid + half_palindrome[::-1])
            return

        for i in xrange(len(chars)):
            if not used[i] and not (i > 0 and chars[i - 1] == chars[i] and used[i - 1]):
                used[i] = True
                cur.append(chars[i])
                self.permute2(chars, mid, used, cur, res)
                cur.pop()
                used[i] = False





if __name__ == '__main__':
    print Solution().generatePalindromes2('aaaabbbb')
