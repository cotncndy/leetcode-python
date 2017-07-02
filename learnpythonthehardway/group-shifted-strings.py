# Time:  O(nlogn)
# Space: O(n)

from collections import defaultdict


class Solution:
    # @param {string[]} strings
    # @return {string[][]}
    def groupStrings(self, strings):
        offset_map, res = defaultdict(list), []
        for w in strings:
            offset_map[self.get_hash(w)].append(w)

        for key, val in offset_map.iteritems():  # review map's iteritems
            res.append(val)

        return res

    def get_hash(self, s):
        hash_str, base = "", ord(s[0])
        for c in s:
            hash_str += str((ord(c) + 26 - base) % 26) + ','

        return hash_str


if __name__ == '__main__':
    # this test case would cause trouble
    # b-a = 1, c-a = 2, so hash_str is 012
    # m-am = 12, so hash_str is also 012
    print Solution().groupStrings(["abc", "am"])
