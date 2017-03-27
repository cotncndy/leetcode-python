# Time:  O(n^2)
# Space: O(1)
#
# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        for i in xrange(numRows):
            result.append([]);
            for j in xrange(i + 1):
                if j in (0, i):
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][j - 1] + result[i - 1][j])
        return result;

    def generate2(self, numRows):
        if not numRows:
            return []

        res = [[1]]
        for i in range(1, numRows):
            # finally figure it out, let's say we got [[1],[1,1]] arleady
            # res[-1]=[1,1] ,res[-1] + [0] = [1,1,0]
            # [0] + res[-1] = [0,1,1]
            # then x + y = [1,1,0]+[0,1,1] = [1,2,1]
            # hence we got [[1],[1,1],[1,2,1]]..
            res += [map(lambda x,y:x+y, res[-1]+[0],[0] + res[-1] )]
        return res[:numRows]


if __name__ == "__main__":
    print Solution().generate(5)
    print Solution().generate2(6)
