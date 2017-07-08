# Time:  O(logn)
# Space: O(1)

# There is a list of sorted integers from 1 to n. Starting from left to right,
# remove the first number and every other number afterward until you reach the end of the list.
#
# Repeat the previous step again, but this time from right to left,
# remove the right most number and every other number from the remaining numbers.
#
# We keep repeating the steps again, alternating left to right and right to left,
# until a single number remains.
#
# Find the last number that remains starting with a list of length n.
#
# Example:
#
# Input:
# n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6
#
# Output:
# 6

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        base, res = 1, 1
        while base * 2 <= n:
            res += base
            base *= 2
            if base * 2 > n:
                break
            if ((n / base) % 2 == 1):
                res += base
            base *= 2

        return res

    def lastRemaining2(self, n):
        start, dire, step = 1, 1, 2
        while n > 1:
            start += dire * (step * (n / 2) - step / 2)
            n /= 2
            step *= 2
            dire *= -1

        return start


if __name__ == '__main__':
    print Solution().lastRemaining(9)
