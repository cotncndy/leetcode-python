# Time:  O(n * 2^n)
# Space: O(n)

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """

        def backtrack(word, i, cur, res):
            if i == len(word):
                res.append(''.join(cur))
                return
            cur.append(word[i])
            backtrack(word, i + 1, cur, res)
            cur.pop()

            if not cur or not cur[-1][-1].isdigit():
                for l in xrange(1, len(word) - i + 1):
                    cur.append(str(l))
                    backtrack(word, i + l, cur, res)
                    cur.pop()

        res = []
        backtrack(word, 0, [], res)
        return res


if __name__ == '__main__':
    print Solution().generateAbbreviations('word')
