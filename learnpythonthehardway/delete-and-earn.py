# Given an array nums of integers, you can perform operations on the array.
#
# In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element
# equal to nums[i] - 1 or nums[i] + 1.
#
# You start with 0 points. Return the maximum number of points you can earn by applying such operations.
#
# Example 1:
# Input: nums = [3, 4, 2]
# Output: 6
# Explanation:
# Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points. 6 total points are earned.
# Example 2:
# Input: nums = [2, 2, 3, 3, 3, 4]
# Output: 9
# Explanation:
# Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.
# Note:
#
# The length of nums is at most 20000.
# Each element nums[i] is an integer in the range [1, 10000].
import collections


class Solution(object):
    # time complexity O(N^2)
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dict = collections.defaultdict(int)

        for i in nums:
            dict[i] += 1

        n = len(dict)
        res, newNums = [[0] * n for _ in xrange(n)], sorted(dict.keys())

        for d in xrange(0, n):
            for i in xrange(0, n - d):
                if d == 0:
                    res[i][i + d] = newNums[i] * dict[newNums[i]]
                else:
                    for k in xrange(i, i + d + 1):
                        a, b = res[i][k - 1] if k >= i + 1 else 0, res[k + 1][i + d] if k + 1 <= i + d else 0
                        if k > 0 and newNums[k] == newNums[k - 1] + 1:
                            a = res[i][k - 2] if k - 2 >= i else 0
                        if k + 1 < n and newNums[k] == newNums[k + 1] - 1:
                            b = res[k + 2][i + d] if k + 2 <= i + d else 0
                        temp = a + newNums[k] * dict[newNums[k]] + b
                        res[i][i + d] = max(res[i][i + d], temp)

        return res[0][n - 1]

    # O(N+W) w - range 1-10000
    def deleteAndEarn2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, using, avoiding, prev = [0] * 10001, 0, 0, -1

        for i in nums:
            count[i] += 1

        for i in xrange(10001):
            m = max(using, avoiding)
            if i - 1 != prev:
                using = m + i * count[i]
            else:
                using = avoiding + i * count[i]
            avoiding, prev = m, i

        return max(using, avoiding)

    # O(NlogN) , somehow it is faster than the prevous one
    def deleteAndEarn3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        using, avoiding, prev = 0, 0, -1

        for k in sorted(count):
            m = max(using, avoiding)
            if k - 1 == prev:
                using = avoiding + k * count[k]
            else:
                using = m + k * count[k]
            prev, avoiding = k, m

        return max(using, avoiding)






if __name__ == '__main__':
    print Solution().deleteAndEarn2([5, 7, 2])
    print Solution().deleteAndEarn2([2, 2, 3, 3, 3, 4])
    print Solution().deleteAndEarn3([2, 2, 3, 3, 3, 4])
