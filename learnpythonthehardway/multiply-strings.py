# Time:  O(m * n)
# Space: O(m + n)
#
# Given two numbers represented as strings, return multiplication of the numbers as a string.
#
# Note: The numbers can be arbitrarily large and are non-negative.
#

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1, l2 = len(num1), len(num2)
        res = [0] * (l1 + l2)
        for i in reversed(xrange(l1)):
            for j in reversed(xrange(l2)):
                k = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum = k + res[i + j + 1]
                res[i + j] += sum / 10
                res[i + j + 1] = sum % 10

        # s = ''.join(map(str, res))
        s = ""
        for i in xrange(l1 + l2):
            if not (res[i] == 0 and len(s) == 0):
                s += str(res[i])

        return "0" if len(s) == 0 else s


if __name__ == "__main__":
    print Solution().multiply("123", "0")
