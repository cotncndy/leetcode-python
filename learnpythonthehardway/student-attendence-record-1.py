# You are given a string representing an attendance record for a student. The record only contains the following
# three characters:
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two
# continuous 'L' (late).
#
# You need to return whether the student could be rewarded according to his attendance record.
#
# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        aCnt = 0

        for k, v in enumerate(s):
            if v == 'A':
                aCnt += 1
                if aCnt > 1:
                    return False
            if k < len(s) - 2 and v == 'L' and s[k + 1] == v and s[k + 2] == v:
                return False

        return True

    def checkRecord2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        aCnt, lCnt = 0, 0

        for k, v in enumerate(s):
            if v == 'A':
                lCnt = 0
                aCnt += 1
                if aCnt > 1:
                    return False
            elif v == 'L':
                lCnt += 1
                if lCnt > 2:
                    return False
            else:
                lCnt = 0

        return True

if __name__ == '__main__':
    print Solution().checkRecord("PPALLP")
    print Solution().checkRecord("PPALLL")
    print Solution().checkRecord("APPLLPPLLPPLLL")
    print Solution().checkRecord("APPLLPPLLPPLL")
    print Solution().checkRecord("APPLLPPLLPPLLA")
