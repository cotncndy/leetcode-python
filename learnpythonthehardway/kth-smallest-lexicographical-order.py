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
        self.count = 0

    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        start = ""
        return self.recur(n, k, start)

    def recur(self, n, k, start):
        if len(start) > 0 and (int(start) > n or self.count == k + 1):
            return -1
        if self.count == k:
            return int(start)

        temp = start
        for i in xrange(10):
            if len(start) == 0 and i == 0:
                continue
            if int(start + str(i)) > n:
                return -1
            start += str(i)
            self.count += 1
            t = self.recur(n, k, start)
            if t == -1:
                start = temp
                continue
            if self.count == k:
                return t
        return -1

    def findKthNumber2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        cur, k = 1, k - 1
        while k:
            step = self.calcSteps(n, cur, cur + 1)
            if step < k:
                k, cur = k - step, cur + 1
            else:
                k, cur = k - 1, cur * 10
        return cur

    def calcSteps(self, n, n1, n2):
        step = 0
        while n1 <= n:
            step += min(n + 1, n2) - n1
            n1, n2 = n1 * 10, n2 * 10
        return step



if __name__ == '__main__':
    # print Solution().findKthNumber2(4289384, 1922239)
    # print Solution().findKthNumber(4289384, 1922239)
    print Solution().findKthNumber2(13, 8)
