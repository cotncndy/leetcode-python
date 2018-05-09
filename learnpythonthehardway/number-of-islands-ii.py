# Time:  O(klog*k) ~= O(k), k is the length of the positions

# A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which
# turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of
# islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example:
#
# Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).
#
# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
#
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
#
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# We return the result as an array: [1, 1, 2, 3]
#
# Challenge:
#
# Can you do it in time complexity O(k log mn), where k is the length of the positions?
# Space: O(k)

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """

        def get_node_id(node, n):
            return node[0] * n + node[1]

        def find(x):
            if set[x] != x:
                set[x] = find(set[x])  # path compression

            return set[x]

        def union(x, y):
            x_group, y_group = map(find, (x, y))
            if x_group != y_group:
                set[min(x_group, y_group)] = max(x_group, y_group)

        res = []
        num = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        set = {}

        for position in positions:
            node = (position[0], position[1])
            set[get_node_id(node, n)] = get_node_id(node, n)
            num += 1

            for d in directions:
                neighbor = (position[0] + d[0], position[1] + d[1])
                if 0 <= neighbor[0] < m and 0 <= neighbor[1] < n and \
                                get_node_id(neighbor, n) in set:
                    # first check, then merge the previously unconnected islands
                    if find(get_node_id(node, n)) != find(get_node_id(neighbor, n)):
                        union(get_node_id(node, n), get_node_id(neighbor, n))
                        num -= 1
            res.append(num)

        return res


if __name__ == '__main__':
    print Solution().numIslands2(3, 3, [[0, 1], [1, 2], [2, 1], [1, 0], [0, 2], [0, 0], [1, 1]])
    print Solution().numIslands2(3, 3, [[0, 1], [0, 2], [2, 1], [1, 0], [0, 2], [0, 0], [1, 1]])
