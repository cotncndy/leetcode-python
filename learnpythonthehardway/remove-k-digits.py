# Time:  O(n)
# Space: O(n)

# Given a non-negative integer num represented as a string,
# remove k digits from the number so that the new number is the smallest possible.
#
# Note:
# The length of num is less than 10^5 and will be >= k.
# The given num does not contain any leading zero.
# Example 1:
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:
#
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200.
# Note that the output must not contain leading zeroes.
# Example 3:
#
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res = []
        if k == 0:
            return num
        for i in xrange(len(num)):
            while res and res[-1] > num[i] and k:
                res.pop()
                k -= 1
            res.append(num[i])

        # bugfixed for test case 9, 1, we got res = [9],but k is still 1, so we need res[:-k] at this case, since we need to remove
        # k chars. but for test cases 1342219, 3, we got 1219, k = 0, then res[:0] = '', so we need do [:(-k or None]
        return "".join(res).lstrip('0')[:(-k or None)] or '0'  # bugfixed


if __name__ == '__main__':
    # print Solution().removeKdigits("10", 2)
    # print Solution().removeKdigits("9", 1)
    print Solution().removeKdigits("1342219", 3)
