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
        chars = ''.join(k * (v / 2) for k, v in cnt.iteritems())

        res = []
        self.permute(chars, 0, mid, res)
        return res

    def permute(self, chars, start, mid, res):
        if start == len(chars):
            res.append(chars + mid + chars[::-1])

        for i in xrange(start, len(chars)):
            if i != start and chars[i] == chars[start]:
                continue
            st = list(chars)
            st[i], st[start] = st[start], st[i]
            self.permute(''.join(st), start + 1, mid, res)


if __name__ == '__main__':
    print Solution().generatePalindromes('abcdbac')
