class Solution(object):
    def ipToCIDR(self, ip, range):
        """
        :type ip: str
        :type range: int
        :rtype: List[str]
        """
        res, num = [], self.ipString2Num(ip)

        while range:
            i = self.detectsTrailingZero(num)
            curRange = (1 << i)
            curRange = min(curRange, range)
            self.buildCidr(num, curRange, res)
            num += curRange
            range -= curRange

        return res

    def ipString2Num(self, ip):
        ips = ip.split(".")
        ints, num = map(int, ips), 0
        for i in xrange(4):
            num += ints[i] << (8 * (3 - i))
        return num

    def num2IpString(self, num):
        res = ""
        for i in xrange(4):
            if i > 0:
                res = "." + res
            res = str(num & 255) + res
            num >>= 8

        return res

    def buildCidr(self, num, range, res):
        if range <= 0:
            return
        i = 0
        while (1 << (i + 1)) <= range:  # bugfixed shoud be 1<<(i+1) instead of 1 << i, also should be <= instead of <<
            i += 1
        newRange, suffix = 1 << i, str(32 - i)
        res.append(self.num2IpString(num) + "/" + str(suffix))
        num, range = num + newRange, range - newRange
        self.buildCidr(num, range, res)

    def detectsTrailingZero(self, num):
        count = 0
        while (num & 1) == 0:
            num >>= 1
            count += 1

        return count

    def ipToCIDR2(self, ip, rng):
        """
        :type ip: str
        :type range: int
        :rtype: List[str]
        """
        res = []
        MX = 256

        def toip(n):
            ip = []
            while len(ip) < 4:
                ip.append(str(n % MX))
                n /= MX
            return ".".join(reversed(ip))

        def toint(ip):
            n = 0
            for nn in map(int, ip.split(".")):
                n *= MX
                n += nn
            return n

        start = toint(ip)
        end = start + rng

        def maxcomm(start, end):
            for b in xrange(32, -1, -1):
                mask = ((1 << b) - 1)
                if start & mask == 0 and start | mask < end:
                    return 32 - b, start | mask
            assert (False)

        while start < end:
            comm, newstart = maxcomm(start, end)
            res.append("{}/{}".format(toip(start), comm))
            start = newstart + 1

        return res


if __name__ == '__main__':
    print Solution().ipToCIDR2("255.0.0.7", 10)
    print Solution().ipToCIDR2("117.145.102.62", 8)
