# Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in
# ascending order.
#
# Note:
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as
# "abc" or "zerone" are not permitted.
# Input length is less than 50,000.
# Example 1:
# Input: "owoztneoer"
#
# Output: "012"
# Example 2:
# Input: "fviefuro"
#
# Output: "45"
import collections


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnts, clues, nums, res = collections.defaultdict(int), ['z', 'w', 'u', 'x', 'g', 'o', 'r', 'f', 's', 'n'], \
                                 ['0', '2', '4', '6', '8', '1', '3', '5', '7', '9'], ""
        mappings = ['zero', 'two', 'four', 'six', 'eight', 'one', 'three', 'five', 'seven', 'nine']
        for c in s:
            cnts[c] += 1

        for i in xrange(len(clues)):
            c = clues[i]
            cnt = cnts[c]
            if cnt > 0:
                res += nums[i] * cnt
                for c in mappings[i]:
                    cnts[c] -= cnt

        return sorted(res)


if __name__ == '__main__':
    print Solution().originalDigits('owoztneoer')
