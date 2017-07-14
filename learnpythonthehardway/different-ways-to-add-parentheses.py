# Time:  O(n * 4^n / n^(3/2)) ~= n * Catalan numbers = n * (C(2n, n) - C(2n, n - 1)),
#                                due to the size of the results is Catalan numbers,
#                                and every way of evaluation is the length of the string,
#                                so the time complexity is at most n * Catalan numbers.
# Space: O(n * 4^n / n^(3/2)), the cache size of lookup is at most n * Catalan numbers.
#
# Given a string of numbers and operators, return all possible
# results from computing all the different possible ways to
# group numbers and operators. The valid operators are +, - and *.
#
#
# Example 1
# Input: "2-1-1".
#
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Output: [0, 2]
#
#
# Example 2
# Input: "2*3-4*5"
#
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10]
#
import operator, re


class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        tokens = re.split('(\D)', input)  # knowledge '\D' match non-digits
        nums = map(int, tokens[::2])
        # knowledge how to use map
        ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
        lookup = [[None for _ in xrange(len(nums))] for _ in xrange(len(nums))]

        def helper(left, right):
            if left == right:
                return [nums[left]]

            if lookup[left][right]:  # review use memo
                return lookup[left][right]

            lookup[left][right] = [ops[i](x, y)
                                   for i in xrange(left, right)
                                   for x in helper(left, i)
                                   for y in helper(i + 1, right)]
            return lookup[left][right]

        return helper(0, len(nums) - 1)


if __name__ == '__main__':
    print Solution().diffWaysToCompute("2-1-1")
