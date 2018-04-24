# You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /,
# +, -, (, ) to get the value of 24.
#
# Example 1:
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
# Example 2:
# Input: [1, 2, 1, 2]
# Output: False
# Note:
# The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example,
# with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
import itertools


class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l, eps = len(nums), 0.001
        lookup = [[0] * l for _ in xrange(l)]

        def helper(n,left, right):
            if left == right:
                return [n[left]]
            if lookup[left][right]:
                return lookup[left][right]

            temp = []
            for i in xrange(left, right):
                for x in helper(n,left, i):
                    for y in helper(n,i+1, right):
                        for op in ('+','-','*','/'):
                            temp.append(x+y)
                            temp.append(x-y)
                            temp.append(x * y)
                            if x > eps and y:
                                temp.append(x*1.000/y)
                            if y > eps and x:
                                temp.append(y*1.000/x)

            lookup[left][right] = temp

            return lookup[left][right]

        for n in set(itertools.permutations(nums)): # change from list to set, so no duplicates permutations for ex [9,9,5,9]
            helper(n,0, l-1)
            for i in lookup[0][l-1]:
                if abs(24-i) < eps:
                    return True
            lookup = [[0] * l for _ in xrange(l)]
        return False

if __name__ == '__main__':
    print Solution().judgePoint24([4,1,8,7])
    print Solution().judgePoint24([8,1,6,6]) # 6 / (1-6/8) = 6/(1/4) = 24
    print Solution().judgePoint24([5,1,5,5])
    print Solution().judgePoint24([9,9,5,9])






