# Time:  O(n^2 * 5^(n/2))
# Space: O(n)

class Solution:
    lookup = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    # @param {integer} n
    # @return {string[]}
    def findStrobogrammatic(self, n):
        return self.find(n, n)

    def find(self, k, n):
        if k == 0:
            return ['']
        if k == 1:
            return ['0', '1', '8']

        result = []
        for t in self.find(k - 2, n):
            for key, val in enumerate(self.lookup):
                if k != n or key != '0':
                    result.append(key + t + val)

        return result


if __name__ == '__main__':
    print Solution().findStrobogrammatic(3)
