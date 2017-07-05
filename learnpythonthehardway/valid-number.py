# Time:  O(n)
# Space: O(1)
#
# Validate if a given string is numeric.
#
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Note: It is intended for the problem statement to be ambiguous.
# You should gather all requirements up front before implementing one.
#

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        seenSign, seenE, seenDot, seenNum = False, False, False, False
        for i in xrange(len(s)):
            if s[i] == '+' or s[i] == '-':
                if not i == 0 or (not i > 0 and s[i] == 'e') or seenSign:
                    return False
                seenSign = True
            elif s[i] == 'e':
                if seenE or not seenNum:
                    return False
                seenE = True
                seenNum = False  # there must be number follow e, otherwise is wrong, 1.3e is wrong
            elif s[i] == '.':
                if seenDot or seenE:
                    return False
                seenDot = True
            elif s[i].isdigit():
                seenNum = True
            else:
                return False

        return seenNum
