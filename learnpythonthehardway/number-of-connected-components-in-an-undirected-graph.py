# Time:  O(nlog*n) ~= O(n), n is the length of the positions
# Space: O(n)

class UnionFind(object):
    def __init__(self, n):
        self.__group = range(n)
        self.count = n

    def find(self, x):
        if self.__group[x] != x:
            # path compression
            self.__group[x] = self.find(self.__group[x])

        return self.__group[x]

    def find2(self, x):
        while x != self.__group[x]:
            self.__group[x] = self.__group[self.__group[x]]
            x = self.__group[x]

        return x

    def union(self, x, y):
        x_group, y_group = map(self.find2, (x, y))  # review how to use map
        if x_group != y_group:
            self.__group[min(x_group, y_group)] = max(x_group, y_group)
            self.count -= 1

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        union_find = UnionFind(n)

        for i, j in edges:
            union_find.union(i, j)

        return union_find.count


if __name__ == '__main__':
    print Solution().countComponents(6, [[0, 1], [2, 3], [2, 4]])
