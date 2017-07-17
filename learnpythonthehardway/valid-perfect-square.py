# Time:  O(logn)
# Space: O(1)

# Given a positive integer num, write a function
# which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Returns: True
# Example 2:
#
# Input: 14
# Returns: False

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 0, num // 2
        while left <= right:
            mid = (left + right) / 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return left * left == num


if __name__ == '__main__':
    print Solution().isPerfectSquare(0)
    print Solution().isPerfectSquare(4)
    print Solution().isPerfectSquare(9)
    print Solution().isPerfectSquare(16)
    print Solution().isPerfectSquare(17)
