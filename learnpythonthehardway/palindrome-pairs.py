# Time:  O(n * k^2), n is the number of the words, k is the max length of the words.
# Space: O(n * k)

# Given a list of unique words. Find all pairs of indices (i, j)
# in the given list, so that the concatenation of the two words,
# i.e. words[i] + words[j] is a palindrome.
#
# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]
# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res, lookup = [], {}
        for i, w in enumerate(words):
            lookup[w] = i

        for i in xrange(len(words)):
            # don't remember  + 1, otherwise, you would not get last char
            for j in xrange(len(words[i]) + 1):
                suffix = words[i][j:]
                prefix = words[i][:j]
                # dont' forget to check if j > 0 or not, when j = 0, empty string
                if j > 0 and prefix == prefix[::-1] and suffix[::-1] in lookup and lookup[suffix[::-1]] != i:
                    res.append([lookup[suffix[::-1]], i])
                # if the second substr is a palindrome, for ex, xxxab, you just need to do baxxxab, then you get a palindrome
                if suffix == suffix[::-1] and prefix[::-1] in lookup and lookup[prefix[::-1]] != i:
                    res.append([i, lookup[prefix[::-1]]])

        return res

        # todo, manacher and trie ways to crack this issue.


if __name__ == '__main__':
    print Solution().palindromePairs(["abcd", "dcba", "lls", "s", "ssll"])
