# Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each
# step:
#
# Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted.
#  Output the minimum number of steps to get n 'A'.
#
# Example 1:
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
# Note:
# The n will be in the range [1, 1000].


class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:  # bugfixed
            return 0
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 0, 2
        for i in xrange(3, n + 1):
            j = i - 1
            while j and i % j:
                j -= 1
            dp[i] = dp[j] + i / j;

        return dp[n]

    def minSteps2(self, n):  # review , smart method, no need to keep the intermedia results.
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        res = 0
        i = 2
        while i * i <= n:
            while n % i == 0:
                res += i
                n = n // i
            i += 1
        if n != 1:
            res += n
        return res


if __name__ == '__main__':
    print Solution().minSteps(3)
    print Solution().minSteps(4)
    print Solution().minSteps(5)
    print Solution().minSteps(6)
    print Solution().minSteps(7)
    print Solution().minSteps(8)
    print Solution().minSteps(9)
    print Solution().minSteps(10)
    print Solution().minSteps(11)
    print Solution().minSteps(12)
    print Solution().minSteps(13)
    print Solution().minSteps(14)
    print Solution().minSteps(15)
    print Solution().minSteps(16)
