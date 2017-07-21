# Time:  O(m * n)
# Space: O(g)

from collections import deque


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        # knowledge see how to do 2-dimensional for loop
        q = deque([(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r])
        while q:
            (i, j) = q.popleft()
            for I, J in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= I < len(rooms) and 0 <= J < len(rooms[I]) and \
                                rooms[I][J] == INF:
                    rooms[I][J] = rooms[i][j] + 1
                    q.append((I, J))
        return rooms


if __name__ == '__main__':
    print Solution().wallsAndGates(
        [[2147483647, 0, -1], [2147483647, 2147483647, 2147483647], [2147483647, 0, 2147483647]])
