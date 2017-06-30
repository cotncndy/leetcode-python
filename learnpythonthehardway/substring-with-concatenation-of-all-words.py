# Time:  O(m * n * k), where m is string length, n is dictionary size, k is word length

# Space: O(n * k)
#
# You are given a string, S, and a list of words, L, that are all of the same length.
# Find all starting indices of substring(s) in S that is a concatenation of each word
# in L exactly once and without any intervening characters.
#
# For example, given:
# S: "barfoothefoobarman"
# L: ["foo", "bar"]
#
# You should return the indices: [0,9].
# (order does not matter).
#
import collections


class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        res, words_num, word_len = [], len(L), len(L[0])
        words = collections.defaultdict(int)
        for w in L:
            words[w] += 1
        for i in xrange(0, len(S) - words_num * word_len):
            contrasts = collections.defaultdict(int)
            for j in xrange(word_len):
                t = S[i + j * word_len: i + word_len * (j + 1)]
                if words[t] == 0:
                    break;
                contrasts[t] += 1
                if contrasts[t] > words[t]:
                    break;
            if j == word_len - 1:
                res.append(i)

        return res


if __name__ == "__main__":
    print Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])
