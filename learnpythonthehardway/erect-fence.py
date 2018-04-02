# There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is
# to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if
# all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the
# fence perimeter.
#
# Example 1:
# Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
# Explanation:
#
# Example 2:
# Input: [[1,2],[2,2],[4,2]]
# Output: [[1,2],[2,2],[4,2]]
# Explanation:
#
# Even you only have trees in a line, you need to use rope to enclose them.
# Note:
#
# All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more
# than one group.
# All input integers will range from 0 to 100.
# The garden has at least one tree.
# All coordinates are distinct.
# Input points have NO order. No order required for output.


# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        res, collinear, start = set(), set(), points[0]
        for p in points:  # find the left most point
            if p.x < start.x:
                start = p
        res.add(start)
        cur = start
        while True:
            next = points[0]
            for p in points:
                if p == cur:
                    continue
                cross = self.crossProduct(cur, next, p)
                if cross > 0:
                    next, collinear = p, set()
                elif cross == 0:
                    if self.dist(cur, next) < self.dist(cur, p):
                        collinear.add(next)
                        next = p
                    else:
                        collinear.add(next)

            for p in collinear:
                res.add(p)

            if next == start:
                break

            res.add(next)
            cur = next
        return list(res)

    def crossProduct(self, a, b, c):
        baX, baY = a.x - b.x, a.y - b.y
        bcX, bcY = c.x - b.x, c.y - b.y

        return baX * bcY - baY * bcX

    def dist(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2

    def wrapper(self, a):
        li = []
        for p in a:
            li.append(Point(p[0], p[1]))

        return self.outerTrees(li)


if __name__ == '__main__':
    s = Solution().wrapper([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]])
