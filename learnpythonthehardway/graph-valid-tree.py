# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)

# BFS solution. Same complexity but faster version.
class Solution:
    # @param {integer} n
    # @param {integer[][]} edges
    # @return {boolean}
    def validTree(self, n, edges):
        group = [-1] * n

        for i, j in edges:
            x, y = self.find(i, group), self.find(j, group)
            if x == y:
                return False
            group[x] = y

        return len(edges) == n - 1

    def find(self, i, group):
        while group[i] != -1:
            i = group[i]
        return i
