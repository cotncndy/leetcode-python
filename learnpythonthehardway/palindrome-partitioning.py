# Time:  O(n^2 ~ 2^n)
# Space: O(n^2)
#
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
#   [
#     ["aa","b"],
#     ["a","a","b"]
#   ]

# Time:  O(n^2 ~ 2^n)
# Space: O(n^2)
# dynamic programming solution
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        n = len(s)

        is_palindrome = [[False for j in xrange(n)] for i in xrange(n)]
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                is_palindrome[i][j] = s[i] == s[j] and ((j - i < 2) or is_palindrome[i + 1][j - 1])

        dp = [[] for i in xrange(n)]
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                if is_palindrome[i][j]:  # if [i][j] is palindrome
                    if j + 1 < n:  # if we have another part starting from j+1
                        for k in dp[j + 1]:
                            dp[i].append([s[i:j + 1]] + k)  # bugfixed
                    else:
                        dp[i].append([s[i:j + 1]])  # bugfixed
        return dp[0]


if __name__ == "__main__":
    print Solution().partition("aab")
