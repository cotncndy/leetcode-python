# Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.
#
# If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.
#
# Example 1
# Input:
#
# 48
# Output:
# 68
# Example 2
# Input:
#
# 15
# Output:
# 35


class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        factors = []
        for i in reversed(xrange(2, 10)):
            while a % i == 0:
                a /= i
                factors += i,

        if a > 1:
            return 0
        res = 0
        for i in reversed(xrange(len(factors))):
            res = res * 10 + factors[i]
            if res > (1 << 32 - 1):
                return 0


        return res

    def smallestFactorization2(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a <= 1:
            return a

        A = []

        for i in xrange(9, 1, -1):
            while a % i == 0:
                a /= i
                A.append(str(i))

        if a >= 2:
            return 0

        ans = int(''.join(A[::-1]))  # review, so concise

        return ans if ans < 2 ** 31  else 0


if __name__ == '__main__':
    print Solution().smallestFactorization(18000000)
