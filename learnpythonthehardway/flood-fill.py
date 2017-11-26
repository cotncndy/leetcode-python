class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        def dfs(image, sr, sc, newColor, oldColor, visited):
            if sr >= len(image) or sr < 0 or sc >= len(image[0]) or sc < 0:
                return
            if visited[sr][sc]:
                return
            if image[sr][sc] != oldColor:
                return
            else:
                image[sr][sc], visited[sr][sc] = newColor, True

            dfs(image, sr + 1, sc, newColor, oldColor, visited)
            dfs(image, sr - 1, sc, newColor, oldColor, visited)
            dfs(image, sr, sc + 1, newColor, oldColor, visited)
            dfs(image, sr, sc - 1, newColor, oldColor, visited)

        row, col = len(image), len(image[0])
        visited = [[False] * col for _ in xrange(row)]
        old = image[sr][sc]

        dfs(image, sr, sc, newColor, old, visited)

        return image


if __name__ == '__main__':
    print Solution().floodFill([[1, 1, 1], [0, 1, 1], [1, 0, 1]], 1, 1, 2)
    print Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
