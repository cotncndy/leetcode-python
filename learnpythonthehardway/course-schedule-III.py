# There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and
# closed on dth day. A course should be taken continuously for t days and must be finished before or on the dth day.
# You will start at the 1st day.
#
# Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be
# taken.
#
# Example:
# Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
# Output: 3
# Explanation:
# There're totally 4 courses, but you can take 3 courses at most:
# First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next
# course on the 101st day.
# Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next
#  course on the 1101st day.
# Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
# The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
# Note:
# The integer 1 <= d, t, n <= 10,000.
# You can't take two courses simultaneously.
from _heapq import heappop, heappush, heappushpop


class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """

        def compare(c1, c2):
            if c1[0] == c2[0]:
                return c1[1] - c2[1]
            return c1[0] - c2[0]

        def compare2(c1, c2):
            if c1[1] == c2[1]:
                return c1[0] - c2[0]
            return c1[1] - c2[1]

        sC = sorted(courses, cmp=compare2)
        curTime, res = 0, 0
        for k, v in enumerate(sC):
            if curTime + v[0] <= v[1]:
                curTime += v[0]
                res += 1

        return res

    def scheduleCourse2(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        heap, curTime, res = [], 0, 0
        courses.sort(key=lambda c: c[1])
        for k, v in enumerate(courses):
            curTime += v[0]
            heappush(heap, -v[0])
            if curTime > v[1] and heap:  # bugfixed need to check if heap is empty or not
                item = heappop(heap)
                curTime += item
        return len(heap)

    def scheduleCourse3(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """

        if len(courses) == 0:
            return 0

        courses.sort(key=lambda x: x[1])

        selectedT = []
        sumT = 0

        for course in courses:
            t, d = course
            if sumT + t <= d:
                sumT += t
                heappush(selectedT, -t)
            else:
                if len(selectedT) > 0 and -selectedT[0] > t:
                    sumT = sumT - (-selectedT[0]) + t
                    heappushpop(selectedT, -t)

        return len(selectedT)


if __name__ == '__main__':
    # print Solution().scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])
    # print Solution().scheduleCourse2([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])
    # print Solution().scheduleCourse([[5, 15], [3, 19], [6, 7], [2, 10], [5, 16], [8, 14], [10, 11], [2, 19]])
    # print Solution().scheduleCourse2([[5, 15], [3, 19], [6, 7], [2, 10], [5, 16], [8, 14], [10, 11], [2, 19]])
    # print Solution().scheduleCourse([[5, 5], [4, 6], [2, 6]])
    # print Solution().scheduleCourse2([[5, 5], [4, 6], [2, 6]])
    # print Solution().scheduleCourse2([[100, 2], [32, 50]])
    print Solution().scheduleCourse2([[7, 17], [3, 12], [10, 20], [9, 10], [5, 20], [10, 19], [4, 18]])
