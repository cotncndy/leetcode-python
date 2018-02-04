# You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
#
# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in
# this fashion.
#
# Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs.
# You can select pairs in any order.
#
# Example 1:
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
# Note:
# The number of given pairs will be in the range [1, 1000].

import heapq


class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort()
        heap, res = [], []

        for p in pairs:
            while heap and p[1] < heap[0][0]:
                heapq.heappop(heap)

            if not heap:
                heapq.heappush(heap, (p[1], p))
            elif p[0] > heap[0][0]:
                while heap and p[0] > heap[0][0]:
                    end, pair = heapq.heappop(heap)
                    res.append(pair)
                heapq.heappush(heap, (p[1], p))

        return len(res) + len(heap)


if __name__ == '__main__':
    print Solution().findLongestChain([[-10, -8], [8, 9], [-5, 0], [6, 10], [-6, -4], [1, 7], [9, 10], [-4, 7]])
