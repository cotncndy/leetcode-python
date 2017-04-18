# Time:  O(n) ~ O(n^2)
# Space: O(n)

# Given a string array words, find the maximum value of
# length(word[i]) * length(word[j]) where the two words
# do not share common letters. You may assume that each
# word will contain only lower case letters. If no such
# two words exist, return 0.
#
# Example 1:
# Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# Return 16
# The two words can be "abcw", "xtfn".
#
# Example 2:
# Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# Return 4
# The two words can be "ab", "cd".
#
# Example 3:
# Given ["a", "aa", "aaa", "aaaa"]
# Return 0
# No such pair of words.
#
# Follow up:
# Could you do better than O(n2), where n is the number of words?

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bit_res = [0] * len(words)
        maxLen = 0
        for i, w in enumerate(words):
            for c in w:
                bit_res[i] |= ( 1 << (ord(c)-ord('a')))

            for j in xrange(i):
                if not(bit_res[i] & bit_res[j]):
                   maxLen = max(maxLen, len(w) * len(words[j]))

        return maxLen
