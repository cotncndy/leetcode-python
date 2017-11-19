class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def selfDividing(num):
            t = num
            while t:
                k = t % 10
                if not k or num % k:
                    return False
                t /= 10
            return True

        res = []
        for i in xrange(left, right + 1):
            if selfDividing(i):
                res.append(i)
        return res


if __name__ == '__main__':
    print Solution().selfDividingNumbers(1, 22)
