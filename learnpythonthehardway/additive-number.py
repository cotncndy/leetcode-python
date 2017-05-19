# Time:  O(n^3)
# Space: O(n)
#
# Additive number is a positive integer whose digits can form additive sequence.
#
# A valid additive sequence should contain at least three numbers.
# Except for the first two numbers, each subsequent number in the sequence
# must be the sum of the preceding two.
#
# For example:
# "112358" is an additive number because the digits can form an additive sequence:
#   1, 1, 2, 3, 5, 8.
#
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# "199100199" is also an additive number, the additive sequence is:
# 1, 99, 100, 199.
#
# 1 + 99 = 100, 99 + 100 = 199
# Note: Numbers in the additive sequence cannot have leading zeros,
# so sequence 1, 2, 03 or 1, 02, 3 is invalid.
#
# Given a string represents an integer, write a function to determine
# if it's an additive number.
#
# Follow up:
# How would you handle overflow for very large input integers?
#

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in xrange(1, len(num)):
            for j in xrange(i + 1, len(num)):
                s1, s2 = num[0:i], num[i:j]
                if (len(s1) > 1 and s1[0] == '0') or (len(s2) > 1 and s2[0] == '0'):
                    continue
                d1, d2 = long(s1), long(s2)
                d = d1 + d2
                nexts = s1 + s2 + str(d);
                while len(nexts) < len(num):
                    d1, d2 = d2, d
                    d = d1 + d2
                    nexts += str(d)
                if nexts == num:
                    return True

        return False


if __name__ == "__main__":
    print Solution().isAdditiveNumber("112358")
    print Solution().isAdditiveNumber("199100199")
    print Solution().isAdditiveNumber("1122335588")
    print Solution().isAdditiveNumber("1122335589")
    print Solution().isAdditiveNumber("1023")
    print Solution().isAdditiveNumber("101")
