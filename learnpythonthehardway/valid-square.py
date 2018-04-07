# Given the coordinates of four points in 2D space, return whether the four points could construct a square.
#
# The coordinate (x,y) of a point is represented by an integer array with two integers.
#
# Example:
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
# Note:
#
# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).
# Input points have no order.


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        def dotProduct(a, b, c):
            baX, baY = b[0] - a[0], b[1] - a[1]
            caX, caY = c[0] - a[0], c[1] - a[1]  # bugfixed, typo
            print  baX * caX + baY * caY
            return baX * caX + baY * caY  # bugfixed dot product

        def distance(a, b):
            print (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
            return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

        if not dotProduct(p1, p2, p3) and not dotProduct(p4, p2, p3):
            if distance(p1, p2) == distance(p1, p3) and distance(p1, p2) == distance(p4, p2):
                return True
        if not dotProduct(p1, p4, p3) and not dotProduct(p2, p4, p3):
            if distance(p1, p4) == distance(p1, p3) and distance(p1, p4) == distance(p2, p4):
                return True
        if not dotProduct(p1, p2, p4) and not dotProduct(p3, p2, p3):
            if distance(p1, p2) == distance(p1, p4) and distance(p1, p2) == distance(p3, p2):
                return True
        return False


if __name__ == '__main__':
    # print Solution().validSquare([0, 0], [1, 1], [1, 0], [0, 1])
    # print Solution().validSquare([1, 0], [-1, 0], [0, 1], [0, -1])
    # print Solution().validSquare([1, 0], [-1, 0], [0, 1], [0, -1])
    # print Solution().validSquare([0, 0], [5, 0], [5, 4], [0, 4])
    print Solution().validSquare([0, 0], [-1, 0], [1, 0], [0, 1])
