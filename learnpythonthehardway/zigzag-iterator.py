# Time:  O(n)
# Space: O(k)

from collections import deque


class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your q structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.que = deque([(len(v), iter(v)) for v in (v1, v2) if v])

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.que)

    def next(self):
        """
        :rtype: int
        """
        leng, itera = self.que.popleft()
        if leng > 1:
            self.que.append((leng - 1, itera))
        return next(itera)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
