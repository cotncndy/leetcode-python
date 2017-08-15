# Time:  O(logn)
# Space: O(1)

# Given a positive integer n and you can do operations as follow:
#
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
# What is the minimum number of replacements needed for n to become 1?
#
# Example 1:
#
# Input:
# 8
#
# Output:
# 3
#
# Explanation:
# 8 -> 4 -> 2 -> 1
# Example 2:
#
# Input:
# 7
#
# Output:
# 4
#
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1

# Iterative solution.
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if not n & 1:
            return 1 + self.integerReplacement(n >> 1)
        else:
            return 1 + min(self.integerReplacement(n - 1), self.integerReplacement(n + 1))

    def integerReplacement2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if not n & 1:
            return 1 + self.integerReplacement(n >> 1)
        else:
            return 2 + min(self.integerReplacement((n - 1) >> 1), self.integerReplacement((n + 1) >> 1))

    def integerReplacement3(self, n):
        """
        :type n: int
        :rtype: int
        """
        p, res = n, 0

        while p != 1:
            if p & 1:
                if p & 3:  # notice, 3 is 011, then add 1 would be come 100, which is multiplications of 4
                    p += 1  # if x & 3, for ex 15, 15-16-8-4-2-1(6), or 15-14-7-8-4-2-1(7)
                else:
                    p -= 1
            else:
                p /= 2

            res += 1

        return res
