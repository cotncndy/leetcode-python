# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.
#
# Example 1:
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
# Input: 3
# Output: False

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in xrange(1, int((c/2) ** 0.5) + 1):
            for b in xrange(int((c/2) ** 0.5) , int((c) ** 0.5) + 1):
                if a ** 2 + b ** 2 == c:
                    return True

        return False

    def judgeSquareSum2(self, c):
        """
        :type c: int
        :rtype: bool
        """
        s = set()
        for i in xrange(0, int(c ** 0.5) + 1):
            s.add(i * i)
            if c - i * i in s:
                return True
        return False

if __name__ == '__main__':
    print Solution().judgeSquareSum2(5)
    print 5 ** 0.5