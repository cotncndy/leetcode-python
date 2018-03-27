# -*- coding: utf-8 -*-
# A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set
# S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.
#
# Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should
#  be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.
#
# Example 1:
# Input: A = [5,4,0,3,1,6,2]
# Output: 4
# Explanation:
# A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.
#
# One of the longest S[K]:
# S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
# Note:
# N is an integer within the range [1, 20,000].
# The elements of A are all distinct.
# Each element of A is an integer within the range [0, N-1].
import collections


class Solution(object):
    # time complexity : O(2n)
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m, res = collections.defaultdict(set), 0

        a = [0] * len(nums)

        while (sum(a)) < len(nums):
            for k, v in enumerate(a):
                if v == 0:
                    s, start = set(), k
                    while a[nums[start]] == 0:
                        s.add(start)
                        start, a[start] = nums[start], 1

                    res = max(res, len(s))

        return res

    # TODO time complexit : O(n)
    def arrayNesting2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m, res = collections.defaultdict(set), 0

        a = [0] * len(nums)

        for k, v in enumerate(a):
            if v == 1:
                continue
            l, start = 0, k  # bugfixed
            while not a[nums[start]]:
                l, start, a[start] = l + 1, nums[start], 1
                res = max(res, l)

        return res


if __name__ == '__main__':
    print Solution().arrayNesting2([5, 4, 0, 3, 1, 6, 2])
