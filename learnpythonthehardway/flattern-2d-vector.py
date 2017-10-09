# Implement an iterator to flatten a 2d vector.
#
# For example,
# Given 2d vector =
#
# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,
# 5,6].
#
# Follow up:
# As an added challenge, try to code it using only iterators in C++ or iterators in Java.


class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.v = vec2d
        self._row = 0
        self._col = 0

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            self._col += 1
            return self.v[self._row][self._col]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self._col == len(self.v[self._row]):
            self._row, self._col = self._row + 1, 0

        return self._row < len(self.v)


        # Your Vector2D object will be instantiated and called as such:
        # i, v = Vector2D(vec2d), []
        # while i.hasNext(): v.append(i.next())
