# Start from integer 1, remove any integer that contains 9 such as 9, 19, 29...
#
# So now, you will have a new integer sequence: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...
#
# Given a positive integer n, you need to return the n-th integer after removing. Note that 1 will be the first integer.
#
# Example 1:
# Input: 9
# Output: 10
# Hint: n will not exceed 9 x 10^8.

class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n :
            cnt += 1
            if str(cnt).find('9') == -1:
                n -= 1

        return cnt


    def newInteger2(self, n):
        """
        :type n: int
        :rtype: int
        """
        res, base = 0, 1
        while n :
            res += n % 9 * base
            n /= 9

        return res

    def newInteger3(self, n):
        res = ""
        while n :
            res = str(n%9) + res
            n /= 9
        return int(res)

if __name__ == '__main__':
    print Solution().newInteger2()




