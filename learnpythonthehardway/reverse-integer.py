# Time:  O(logn) = O(1)
# Space: O(1)
#
# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# click to show spoilers.
#
# Have you thought about this?
# Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
#
# If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
#
# Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer,
# then the reverse of 1000000003 overflows. How should you handle such cases?
#
# Throw an exception? Good, but what if throwing an exception is not an option?
# You would then have to re-design the function (ie, add an extra parameter).

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)
        res = 0
        while x:
            if abs(res) > 0x7fffffff / 10:  # review for python, division for negative doesn't work, need to figure out
                return 0
            res = res * 10 + x % 10
            x /= 10

        return res


if __name__ == '__main__':
    print Solution().reverse(-123)
