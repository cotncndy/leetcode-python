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
        for key in sorted(lookup.keys()):
            curr += lookup[key]
            res = max(res, curr)
        return res


if __name__ == '__main__':
    intervals = [Interval(4, 9)]
    print Solution().minMeetingRooms(intervals)
