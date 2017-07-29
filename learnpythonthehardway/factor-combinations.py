# Time:  O(nlogn)
# Space: O(logn)

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def getFactors(self, n):
        res, factors = [], []
        self.backtrack(n, factors, res)
        return res

    def backtrack(self, n, factors, res):
        i = 2 if not factors else factors[-1]
        while i < n / i:
            if n % i == 0:
                factors.append(i)
                factors.append(n / i)  # the i and n/i is a valid combination
                res.append(list(factors))
                factors.pop()  # pop out n / i, then prepare to go recursion
                self.backtrack(n / i, factors, res)  # bugfixed
                factors.pop()  # pop again, eject i, prepare for the next loop
            i += 1


if __name__ == '__main__':
    print Solution().getFactors(12)
