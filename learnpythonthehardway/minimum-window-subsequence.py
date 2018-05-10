# Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.
#
# If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple
# such minimum-length windows, return the one with the left-most starting index.
#
# Example 1:
# Input:
# S = "abcdebdde", T = "bde"
# Output: "bcde"
# Explanation:
# "bcde" is the answer because it occurs before "bdde" which has the same length.
# "deb" is not a smaller window because the elements of T in the window must occur in order.
# Note:
#
# All the strings in the input will only contain lowercase letters.
# The length of S will be in the range [1, 20000].
# The length of T will be in the range [1, 100].

class Solution(object):
    def minWindow(self, S, T):
        """
        :param S: str
        :param T: str
        :return: str
        """
        m, n = len(T), len(S)
        dp = [[-1] * n for _ in xrange(m)]
        for j in xrange(n):
            if S[j] == T[0]:
                dp[0][j] = j  # the meaning of dp[i][j] means for T' str (0,i) which is subsequence of S(0,j), the start
                # position in S
            # else:
            #     dp[0][j] = dp[0][j-1]

        for i in xrange(1, m):
            k = -1
            for j in xrange(i,n):
                if k != -1 and S[j] == T[i]:
                    dp[i][j] = k
                # else:
                #     dp[i][j] = dp[i-1][j]
                # dp[i][j] = dp[i-1][j-1] if S[j] == T[i] else dp[i-1][j]
                if dp[i - 1][j] != -1:
                    k = dp[i - 1][j]


        start, length = -1, float('inf')
        for j in xrange(n):
            if dp[m - 1][j] >= 0 and length > j - dp[m - 1][j] + 1:
                start, length = dp[m - 1][j], j - dp[m - 1][j] + 1

        print dp

        return "" if start == -1 else S[start:start + length]


if __name__ == '__main__':
    # print Solution().minWindow('abcdebdde', 'bde')
    print Solution().minWindow('fgrqsqsnodwmxzkzxwqegkndaa', 'fnok') # expected fgrqsqsnodwmxzk
