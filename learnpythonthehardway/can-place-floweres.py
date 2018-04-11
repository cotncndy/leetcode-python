# Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot
# be planted in adjacent plots - they would compete for water and both would die.
#
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty),
# and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
#
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# Note:
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        if not flowerbed:
            return False
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 1:
            return False

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            n, flowerbed[0] = n - 1, 1
            if n == 0:
                return True

        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            n, flowerbed[-1] = n - 1, 1
            if n == 0:
                return True

        for i in xrange(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                n, flowerbed[i] = n - 1, 1
                if n == 0:
                    return True


        return False

    def canPlaceFlowers2(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        r = 0
        zero = 1
        for f in flowerbed:
            if f == 0:
                zero += 1
            else:
                r += (zero - 1) / 2
                zero = 0
        r += zero / 2
        return n <= r

if __name__ == '__main__':
    print Solution().canPlaceFlowers([0, 0, 0, 0, 1], 2)