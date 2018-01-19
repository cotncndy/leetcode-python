# A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
#
# Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as
# ONE single character changed in the gene string.
#
# For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
#
# Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make
# it a valid gene string.
#
# Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to
#  mutate from "start" to "end". If there is no such a mutation, return -1.
#
# Note:
#
# Starting point is assumed to be valid, so it might not be included in the bank.
# If multiple mutations are needed, all mutations during in the sequence must be valid.
# You may assume start and end string is not the same.
# Example 1:
#
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
#
# return: 1
# Example 2:
#
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#
# return: 2
# Example 3:
#
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
#
# return: 3
import collections


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        que, map, res = collections.deque(), collections.defaultdict(int), float('inf')
        for s in bank:
            map[s] = float('inf')
        map[start] = 0
        # map[end] = float('inf')  # bugfixed end might not be in the bank

        que.append(start)

        while que:
            w = que.popleft()
            if w == end:
                res = min(res, map[w])
                continue
            for c in "ACGT":
                for i in xrange(8):
                    if w[i] == c:
                        continue
                    t = ""
                    if i == 0:
                        t = c + w[i + 1:]
                    elif i == 7:
                        t = w[0:i] + c
                    else:
                        t = w[:i] + c + w[i + 1:]
                    if t not in map or map[t] < map[w] + 1:
                        continue
                    que.append(t)
                    map[t] = map[w] + 1

        return res if res < float('inf') else -1


if __name__ == '__main__':
    print Solution().minMutation("AAAAAAAA", "CCCCCCCC",
                                 ["AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC", "AACACCCC", "ACCACCCC",
                                  "ACCCCCCC", "CCCCCCCA"])
