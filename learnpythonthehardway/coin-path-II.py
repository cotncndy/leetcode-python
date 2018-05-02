# -*- coding: utf-8 -*-
# Given an array A (index starts at 1) consisting of N integers: A1, A2, ..., AN and an integer B. The integer B
# denotes that from any place (suppose the index is i) in the array A, you can jump to any one of the place in the
# array A indexed i+1, i+2, …, i+B if this place can be jumped to. Also, if you step on the index i, you have to pay
# Ai coins. If Ai is -1, it means you can’t jump to the place indexed i in the array.
#
# Now, you start from the place indexed 1 in the array A, and your aim is to reach the place indexed N using the
# minimum coins. You need to return the path of indexes (starting from 1 to N) in the array you should take to get to
#  the place indexed N using minimum coins.
#
# If there are multiple paths with the same cost, return the lexicographically smallest such path.
#
# If it's not possible to reach the place indexed N then you need to return an empty array.
#
# Example 1:
# Input: [1,2,4,-1,2], 2
# Output: [1,3,5]
# Example 2:
# Input: [1,2,4,-1,2], 1
# Output: []
# Note:
# Path Pa1, Pa2, ..., Pan is lexicographically smaller than Pb1, Pb2, ..., Pbm, if and only if at the first i where
# Pai and Pbi differ, Pai < Pbi; when no such i exists, then n < m.
# A1 >= 0. A2, ..., AN (if exist) will in the range of [-1, 100].
# Length of A is in the range of [1, 1000].
# B is in the range of [1, 100].


class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """

        if A[0] == -1:
            return []
        m = len(A)
        dp = [[(float('inf'), -1)] for _ in xrange(m)]
        dp[0] = [(A[0], -1)]

        for i in xrange(m):
            if A[i] == -1:
                continue
            for j in xrange(1, B + 1):
                if i + j >= m:
                    break
                if A[i + j] != -1:
                    cost = dp[i][0][0]
                    if cost + A[i + j] < dp[i + j][0][0]:
                        del dp[i + j][:]  # clear the list
                        dp[i + j].append((cost + A[i + j], i))
                    elif cost + A[i + j] == dp[i + j][0][0]:
                        dp[i + j].append((cost + A[i + j], i))

        if dp[-1][0][0] == float('inf'):
            return []

        # print dp
        li = [m]
        self.res = []
        self.backtrack(dp, m - 1, li)
        return self.res
        # return l[::-1]

    def backtrack(self, dp, pos, li):
        if pos == 0:
            if len(li) > len(self.res):
                self.res = li[::-1]
            return

        # [[0]]  [[0,2],[0,3]]
        for p in dp[pos]:
            tmp = []
            tmp.extend(li)
            tmp.append(p[1] + 1)
            self.backtrack(dp, p[1], tmp)

    def cheapestJump2(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """

        m = len(A)
        if A[0] == -1 or A[m - 1] == -1:
            return []
        dp = [(float('inf'), -1)] * m
        dp[m - 1] = (A[m - 1], -1)

        for i in xrange(m - 2, -1, -1):
            if A[i] == -1:
                continue
            j = i + 1
            while j <= min(i + B, m - 1):
                if dp[j][0] == float('inf'):
                    j += 1  # bugfixed
                    continue
                cost = dp[j][0] + A[i]
                if cost < dp[i][0]:
                    dp[i] = (cost, j)
                j += 1

        if dp[0][0] == float('inf'):
            return []
        # print dp
        i, res = 0, [1]
        while i < m:
            i = dp[i][1]
            if i == -1:
                break
            res.append(i + 1)
        return res

    def cheapestJump3(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """

        m = len(A)
        if A[0] == -1 or A[m - 1] == -1:
            return []
        dp = [(float('inf'), -1)] * m
        dp[0] = (A[0], -1)
        leng = [0] * m

        for i in xrange(m):
            if A[i] == -1:
                continue
            j = max(i - B, 0)
            while j < i:
                if dp[j][0] == float('inf'):
                    j += 1  # bugfixed
                    continue
                cost = dp[j][0] + A[i]
                if cost < dp[i][0]  or (cost == dp[i][0] and leng[i] < leng[j] + 1):
                    dp[i] = (cost, j)
                    leng[i] = leng[j] + 1
                j += 1

        if dp[-1][0] == float('inf'):
            return []
        # print dp
        i, res = m - 1, [m]
        while i >= 0:
            i = dp[i][1]
            if i == -1:
                break
            res.append(i + 1)
        return res[::-1]


if __name__ == '__main__':
    # print Solution().cheapestJump3([1, 2, 4, -1, 2], 2)
    # print Solution().cheapestJump([1, 2, 4, -1, 2], 2)
    # print Solution().cheapestJump3([1, 2, 4, -1, 2], 1)
    # print Solution().cheapestJump([1, 2, 4, -1, 2], 1)
    # print Solution().cheapestJump3([0, 0, 0, 0, 0, 0], 3)
    print Solution().cheapestJump([0, 0, 0, 0, 0, 0], 3)
    # print Solution().cheapestJump3([0, -1, -1, -1, -1, -1], 6)
    print Solution().cheapestJump([0, -1, -1, -1, -1, -1], 6)
    # print Solution().cheapestJump3(
    #     [33, 90, 57, 39, 42, 45, 29, 90, 81, 87, 88, 37, 58, 97, 80, 2, 77, 64, 82, 41, 2, 33, 34, 95, 85, 77, 92, 3, 8,
    #      15, 71, 84, 58, 65, 46, 48, 3, 74, 4, 83, 23, 12, 15, 77, 33, 65, 17, 86, 21, 62, 71, 55, 80, 63, 75, 55, 11,
    #      34, -1, 64, 81, 18, 77, 82, 8, 12, 14, 6, 46, 39, 71, 14, 6, 46, 89, 37, 88, 70, 88, 33, 89, 92, 60, 0, 78, 10,
    #      88, 99, 20], 74)
#