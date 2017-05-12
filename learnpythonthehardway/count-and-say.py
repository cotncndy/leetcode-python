# Time:  O(n * 2^n)
# Space: O(2^n)
#
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.
#

class Solution:
    # @return a string
    def countAndSay(self, n):
        i, t_str, res = 1, "1", ""
        while i < n:
            t_str += '#'
            count = 1
            for k in xrange(len(t_str)):
                if k == 0:
                    count = 1
                elif t_str[k] == t_str[k - 1]:
                    count += 1
                else:
                    res += str(count) + t_str[k - 1]
                    count = 1
            t_str = res
            res = ""
            i += 1

        return t_str


if __name__ == "__main__":
    print Solution().countAndSay(5)
