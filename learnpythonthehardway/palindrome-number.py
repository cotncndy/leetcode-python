# Time:  O(1)
# Space: O(1)
#
# Determine whether an integer is a palindrome. Do this without extra space.
#
# Some hints:
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
# you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.
#

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False

        copy, res = x, 0

        while copy:
            res *= 10
            res += copy % 10
            copy /= 10

        return res == x
