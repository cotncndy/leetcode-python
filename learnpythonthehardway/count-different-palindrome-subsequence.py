# Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number
# modulo 10^9 + 7.
#
# A subsequence of a string S is obtained by deleting 0 or more characters from S.
#
# A sequence is palindromic if it is equal to the sequence reversed.
#
# Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.
#
# Example 1:
# Input:
# S = 'bccb'
# Output: 6
# Explanation:
# The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
# Note that 'bcb' is counted only once, even though it occurs twice.
# Example 2:
# Input:
# S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
# Output: 104860361
# Explanation:
# There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
# Note:
#
# The length of S will be in the range [1, 1000].
# Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.

class Solution(object):
    def countPalindromicSubsequences(self, S):
        N = len(S)
        A = [ord(c) - ord('a') for c in S]
        prv = [None] * N
        nxt = [None] * N

        last = [None] * 4
        for i in xrange(N):
            last[A[i]] = i
            prv[i] = tuple(last)

        last = [None] * 4
        for i in xrange(N - 1, -1, -1):
            last[A[i]] = i
            nxt[i] = tuple(last)

        MOD = 10 ** 9 + 7
        memo = [[None] * N for _ in xrange(N)]

        def dp(i, j):
            if memo[i][j] is not None:
                return memo[i][j]
            ans = 1
            if i < j:
                for x in xrange(4):
                    i0 = nxt[i][x]
                    j0 = prv[j][x]
                    if i <= i0 <= j:
                        ans += 1
                    if None < i0 < j0:
                        ans += dp(i0 + 1, j0 - 1)
            ans %= MOD
            memo[i][j] = ans
            return ans

        return dp(0, N - 1) - 1

    def countPalindromicSubsequences2(self, S):
        """
        :type S: str
        :rtype: int
        """
        N = len(S)
        last, prev, next = [None] * 4, [None] * N, [None] * N

        A = [ord(i) - ord('a') for i in S]

        for i in xrange(N):
            last[A[i]] = i
            prev[i] = tuple(last)

        last = [None] * 4

        for i in xrange(N - 1, -1, -1):
            last[A[i]] = i
            next[i] = tuple(last)

        MOOD, memo = 10 ** 9 + 7, [[None] * N for _ in xrange(N)]

        def dp(i, j):
            if memo[i][j] is not None:
                return memo[i][j]
            ans = 1
            if i <= j:  # bugfixed should be i <= j instead of i < j
                for x in xrange(4):  # only a,b,c,d 4 chars
                    i0 = next[i][x]
                    j0 = prev[j][x]

                    if i <= i0 <= j:  # there is an 'x' (a or b or c or d) there
                        ans += 1
                    if None < i0 < j0:
                        ans += dp(i0 + 1, j0 - 1)

            ans %= MOOD
            memo[i][j] = ans

            return memo[i][j]

        return dp(0, N - 1) - 1


if __name__ == '__main__':
    # print Solution().countPalindromicSubsequences('abbcab')
    print Solution().countPalindromicSubsequences2('')
