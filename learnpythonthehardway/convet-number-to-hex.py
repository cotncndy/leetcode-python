# used.
#
# Note:
#
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero
# character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly.
# Example 1:
#
# Input:
# 26
#
# Output:
# "1a"
# Example 2:
#
# Input:
# -1
#
# Output:
# "ffffffff"


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        res = []
        while num > 16:
            res.append(nums[num % 16])
            num /= 16
        res.append(nums[num])

        return ''.join(res[::-1])

    def toHex2(self, num):
        nums = "0123456789abcdef"
        res = []
        for i in xrange(8):
            t = (num >> 4 * i) & 15
            res.append(nums[t])
        return "".join(res[::-1]).lstrip('0') or '0'  # bugfixed

    def toHex3(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        mp = '0123456789abcdef'  # like a map
        ans = ''
        for i in range(8):
            n = num & 15  # this means num & 1111b
            c = mp[n]  # get the hex char
            ans = c + ans
            num = num >> 4
        return ans.lstrip('0')  # strip leading zeroes


if __name__ == '__main__':
    print Solution().toHex2(350)
    print Solution().toHex2(-350)
    print Solution().toHex2(-1)
