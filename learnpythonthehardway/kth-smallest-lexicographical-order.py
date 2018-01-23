# Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.
#
# Note: 1 <= k <= n <= 109.
#
# Example:
#
# Input:
# n: 13   k: 2
#
# Output:
# 10
#
# Explanation:
# The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.


class Solution(object):
    def __init__(self):
        self.count = 1

    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        start = "1"
        return self.recur(n, k, start)

    def recur(self, n, k, start):
        if int(start) > n or self.count == k + 1:
            return -1
        if self.count == k:
            return int(start)

        for i in xrange(10):
            if int(start + str(i)) > n:
                break
            start += str(i)
            self.count += 1
            t = self.recur(n, k, start)
            if self.count == k:
                return t
        return -1


if __name__ == '__main__':
    print Solution().findKthNumber(13, 7)
