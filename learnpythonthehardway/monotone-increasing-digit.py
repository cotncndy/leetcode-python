# Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing
# digits.
#
# (Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy
# x <= y.)
#
# Example 1:
# Input: N = 10
# Output: 9
# Example 2:
# Input: N = 1234
# Output: 1234
# Example 3:
# Input: N = 332
# Output: 299
# Note: N is an integer in the range [0, 10^9].


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res, str_n = [], str(N)
        for i in xrange(len(str_n)):
            for j in xrange(1, 10):
                temp = str(j) * (len(str_n) - i)
                if ''.join(res) + temp > str_n:
                    res.append(str(j - 1))
                    break
        return int(''.join(res))


if __name__ == '__main__':
    print Solution().monotoneIncreasingDigits(1234)
