# There is a strange printer with the following two special requirements:
#
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at any places, and will cover the
# original existing characters.
# Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer
#  needed in order to print it.
#
# Example 1:
# Input: "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# Example 2:
# Input: "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the
# existing character 'a'.
# Hint: Length of the given string will not exceed 100.


class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 0
        dp = [[float('inf')] * l for _ in xrange(l)] # from ith to jth char, the min steps to print them
        dp[0][0] = 1


        for gap in xrange(0, l):
            for start in xrange(0,l-gap):
                if gap == 0:
                    dp[start][start+gap] = 1
                    continue
                t = dp[start][start+gap]
                if s[start+gap] == s[start+gap-1]:
                    t = min(t,dp[start][start+gap-1])
                elif s[start] == s[start+1]:
                    t = min(t,dp[start+1][start+gap])
                else:
                    t = min(t, dp[start+1][start+gap]+1, dp[start][start+gap-1]+1)

                for k in xrange(start+1, start+gap+1):
                    if s[k] == s[start]:
                        t = min(t,dp[k][start + gap])
                dp[start][start+gap] = t

        return dp[0][l-1]

    def strangePrinter2(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 0
        dp = [[float('inf')] * l for _ in xrange(l)] # from ith to jth char, the min steps to print them

        for gap in xrange(0, l):
            for start in xrange(0,l-gap):
                if gap == 0:
                    dp[start][start+gap] = 1
                    continue
                t = dp[start][start+gap]
                t = min(t, dp[start+1][start+gap]+1, dp[start][start+gap-1]+1)

                for k in xrange(start+1, start+gap+1):
                    if s[k] == s[start]:
                        if k - 1 >= start+1:
                            t = min(t, dp[start+1][k-1] + dp[k][start + gap])
                        else:
                            t = min(t, dp[k][start+gap])
                dp[start][start+gap] = t

        return dp[0][l-1]
if __name__ == '__main__':
    print Solution().strangePrinter("aaabbb")
    print Solution().strangePrinter2("aaabbb")
    print Solution().strangePrinter("aba")
    print Solution().strangePrinter2("aba")
    print Solution().strangePrinter("abbac")
    print Solution().strangePrinter2("abbac")
    print Solution().strangePrinter("tbgtgb")
    print Solution().strangePrinter2("tbgtgb")










