# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        left, right, up, down = x, x, y, y
        for i in xrange(0, len(image)):
            for j in xrange(0, len(image[0])):
                if image[i][j] == '1':
                    left, right, up, down = min(left, i), max(right, i), min(up, j), max(down, j)

        return (right - left + 1) * (down - up + 1)
