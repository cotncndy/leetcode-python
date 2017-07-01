# Time:  O(n^2)
# Space: O(n)
#
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
#
import collections


# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        max_points = 0
        for i, start in enumerate(points):
            slope_map, duplicates = collections.defaultdict(int), 1
            for j in xrange(i + 1, len(points)):
                end = points[j]
                if start.x == end.x and start.y == end.y:
                    duplicates += 1
                else:
                    slope = float('inf')
                    if start.x - end.x != 0:
                        slope = (start.y - end.y) * 1.0 / (start.x - end.x)
                    slope_map[slope] += 1

            cur_max = duplicates
            for slope in slope_map:
                cur_max = max(cur_max, slope_map[slope] + duplicates)
            max_points = max(max_points, cur_max)
        return max_points


if __name__ == "__main__":
    # print Solution().maxPoints([Point(), Point(), Point()])
    print Solution().maxPoints([Point(0, 0), Point(0, 1)])
