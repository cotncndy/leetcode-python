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
        while (1 << i) < range:
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


if __name__ == '__main__':
    print Solution().ipToCIDR("255.0.0.7", 10)
