# Time:  O(1)
# Space: O(1)

# Given an integer, write a function to determine
# if it is a power of three.
#
# Follow up:
# Could you do it without using any loop / recursion?
import math


class Solution(object):
    def isPowerOfThree(self, n):
        return n > 0 and int(math.log10(n) / math.log10(3)) - math.log10(n) / math.log10(3) == 0
