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

            for i in xrange(1, len(num) + 1):  # bugfixed notice the range
                cur, next = num[:i:], num[i::]
                if len(cur) > 1 and cur[0] == '0':  # 05 is invalid, don't forget
                    return

                curDiff = long(cur)
                if len(out) > 0:
                    dfs(next, target, curSum + curDiff, curDiff, out + '+' + str(curDiff),
                        res)  # bugfixed, should be nxt
                    dfs(next, target, curSum - curDiff, -curDiff, out + '-' + str(curDiff), res)
                    dfs(next, target, curSum - diff + diff * curDiff, diff * curDiff, out + '*' + str(curDiff), res)
                else:
                    dfs(next, target, curDiff, curDiff, str(curDiff), res)

        res = []
        dfs(num, target, 0, 0, "", res)
        return res


if __name__ == '__main__':
    print Solution().addOperators('123', 6)
