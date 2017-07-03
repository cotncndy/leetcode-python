# Time:  O(klog*k) ~= O(k), k is the length of the positions
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
        directions = [{0, 1}, {0, -1}, {1, 0}, {-1, 0}]
        set = {}

        for position in positions:
            node = (position[0], position[1])
            set[get_node_id(node, n)] = get_node_id(node, n)
            num += 1

            for d in directions:
                neighbor = (position[0] + d[0], position[1] + d[1])
                if 0 <= neighbor[0] < m and 0 <= neighbor[1] < n and \
                                get_node_id(neighbor, n) in set:
                    union(id, get_node_id(neighbor, n))
                    num -= 1
            res.append(num)

        return res
