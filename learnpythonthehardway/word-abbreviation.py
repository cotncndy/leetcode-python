# Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations
# for every word following rules below.
#
# Begin with the first character and then the number of characters abbreviated, which followed by the
# last character.
# If there are any conflict, that is more than one words share the same abbreviation, a longer
# prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
# If the abbreviation doesn't make the word shorter, then keep it as original.
#
# Example:
# Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
# Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
#
# Note:
# Both n and the length of each word will not exceed 400.
# The length of each word is greater than 1.
# The words consist of lowercase English letters only.
# The return answers should be in the same order as the original array.
import collections


class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        n = len(dict)
        res, pre = [''] * n, [1] * n  # bugfixed

        for i in xrange(n):
            res[i] = self.abbrev(dict[i], pre[i])

        for i in xrange(n):
            while True:
                word_set = set()
                for j in xrange(i + 1, n):
                    if res[j] == res[i]:
                        word_set.add(j)
                if not word_set:
                    break
                word_set.add(i)
                for k in word_set:
                    pre[k] += 1
                    res[k] = self.abbrev(dict[k], pre[k])

        return res

    def abbrev(self, s, k):
        return s if k >= len(s) - 2 else s[0:k] + str(len(s) - k - 1) + s[-1]

    def wordsAbbreviation2(self, ds):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        return self.wa2(ds)

    def wa1(self, ds):

        ns = {}
        for s in ds:
            n = len(s)
            ns[n] = ns.get(n, [])
            ns[n].append(s)
        for n in ns:
            ns[n].sort(key=lambda s: s[0] + s[-1] + s[1:-1])

        def diff(s, t):
            i = 0
            for i in xrange(len(s)):
                if s[i] != t[i]:
                    break
            return i + 1

        ss = {}
        for n in ns:
            for i, s in enumerate(ns[n]):
                ret = 1
                for j in xrange(i - 1, -1, -1):
                    t = ns[n][j]
                    if s[0] != t[0] or s[-1] != t[-1]:
                        break
                    ret = max(ret, diff(s, t))
                for j in xrange(i + 1, len(ns[n])):
                    t = ns[n][j]
                    if s[0] != t[0] or s[-1] != t[-1]:
                        break
                    ret = max(ret, diff(s, t))
                ss[s] = ret

        def pshort(s):
            i = ss[s]
            zs = str(len(s) - 1 - i)
            size = i + len(zs) + 1
            return s[:i] + zs + s[-1] if size < len(s) else s

        return [pshort(s) for s in ds]

    def wa2(self, ds):

        ns = {}
        for s in ds:
            key = (len(s), s[0], s[-1])  # knowledge how to write a compound key in python
            ns[key] = ns.get(key, [])  # knowledge for hashmap, get(key, optional] , like java getOrDefault()
            ns[key].append(s)
        for key in ns:
            ns[key].sort()

        def diff(s, t):
            i = 0
            for i in xrange(len(s)):
                if s[i] != t[i]:
                    break
            return i + 1

        ss = {}
        for n in ns:
            for i, s in enumerate(ns[n]):
                ret = 1
                for j, t in enumerate(ns[n]):
                    if i == j: continue
                    ret = max(ret, diff(s, t))
                ss[s] = ret

        def pshort(s):
            i = ss[s]
            zs = str(len(s) - 1 - i)
            size = i + len(zs) + 1
            return s[:i] + zs + s[-1] if size < len(s) else s

        return [pshort(s) for s in ds]

    def wordsAbbreviation3(self, A):
        """
        :type dict: List[str]
        :rtype: List[str]
        """

        def longest_common_prefix(a, b):
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:
                i += 1
            return i

        ans = [None for _ in A]
        # create a hash table, with key as (len(word), word[0]), word[-1]) and value as (word, index)
        groups = collections.defaultdict(list)
        for index, word in enumerate(A):
            groups[len(word), word[0], word[-1]].append((word, index))
        # iterate key and values, sort the value array first, longest common prefix start with 0
        for (size, first, last), enum_words in groups.iteritems():
            enum_words.sort()
            lcp = [0] * len(enum_words)
            for i, (word, _) in enumerate(enum_words):
                if i:
                    word2, _ = enum_words[i - 1]
                    p = longest_common_prefix(word, word2)
                    lcp[i] = max(lcp[i], p)
                    lcp[i - 1] = max(lcp[i - 1], p)
                    # zip word, and lcp together, create answer.
            for (word, index), p in zip(enum_words, lcp):
                delta = size - 2 - p
                if delta <= max(1, len(str(delta)) - 1):
                    ans[index] = word
                else:
                    ans[index] = word[:p + 1] + str(delta) + last

        return ans


if __name__ == '__main__':
    dict = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
    print Solution().wordsAbbreviation2(dict)
