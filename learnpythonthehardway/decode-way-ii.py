# A message containing letters from A-Z is being encoded to numbers using the following mapping way:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers
# from 1 to 9.
#
# Given the encoded message containing digits and the character '*', return the total number of ways to decode it.
#
# Also, since the answer may be very large, you should return the output mod 109 + 7.
#
# Example 1:
# Input: "*"
# Output: 9
# Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
# Example 2:
# Input: "1*"
# Output: 9 + 9 = 18
# Note:
# The length of the input string will fit in range [1, 105].
# The input string will only contain the character '*' and digits '0' - '9'.


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        m, dp = 10**9 + 7, [0] * len(s) + 1
        dp[1] = 1 if s[0] != '*' else 9
        for i in xrange(2,len(s) + 1):
            dp[i] = 0
            if s[i] != '0' and s[i] != '*':
                dp[i] = dp[i-1]
            if s[i] != '*':
                if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                    dp[i] = (dp[i-1] + dp[i-2]) % m
            else :
                if s[i-1] == '0' or s[i-1] > '2':
                    dp[i] =  (10 * dp[i-2]) % m
                elif s[i-1] == '1':
                    dp[i] = (dp[i-2] + 10 * dp[i-1]) % m
                elif s[i-1] == '2':
                    dp[i] = (dp[i-2] + 7 * dp[i-1]) % m
                elif s[i-1] == '*':
                    dp[i] = dp[i-1]  # how to handle 1121**, so we need to divide the result into 4 pars end with 0, 1, 2, and > 2







