# Time:  O(n * n!)
# Space: O(n)
#
# Given a collection of numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
#


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        res, used = [], [False] * len(num)
        self.backtrack(num, used, [], res)
        return res

    def backtrack(self, num, used, cur, res):
        if len(cur) == len(num):
            res.append(list(cur))

        for i in xrange(len(num)):
            if not used[i]:
                used[i] = True
                cur.append(num[i])
                self.backtrack(num, used, cur, res)
                cur.pop()
                used[i] = False

if __name__ == "__main__":
    print Solution().permute([1, 2, 3])