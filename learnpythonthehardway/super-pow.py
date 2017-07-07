# Time:  O(n), n is the size of b.
# Space: O(1)

# Your task is to calculate a^b mod 1337 where a is a positive integer
# and b is an extremely large positive integer given in the form of an array.
#
# Example1:
#
# a = 2
# b = [3]
#
# Result: 8
# Example2:
#
# a = 2
# b = [1,0]
#
# Result: 1024

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """

        def pow(a, b):
            if b == 1:
                return a % 1337
            if b == 0:
                return 1
            return ((pow(a % 1337, b / 2) % 1337) * (pow(a % 1337, b - b / 2) % 1337)) % 1337

        res = 1
        for i in xrange(len(b)):
            res = ((pow(res, 10) % 1337) * (pow(a, b[i]) % 1337)) % 1337

        return res


if __name__ == '__main__':
    print Solution().superPow(2, [3])
