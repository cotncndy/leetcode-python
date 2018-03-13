# Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,
# 4] -> 2 / 3 / 4.
#
# However, you can add any number of parenthesis at any position to change the priority of operations. You should
# find out how to add parenthesis to get the maximum result, and return the corresponding expression in string
# format. Your expression should NOT contain redundant parenthesis.
#
# Example:
# Input: [1000,100,10,2]
# Output: "1000/(100/10/2)"
# Explanation:
# 1000/(100/10/2) = 1000/((100/10)/2) = 200
# However, the bold parenthesis in "1000/((100/10)/2)" are redundant,
# since they don't influence the operation priority. So you should return "1000/(100/10/2)".
#
# Other cases:
# 1000/(100/10)/2 = 50
# 1000/(100/(10/2)) = 50
# 1000/100/10/2 = 0.5
# 1000/100/(10/2) = 2
# Note:
#
# The length of the input array is [1, 10].
# Elements in the given array will be in range [2, 1000].
# There is only one optimal division for each test case.
import collections


class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        m, m1 = collections.defaultdict(), collections.defaultdict(str)
        res = self.dfs(nums, m, m1, len(nums) - 1)
        print res
        return m1[max(res)]

    def dfs(self, nums, m, m1, n):
        if n == 0:
            m[0] = [nums[len(nums) - 1]]
            m1[nums[len(nums) - 1]] = str(nums[len(nums) - 1])
            return [nums[len(nums) - 1]]
        if n in m:
            return m[n]
        res1, res = self.dfs(nums, m, m1, n - 1), []

        for i in res1:
            t = nums[len(nums) - 1 - n] * 1.0 / i
            res.append(t)
            s = m1[i] if '/' not in m1[i] else '(' + m1[i] + ')'
            m1[t] = str(nums[len(nums) - 1 - n]) + '/' + s

        if n > 1:
            res2 = self.dfs(nums, m, m1, n - 2)
            # res.append(nums[len(nums)-1-n] // nums[len(nums)-n] // i for i in res2)
            for i in res2:
                t = nums[len(nums) - 1 - n] * 1.0 / nums[len(nums) - n] / i
                res.append(t)
                s = m1[i] if '/' not in m1[i] else '(' + m1[i] + ')'
                m1[t] = str(nums[len(nums) - 1 - n]) + "/" + str(nums[len(nums) - n]) + '/' + s

        # res.append(nums[len(nums)-1-n] // i for i in res1)

        m[n] = res

        return res

    def optimalDivision2(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        res = str(nums[0]) + '/' + '('
        for i in xrange(1, len(nums)):
            res += str(nums[i])
            if i < len(nums) - 1:
                res += '/'
        res += ')'

        return res

    def optimalDivision3(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) <= 2:
            return "/".join(map(str, nums))
        return str(nums[0]) + '/(' + '/'.join(map(str, nums[1:])) + ')'

if __name__ == '__main__':
    print Solution().optimalDivision3([2])
    print Solution().optimalDivision3([10, 2])
    # print Solution().optimalDivision([100, 10, 2])
    # print Solution().optimalDivision([1000, 100, 10, 2])
    print Solution().optimalDivision3([2, 3, 4])
    print Solution().optimalDivision3([6, 2, 3, 4, 5])
