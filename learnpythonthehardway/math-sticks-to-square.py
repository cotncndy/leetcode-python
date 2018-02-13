# Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has,
# please find out a way you can make one square by using up all those matchsticks. You should not break any stick,
# but you can link them up, and each matchstick must be used exactly one time.
#
# Your input will be several matchsticks the girl has, represented with their stick length. Your output will either
# be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.
#
# Example 1:
# Input: [1,1,2,2,2]
# Output: true
#
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
# Example 2:
# Input: [3,3,3,3,4]
# Output: false
#
# Explanation: You cannot find a way to form a square with all the matchsticks.
# Note:
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.
import collections


class Solution(object):
    # this implementation is wrong
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m, sum, side = collections.defaultdict(int), 0, 0
        for n in nums:
            sum += n
            m[n] += 1
        if sum % 4:
            return False
        side = sum / 4

        cnt = 0
        for k in m:
            if m[k] == 0:
                continue
            if k == side:
                m[k] -= 1
                cnt += 1
                continue
            if m[side - k] == 0:
                return False
            m[k] -= 1  # bugfixed
            m[side - k] -= 1
            cnt += 1

        for k in m:
            if m[k] and k != side:
                return False
        return True if m[side] == 4 - cnt else False

    def makesquare2(self, nums):
        if not nums:  # bugfixed the [] test case
            return False
        m, sum, side = collections.defaultdict(int), 0, 0
        for n in nums:
            sum += n
            m[n] += 1
        if sum % 4:
            return False
        side = sum / 4

        for i in xrange(4):
            if not self.dfs(m, nums, 0, side):
                return False

        return True

    def dfs(self, map, nums, l, size):
        if l == size:
            return True
        for n in nums:
            if map[n] and n <= size - l:
                map[n] -= 1
                if self.dfs(map, nums, l + n, size):
                    return True
                map[n] += 1  # backtrack

        return False

    def makesquare3(self, nums):
        if not nums or len(nums) < 4:
            return False
        sides = [0] * 4
        s = sum(nums)
        size = s / 4
        sorted(nums, reverse=True)  # knowledge  how to sort a list descending

        return self.helper(nums, sides, size, 0)

    def helper(self, nums, sides, size, pos):
        if pos == len(nums):
            if sides[0] == size and sides[1] == size and sides[2] == size:
                return True

        for i in xrange(4):
            if sides[i] + nums[pos] > size:
                continue
            sides[i] += nums[pos]
            if self.helper(nums, sides, size, pos + 1):
                return True
            sides[i] -= nums[pos]  # backtrack

        return False






if __name__ == '__main__':
    # print Solution().makesquare2([1, 1, 2, 2, 2])
    # print Solution().makesquare2([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3])
    print Solution().makesquare2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    print Solution().makesquare3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
