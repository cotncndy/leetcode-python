# Time:  O(n)
# Space: O(n)
from collections import defaultdict
from heapq import heappop, heappush


class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return str;
        cnts = defaultdict(int)
        for c in str:
            cnts[c] += 1
