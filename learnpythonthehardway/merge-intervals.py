# Time:  O(nlogn)
# Space: O(1)
#
# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
#

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)  # knowledge sort usge of lamda and key, key is a function
        # https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
        res = [intervals[0]]
        for i in xrange(1, len(intervals)):
            prev, curr = res[-1], intervals[i]
            if curr.start <= prev.end:
                prev.end = max(curr.end, prev.end)
            else:
                res.append(curr)

        return res


if __name__ == "__main__":
    print Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)])
