# Time:  O(nlogn)
# Space: O(1)
import itertools
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

    # review 1, function pointer 2.lamda
    def minArea2(self, image, x, y):

        def binary_search(left, right, find, imags,
                          has_one):  # knowledge how python pass in function 'find' as parameter
            while left <= right:
                mid = (left + right) / 2
                if find(image, has_one, mid):
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        search_columns = lambda image, has_one, mid: any(int(row[mid]) for row in image) == has_one
        left = binary_search(0, y - 1, search_columns, image, True)  # search the first 1
        right = binary_search(y + 1, len(image[0]) - 1, search_columns, image, False)  # search the first 0, so False

        search_rows = lambda image, has_one, mid: any(itertools.imap(int, image[mid])) == has_one
        up = binary_search(0, x - 1, search_rows, image, True)
        bottom = binary_search(x + 1, len(image) - 1, search_rows, image, False)

        return (right - left) * (bottom - up)
