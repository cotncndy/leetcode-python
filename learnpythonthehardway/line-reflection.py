# Time:  O(n)
# Space: O(n)
from collections import defaultdict


# Hash solution.
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        hash_map = defaultdict(set)
        left, right = float('inf'), float('-inf')
        for p in points:
            hash_map[p[1]].add(p[0])
            left, right = min(left, p[0]), max(right, p[0])

        mid = left + right
        for values in hash_map.values():
            for x in values:
                if mid - x not in values:
                    return False
        return True


if __name__ == '__main__':
    print  Solution().isReflected([[1, 1], [-1, 1], [-2, 2], [2, 2]])
