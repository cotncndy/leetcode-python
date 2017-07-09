# Time:  O(nlogn)
# Space: O(n)

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


from collections import defaultdict


class Solution:
    # @param {Interval[]} intervals
    # @return {integer}
    def minMeetingRooms(self, intervals):
        lookup = defaultdict(int)
        for i in intervals:
            lookup[i.start] += 1
            lookup[i.end] -= 1

        res, curr = 0, 0
        for key, value in lookup.items():
            curr += lookup[key]
            res = max(res, curr)
        return res


if __name__ == '__main__':
    intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    print Solution().minMeetingRooms(intervals)
