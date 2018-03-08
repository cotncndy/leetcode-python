# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any
#  two time points in the list.
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# The number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        # sort
        def compare(t1, t2):
            a, b = t1.split(':'), t2.split(':')
            if a[0] == b[0]:
                return int(a[1]) - int(b[1])
            return int(a[0]) - int(b[0])

        timePoints.sort(cmp=compare)
        print timePoints
        prev, res = None, float('inf')
        for t in timePoints:
            if not prev:
                prev = t
            else:
                res = min(res, self.getDiff(t, prev), self.getDiff(prev, t))
                prev = t
        res = min(res, self.getDiff(timePoints[0], timePoints[-1]), self.getDiff(timePoints[-1], timePoints[0]))
        return res

    def getDiff(self, t1, t2):
        a, b = map(int, t1.split(':')), map(int, t2.split(':'))
        res = a[1] - b[1]
        if res < 0:
            res += 60
            a[0] -= 1
            if a[0] < 0:
                a[0] += 24

        res += min(abs(a[0] - b[0]), 24 - abs(a[0] - b[0])) * 60

        return res

    def time_to_minute(self, t):
        return 60 * int(t[:2]) + int(t[-2:])

    def findMinDifference2(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes = sorted(map(self.time_to_minute, timePoints))
        return min((y - x) % (24 * 60)
                   for x, y in zip(minutes, minutes[1:] + minutes[:1]))


if __name__ == '__main__':
    print Solution().findMinDifference(["13:14", "8:23", "11:49", "6:00", "23:04"])
    print Solution().findMinDifference(["23:59", "00:00"])
