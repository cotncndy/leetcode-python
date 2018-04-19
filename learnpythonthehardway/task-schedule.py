# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters
# represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For
# each interval, CPU could finish one task or just be idle.
#
# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n
# intervals that CPU are doing different tasks or just be idle.
#
# You need to return the least number of intervals the CPU will take to finish all the given tasks.
#
# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# Note:
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].
import collections
from _heapq import heappush, heappop


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        heap, m = [], collections.defaultdict(int)
        for t in tasks:
            m[t] += 1

        res = 0
        for k, v in m.iteritems():
            heappush(heap, [-v, k])

        while heap:
            temp = []
            l = min(n + 1, len(heap))
            for i in xrange(l):
                item = heappop(heap)
                item[0] = item[0] + 1
                if item[0] <= 0:
                    temp.append(item)

            if not temp:
                break
            res += len(temp)
            if temp[0][0] != 0:
                res += max(0, n + 1 - len(temp))
            for t in temp:
                heappush(heap, t)

        return res


if __name__ == '__main__':
    print Solution().leastInterval(["A","A","A","B","B","B"],2)
    print Solution().leastInterval(["A","A","A","B","B","B"],1)
    print Solution().leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
