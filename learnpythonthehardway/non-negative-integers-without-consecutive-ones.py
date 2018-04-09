# Given a positive integer n, find the number of non-negative integers less than or equal to n, whose binary
# representations do NOT contain consecutive ones.
#
# Example 1:
# Input: 5
# Output: 5
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
# Note: 1 <= n <= 109
import math


class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """

        def hasConsecutiveOnes(n):
            for i in xrange(1, len(n)):
                if n[i] == n[i - 1] and n[i] == '1':
                    return True

            return False

        count = 0
        for i in xrange(num + 1):
            if hasConsecutiveOnes(bin(i)[2:]):  # knowledge how to convert num to binay string, it has '0b10101' format
                continue
            count += 1

        return count

    def findIntegers2(self, num):
        """
        :type num: int
        :rtype: int
        """
        dp = [0] * (num + 1)
        dp[0] = 1
        for i in xrange(1, num + 1):
            if self.isConsecutiveOnes(i):
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 1] + 1

        return dp[num]

    def isConsecutiveOnes(self, n):
        st = bin(n)[2:]
        for i in xrange(1, len(st)):
            if st[i] == st[i - 1] and st[i] == '1':
                return True
        return False



if __name__ == '__main__':
    print Solution().findIntegers(5)
    print Solution().findIntegers2(5)
    print Solution().findIntegers(50)
    print Solution().findIntegers2(50)
    # print Solution().findIntegers(10000000)
    print Solution().findIntegers2(10000000)
