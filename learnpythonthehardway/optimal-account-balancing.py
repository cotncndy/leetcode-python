# Time:  O(n * 2^n), n is the size of the debt.
# Space: O(n * 2^n)

import collections


class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        account = collections.defaultdict(int)
        for t in transactions:
            account[t[0]] -= t[2]
            account[t[1]] += t[2]

        debt = []
        for v in account.values():  # knowledge how to loop the hashmap value in python
            if v:
                debt.append(v)

        if not debt:
            return 0

        n = 1 << len(debt)
        dp, subset = [float('inf')] * n, []
        for i in xrange(1, n):
            next_debt, number = 0, 0
            for j in xrange(len(debt)):
                if i & (1 << j):
                    next_debt += debt[j]
                    number += 1

            if next_debt == 0:
                dp[i] = number - 1

        return dp[-1]


if __name__ == '__main__':
    print Solution().minTransfers([[0, 1, 10], [2, 0, 5]])
