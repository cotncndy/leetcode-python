# Find the largest palindrome made from the product of two n-digit numbers.
#
# Since the result could be very large, you should return the largest palindrome mod 1337.
#
# Example:
#
# Input: 2
#
# Output: 987
#
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
#
# Note:
#
# The range of n is [1,8].

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in reversed(xrange(10 ** n)):
            for j in reversed(xrange(10 ** n)):
                if self.isPalindrome(i * j):
                    return i * j % 1337

    def isPalindrome(self, num):
        res, n = 0, num
        while n:
            r = n % 10
            res = res * 10 + r
            n /= 10

        if res == num:
            return True
        return False

    def largestPalindrome2(self, n):
        upper = 10 ** n - 1
        lower = upper / 10
        for i in reversed(xrange(lower + 1, upper + 1)):  # fix the lower bound bug
            s = str(i) + str(i)[::-1]
            j = upper
            while j * j > int(s):
                if long(s) % j == 0:
                    return long(s) % 1337
                j -= 1
        return 9

if __name__ == '__main__':
    # print Solution().largestPalindrome(8)
    print Solution().largestPalindrome2(1)
