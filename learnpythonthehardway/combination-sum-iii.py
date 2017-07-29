# Time:  O(k * C(n, k))
# Space: O(k)
#
# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Ensure that numbers within the set are sorted in ascending order.
#
#
# Example 1:
#
# Input: k = 3, n = 7
#
# Output:
#
# [[1,2,4]]
#
# Example 2:
#
# Input: k = 3, n = 9
#
# Output:
#
# [[1,2,6], [1,3,5], [2,3,4]]
#

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        res = []
        self.backtrack(k, n, 1, [], res)
        return res

    def backtrack(self, k, n, start, cur, res):
        if k == 0 and n == 0:
            # res.append(list(cur))
            res.append(cur[:])
        elif k < 0:
            return
        # start 1-9, also start + start+1 + start+2 +..+ (start+k-1) <= target
        while start < 10 and start * k + k * (k - 1) / 2 <= n:
            cur.append(start)
            self.backtrack(k - 1, n - start, start + 1, cur, res)
            cur.pop()
            start += 1


if __name__ == '__main__':
    print Solution().combinationSum3(3, 9)
