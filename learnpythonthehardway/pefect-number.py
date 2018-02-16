# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except
# itself.
#
# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# Note: The input number n will not exceed 100,000,000. (1e8)


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False

        sign = -1 if num < 0 else 1
        sum, i, num = 1, 2, abs(num)  # bugfixed negative number issue
        while i <= int(num ** 0.5):
            if num % i == 0:
                sum += i
                if i != num ** 0.5:
                    sum += num / i * sign
            i += 1

        return sum == num


if __name__ == '__main__':
    print Solution().checkPerfectNumber(28)
    print Solution().checkPerfectNumber(64)
