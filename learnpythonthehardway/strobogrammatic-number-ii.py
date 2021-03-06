# Time:  O(n^2 * 5^(n/2))
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Find all strobogrammatic numbers that are of length = n.
#
# For example,
# Given n = 2, return ["11","69","88","96"].
#
# Hint:
#
# Try to use recursion and notice that it should recurse with n - 2 instead of n - 1.
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
            for key, val in self.lookup.iteritems():  # bugfixed
                if k != n or key != '0':
                    result.append(key + t + val)

        return result


if __name__ == '__main__':
    print Solution().findStrobogrammatic(3)
