# -*- coding: utf-8 -*-
# You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty.
#
# For each move, you could choose any m (1 ≤ m ≤ n) washing machines, and pass one dress of each washing machine to
# one of its adjacent washing machines at the same time .
#
# Given an integer array representing the number of dresses in each washing machine from left to right on the line,
# you should find the minimum number of moves to make all the washing machines have the same number of dresses. If it
#  is not possible to do it, return -1.
#
# Example1
#
# Input: [1,0,5]
#
# Output: 3
#
# Explanation:
# 1st move:    1     0 <-- 5    =>    1     1     4
# 2nd move:    1 <-- 1 <-- 4    =>    2     1     3
# 3rd move:    2     1 <-- 3    =>    2     2     2
#
# Example2
#
# Input: [0,3,0]
#
# Output: 2
#
# Explanation:
# 1st move:    0 <-- 3     0    =>    1     2     0
# 2nd move:    1     2 --> 0    =>    1     1     1
#
# Example3
#
# Input: [0,2,0]
#
# Output: -1
#
# Explanation:
# It's impossible to make all the three washing machines have the same number of dresses.
#
# Note:
#
#     The range of n is [1, 10000].
#     The range of dresses number in a super washing machine is [0, 1e5].

class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        s, l = sum(machines), len(machines)
        if s % l != 0:
            return -1
        avg = s / l

        res = 0
        for k, v in enumerate(machines):
            machines[k] = v - avg
            res = max(res, machines[k])

        for k, v in enumerate(machines):
            if k == 0:
                continue
            machines[k] = v + machines[k - 1]
            res = max(abs(machines[k]), res)
            machines[k - 1] = 0

        return res

    def findMinMoves2(self, machines):
        s, l = sum(machines), len(machines)
        if s % l != 0:
            return -1
        avg = s / l

        res, cnt, prev = 0, 0, 0
        for k, v in enumerate(machines):
            cnt = v - avg
            res = max(cnt, abs(prev + cnt), res)
            prev += cnt
        return res

    def findMinMoves3(self, machines):
        s, l = sum(machines), len(machines)
        if s % l != 0:
            return -1
        avg = s / l

        res, cnt = 0, 0
        for k, v in enumerate(machines):
            cnt += v - avg
            res = max(v - avg, abs(cnt), res)

        return res


if __name__ == '__main__':
    # print Solution().findMinMoves([0, 0, 11, 5])
    # print Solution().findMinMoves2([0, 0, 11, 5])
    # print Solution().findMinMoves([1, 0, 5])
    # print Solution().findMinMoves2([1, 0, 5])
    # print Solution().findMinMoves([0, 3, 0])
    # print Solution().findMinMoves2([0, 3, 0])
    # print Solution().findMinMoves([9, 1, 8, 8, 9])
    print Solution().findMinMoves3([9, 1, 8, 8, 9])
