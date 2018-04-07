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
            caX, caY = c[0] - a[0], c[1] - b[1]

            return baX * caY - baY * caX

        if not dotProduct(p1, p2, p3) and not dotProduct(p4, p2, p3):
            return True
        if not dotProduct(p1, p4, p3) and not dotProduct(p2, p4, p3):
            return True
        if not dotProduct(p1, p3, p4) and not dotProduct(p2, p4, p3):
            return True
        return False
