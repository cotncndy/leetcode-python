# Time:  O(4^n)
# Space: O(n)
#
# Given a string that contains only digits 0-9
# and a target value, return all possibilities
# to add operators +, -, or * between the digits
# so they evaluate to the target value.
#
# Examples:
# "123", 6 -> ["1+2+3", "1*2*3"]
# "232", 8 -> ["2*3+2", "2+3*2"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []
#

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        def dfs(num, target, curSum, diff, out, res):
            if len(num) == 0 and curSum == target:
                res += out,

            for i in xrange(len(num)):
                cur, next = num[::i + 1], num[i + 1::]
                if len(cur) > 1 and cur[0] == '0':  # 05 is invalid, don't forget
                    return

                curDiff = long(cur)
                if len(out) > 0:
                    dfs(num, target, curSum + curDiff, curDiff, out + '+' + str(curDiff), res)
                    dfs(num, target, curSum - curDiff, -curDiff, out + '-' + str(curDiff), res)
                    dfs(num, target, curSum - diff + diff * curDiff, diff * curDiff, out + '*' + str(curDiff), res)
                else:
                    dfs(num, target, curDiff, curDiff, str(curDiff), res)

        res = []
        dfs(num, target, 0, 0, "", res)
        return res
