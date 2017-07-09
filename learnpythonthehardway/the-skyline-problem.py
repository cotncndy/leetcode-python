# Time:  O(nlogn)
# Space: O(n)
#
# A city's skyline is the outer contour of the silhouette formed
# by all the buildings in that city when viewed from a distance.
# Now suppose you are given the locations and height of all the
# buildings as shown on a cityscape photo (Figure A), write a
# program to output the skyline formed by these buildings
# collectively (Figure B).
#
# The geometric information of each building is represented by a
# triplet of integers [Li, Ri, Hi], where Li and Ri are the x
# coordinates of the left and right edge of the ith building,
# respectively, and Hi is its height. It is guaranteed that 0 <= Li,
# Ri <= INT_MAX, 0 < Hi <= INT_MAX, and Ri - Li > 0. You may assume
# all buildings are perfect rectangles grounded on an absolutely
# flat surface at height 0.
#
# Notes:
#
# The number of buildings in any input list is guaranteed to be
# in the range [0, 10000].
# The input list is already sorted in ascending order by the
# left x position Li.
# The output list must be sorted by the x position.
# There must be no consecutive horizontal lines of equal height
# in the output skyline.
# For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is
# not acceptable;
# the three lines of height 5 should be merged into one
# in the final output as such: [...[2 3], [4 5], [12 7], ...]
#

# Divide and conquer solution.
import heapq


class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}

    # the code is so concise, but it is hard to understand
    # review this code
    def getSkyline(self, buildings):
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]:
                heapq.heappop(hp)
            if negH:
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]:
                res += [x, -hp[0][0]],
        return res[1:]


if __name__ == '__main__':
    print Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
