# Time:  O(n^m) = O(3^4)
# Space: O(n * m) = O(3 * 4)
#
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
#

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        result = []
        self.backtrack(s, 0, 0, "", result)
        return result

    def backtrack(self, s, start, dots, cur, res):
        # (4-dots) * 3 < len(s) -start means if the parts left (each parts can hold 3 digits) is not long enough
        # to hold the remaining numbers, then return
        # (4-dots) means even the left part only put 1 digit, still too long for the remaing part of s, also return
        if (4 - dots) * 3 < len(s) - start or (4 - dots) > len(s) - start:
            return

        if start == len(s) and dots == 4:
            res.append(cur[:-1])
            return

        for i in xrange(start, start + 3):
            # when arrived at last part, i might exceed the len(s), so need to check
            if i < len(s) and self.is_valid(s[start:i + 1]):
                cur += s[start:i + 1] + '.'
                self.backtrack(s, i + 1, dots + 1, cur, res)
                cur = cur[:-(i - start + 2)]  # backtrack

    def is_valid(self, s):
        if len(s) == 0 or (s[0] == '0' and s != '0'):
            return False

        return int(s) < 256


if __name__ == "__main__":
    print Solution().restoreIpAddresses("0000")
