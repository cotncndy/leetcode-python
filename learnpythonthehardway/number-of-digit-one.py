# Time:  O(logn)
# Space: O(1)
#
# Given an integer n, count the total number of digit 1 appearing
# in all non-negative integers less than or equal to n.
#
# For example:
# Given n = 13,
# Return 6, because digit 1 occurred in the following numbers:
#  1, 10, 11, 12, 13.
#

class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        # todo  https://www.evernote.com/shard/s2/nl/20757047/267fab1f-ceb4-472d-8f84-497967b37488/
        res, a, b = 0, 1, 1
        while n > 0:
            res += (n + 8) / 10 * a + (b if n % 10 == 1 else 0)
            b += n % 10 * a
            a *= 10
            n /= 10

        return res

    def countDigitOne2(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = n
        i = 0
        j = 1
        res = 0
        while n > 0:
            k = n % 10
            res += k * i + (j if k > 1 else (t % j + 1 if k == 1 else 0))
            i *= 10
            i += j
            n //= 10
            j *= 10
        return res


if __name__ == '__main__':
    print Solution().countDigitOne(99)
    print Solution().countDigitOne(156)
