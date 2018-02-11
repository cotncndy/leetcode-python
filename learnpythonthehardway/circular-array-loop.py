# You are given an array of positive and negative integers. If a number n at an index is positive, then move forward
# n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward
#  next to the last element, and the last element is backward next to the first element. Determine if there is a loop
#  in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must
#  be "forward" or "backward'.
#
# Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.
# Example 2: Given the array [-1, 2], there is no loop.
#
# Note: The given array is guaranteed to contain no element "0".
#
# Can you do it in O(n) time complexity and O(1) space complexity?

class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in xrange(len(nums)):
            slow, fast = i, i
            while slow < len(nums):
                s = self.goNext(nums, slow)
                if slow == s or s == self.goNext(nums, s):
                    break
                f = self.goNext(nums, self.goNext(nums, fast))

                if s == f:
                    if nums[s] * nums[slow] > 0 and nums[f] * nums[fast] > 0:
                        return True
                    return False
                fast, slow = f, s

        return False

    def goNext(self, nums, k):
        t = (k + nums[k]) % len(nums)
        return t if t >= 0 else t + len(nums)


if __name__ == '__main__':
    print Solution().circularArrayLoop([2, -1, 1, 2, 2])
    print Solution().circularArrayLoop([-1, 2])
    print Solution().circularArrayLoop([-2, 1, -1, -2, -2])
    print Solution().circularArrayLoop([-1, -2, -3, -4, -5])
